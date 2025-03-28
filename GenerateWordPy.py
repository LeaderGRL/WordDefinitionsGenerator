import os
import json
import time
import openai
from dotenv import load_dotenv

# Charger les variables d'environnement depuis un fichier .env
load_dotenv()

# Configurer l'API OpenAI avec votre clé
# openai.api_key = os.getenv("YOUR OPENAI API KEY")

def generate_word_info(word):
    """Utilise l'API de ChatGPT pour générer la définition et la difficulté d'un mot."""
    try:
        # Création de la requête pour ChatGPT
        prompt = f"""
        Donne-moi 2 très courte définition différentes pour mots croisé en français du mot "{word}", attribue-lui un niveau 
        de difficulté ainsi qu'une catégorie.
        de 1 à 10 (où 1 est très facile parce que c'est un mot commun et simple et 10 est très difficile).
        Réponds uniquement au format JSON avec cette structure exacte:
        {{
            "word": "{word}",
            "description1": "la courte définition du mot",
            "description2": "une autre courte définition du mot",
            "category": "la catégorie du mot",
            "difficulty": niveau_difficulté_numérique
        }}
        """

        # Appel à l'API
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": "Tu es un assistant linguistique qui répond uniquement au format JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3  # Valeur basse pour plus de cohérence
        )

        # Extraire la réponse
        result = response.choices[0].message.content.strip()
        
        # Nettoyer la réponse pour s'assurer qu'elle est au format JSON valide
        # Enlever les backticks s'ils sont présents
        if result.startswith("```json"):
            result = result.replace("```json", "", 1)
        if result.endswith("```"):
            result = result.replace("```", "", 1)
        
        result = result.strip()
        
        # Convertir la réponse en objet JSON
        word_data = json.loads(result)
        return word_data
    
    except Exception as e:
        print(f"Erreur pour le mot '{word}': {e}")
        # En cas d'erreur, retourner une entrée avec une mention d'erreur
        return {
            "word": word,
            "description": "Erreur lors de la génération de la définition",
            "difficulty": 0
        }

def add_to_json_file(word_data, json_file_path):
    """Ajoute un seul mot au fichier JSON existant."""
    try:
        # Vérifier si le fichier existe
        if os.path.exists(json_file_path):
            # Lire le fichier JSON existant
            with open(json_file_path, 'r', encoding='utf-8') as f:
                try:
                    existing_data = json.load(f)
                    # Vérifier si existing_data est une liste
                    if not isinstance(existing_data, list):
                        # Si c'est un dictionnaire ou autre chose, créer une liste
                        existing_data = [existing_data] if existing_data else []
                except json.JSONDecodeError:
                    # Si le fichier est vide ou corrompu, initialiser avec un tableau vide
                    existing_data = []
        else:
            # Initialiser avec un tableau vide si le fichier n'existe pas
            existing_data = []
        
        # Ajouter la nouvelle donnée
        existing_data.append(word_data)
        
        # Écrire les données mises à jour dans le fichier
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)
        
        return True
    
    except Exception as e:
        print(f"Erreur lors de la mise à jour du fichier JSON: {e}")
        return False

def process_words_from_file(input_file_path, output_json_path, start_from=0):
    """Traite tous les mots d'un fichier texte et met à jour le fichier JSON de manière progressive."""
    try:
        # Lire le fichier texte contenant les mots
        with open(input_file_path, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
        
        total_words = len(words)
        print(f"Traitement de {total_words} mots à partir de l'index {start_from}...")
        
        # Créer le fichier de suivi pour stocker l'index actuel
        progress_file = f"{output_json_path}.progress"
        
        # Reprendre à partir de l'index spécifié
        for i in range(start_from, total_words):
            word = words[i]
            print(f"Traitement du mot {i+1}/{total_words}: {word}")
            
            try:
                # Générer les infos pour ce mot
                word_info = generate_word_info(word)
                
                # Ajouter au fichier JSON
                success = add_to_json_file(word_info, output_json_path)
                
                if success:
                    # Mettre à jour le fichier de progression
                    with open(progress_file, 'w', encoding='utf-8') as f:
                        f.write(str(i+1))
                    
                    print(f"Mot {word} traité et sauvegardé (progrès: {i+1}/{total_words})")
                else:
                    print(f"Échec de la sauvegarde du mot {word}, tentative à nouveau...")
                    i -= 1  # Réessayer ce mot
            
            except KeyboardInterrupt:
                print(f"\nInterruption détectée! Progression sauvegardée à l'index {i}.")
                print(f"Pour reprendre, exécutez le script avec l'option --start-from {i}")
                break
                
            except Exception as e:
                print(f"Erreur lors du traitement du mot '{word}': {e}")
                # Continuer avec le mot suivant
            
            # Pause pour éviter de dépasser les limites de l'API
            time.sleep(1)
        
        print("Traitement terminé avec succès!")
        
        # Supprimer le fichier de progression si tout est terminé
        if os.path.exists(progress_file) and i == total_words - 1:
            os.remove(progress_file)
    
    except Exception as e:
        print(f"Erreur lors du traitement des mots: {e}")

if __name__ == "__main__":
    import argparse
    
    # Analyser les arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Générer des définitions de mots avec GPT")
    parser.add_argument("--input-file", help="Chemin du fichier texte contenant les mots")
    parser.add_argument("--output-file", help="Chemin du fichier JSON de sortie")
    parser.add_argument("--start-from", type=int, default=0, help="Index à partir duquel commencer/reprendre (0 par défaut)")
    args = parser.parse_args()
    
    # Vérifier que la clé API est configurée
    if not os.getenv("OPENAI_API_KEY"):
        print("Erreur: Clé API OpenAI non trouvée. Créez un fichier .env avec OPENAI_API_KEY=votre_clé_api")
        exit(1)
    
    # Obtenir les chemins des fichiers
    input_file = args.input_file
    if not input_file:
        input_file = input("Entrez le chemin du fichier texte contenant les mots: ")
    
    output_file = args.output_file
    if not output_file:
        output_file = input("Entrez le chemin du fichier JSON de sortie: ")
    
    # Vérifier s'il y a un fichier de progression
    progress_file = f"{output_file}.progress"
    start_from = args.start_from
    
    if os.path.exists(progress_file) and start_from == 0:
        with open(progress_file, 'r') as f:
            try:
                saved_index = int(f.read().strip())
                print(f"Fichier de progression trouvé. Dernière position: {saved_index}")
                resume = input(f"Voulez-vous reprendre à partir de l'index {saved_index}? (O/n): ")
                if resume.lower() != 'n':
                    start_from = saved_index
            except:
                print("Fichier de progression corrompu, démarrage depuis le début.")
    
    # Traiter les mots
    process_words_from_file(input_file, output_file, start_from)