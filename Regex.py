import re

# Exemple de texte multiligne
texte = """
A : Pas de d�finition
ABAISSANT : Avilissant
ABAISSES : Avilisses
ABANDONNE : D�laisse
ABASOURDI : Etonn�
ABATARDI : D�g�n�r�
ABATTABLE : Que l'on peut descendre
ABATTAIT : Tuait
ABATTEMENT : D�prime
ABATTISSENT : Tuassent
ABATTRE : Tuer
ABATTUES : Tu�es
ABBESSE : Sup�rieure d'un monast�re de femmes
ABC : Le premier livre
ABDIQUANT : Renon�ant au pouvoir
ABDOMINAUX : Muscles
ABEILLE : Insecte
ABERRANTE : Absurde
ABHORRE : D�teste
ABJURE : Renonce
ABOLI : Abrog�
ABOLITIONNISTE : Qui est contre l'esclavage
ABOMINER : D�tester
ABONDER : Ne pas manquer
ABONNER : Habituer
ABORD : Acc�s
ABORDER : Accoster
ABORTIVE : Elle fait avorter
ABOULIE : Maladie de la volont�
ABOUTEMENT : Action de mettre bout � bout
ABOUTISSANTS : Avec les tenants on en a une id�e nette
ABOYEUSE : Elle crie trop fort
ABRASANT : Erodant
ABRASION : Erosion
ABREGE : Raccourci
ABREUVE : Donne � boire
ABREVIATIVE : Elle raccourcit
ABRICOTE : La p�che peut l'�tre 
ABROGEANT : Annulant
ABRUTISSANTE : Etourdissante
ABS : Pratique pour s'arr�ter en douceur
ABSCONSE : Pas claire
ABSENTEISME : Absence
ABSIDALE : Une chapelle peut l'�tre
ABSIDIAUX : Relatif au choeur
ABSOLUE : Totale
ABSOLUTOIRE : Qui absout
ABSOLVENT : Pardonnent
ABSORBABLE : Buvable
ABSORPTION : Action d'avaler
ABSTENAIENT : Privaient 
ABSTENIEZ : Priviez 
ABSTENTIONNISME : Absence
ABSTIENDRAIENT : Priveraient 
ABSTIENDRIONS : Priverions
ABSTINENCE : Privation
ABSTINT : Priva
ABSTRAIES : Eloign�es de la r�alit�
ABSTRAIRAS : Eloigneras de la r�alit�
ABSTRAIRONT : Eloigneront de le r�alit�
ABSTRAITS : Difficiles � comprendre
ABSURDITE : B�tise
ABUSIVE : Contraire aux r�gles
ABYSSAUX : Tr�s profonds
ABYSSINIENNE : Ancienne Ethiopienne
ACADEMIQUE : Classique
ACAJOU : Bois exotique
ACARIATRE : Peu aimable
ACCALMIE : R�pit
ACCAPAREUSE : Elle ne partage pas
ACCEDER : Parvenir
ACCELERATEUR : Champignon
ACCELERENT : H�tent
ACCENT : Signe graphique
ACCENTUELLE : Porte l'accent
ACCEPTABLE : Tol�rable
ACCEPTEUR : Tir�
ACCESSIBILITE : Facilit� d'approche
ACCIDENTEL : Caus� par un impr�vu
ACCLIMATANT : Habituant
ACCLIMATER : Habituer
ACCOINTER : Lier avec Quelqu'un
ACCOLE : Joint
ACCOMMODANT : Conciliant
ACCOMMODER : Concilier
ACCOMPAGNER : Escorter
ACCORD : Conformit�
ACCORDER : Consentir
ACCORDENT : Consentent
ACCORDEZ : Consentez
ACCORDS : Pactes
ACCOSTE : Aborde
ACCOTER : Appuyer
ACCOUCHER : Cr�er
ACCOUDE : Appuie
ACCOUPLEMENT : Lien
ACCOURANT : Venant en h�te
ACCOURIEZ : Veniez en h�te
ACCOURRAI : Viendrai en h�te
ACCOURREZ : Viendrez en h�te
ACCOURRONT : Viendront en h�te
ACCOURUMES : Arriv�mes en h�te
ACCOURUTES : Arriv�tes en h�te
ACCOUTUMANCE : Habitude
ACCOUVAGE : S'occupe des oeufs
ACCREDITEUR : Donne sa garantie
ACCRESCENTE : Se dit d'une partie de fleur
ACCROCHER : Attacher
ACCROIS : Augmente
ACCROISSE : Augmente
ACCROISSIEZ : Augmentiez
ACCROITRA : Augmentera
ACCROITRAIS : Augmenterais
ACCROITRE : Augmenter
ACCROITRIONS : Augmenterions
ACCROUPIR : Baisser
ACCRUES : Augmentation d'un terrain
ACCRUSSENT : Augmentassent
ACCUEILLAIS : Recevais
ACCUEILLENT : Re�oivent
ACCUEILLERAS : Recevras
ACCUEILLES : Re�ois
ACCUEILLIT : Re�ut
ACCULANT : Coin�ant
ACCUMULATEUR : R�servoir
ACCUSATEUR : Procureur
ACCUSE : Imputer un d�faut
ACERBE : Mordant
ACESCENCE : Tendance � l'acidit�
ACETAMIDE : Amide
ACETIFIE : Change en acide
ACETIQUE : Acide
ACHALANDE : Approvisionne
ACHARNEMENT : Ardeur furieuse
ACHEMINE : Emm�ne
ACHETAIENT : Acqu�raient
ACHETANTES : Acqu�rantes
ACHETENT : Acqui�rent
ACHETERAIENT : Acquerraient
ACHETEREZ : Acquerrez
ACHETEUR : Acqu�reur
ACHETIEZ : Acqu�riez
ACHEVEE : Termin�e
ACHEVERAIS : Terminerais
ACHEVERONS : Termineront
ACHOPPANT : Butant
ACHROMATISME : Propri�t� de certaines lentilles
ACIDE : Compos� Hydrog�n�
ACIDIFIER : Transformer en un compos� Hydrog�n�
ACIDOSE : Etat pathologique du sang
ACIERAGE : Durcissement d'un m�tal
ACIERE : Ajoute du carbone dans du fer
ACINEUSE : Caract�ristique de certaines glandes
ACOLYTES : Clercs
ACOQUINE : Lie � un fripon
ACOUSTICIENNE : S'occupe du son
ACQUEREUR : Acheteur
ACQUERRA : Ach�tera 
ACQUERREZ : Ach�terez
ACQUETS : Bien
ACQUIESCANT : Consentant
ACQUIS : exp�rience
ACQUISITION : Achat
ACQUITTER : Payer
ACQUITTES : Payes
ACRIMONIE : Mauvaise humeur
ACROBATIQUE : Scabreux
ACROTERE : Socle
ACTEUR : Artiste
ACTINIUM : M�tal radioactif
ACTINOMYCOSE : Maladie infectieuse
ACTIONNARIAT : Syst�me de gestion
ACTIVANT : Acc�l�rant
ACTIVEUR : Acc�l�rateur
ACTRICE : Artiste
ACTUALITE : Du moment pr�sent
ACTUELLE : Contemporain
ACUPONCTURE : Traitement m�dical chinois
AD : Ann�e du Seigneur (Abr.)
ADAMANTINE : Dure et brillante
ADAPTABLE : Applicable
ADDITIF : Ajout
ADDITIONNELLE : Doit �tre ajout�e
ADDUCTEUR : Muscle
ADENT : Entaille
ADERMINE : Vitamine
ADHERENTE : Collante
ADHESION : Union
ADIEU : Lorsqu'on se quitte
ADIPOSITE : Accumulation de graisses
ADJECTIVALE : A la fonction de qualifier
ADJOIGNAIS : Associais
ADJOIGNANTES : Associantes
ADJOIGNES : Associes
ADJOIGNIRENT : Associ�rent
ADJOINDRE : Associer
ADJUDANT : Sous-officier
ADJUDICATRICE : Elle attribue
ADJURE : Supplie
ADMETS : Permets l'acc�s
ADMETTANT : Permettant l'acc�s
ADMETTIONS : Permettions l'acc�s
ADMINISTRATIF : Appartient � la direction
ADMINISTRER : Gouverner
ADMIRATEUR : Fan
ADMIRATRICE : Fan
ADMISE : Accept�e
ADMISSION : Entr�e d'air
ADMONESTATION : R�primande
ADN : Acide
ADNEES : Lamelle de champignon
ADONNA : Passionna
ADOPTANTE : Prenant pour enfant
ADOPTIF : Pris pour enfant
ADORANT : Aimant
ADORER : Aimer
ADOSSER : Appuyer
ADOUCIR : Amadouer
ADOUCISSEUR : Produit pour traiter l'eau
ADRESSE : Habilet�
ADSORBANT : Buvant
ADULATION : Basse flatterie
ADULIONS : Flattions
ADULTERES : Tromperie
ADVENAIT : Arrivait
ADVENU : Arriv�
ADVERBIAUX : Tiennent d'un mot qui modifie le sens
ADVERSITE : Infortune
ADVIENNENT : Arrivent
ADYNAMIE : Manque de forces physiques
AERATION : Ventilation
AERE : Ventile
AERIENNE : Form�e d'air
AEROBIE : Besoin d'oxyg�ne
AERODROME : Terrain d'envol
AEROGLISSEUR : Bateau avion
AERONAVALE : Entre air et mer
AEROPHAGIE : D�glutition d'air
AEROPORT : Lieu d'escale
AEROSPATIAL : Interstellaire
AEROSTIER : Pilote de montgolfi�re
AEROTRANSPORTE : Arriv� du ciel
AFFABULATION : Mensonge
AFFADISSANT : Enlevant la vigueur
AFFAIBLISSEMENT : Diminution
AFFAIRER : Occuper
AFFAISSE : Baisse
AFFAISSEE : Baiss�e
AFFALE : Laisse tomber
AFFAME : Prive
AFFECTEE : Pas naturel
AFFECTER : Destiner
AFFECTIONNE : Aime
AFFECTUEUX : Tendre
AFFERMANT : Donnant � bail
AFFERMISSEMENT : Durcissement
AFFICHETTE : Petit avis
AFFILAGE : Aiguisage
AFFILIANT : Aiguisant
AFFILOIR : Aiguisoir
AFFINEUR : Purificateur
AFFIRMATIVE : Positive
AFFIXE : Particule
AFFLEURER : Mettre de niveau
AFFLIGEANTE : Causant du chagrin
AFFLUE : Coule
AFFOLANT : Troublant la raison
AFFOUAGE : Droit de prendre du bois
AFFOUAGISTE : Jouis d'un droit sur le bois
AFFOURAGEANT : Nourrissant des bestiaux
AFFOURCHER : Technique de mouillage
AFFRETEUR : Loueur
AFFRIANDE : App�te
AFFRIQUEE : Consonne � la prononciation particuli�re
AFFRONTE : Attaque
AFFUBLANT : Habillant bizarrement
AFFUT : Support
AFFUTEUSE : Machine outil
AFGHANISTAN : Pays d'Asie
AFOCAL : Dont les foyers sont � l'infini
AFRICANISER : Rendre africain
AFRIKANER : Hollandais d'Afrique
AG : Argent
AGA : Dignitaire oriental
AGACANTE : Enervante
AGALACTIE : Absence de lait
AGARICACEES : Famille de champignons
AGE : Dur�e de la vie
AGEES : Vieilles
AGENCE : Entreprise commerciale
AGENESIE : Absence de d�veloppement d'un tissu
AGENT : Mandataire
AGES : Vieux
AGGLOMERATION : Ville
AGGLOMERES : Amoncel�s
AGGLUTINATION : Ph�nom�ne de d�fense des organismes
AGGRAVANTE : Empirante
AGI : Produit un effet
AGIOTAGE : Trafic sur le cours des effets
AGIR : Produire un effet
AGIT : Fait quelque chose
AGITA : Remua
AGITATEUR : Baguette de verre
AGITE : Remue
AGITEE : Remu�e
AGITEES : Remu�es
AGITER : Remuer
AGITERA : Remuera
AGITERAI : Remuerai
AGITERAIS : Remuerais
AGITERAIT : Remuerait
AGITES : Remu�s
AGNATION : Parent�
AGNELER : Mettre bas
AGNELINE : Laine de la premi�re tonte
AGNOSIQUE : Atteint d'un d�faut de perception
AGONIE : Dernier instant
AGRAFER : Attacher
AGRANDIR : Accro�tre
AGRARIEN : Partisan des lois agraires
AGREE : reconnu
AGREEMENT : Reconnaissance
AGREGER : Associer
AGREMENTER : Orner
AGRESSION : Attaque
AGRICOLE : Relatif au travail de la terre
AGRIFFER : Accrocher
AGROCHIMIE : Chimie agricole
AGRUME : Cat�gorie de fruit
AGUERRISSANT : Accoutumant � la guerre
AGUICHE : Attire
AH : Interjection
AHANANT : Peinant
AHURISSANT : Stup�fiant
AI : Mammif�re arboricole d'Am�rique de Sud
AICHE : App�t
AIDANT : Assistant
AIE : Interjection
AIGLEFIN : Petite morue
AIGRELETTE : Un peu aigre
AIGREUR : Sensation d�sagr�able
AIGRISSEMENT : Action d'irriter
AIGUES : Pierre fine
AIGUILLEE : Longueur de fil
AIGUILLETE : Ornement militaire
AIGUILLONNANT : Piquant
AIGUISAGE : Action de rendre aigu
AIGUISEUR : R�mouleur
AILE : Plan de sustentation
AILLADE : Cro�ton de pain
AIMA : Appr�cia
AIMABLEMENT : En plaisant
AIMANTER : Rendre attirant
AIME : Appr�cie
AIMEE : Appr�ci�e
AIMEES : Appr�ci�es
AIMER : Appr�cier
AIMERA : Appr�ciera
AIMERAI : Appr�cierai
AIMERAIS : Appr�cierais
AIMERAIT : Appr�cierait
AIMES : Appr�cies
AIN : D�partement fran�ais
AINE : Baguette
AINEE : Ancienne
AINEES : Anciennes
AINES : Baguettes
AIR : Fluide gazeux
AIRAIN : Alliage
AIRE : Surface
AIRES : Surfaces
AIRS : M�lodies
AIS : Planche de bois
AISANCE : Facilit�
AISE : Etat agr�able
AISEE : Fortun�e
AISEES : Fortun�es
AISES : Fortun�s
AISSELLE : Cavit� sous l'�paule
AISY : Bouillon de culture
AISYS : Bouillons de culture
AJACCIEN : Corse
AJOURE : A trous
AJOURNER : Renvoyer
AJOUTE : Additionne
AJUSTE : Adapte
AKENE : Fruit sec
AL : Aluminium
ALAMBIC : Appareil pour distiller
ALANGUIR : Affaiblir
ALARMANTE : Inqui�tante
ALBANAIS : Habitant entre l'Italie et la Gr�ce
ALBERGIER : Arbre
ALBI : Ville du Tarn
ALBUMINE : Substance organique azot�e
ALCAIQUE : Se dit au sujet de vers grecs ou latins
ALCALIMETRIE : Mesure le titre
ALCALOSE : Etat anormal du sang
ALCHIMIE : Art de transformer
ALCOOL : Esprit de vin
ALCOOLISANT : Rajoutant de l'�thanol
ALCOOTEST : B�te noire du conducteur f�tard
ALDEHYDE : Issue de d�shydrog�nation
ALDOSE : Ose � fonction ald�hyde
ALE : Fabriqu� avec du malt
ALEA : Risque
ALEAS : Risques
ALEATOIRE : Incertain
ALEM : Savant musulman
ALENE : Poin�on
ALERTER : Avertir
ALES : Fabriqu�s avec du malt
ALESA : Per�a
ALESE : Perce
ALESEE : Perc�e
ALESER : Percer
ALESERA : Percera
ALESERAI : Percerai
ALESERAIS : Percerais
ALESERAIT : Percerait
ALEVINER : Peupler
ALEXANDRIN : Grand vers
ALEXIE : C�cit� verbale
ALFATIER : Relatif � une herbe d'Afrique du Nord
ALGEBRISTE : Il aime les maths
ALGEROIS : Habitant d'une ville d'Afrique du Nord
ALGINATE : Permet la prise des empreintes dentaires
ALGONQUIN : Partie sup�rieure du pr�cambrien
ALIBI : Preuve
ALIENABLE : Peut perdre le raison
ALIENATRICE : Elle fait perdre la raison
ALIENE : Fait perdre la raison
ALIGNE : Met sur le m�me axe
ALIMENT : N�cessaire � la vie
ALIMENTE : Approvisionne
ALISE : Fruit
ALISMACEES : Famille de plantes
ALITER : Coucher
ALLAI : Marchai
ALLAITEMENT : Repas des d�buts
ALLANTE : Aime le mouvement
ALLAS : Marchas
ALLECHANT : Attirant
ALLEGATION : Affirmation
ALLEGE : Petit mur
ALLEGORIES : Image
ALLEGRO : Vivement
ALLELE : Se dit d'un caract�re h�r�ditaire
ALLELOMORPHE : Se dit d'un caract�re h�r�ditaire
ALLER : Se rendre
ALLERGIQUE : Hyper sensible
ALLEU : Propri�t� h�r�ditaire
ALLIANCE : Union
ALLIE : Uni 
ALLITERATION : R�p�tition
ALLO : Interjection
ALLODIAL : Tenu en franc-alleu
ALLONGEANTE : Etirante
ALLOPATHE : M�decin
ALLOTROPIE : Propri�t� d'avoir plusieurs formes
ALLUMANT : Excitant
ALLUMEUR : D�clencheur
ALLUSIF : A un sens cach�
ALLUSIVEMENT : De mani�re d�tourn�e
ALLUVIONNER : Disposer des d�p�ts
ALMANDIN : Pierre fine rouge
ALOI : Proportion
ALOUETTE : Oiseau
ALOYAUX : Pi�ce de boeuf
ALPAX : Alliage d'aluminium et de silicium
ALPHABET : Livre contenant les lettres
ALPHANUMERIQUE : Contient des lettres et des chiffres
ALPINISTE : Il atteint les sommets
ALTERE : Assoiff�
ALTERER : Ab�mer
ALTERITE : Caract�re de ce qui est autre
ALTERNATIVE : Possibilit�
ALTERNE : Succ�de
ALTIMETRIE : Mesure de la hauteur par rapport � la mer
ALTOSTRATUS : Nuage
ALU : Aluminium
ALUMINE : Oxyde
ALUMINIAGE : Proc�d� de protection du fer
ALUN : Sulfate d'aluminium et de potassium
ALUNIR : Se poser sur un croissant
ALUNISSENT : Se posent sur un croissant
ALVEOLE : Cavit�
AM : Modulation d'amplitude
AMADOU : Substance spongieuse 
AMAIGRI : Diminu� de volume
AMALGAMANT : M�langeant
AMANDE : Graine comestible
AMANITE : Champignon
AMARINANT : Habituant � la mer
AMARRAGE : Action d'attacher
AMASSANT : R�unissant
AMATEUR : Qui aime
AMAZONE : Femme dangereuse
AMBASSADEUR : Repr�sentant
AMBIGU : Pas clair
AMBITIEUSEMENT : Cupidement
AMBIVALENCE : Dualit�
AMBLER : Marcher comme une girafe
AMBREE : L�g�rement jaune
AMBROSIE : Nourriture des dieux
AMBULANCE : Voiture rapide
AME : Noyau
AMELIE : Pr�nom f�minin
AMELIORE : Perfectionne
AMEN : Mot h�breu
AMENAGER : Disposer avec ordre
AMENAIT : Faisait venir avec lui
AMENDER : Modifier
AMENERAI : Ferai venir avec moi
AMENERAIT : Ferait venir avec lui
AMENERONS : Ferons venir avec nous
AMENITE : Douceur
AMENUISANT : Diminuant
AMER : Point de rep�re
AMERE : Qui a une saveur rude
AMERES : Qui ont une saveur rude
AMERICANISATION : Action de prendre des airs de cow-boy
AMERINDIEN : Ethnie d'Am�rique
AMERRIR : Se poser
AMERS : Points de rep�re
AMES : Noyaux
AMETROPE : Atteint d'un d�faut de vision
AMEUBLIR : Ramollir
AMHARIQUE : Langue s�mitique
AMI : Relation
AMIBIASE : Affection g�n�ralement intestinale
AMICALE : Groupement de membres d'une m�me profession
AMIDONNAGE : Action d'empeser le linge
AMIDONNIER : Bl� de l'Europe centrale
AMIE : Relation
AMIES : Relations
AMINE : Aminoacide
AMIRAL : Officier de marine
AMIS : Relations
AMMONIAC : Gaz � l'odeur piquante
AMNESIE : Oubli
AMNISTIANT : Pardonnant
AMOCHA : Ab�ma
AMODIATAIRE : Locataire
AMOINDRISSANT : Diminuant
AMOLLISSANT : Affaiblissant
AMONCELE : Met en tas
AMORALE : Ne respecte pas certaines r�gles
AMORCAGE : Dispositif qui provoque l'�clatement
AMOROSO : Tendrement
AMORTISSEMENT : Diminution de l'amplitude
AMOURACHE : S'�prend de passion
AMOUREUX : Parfois sur les bancs publics
AMPHIGOURIQUE : Inintelligible
AMPHITRYON : H�te
AMPLIFICATION : Augmentation
AMPOULE : Tube de verre soud�
AMPUTE : Coupe
AMSTERDAM : Ville hollandaise
AMULETTE : Objet protecteur
AMUSE : Divertit
AMYLACE : Enzyme
AN : Dur�e
ANA : Recueil de bons mots
ANABOLISANT : M�dicament
ANACARDIER : Arbre d'Am�rique tropicale
ANAGRAMMATIQUE : Fait avec les lettres d'un autre 
ANAGRAMME : Mot form� des lettres d'un autre
ANALEPTIQUE : M�dicament stimulant
ANALOGIQUE : Non num�rique
ANALYSANT : D�composant
ANALYSTES : Sp�cialistes de psychanalyse
ANANAS : Fruit originaire d'Am�rique tropicale
ANAPHORE : R�p�tition
ANARCHIE : D�sordre
ANARCHISTE : Partisan du d�sordre
ANASTOMOSE : Accolement
ANATHEMATISE : Frappe d'excommunication
ANATIDES : Famille d'oiseaux palmip�des
ANATOMIQUE : Relatif � la structure des �tres organis�s
ANCESTRAL : Appartient aux anciens
ANCHOIS : Poisson
ANCIENNEMENT : Autrefois
ANCRE : Grappin
ANDALOUSIE : R�gion d'Espagne
ANDIN : Des Andes
ANDOUILLETTE : Saucisse
ANDROGYNE : Mono�que
ANE : Mammif�re de l'ordre des ongul�s
ANEANTISSEMENT : Destruction
ANECDOTIQUE : Tient d'un fait curieux
ANEE : Quantit� charg�e sur le dos
ANEL : Pi�ce d'une tenaille
ANEMIE : P�leur
ANEMOPHILE : F�cond� par le vent
ANES : Mammif�res de l'ordre des ongul�s
ANESTHESIER : Endormir
ANEURINE : Vitamine
ANFRACTUOSITE : Cavit�
ANGERS : Ville du Maine et Loire
ANGINE : Maladie
ANGIOME : Tumeur 
ANGLAIS : Langue assez r�pandue
ANGLE : Coin
ANGLICISANT : Donnant un air anglais
ANGLOMANIE : Manie 
ANGOISSANT : Causant de l'anxi�t�
ANGOISSE : Anxi�t�
ANGOULEME : Ville de Charente
ANGUILLE : Poisson
ANGUILLES : Poissons
ANHARMONIQUE : Type de rapport
ANHELE : Respire p�niblement
ANHYDRE : Sec
ANIMADVERSION : R�probation
ANIMALIER : Personne qui reproduit des animaux
ANIMATION : Mouvement
ANIMELLES : Mets
ANIMISME : Religion
ANION : Charge n�gative
ANIS : Plante odorante
ANKYLOSE : Disparition du mouvement
ANNALES : Archives
ANNATE : Redevance
ANNEAU : Cercle
ANNELER : Disposer en cercle
ANNELIDES : Embranchement d'animaux
ANNEXION : Attachement
ANNIHILASSENT : An�antissent
ANNONCE : Avis
ANNONCER : D�clarer
ANNOTA : Fit une remarque
ANNOTER : Faire un remarque
ANNUEL : Cinq fois par lustre
ANNULABILITE : Disposition d'un acte
ANNULATIVE : Qui efface
ANOBLIR : Conf�rer un titre
ANODIQUE : Relatif � une �lectrode
ANODONTE : Mollusque bivalve
ANONNEMENT : H�sitation
ANONYME : Incognito
ANOREXIQUE : Pas affam�
ANOSMIE : Maladie du flair
ANS : p�riodes
ANSE : Poign�e
ANSEE : Munie d'un anneau
ANSEES : Munies d'un anneau
ANSERINE : Ch�nopode
ANSES : poignets
ANTALGIQUE : Calme la douleur
ANTECAMBRIEN : Pr�cambrien
ANTECHRIST : Imposteur
ANTENAISE : Ovin de dix � dix-huit mois
ANTHERE : Partie de l'�tamine
ANTHOLOGIE : Recueil
ANTHRACITE : Charbon
ANTHROPOLOGISTE : Sp�cialiste de l'�tude de l'homme
ANTHROPOPHAGIE : Sp�cialit� culinaire heureusement disparue
ANTIALCOOLISME : Combat contre une mauvaise habitude
ANTIBROUILLARD : Le radar en est un
ANTICHRESE : Contrat
ANTICIPE : Devance
ANTICLINAL : Se dit de la partie convexe d'un pli
ANTICOAGULANTE : Emp�che de durcir
ANTICYCLONE : Souvent synonyme de beau temps
ANTIDATER : Il est interdit de le faire sur un ch�que
ANTIDERAPANT : Est utilis� sur les marches d'escalier ou les ponts des bateaux
ANTIDOPING : Contr�le effectu� durant une comp�tition
ANTIEMETIQUE : M�dicament
ANTIFADING : Dispositif am�liorant la r�ception
ANTIGEL : Additif dans un moteur
ANTILLES : Iles de l'oc�an Atlantique
ANTIMERIDIEN : Antipode
ANTINATIONAL : Oppos� � l'int�r�t de son pays
ANTINEVRALGIQUE : M�dicament calmant
ANTIPARALLELE : Se dit de deux droites
ANTIPATRIOTIQUE : N'aime pas son pays
ANTIPHONAIRE : Livre d'�glise
ANTIPOISON : Antidote
ANTIRABIQUE : Se dit d'un traitement m�dical d�couvert par Pasteur
ANTIRATIONNELLE : Pas raisonnable du tout
ANTIREPUBLICAIN : Conservateur
ANTIROUILLE : Peinture
ANTITUSSIF : Sirop
ANTIVOL : Syst�me de s�curit�
ANTONYME : Contraire
ANURIES : Probl�mes r�naux
ANXIEUSE : Soucieuse
AORTE : Art�re
AOUT : Mois
APACHES : Indiens
APAISE : Calme
APATHIE : Nonchalance
APERCEPTION : Appr�hension
APERCEVEZ : Remarquez
APERCEVRAI : Remarquerai
APERCEVRONT : Remarqueront
APERCU : Vu
APERCURENT : Virent
APERCUTES : V�tes
APERTURE : Ouverture du canal buccal
APEX : Point dans la constellation d'Hercule
APHONE : Silencieux
APHTEUX : A des boutons
APICOLE : Rapport � l'�levage d'insecte
APIDES : Famille d'insectes
APIECEUR : Ouvrier du textile
APIQUER : Hisser
APLANIR : Rendre uni
APLANISSEMENT : Action de rendre uni
APLATIE : Ecras�e
APLATISSEUR : Lamineur
APOCOPE : Abr�viation
APODES : Ordre des batraciens
APOGEE : Sommet
APOLOGIE : Eloge
APONEVROSE : Enveloppe des muscles
APOPLEXIE : Coma
APOSTANT : Pla�ant un observateur
APOSTE : Place un observateur
APOSTOLAT : Mission
APOTHEME : Perpendiculaire du centre d'un polygone sur un de ses c�t�s
APOTRE : Disciple
APPARAIS : Se montre
APPARAISSENT : Se montrent
APPARAISSONS : Arrivons
APPARAITRE : Se montrer
APPAREILLAGE : D�part
APPAREMMENT : Il semblerait
APPARENTE : Alli�
APPARIER : Assortir par couple
APPARTENAIS : Faisais partie
APPARTENIONS : Faisions partie
APPARTIENDRIONS : Ferions partie
APPARTIENNES : Fasses partie
APPARTINRENT : Firent partie
APPARUS : Te montras
APPARUT : Se montra
APPAS : Attraits
APPATE : Attire
APPEAUX : Sifflet
APPELLATION : D�nomination
APPENDAIT : Suspendait
APPENDES : Suspendes
APPENDICES : Prolongements
APPENDIEZ : Suspendiez
APPENDIT : Suspendit
APPENDRE : Suspendre
APPENDU : Suspendu
APPETISSANT : Qui excite le d�sir
APPLAUDIR : Faire du bruit avec les mains
APPLICATION : Mise en pratique
APPLIQUE : Objet fix� a un mur
APPOINTANT : R�mun�rant
APPONTANT : Posant
APPONTEUR : Officier dans l'a�ronavale
APPORTER : Amener
APPRECIANT : Estimant
APPREHENDANT : Saisissant
APPRENAIS : Etudiais
APPRENDRAIENT : Etudieraient
APPRENDRONT : Etudieront
APPRENNENT : Etudient
APPRET : Sous-couche
APPRETEUSE : Ouvri�re qui pr�pare les toiles
APPRISE : Connue
APPRIVOISABLE : Que l'on peu rendre sociable
APPRIVOISER : Rendre sociable
APPROBATIVEMENT : Avec consentement
APPROCHEE : Approximative
APPROPRIE : Pertinent
APPROVISIONNANT : Fournissant
APPROXIMATIF : Approch�
APPUYER : Insister avec force
APRES : Marque de post�riorit�
APTITUDE : Disposition
APYRE : Inalt�rable au feu
AQUACULTURE : Elevage humide
AQUARELLISTE : Peintre
AQUAVIT : Liqueur
AQUICULTURE : Elevage humide
AQUITAINE : R�gion fran�aise
AR : Argon
ARA : Perroquet
ARABESQUE : Ornement
ARACHNEEN : Propre � l'araign�e
ARACHNOIDIEN : Appartient � une m�ninge
ARAGONITE : Carbonate de calcium
ARAK : Liqueur de riz
ARAMEEN : Langue s�mitique
ARANEIDES : Araign�es
ARAS : Perroquets
ARATOIRE : Qui concerne l'agriculture
ARBITRAGISTE : Contr�leur en bourse
ARBITRANT : Contr�lant
ARBORE : D�ploie
ARBORESCENT : Fait des branches
ARBORICULTEUR : Cultivateur sp�cialis�
ARBOUSIER : Arbrisseau du Midi
ARBUSTIVE : Compos� de petits arbres
ARC : Arme
ARCADIE : R�gions de la Gr�ce ancienne
ARCEAU : Partie courbe d'une vo�te
ARCHAISME : Construction qui n'est plus en usage
ARCHE : Grand bateau
ARCHET : Appareil sonore des sauterelles
ARCHETYPE : Mod�le primitif
ARCHIDIACRE : Vicaire g�n�ral
ARCHIDUC : Titre autrichien
ARCHIEPISCOPALE : Relatif � un Archev�que
ARCHITECTE : Concepteur
ARCHITECTURE : Forme
ARCHIVANT : Classant
ARCHIVISTE : Personne qui classe
ARCON : Armature d'une selle
ARCS : Armes
ARCURE : Courbure
ARDENNAISE : Habitante du Nord-est de la France
ARDEUR : Chaleur
ARDOISE : Roche schisteuse
ARDUS : Difficile
ARE : Unit� de mesure de surface
AREC : Palmier
ARECS : Palmiers
AREIQUE : Sec
AREOPAGE : Ancien tribunal d'Ath�nes
ARETIER : Ligne saillante d'un comble
ARGENTAIS : Recouvrais d'un d�p�t brillant
ARGENTAN : Cuivre plus nickel plus zinc
ARGENTA : Recouvrit d'un d�p�t brillant
ARGENTERIE : Vaisselle
ARGENTIN : Qui a un son clair
ARGILE : Roche s�dimentaire terreuse
ARGONAUTE : Mollusque des mers chaudes
ARGOT : Vocabulaire de la rue
ARGUMENT : Preuve
ARGUS : Homme tr�s clairvoyant
ARIDITE : S�cheresse
ARIETTE : Petite m�lodie
ARISANT : Diminuant la toile
ARISER : Diminuer la toile
ARISTOCRATIE : Gouvernement
ARITHMETIQUE : Science des nombres
ARLEQUINADE : Bouffonnerie
ARMAGNAC : Liqueur
ARMEMENT : Mat�riel n�cessaire � un voyage
ARMENIENNE : Habitante d'une r�gion de l'Asie occidentale
ARMENIEN : Habitant d'une r�gion de l'Asie occidentale
ARMORIAL : En parlant des ornements de l'�cu d'un �tat
ARMORIES : Ornements de l'�cu d'un �tat
ARNAQUE : Escroquerie
AROMATISANT : Parfumant
ARPEGEANT : Faisant des accords
ARPENTE : Parcourt � grands pas
ARQUANT : Courbant
ARQUER : Courber
ARRACHEMENT : Extraction
ARRACHIS : Plant dont les racines sont � nu
ARRANGEANT : Mettant en ordre
ARRAS : Ancienne capitale de l'Artois
ARRESTATION : Etat plut�t contrariant
ARRETER : Emp�cher d'avancer
ARRIERE : Dos
ARRIMANT : Attachant
ARRIVAGE : Livraison
ARRIVISME : Ambition
ARROGANTE : Hautaine
ARRONDIR : Adoucir les angles
ARROSAGE : Jet d'eau
ARROSEUR : Derni�re ramification d'un r�seau d'irrigation
ARSENIATE : Sel de l'acide ars�nique
ARSENIEUX : Se dit de l'anhydride
ARSENIURE : Combinaison de l'arsenic avec un corps simple
ART : Mani�re de faire
ARTERE : Voie de communication
ARTERITE : Maladie des art�res
ARTHRITIQUE : Au sujet des articulations
ARTICULATION : Assemblage mobile
ARTIFICE : Ruse
ARTISAN : Auteur
ARTISTE : Esth�te
ARTS : Mani�res de faire
ARUM : Plante � petites fleurs
ARYLE : Groupement d'atomes d�riv� des compos�s benz�niques
AS : Champion
ASCARIDE : Ver parasite
ASCENDANTE : Montante
ASCENSIONNISTE : Personne qui s'�l�ve
ASCIDIE : Animal marin vivant fix� aux rochers
ASDIC : Appareil de d�tection sous-marine
ASEPTISE : Prot�ge contre les microbes
ASOCIAL : Inadapt� � la vie en groupe
ASPARAGUS : Plante d'appartement
ASPERGES : Plantes dont on mange les tiges
ASPERME : Qui ne produit pas de graine
ASPHALTER : Couvrir de bitume
ASPHYXIER : Emp�cher de respirer
ASPIRANT : Candidat
ASPIRE : Attirer
ASPRE : Colline
ASSAILLAIENT : Attaquaient
ASSAILLE : Attaque
ASSAILLI : Attaqu�
ASSAILLIR : Attaquer
ASSAILLIRAS : Attaqueras
ASSAILLIRONT : Attaqueront
ASSAILLIT : Attaqua
ASSAINISSEMENT : D�sinfection
ASSAISONNER : Accommoder
ASSARMENTER : D�barrasser des branches inutiles
ASSASSINER : Tuer
ASSECHENT : Mettent � sec
ASSEMBLE : Pas fondamental de la danse
ASSENA : Frappa
ASSENANT : Frappant
ASSENAT : Frapp�t
ASSENEES : Frapp�es
ASSENERAI : Frapperai
ASSENERIEZ : Frapperiez
ASSENIONS : Frappions
ASSERMENTE : Reconnu par l'�tat
ASSERVIR : R�duire � l'esclavage
ASSESSEUR : Assistant
ASSETTE : Asseau
ASSEZ : Passablement
ASSIED : Pose
ASSIEGE : Importune
ASSIERAIS : Poserais
ASSIERONS : Poserons
ASSIGNABLE : Auquel on peut attribuer une place
ASSIMILER : Etablir une comparaison
ASSIS : Stable
ASSISTANT : Aide
ASSISTER : Seconder
ASSOCIATIVE : Comme l'addition ou la multiplication
ASSOIE : Pose
ASSOIFFE : Avide
ASSOIRAS : Poseras
ASSOIS : Pose
ASSOMBRI : Attrister
ASSOMME : Importune
ASSONANCE : Figure de style
ASSOUPI : Endormi
ASSOUPLIR : Rendre mall�able
ASSOURDISSANT : Tr�s bruyant
ASSOUVISSEMENT : Contentement
ASSUJETTIR : Ranger sous sa domination
ASSUME : Accepte
ASSUREE : Couverte
ASSYRIEN : Du royaume de l'ancienne Asie
ASTATIQUE : En �quilibre
ASTERISQUE : Petit signe typographique
ASTHMATIQUE : Qui a de la peine � respirer
ASTICOTE : Taquine
ASTIQUE : Fait briller
ASTRE : Corps lumineux
ASTREIGNAIENT : Obligeaient
ASTREIGNANTE : Contraignante
ASTREIGNES : Obliges
ASTREIGNIEZ : Contraigniez
ASTREIGNIT : Contraignit
ASTREINT : Contraint
ASTROLOGIE : Art divinatoire
ASTRONOMIQUE : Type de lunette
ASTUCIEUSE : Rus�e
ASYMETRIE : D�s�quilibre
ATAXIE : D�faut de coordination
ATERMOYANT : Ajournement
ATHENEE : Etablissement d'enseignement secondaire belge
ATHLETE : Sportif
ATLANTIDE : Ile perdue
ATMOSPHERIQUE : Dans l'air
ATOMISANT : R�duisant en petites particules
ATOMISME : Syst�me philosophique
ATONAUX : Ecrits � la mani�re de Xenakis
ATOUT : Avantage
ATRE : Foyer
ATROCEMENT : Tr�s m�chamment
ATROPINE : Alcalo�de extrait de la belladone
ATTACHANTE : Liante
ATTAQUANT : Premi�re ligne
ATTARDE : Idiot
ATTEIGNANT : Touchant
ATTEIGNEZ : Touchez
ATTEIGNIRENT : Touch�rent
ATTEIGNONS : Touchons
ATTEINTE : Touch�e
ATTELE : Attache
ATTENANTE : Contigu�
ATTENDAIT : Patientait
ATTENDIEZ : Patientiez
ATTENDIT : Patienta
ATTENDRAIENT : Patienteraient
ATTENDRIES : Emues
ATTENDRIR : Emouvoir
ATTENDS : Patiente
ATTENTER : Commettre une tentative criminelle
ATTENTIVE : Appliqu�e
ATTENUE : Minimise
ATTERRER : Consterner
ATTERRISSAGE : Retour au port
ATTESTER : Certifier
ATTIEDISSENT : R�chauffent ou refroidissent
ATTIFEMENT : Ornement de mauvais go�t
ATTIRAIL : Ensemble de choses n�cessaires
ATTIRANTE : S�duisante
ATTITRE : Titulaire
ATTOUCHEMENT : Contact
ATTRAIT : Atout
ATTRAYANT : S�duisant
ATTRIBUANT : Accordant
ATTRIBUTION : Comp�tence
ATTRISTER : Assombrir
AU : Or
AUBEPINE : Arbrisseau �pineux de la famille des rosac�es
AUBIER : Partie jeune du tronc
AUCUN : Nul
AUDACIEUX : Intr�pide
AUDITIONNANT : Ecoutant
AUDITORIUM : Salle de musique
AUGE : Mangeoire
AUGMENTATION : Inflation
AUGURANT : Faisant une conjecture
AUGURER : Faire une conjecture
AUGUSTINIEN : Th�orie adopt�e par les Jans�nistes
AULNE : Arbre de la famille des b�tulac�es
AUNE : Ancienne mesure de longueur
AUNIS : Ancienne province de France
AURA : Halo
AURELIE : Pr�nom f�minin
AURICULAIRE : Le plus petit des cinq
AURIFERE : Contient un m�tal pr�cieux
AURIQUE : Type de gr�ement
AURORE : Premi�res lueurs
AUSCULTATION : Visite m�dicale
AUSSI : Adverbe
AUSTEREMENT : S�v�rement
AUSTRAL : Au p�le Sud
AUSTRALIE : Etat de l'Oc�anie
AUTANT : Adverbe
AUTEL : Table
AUTHENTIFIE : Certifie
AUTISTE : Schizophr�ne
AUTOCOAT : Pardessus pour automobiliste
AUTOCRATE : Monarque absolu
AUTOCUISEUR : Etuve
AUTODIDACTE : Ne passe pas par l'�cole
AUTOGENE : Type de soudure
AUTOGIRE : A�ronef
AUTOGRAPHIE : Reproduction
AUTOLYSE : Destruction des tissus
AUTOMATIQUE : Involontaire
AUTOMATISE : Remplace l'homme par la machine
AUTOMOBILISTE : Conducteur
AUTONOMIE : Distance franchissable
AUTONYME : Usage particulier d'un mot
AUTOPROPULSEUR : Moteur
AUTOPSIER : Diss�quer
AUTOREGLAGE : Propri�t� de retrouver son r�gime initial
AUTORISANTE : Permettant
AUTORITAIRE : Ne souffre pas la contradiction
AUTOROUTE : Voie rapide
AUTOUR : Oiseau de proie
AUTRICHIEN : Voisin des Allemands
AUVERGNAT : Habitant du centre de la France
AUXERRE : Ville de l'Yonne
AUXINE : Hormone v�g�tale
AV : Avant
AVACHI : Ramolli
AVALANCHE : Catastrophe
AVALERAIS : Absorberais
AVALISEUR : Qui donne sa garantie
AVANCEE : Progr�s
AVANIE : Affront
AVANTAGEUSE : Int�ressante
AVARICE : Attachement excessif aux richesses
AVARIER : Endommager
AVE : Salut
AVEC : Pr�position
AVELINIER : Noisetier
AVEN : Puits
AVENT : Les quatre Dimanches pr�c�dents No�l
AVENTUREUSEMENT : Hardiment
AVENTURISME : Tendance prendre des d�cisions irr�fl�chies
AVERAIENT : R�v�laient
AVERANT : R�v�lant
AVERE : R�v�le
AVERSE : Grain
AVERTISSANT : Informant
AVEU : Confession
AVEUGLANT : Frappant par son �vidence
AVEUGLETTE : Au hasard
AVEUX : Confession
AVEYRON : D�partement du Massif Central
AVIATION : Mode de locomotion
AVIDITE : D�sir ardent
AVILIE : D�pr�cie
AVINE : Saoul
AVIONIQUE : Sp�cialit� �lectronique
AVISE : Circonspect
AVITAILLE : Remplit la cambuse
AVIVANT : Donnant de l'�clat
AVOCATIER : Arbre fruitier
AVOINE : C�r�ale
AVOISINE : Habite � cot�
AVORTER : Echouer
AVOUE : Reconna�t
AVUNCULAIRE : De l'oncle
AXER : Centrer
AXIOLOGIE : Th�orie des valeurs philosophiques
AXIOMATISER : R�duire � l'�vidence
AXONE : Prolongement d'une cellule nerveuse
AZERBAIDJAN : Plaine de la Koura
AZEROLIER : Aub�pine
AZOIQUE : Sans vie
AZOTE : Gaz
AZOTOBACTER : Bact�rie
AZUR : Substance min�rale color�e
AZURER : Teindre en bleu
B : Pas de d�finition
BA : Baryum
BABILLANT : Parlant pour ne rien dire
BABILLE : Parle pour ne rien dire
BABOUVISME : Doctrine
BAC : Bateau
BACCHANALE : Orgie
BACHANT : Couvrant
BACHOTAGE : Pr�paration
BACILLE : Insecte herbivore du Midi
BACLE : Pi�ce de bois
BACTERIE : Microbe 
BACTERIOPHAGE : Virus
BADE : R�gion d'Allemagne
BADIGEONNANT : Peignant
BADINANT : Plaisantant
BAFOUE : Ridiculise
BAFOUILLEUR : Bredouilleur
BAGAGISTE : Porteur
BAGARREUSE : Toujours pr�te pour la lutte
BAGNARD : For�at
BAGUENAUDER : Perdre son temps
BAGUER : Faire des points invisibles
BAGUETTISANT : Sourcier
BAH : Interjection
BAI : Couleur de robe
BAIE : Ouverture
BAIES : Ouvertures
BAIGNEUR : Petite poup�e nue
BAIL : Contrat
BAILE : Titre des gouverneurs des colonies v�nitiennes
BAILLER : Etre entrouvert
BAILLI : Agent du roi
BAILLONNEMENT : R�duire au silence
BAIN : Liquide utilis� pour l'immersion
BAINS : Liquides utilis�s pour l'immersion
BAIRAM : F�te musulmane
BAIS : Ville de Mayenne
BAISA : Appliqua
BAISE : Applique
BAISEMENT : Pratiqu� le jeudi saint sur les pauvres
BAISER : Appliquer
BAISSA : Diminua
BAISSIER : Sp�culateur
BAL : R�union de danseurs
BALADE : Promenade
BALAFRE : Cicatrice
BALALAIKA : Luth triangulaire
BALANCE : Instrument de comparaison des masses
BALAYAGE : Nettoyage
BALAYERAI : Chasserai
BALAYERIEZ : Chasseriez
BALAYEUR : Nettoyeur
BALBUTIER : B�gayer
BALEARE : Archipel m�diterran�en
BALEINE : Renfort de v�tement
BALISAGE : Signalisation
BALISTE : Machine de guerre romaine
BALIVERNE : Bagatelle
BALKANS : P�ninsule de l'Europe m�ridionale
BALLASTAGE : Remplissage du lest
BALLES : Enveloppes
BALLON : A�ronef
BALLONNER : Enfler
BALLOT : Paquet
BALLOTTANT : Agitant
BALNEAIRE : Au bord de l'eau
BALOURDISE : B�tise
BALS : R�unions de danseurs
BALSA : Bois l�ger
BALSAMIQUE : Qui a les propri�t�s du baume
BALUSTRADE : Cl�ture
BALZANE : Tache de poils blancs
BAMBOCHARD : Qui aime la d�bauche
BAMBOU : Gramin�e des pays chauds
BAN : Proclamation officielle
BANALEMENT : De fa�on courante
BANC : Si�ge
BANCABLE : D'un effet de commerce
BANCAL : Sabre court
BANCHIONS : Coulions
BANCO : Tenir l'enjeu
BANCS : Si�ges
BANDEAU : Assise de pierre
BANDER : Tendre
BANDITISME : Moeurs de voyous
BANIAN : Figuier de l'Inde
BANNE : Toile
BANNIE : Expuls�e
BANNISSEMENT : Expulsion
BANQUE : Lieu s�r
BANQUEROUTE : Faillite
BANQUET : Festin
BANS : Proclamations officielles
BAPTEME : C�r�monie religieuse
BAPTISER : Nommer
BAPTISME : Doctrine
BAR : Poisson marin
BARAGOUINER : Parler mal
BARAQUE : Maison
BARATIN : Discours
BARATINEUR : Qui sait raconter des boniments
BARBARESQUE : De l'ancienne Afrique du Nord
BARBECUE : Appareil de cuisson
BARBERAIENT : Ennuieraient
BARBIER : Raseur
BARBITURIQUE : S�datif
BARBOTER : D�rober
BARBOTINE : P�te � poterie
BARBOUILLER : Peindre
BARBUE : Poisson marin
BARCELONE : Ville espagnole
BARDE : Po�te
BARDOT : Mulet
BARGUIGNE : H�site
BARIL : Tonneau
BARIOLE : A bandes ou � taches
BARMAN : Serveur
BARN : Unit� de surface
BAROMETRE : Instrument de mesure
BARONET : Titre h�r�ditaire anglais
BAROQUE : Style
BARQUE : Bateau
BARRAIS : Dirigeais
BARRE : Dirige
BARREUR : Conducteur
BARRIERE : Obstacle
BARROT : Poutre
BARS : Poissons marins
BARYTE : Oxyde de baryum
BAS : Partie inf�rieure
BASA : Fonda
BASANER : Bistrer
BASCULANT : Renversant
BASE : Assise
BASEES : Domicili�es
BASER : Domicilier
BASERA : Domiciliera
BASERAI : Domicilierai
BASERAIS : Domicilierais
BASERAIT : Domicilierait
BASES : Fondements
BASILIC : Plante aromatique
BASOCHE : Juridiction des anciens clercs de producteur
BASQUET : Caissette
BASSEMENT : De fa�on vile
BASSIN : R�cipient
BASSINE : R�cipient
BASSON : Instrument de musique
BASTIDE : Maison
BASTINGAGE : Partie d'un bateau
BASTONNADE : Vol�e de coups
BAT : Selle
BATA : Port d'Afrique
BATAILLE : Combat
BATAILLEUR : Belliqueux
BATARDEAU : Digue provisoire
BATAVE : Ancien nom des Pays-Bas
BATE : B�ton
BATEE : Sotte
BATEES : Sottes
BATELEUR : Acrobate
BATER : Seller
BATERA : Sellera
BATERAI : Sellerai
BATERAIS : Sellerais
BATERAIT : Sellerait
BATES : B�tons
BATH : Tr�s beau
BATHYSCAPHE : Sous-marin
BATI : Ch�ssis
BATIE : Faite
BATIES : Faites
BATIFOLER : Jouer
BATIK : Tissus d�cor�
BATIR : Construire
BATIRA : Construira
BATIRAI : Construirai
BATIRAIS : Construirais
BATIRAIT : Construirait
BATIRAS : Construiras
BATIS : Construis
BATISSANT : Construisant
BATON : Pi�ce de bois
BATONNETS : Petites pi�ces de bois
BATRACIENS : Classe de vert�br�s
BATS : Selles
BATTANT : Partie d'une porte
BATTEUR : Musicien
BATTOIR : Main large
BATTRE : Frapper
BAU : Poutre
BAUD : Unit� de vitesse de transmission
BAUDET : Ane
BAUME : R�sine
BAVARDAGE : Indiscr�tion
BAVEUX : Coulant
BAYADERE : Danseuse en Inde
BAYER : Regarder niaisement en l'air
BAZAR : On y trouve de tout
BE : B�ryllium
BEAGLE : Chien anglais
BEARNAISE : Sauce
BEATIFICATION : Sanctification
BEAU : Agr�able � regarder
BEAUFORT : Echelle de vent
BEAUX : Agr�ables � regarder
BEC : Extr�mit� d'un instrument de musique
BECARD : Grand saumon
BECASSEAUX : Oiseau �chassier
BECHANT : Retournant
BECHOIR : Houe carr�e
BECQUEREL : Physicien fran�ais
BECQUETTE : Pique les fruits
BECS : Extr�mit�s des br�leurs
BEDANE : Ciseau
BEDONNANTE : Qui a du ventre
BEDOUIN : Nomade
BEE : Frapp� d'admiration
BEER : Etre ouvert
BEGAYANT : Pronon�ant avec peine
BEGAYERAIENT : Prononceraient avec peine
BEGAYERIONS : Prononcerions avec peine
BEGONIA : Plante originaire d'Am�rique du Sud
BEGUETE : Imite une ch�vre
BEGUETER : Imiter une ch�vre
BEGUEULE : Femme prude
BEGUM : Titre donn� aux princesses indiennes
BEIGE : Couleur naturelle de la laine
BEL : Unit� d'intensit� sonore
BELER : Imiter un mouton
BELFORTAIN : Vosgien
BELIER : Machine de guerre
BELLATRE : A des pr�tentions � la beaut�
BELLES : Agr�ables � regarder
BELLIGERANT : Combattant
BELLUAIRE : Gladiateur romain
BELUGA : C�tac�
BEN : Mot s�mitique
BENARDE :  S'ouvrant des deux cot�s
BENEDICTINE : Religieuse
BENEFICIANT : Tirant profit
BENEFICIER : Tirer profit
BENET : Niais
BENETS : Niais
BENGALI : Petit oiseau
BENIN : Sans cons�quences graves
BENIR : Consacrer au culte
BENITE : Consacr�e
BENITIER : Mollusque
BENITS : Consacr�s
BENOITE : Plante herbac�e
BENZENE : Hydrocarbure
BENZOLISME : Maladie professionnelle
BEOTIENNE : Ignorante
BEQUILLE : Appui
BER : Support
BERBERE : Langue d'Afrique du Nord
BERCEAUX : Lits
BERCEUSE : Chanson
BERGE : Bord
BERIBERI : Maladie due � une carence en vitamine
BERLINGOT : Bonbon
BERMUDIEN : Type de gr�ement
BERNAIENT : Se moquaient
BERNEE : Tromp�e
BERNOISE : Habitante d'une ville suisse
BERS : Supports
BERTHE : Princesse de Bourgogne
BESOGNER : Travailler
BESSONNE : Jumelle
BESTIALEMENT : De fa�on brutale
BETA : Lettre de l'alphabet grec
BETE : Idiot
BETISIER : Recueil de sottises
BETONNE : Construit solide
BETTE : L�gume
BETULACEES : Famille de plantes
BEURRA : Tartina
BEURRE : Substance grasse et onctueuse
BEY : Ancien titre de l'arm�e musulmane
BEZIERS : Ville du Sud-ouest
BF : Fr�quences que l'on peut entendre
BI : Bismuth
BIAISER : User de finesse
BIATHLON : Comp�tition
BIBERONNER : Boire avec exc�s
BIBLIOGRAPHIE : Documentation
BIBLIOPHILIE : Amour du livre
BIBLIQUE : Une parole peut l'�tre
BICARBONATE : Sel de sodium
BICEPS : Muscle
BICHER : Etre satisfait
BICHONNE : Prend soin
BICOLORE : Qui a deux couleurs
BICOT : Chevreau
BIDENT : Fourche
BIDON : R�cipient
BIELLE : Barre de liaison
BIENFAISANT : Qui a une action salutaire
BIENHEUREUX : Personne qui jouit de la b�atitude �ternelle
BIENSEANT : Qu'il convient de faire
BIENVENU : Accueilli avec plaisir
BIFFAGE : Rature
BIFFURE : Rature
BIFOCAUX : Poss�dent plusieurs foyers
BIGAME : Trop bien mari�
BIGARRE : Disparate
BIGARREE : Disparate
BIGLER : Avoir les yeux de travers
BIGORNEAU : Coquillage
BIGOUDI : Ustensile de coiffure
BIJECTION : El�ment de la th�orie des ensembles
BIJOUX : Objets de d�coration
BILAME : Bande m�tallique double
BILATERAL : Qui poss�de deux faces
BILE : S�cr�tion
BILIEUSE : Enclin � la col�re
BILINGUISME : Caract�ristique des populations frontali�res
BILLARD : Jeu de boules
BILLETTE : Morceau de bois fendu
BILLEVESEE : Chose frivole
BILLOT : Tronc de bois
BILOQUER : Labourer
BIMETALLISME : Syst�me mon�taire
BINAIRE : Ne peut prendre que deux valeurs
BINAURICULAIRE : Appareil d'optique
BINETTE : Outil de jardinier
BINOCLE : Lorgnon
BIOCHIMIE : Etude des constituants de la mati�re vivante
BIOGRAPHIQUE : Se rapporte � la vie de quelqu'un
BIOSPHERE : Couche autour de l'�corce terrestre
BIOTITE : Mica
BIOXYDE : Oxyde contenant beaucoup d'oxyg�ne
BIPARTITION : Division
BIPENNE : Hache antique
BIPIED : Support
BIQUOTIDIEN : Matin et soir
BIRMAN : Habitant de la r�publique de l'Indochine occidentale
BIS : Encore
BISAIEUL : Arri�re grand-p�re
BISBILLE : Querelle
BISCAYENNE : Dialecte basque
BISCOTTE : tranche de pain de mie s�ch�e au four
BISCUITER : Cuire la porcelaine
BISE : Vent
BISEAUTER : Tailler
BISER : D�g�n�rer des c�r�ales
BISES : Baisers
BISET : Pigeon sauvage
BISMUTH : M�tal
BISONTINE : De Besan�on
BISQUE : Mauvaise humeur
BISSAC : Sorte de besace
BISSEXTILE : Plus longue d'un jour
BISSEXUE : Hermaphrodite
BISTOURNE : D�forme
BISTROT : Caf�
BIT : Unit� d'information
BITORD : Petit cordage
BITTE : Pi�ce d'amarrage
BITTER : Liqueur
BITUMER : Recouvrir de goudron
BITURE : Ivresse
BIVALENT : Qui ne consid�re que deux valeurs
BIVOUAQUANT : Campant
BIZARROIDE : Etrange
BIZUTER : Brimer
BLAFARD : Pale
BLAGUEUSE : Qui plaisante
BLAIRER : Avoir de la sympathie
BLANCHE : Demie ronde
BLANCHEUR : Clart�
BLANCHISSANT : Disculpant
BLANCHISSEUSE : Laveuse
BLASERONT : Fatigueront
BLASONNER : Interpr�ter des armoiries
BLASTODERME : D�but d'embryon
BLASTULA : Forme embryonnaire
BLAZER : Veste
BLEMIR : P�lir
BLENNIES : Poissons d'eau douce
BLESE : Substitue
BLESOISE : Habitante d'une ville du Loir et Cher
BLET : Trop m�r
BLETTISSEMENT : Pourrissement
BLEU : Fromage
BLEUATRE : Tire sur la couleur du ciel
BLINDER : Prot�ger
BLOCAGE : Calage
BLOCUS : Investissement d'une ville
BLONDE : Souvent d�color�e
BLONDINETTE : Jeune su�doise
BLOQUEE : Coinc�e
BLOUSE : V�tement
BLUFF : Illusion
BLUTAGE : Tamisage de la farine
BLUTOIR : Tamis
BOBARD : Fausse nouvelle
BOBINE : Cylindre de fil
BOBINEUSE : Machine � enrouler
BOCAGE : R�gion de champs
BOGHEI : Cabriolet
BOHEME : Vie d�sordonn�e
BOIS : Cornes
BOISERIE : Ornement
BOISSEAUX : Partie d'un robinet
BOITEUSE : A un d�faut d'aplomb
BOITEUX : A un d�faut d'aplomb
BOITILLEMENT : Petit d�faut de marche
BOL : R�cipient
BOLET : Champignon
BOLIER : Filet de p�che
BOLOGNE : Ville italienne
BOMBANT : Rendant convexe
BOMBARDON : Contrebasse � vent
BOMBER : Rendre convexe
BOME : Espar
BONASSERIE : Bont� excessive
BOND : Saut
BONDERISATION : Protection contre la rouille
BONDISSANT : Sautant
BONHOMIE : Bont� de coeur
BONIFIE : Am�liore
BONJOUR : Salutation
BONNETEAU : Jeu de carte
BONNETTE : Petite voile
BONUS : Cadeau
BOOLEEN : Ne peu prendre que deux valeurs
BOOMERANG : Arme fid�le
BOQUETEAUX : Petits bois
BORA : Vent violent
BORDEE : Rang�e de canons
BORDEREAUX : Enum�rations �crites
BORDIGUE : Enceinte de claies
BOREAL : Du nord
BORIQUE : Type d'acide
BORNE : Marque de parcours
BOSCO : Cuisinier
BOSNIENNE : Habitante d'un pays de l'Est de l'Europe
BOSSE : Grosseur
BOSSELLE : D�former
BOSSOIR : Appareil de levage
BOSTON : Ville des Etats Unis
BOTANISTE : Sp�cialiste en plantes vertes
BOTTELAGE : Liage
BOTTER : Lier
BOTULISME : Empoisonnement
BOUBOULER : Crier
BOUCANER : Fumer
BOUCAU : Entr�e de port
BOUCAUD : Crevette grise
BOUCHARDE : Marteau � deux t�tes
BOUCHERIE : Carnage
BOUCHON : Flotteur
BOUCHONNER : Essuyer
BOUCLAIS : Passais un anneau dans le nez
BOUCLER : Passer un anneau dans le nez
BOUDDHISME : Religion
BOUDEUR : Qui marque du d�pit
BOUDIN : Boyau 
BOUDINER : Tordre
BOUEUSE : sale
BOUFFE : Op�ra
BOUFFIE : Boursoufl�e
BOUFFONNER : Faire rire
BOUGEANT : D�pla�ant
BOUGERAIENT : D�placeraient
BOUGONNE : R�le
BOUGONNEUR : R�leur
BOUILLE : Hotte
BOUILLEUR : Distillateur
BOUILLIONS : Remous
BOUILLISSAGE : Op�ration subie par la p�te � papier
BOUILLON : Aliment liquide
BOUILLONNER : Faire des plis � une robe
BOULANGISME : Mouvement politique
BOULE : Corps sph�rique
BOULER : Rouler
BOULETTE : B�vue
BOULEVERSER : Mettre en d�sordre
BOULIN : Support d'�chafaudage
BOULONNAIS : Assemblais
BOULONNER : Assembler
BOULOTTER : Manger
BOUQUETIERE : Marchande de fleurs
BOUQUINE : Lit
BOURBE : Amas de boue
BOURBON : Ancien nom de la R�union
BOURDE : Erreur grossi�re
BOURDONNER : Faire un bruit sourd et continu
BOURGEOISE : Citoyenne privil�gi�e
BOURGEONNE : a des boutons
BOURGES : Ville du centre de la France
BOURGUIGNON : Plat de boeuf
BOURLINGUEUSE : Aventuri�re
BOURRANT : Remplissant
BOURRE : Partie de la laine
BOURRELE : Tourment�
BOURRICHE : Panier
BOURSICOTER : Faire des op�rations en bourse
BOURSOUFLE : Enfl�
BOUSE : Fiente
BOUSILLER : Endommager gravement
BOUSTROPHEDON : Ancienne �criture
BOUT : Fin
BOUTEFEU : B�ton muni d'une m�che
BOUTERAS : Pousseras
BOUTIQUIER : Commer�ant
BOUTONNEUX : Acn�ique
BOUTURE : Jeune pousse
BOUVIER : Chien
BOVARYSME : Insatisfaction
BOVIDES : Famille de mammif�res
BOXE : Sport de combat
BOY : Domestique
BOYCOTTAGE : Cessation de toute relation
BOYCOTTER : Cesser toute relation
BR : Brome
BRACHIAL : Du bras
BRACHIOPODES : Animaux marins
BRACONNER : Chasseur
BRACTEE : Petite feuille
BRADERIE : Vente publique
BRAGUETTE : Ouverture d'un pantalon
BRAI : Produit d'�tanch�it�
BRAILLANT : Criant
BRAILLEMENT : Cri
BRAILLEUR : Crieur
BRAIRE : Crier
BRAISER : Cuire
BRAISIERE : Etouffoir
BRAN : Partie du son
BRANCARDIER : Porteur
BRANCHEMENT : Raccordement
BRANCHIES : Organes de respiration
BRANDADE : Plat de morue
BRANDIR : Agiter en l'air
BRANDON : Flambeau
BRANT : Po�te satirique alsacien
BRAQUE : Chien de chasse
BRAQUER : Tourner
BRASERO : Appareil de chauffage
BRASSE : Mesure de longueur
BRASSEUSE : Nageuse
BRAVANT : Affrontant le danger
BRAVOURE : Courage
BREDOUILLANT : Parlant de mani�re peu distincte
BREDOUILLER : Parler de mani�re peu distincte
BRELE : Attache
BRELOQUE : Petit bijou de fantaisie
BRESILLER : Tomber en poussi�re
BREST : Ville du Finist�re
BRETELLE : Courroie
BRETTE : Longue �p�e
BRETTEURS : Personnes qui aiment se battre � l'�p�e
BREVE : Courte
BREVETA : Prot�gea
BREVETAIS : Prot�geais
BREVETER : Prot�ger
BREVETERENT : Prot�g�rent
BREVETTENT : Prot�gent
BRIBES : Fragments
BRICOLAGE : Petit travail
BRICOLEUR : Sp�cialiste en petits travaux
BRIDE : Lien m�tallique unissant deux pi�ces
BRIDER : Serrer
BRIEFING : R�union tactique
BRIGADIER : Grade militaire
BRIGANTINE : Voile
BRILLANCE : Eclat
BRILLANTE : Lumineuse
BRILLE : Illumine
BRIMBALENT : Agitent
BRINDILLE : Petite branche
BRINGUEBALER : Balancer
BRIOCHE : P�tisserie
BRION : Pi�ce de charpente
BRIQUETANT : Pavant
BRIQUETTE : Agglom�rat servant de combustible
BRISCARD : Vieux soldat
BRISEES : Cass�es
BRISQUARD : Vieux soldat
BRITTONIQUE : Relatif aux peuples celtes de Grande-Bretagne
BROCANTEUSE : Commer�ante
BROCARDER : Piquer par des railleries
BROCHAGE : Reliure
BROCHETTE : Ensemble de petits morceaux de viande
BRODEQUIN : Chaussure
BROIE : Outil servant � briser le chanvre
BROMELIACEES : Famille de monocotyl�dones
BRONCHE : Conduit d'air
BRONCHITE : Inflammation
BRONZEE : Basan�e
BROQUETTE : Petit clou
BROSSER : Nettoyer
BROU : Enveloppe de fruit
BROUETTEE : Petit tombereau
BROUETTERAIENT : Transporteraient
BROUETTERIONS : Transporterions
BROUILLANT : Troublant
BROUILLENT : Troublent
BROUILLON : Premier jet
BROUSSAILLES : Buissons
BROUTAGE : Mouvement saccad�
BROUTER : Pa�tre
BROWNIEN : Type de mouvement d� � l'agitation mol�culaire
BROYER : R�duire en poudre
BRU : Belle-fille
BRUANT : Oiseau passereau des champs
BRUGNON : Sorte de p�che
BRUINE : Pluie fine
BRUISSEMENT : Bruit faible
BRUITE : Fait des bruits
BRULANT : Tr�s chaud
BRULERIE : Atelier o� l'on torr�fie le caf�
BRULURE : Effet du feu
BRUME : Trouble de l'atmosph�re
BRUN : Fonc�
BRUNE : Fonc�e
BRUNES : Fonc�es
BRUNI : Aspect d'un m�tal poli
BRUNIR : Polir
BRUNIRA : Polira
BRUNIRAI : Polirai
BRUNIRAIS : Polirais
BRUNIRAIT : Polirait
BRUNIS : Polis
BRUNISSEUR : Polisseur
BRUNS : Fonc�s
BRUSHING : Coiffure
BRUT : A l'�tat naturel
BRUTALEMENT : Sans d�licatesse
BRUTAUX : Violents
BRUTE : Personne grossi�re
BRUTES : Personnes grossi�res
BRUTS : A l'�tat naturel
BRYOLOGIE : Etude des mousses
BT : Basse tension
BTU : Unit� calorifique anglaise
BUBON : Inflammation
BUCCAUX : Dans la bouche
BUCHER : Travailler sans rel�che
BUCHEUSE : Travailleuse
BUCRANE : Motif ornemental
BUE : Absorb�e
BUEE : Vapeur
BUEES : Vapeurs
BUES : Absorb�es
BUFFLE : Mammif�re ruminant
BUGLE : Plante de la famille des labiac�es
BUISSON : Touffe
BULBE : Organe v�g�tal souterrain
BULGARIE : R�publique de la p�ninsule des Balkans
BULLE : Sceau attach� � un acte
BUNGALOW : Habitation indienne
BUREAUCRATE : Employ� administratif
BUREAUTIQUE : A remplacer la m�canographie
BURENT : Absorb�rent
BURGAUX : Grosses coquilles
BURINE : Grave
BURNOUS : Manteau
BUS : Moyen de transport
BUSE : Oiseau rapace
BUSQUE : Convexe
BUSTIER : V�tement f�minin
BUT : Point que l'on vise
BUTA : Heurta
BUTE : Heurte
BUTEE : Arr�toir
BUTEES : Arr�toirs
BUTER : Heurter
BUTERA : Heurtera
BUTERAI : Heurterai
BUTERAIS : Heurterais
BUTERAIT : Heurterait
BUTES : Heurtes
BUTINER : Amasser des provisions
BUTOIR : Pi�ce d'appui
BUTS : Points que l'on vise
BUTTERONS : Heurterons
BUTYREUX : Comme du beurre
BUTYROMETRE : Instrument de mesure de la richesse du lait
BUVAIT : Absorbait
BUVEE : Breuvage pour bestiaux
BUVIEZ : Absorbiez
BYZANTINISME : Aime discuter de questions subtiles
C : Pas de d�finition
CA : Calcium
CAB : V�hicule � cheval
CABALE : Interpr�tation de la Bible
CABANE : Abri
CABARETIERE : H�teli�re
CABILLAUD : Poisson
CABLEE : Reli�e
CABLOGRAMME : T�l�gramme
CABOCHARDE : Ent�t�e
CABOSSER : D�former
CABOTER : Naviguer
CABOTINE : Com�dienne
CABRI : Chevreau
CABS : V�hicules � cheval
CACA : Sale
CACAO : Graine 
CACAOYER : Petite sterculiac�e
CACHALOT : Mammif�re de l'ordre des c�tac�s
CACHER : Dissimuler
CACHETE : Planque
CACHOTTIER : Pas franc
CACOGRAPHIE : Orthographe vicieuse
CACTACEES : Famille de plantes dicotyl�dones
CAD : C'est � dire
CADASTRE : Document communal
CADAVERIQUE : P�le
CADE : Gen�vrier
CADEAUX : Pr�sent
CADENCE : Rythme
CADET : Ag� de quinze � dix-sept ans
CADETS : Ag�s de quinze � dix-sept ans
CADI : Juge
CADMIER : Prot�ger l'acier
CADRAN : Fen�tre
CADRER : Viser
CADUQUE : Obsol�te
CAECUM : Cul de sac
CAF : Vente maritime
CAFARDER : Rapporter
CAFE : Infusion
CAFES : Infusions
CAFETERIA : Lieu de restauration
CAFETIERE : Appareil � infuser
CAFOUILLER : Fonctionner de fa�on d�sordonn�e
CAFTEUR : Rapporteur
CAGET : Natte de paille sur laquelle on fait �goutter les fromages
CAGOT : Tartufe
CAHOTER : Secouer
CAILLAGE : Action de coaguler
CAILLASSE : Pierre
CAILLE : Oiseau
CAILLEBOTIS : Treillis de bois
CAILLOU : Pierre
CAIQUE : Bateau
CAISSERIE : Fabrique d'emballage
CAJOLANT : Caressant
CAL : Durillon
CALABRE : R�gion italienne
CALAIS : Ville du Nord de la France
CALAMBAC : Bois d'Insulinde
CALAMINE : R�sidu de combustion
CALANDRE : Enjoliveur
CALANQUE : Ria 
CALCARONE : Four
CALCIFEROL : Vitamine D
CALCIN : D�p�t calcaire
CALCIPHOBE : N'aime pas la craie
CALCUL : Concr�tion pierreuse
CALCULE : Evalue
CALDEIRA : D�pression volcanique
CALDWELL : Ecrivain am�ricain
CALE : Pi�ce de bois
CALEBASSE : R�cipient
CALECON : Sous-v�tement
CALEES : Dou�es
CALEPIN : Carnet
CALER : Coincer
CALERA : Coincera
CALERAI : Coincerai
CALERAIS : Coincerais
CALERAIT : Coincerait
CALES : Pi�ces de bois
CALFATER : Etancher
CALFEUTRER : Isoler
CALIBRER : Classer
CALICULES : A l'ext�rieur du calice chez certaines fleurs
CALIFORNIENNE : Am�ricaine
CALINER : Cajoler
CALISSON : Petit four en p�te d'amandes
CALLIGRAPHIER : Ecrire
CALMANTE : Reposante
CALMER : Apaiser
CALO : Argot espagnol
CALOMNIATEUR : Diffamateur
CALOMNIEUX : Contient des propos diffamateurs
CALORIFUGE : Emp�che les pertes
CALORIPORTEUR : Liquide de refroidissement
CALOT : Bonnet
CALOTS : Bonnets
CALOTTANT : Frappant
CALOYER : Moine Grec
CALQUANT : Imitant
CALS : Durillons
CALVINISME : Doctrine
CAMALDULE : Religieux de l'ordre de Saint-Romuald
CAMARGUAISE : Habitante d'une r�gion du Sud de la France
CAMBIAL : Du change
CAMBODGIENNE : Habitante d'Indochine
CAMBRE : Courbe
CAMBRIEN : De la premi�re p�riode de l'�re primaire
CAMBRIOLEUR : Voleur
CAMBUSE : Magasin contenant les vivres
CAMELIA : Fleur d'Asie orientale
CAMELLE : Tas de sel
CAMERA : Appareil de prise de vues
CAMERISTE : Femme de chambre
CAMEROUNAISE : Africaine
CAMIONNETTE : V�hicule utilitaire
CAMOUFLANT : D�guisant
CAMPAGNOL : Mammif�re rongeur
CAMPANIFORME : En forme de cloche renvers�e
CAMPANILE : Tour
CAMPER : S'installer de fa�on provisoire
CAMPHRE : Substance aromatique
CAMPING : Terrain am�nag�
CANADAIR : Avion canadien
CANAL : Conduit
CANALISER : Conduire
CANAPE : Fauteuil
CANARDEAUX : Jeunes palmip�des
CANARI : Esp�ce de Serin
CANCALE : Hu�tre
CANCAN : Bavardage
CANCERIGENE : Mauvais pour la sant�
CANCERISATION : D�g�n�rescence
CANCOILLOTTE : Fromage � p�te molle
CANDEUR : Puret�
CANDIDES : Innocents
CANE : Nom usuel de divers oiseaux aquatiques
CANEPETIERE : Petite outarde �   collier blanc
CANETTE : Bouteille
CANICULE : Grande chaleur
CANINE : Dent
CANNA : Plante herbac�e
CANNAGE : Fond de si�ge
CANNE : B�ton
CANNELER : Orner
CANNELLE : Robinet
CANNIBALISME : Pratique culinaire disparue
CANON : Arme � feu
CANONICAT : Office de chanoine
CANONIQUE : Conforme aux r�gles de l'�glise
CANONNIER : Soldat
CANOTE : Rame
CANTAL : Fromage � p�te ferme
CANTALOUP : Villa du pape
CANTER : Galop d'essai
CANTINIER : Restaurateur
CANTONADE : C�t� de la sc�ne d'un th��tre
CANTONNE : Limite
CANULANT : Ennuyeux
CANULER : Ennuyer
CAOUANNE : Tortue marine
CAOUTCHOUTEUX : Elastique
CAP : Pointe
CAPACITAIRE : Type de suffrage
CAPARACON : Housse
CAPE : Maneouvre de gros temps
CAPELANT : Poisson
CAPELER : Attacher
CAPES : Manteaux
CAPEYER : Attendre que �a se calme
CAPITAINE : Officier
CAPITAL : Bien
CAPITALISER : Amasser
CAPITEUSE : Qui porte � la t�te
CAPITON : Rembourrage
CAPITONNE : Rembourre
CAPITULATION : Reddition
CAPONNE : L�che
CAPORALISME : R�gime politique
CAPOTE : Manteau
CAPRICE : D�cision subite et irr�fl�chie
CAPRICORNE : Col�opt�re
CAPRIFICATION : Op�ration effectu�e sur les figuiers
CAPS : Pointes
CAPSULER : Boucher
CAPTAL : Capitaine de seigneur
CAPTATOIRE : Dans le but d'attraper
CAPTIEUSE : Qui cherche � tromper
CAPTIVE : Prisonni�re
CAPUCE : Chapeau pointu
CAPUCHON : Rabat
CAQUE : Barrique
CAQUETAGE : Discours de poule
CAR : V�hicule
CARABINE : Arme
CARACOLANT : Sautillant
CARACTERIEL : Perturb�
CARACTEROLOGIE : Science du comportement
CARAIBE : Des Antilles
CARAMBOLER : Coup au billard
CARAMBOUILLEUR : Escroc
CARAMELISATION : R�duction du sucre
CARAPATER : S'enfuir (se)
CARATE : Maladie de peau
CARAVANE : Groupe de voyageur
CARBET : Grande case
CARBONARISME : Soci�t� politique secr�te italienne
CARBONATE : Sel d'un acide
CARBONISER : Br�ler
CARBONISERIEZ : Br�leriez
CARBONYLE : M�lange utilis� pour prot�ger le bois
CARBURE : Combinaison de carbone avec un autre corps simple
CARCAILLANT : Criant
CARCASSONNE : Ville de l'Aude
CARCEL : Lampe � huile
CARCINOME : Cancer
CARDAN : Articulation
CARDER : Peigner
CARDIGAN : Chandail
CARDINAL : Pr�lat
CARDIOGRAPHE : Enregistreur
CARDIOPATHIE : Affection cardiaque
CARENANT : Nettoyant
CARENER : Nettoyer
CARENES : Parties immerg�es
CARESSE : Geste affectueux
CARGUANT : Serrant
CARI : Epice
CARIANT : G�tant
CARICATURAUX : Contrefaits
CARIE : Maladie cryptogamique du bl�
CARIER : G�ter
CARILLONNER : Faire savoir � grand bruit
CARINATE : Sous-classe d'oiseaux
CARLIN : Ancienne monnaie d'Italie
CARLISME : Partie politique
CARMEN : Nouvelle de M�rim�e
CARNAGE : Massacre
CARNAVAL : F�te
CARNE : Mauvais cheval
CAROLINGIEN : D'une dynastie
CAROTENE : Pigment
CAROTTAGES : Extractions
CAROTTE : L�gume
CAROUBE : Fruit
CARPETTE : Tapis
CARPILLON : Petite carpe
CARRARE : Marbre blanc
CARRELANT : Pavant
CARRELET : Grosse aiguille
CARRES : Formes g�om�triques
CARRIERE : Man�ge pour l'apprentissage de l'�quitation
CARROSSE : Voiture de luxe
CARROYANT : Quadrillant
CARS : V�hicules
CARTE : Pi�ce d'un jeu
CARTESIENNE : Rationnelle
CARTIER : Fabricant de jeux
CARTOGRAPHE : Dessinateur utile au voyageur
CARTON : Papier grossier
CARTONNERIE : Fabrique d'emballage
CARTOON : Dessin anim�
CARTOUCHIERE : Etui
CARYATIDE : Colonne
CAS : Circonstance
CASABLANCAIS : Habitant d'une ville du Maroc
CASAQUE : Blouse
CASBAH : Palais d'un chef
CASCADEUSE : Acrobate
CASE : Habitation
CASEEUX : De la nature du fromage
CASER : Mettre dans un compartiment
CASERA : Mettra dans un compartiment
CASERAI : Mettrai dans un compartiment
CASERAIS : Mettrais dans un compartiment
CASERAIT : Mettrait dans un compartiment
CASERNE : B�timent militaire
CASES : Habitations
CASH : Comptant
CASHER : Abattu selon les rites
CASQUE : Protection
CASSABLE : Fragile
CASSANT : Fragile
CASSE : Grande cuill�re  m�tallique
CASSEROLE : Ustensile de cuisine
CASSIE : Arbre des Antilles
CASSON : Pain de sucre
CASTEL : Grande b�tisse
CASTILLE : R�gion espagnole
CASTRAT : Chanteur italien
CASUISTE : Th�ologien
CASUISTIQUE : Etude des cas de conscience
CATACHRESE : M�taphore
CATACOMBES : Cimeti�res souterrains 
CATALAN : Langue romaine
CATALOGUANT : Inscrivant par ordre
CATALYSER : Provoquer une r�action
CATAPLASME : Bouillie m�dicinale
CATARACTE : Chute d'eau
CATARRHEUX : Atteint d'inflammation des muqueuses
CATATONIE : Syndrome de la schizophr�nie
CATCHEUSE : Lutteuse
CATECHISTE : Enseignant
CATEGORIE : Classe
CATGUT : Lien employ� en chirurgie
CATHARSIS : M�thode psychanalytique
CATHERINETTE : Jeune fille
CATHOLICISME : Religion
CATIN : Femme de mauvaises moeurs
CATOPTRIQUE : Partie de l'optique s'occupant de la r�flexion
CAUCASIENNE : Habitante d'une r�gion de la Russie
CAUCHEMARDEUX : Produit une impression tr�s d�sagr�able
CAUDAUX : De la queue
CAUSALE : Donne la raison
CAUSANTE : Communicative
CAUSERIE : Conversation
CAUSTIQUE : Corrosif
CAUTERISATION : br�lure
CAUTIONNER : Garantir
CAVALCADE : D�fil� pompeux
CAVALEUR : Coureur
CAVATINE : Air court
CAVE : Abri
CAVIAR : Oeufs
CAVICORNES : Type de ruminants
CB : Radio
CD : Disque
CE : C�rium
CEANS : Ma�tre du logis
CEDA : Abandonna
CEDILLE : Signe orthographique
CEDRAIE : Plantation d'arbres
CEDRATIER : Citronnier
CEINTURANT : Entourant
CELA : Pronom d�monstratif
CELADON : Amoureux platonique et sentimental
CELEBRANT : Officiant
CELERI : Plante potag�re
CELERIFERE : Anc�tre de la bicyclette
CELESTE : Divin
CELIBATAIRE : Qui vit seul
CELLERIER : Econome dans un monast�re
CELLULAR : Etoffe de coton
CELLULOID : Mati�re plastique
CELTIQUE : Langue indo-europ�enne
CEMENTANT : Chauffant
CEMENTATION : Chauffage
CENDRE : R�sidu
CENELLE : Fruit de l'aub�pine
CENOBITISME : Aust�rit�
CENSEE : Suppos�e
CENSIVE : F�odalit�
CENT : Adjectif num�ral
CENTAURE : Moiti� homme moiti� cheval
CENTON : Fait d'emprunts � divers auteurs
CENTRALISANT : R�unissant
CENTRALISER : R�unir
CENTRAUX : Principaux
CENTRIFUGE : Fuit le milieu
CENTRIPETE : Tend vers le milieu
CENTUPLANT : Multiplier
CEP : Pied
CEPAGE : plant
CEPE : Champignon
CEPEE : Touffe de tiges
CEPEES : Touffes de tiges
CEPES : Champignons
CEPHALOPODES : Mollusques
CEPS : Pieds
CERASTE : Serpent venimeux
CERCEAUX : Pi�ces d'un tonneau
CERCUEIL : Coffre
CEREALE : Plante � grains
CEREBRAUX : Qui concernent l'esprit
CEREMONIE : Politesse excessive
CERISAIE : Plantation d'arbres fruitiers
CERNER : Entourer
CERTAINE : Sans doute
CERTIFICATEUR : qui cautionne
CERTIFIE : Assure
CERUSE : Carbonate basique de plomb
CERVELAS : Saucisse
CERVICALE : Du cou
CERVIDES : Famille de ruminants
CES : Adjectif d�monstratif
CESARISME : Syst�me de gouvernement
CESSER : Interrompre
CESTES : Gants renforc�s
CET : Adjectif d�monstratif
CETACES : Ordre de mammif�res
CETOINE : Insecte de l'ordre des col�opt�res
CETTE : Adjectif d�monstratif
CH : Cheval 
CHABROT : Mettre du vin dans du bouillon
CHADBURN : Transmetteur d'ordres
CHAGRIN : Peine
CHAGRINER : Attrister
CHAHUTER : Importuner
CHAINE : Lien
CHAINEUR : Mesureur
CHAIRE : Tribune
CHALAND : Bateau
CHALCOPYRITE : Pyrite de cuivre
CHALET : Habitation en bois
CHALIT : Armature d'un lit
CHALLENGER : D�fier
CHALUMEAU : Fl�te champ�tre
CHAMAILLANT : se quereller (se)
CHAMAILLE : Querelle
CHAMARRER : Charger de passementeries
CHAMBARDEMENT : Bouleversement
CHAMBERY : Ville de Savoie
CHAMBRER : Acclimater
CHAMBRIERE : Fouet
CHAMELLE : Femelle � bosses
CHAMOISAGE : Tannage
CHAMOTTE : Argile cuite
CHAMPART : M�lange de froment d'orge et de seigle
CHAMPIGNON : V�g�tal sans fleurs et sans chlorophylle
CHAMPIONNAT : Epreuve sportive
CHAMPLEVENT : Gravent
CHAMPLEVER : Graver
CHAMPLEVERAS : Graveras
CHAMPLEVES : Graves
CHANCELER : Vaciller
CHANCEUSE : Favoris�e
CHANCIR : Moisir
CHANDELIER : Support
CHANFREINER : Tailler les coins
CHANGEMENT : Modification
CHANSON : Composition musicale
CHANSONNIER : Auteur
CHANTEAU : Rallonge
CHANTERELLE : Corde
CHANTOUNG : Etoffe de soie sauvage
CHANTOURNANT : D�coupant
CHANVRE : Plante � feuilles palm�es
CHAPARDE : Maraude
CHAPEAUTANT : Coiffant
CHAPELAIN : Pr�tre
CHAPELIERE : Malle 
CHAPERONNANT : Surveillant
CHAPITEAU : Partie sup�rieure d'un alambic
CHAPITRE : Division
CHAPONNANT : Castrant
CHAPTALISER : Sucrer
CHARADE : Enigme
CHARBONNAGE : Exploitation
CHARCUTER : Couper maladroitement
CHARDON : Plantes �pineuse
CHARGE : Fonction publique
CHARIOT : Pi�ce d'une machine qui porte l'outil
CHARIVARI : Tapage
CHARMANTE : Plaisante
CHARNUE : A la pulpe �paisse
CHAROGNE : Cadavre
CHARPENTER : Tailler des pi�ces de soutien
CHARRETIER : Conducteur
CHARRETTE : Voiture de charge � deux roues
CHARRIER : Emporter dans son cours
CHARTREUSE : Liqueur aromatique
CHARTRIER : Recueil de r�gles
CHASSEPOT : Fusil de guerre
CHASSER : Expulser
CHASSIS : Cadre
CHASSOIR : Outil
CHASUBLE : Manteau de pr�tre
CHATEAUBRIAND : Filet de boeuf grill�
CHATELAINE : Ornement de ceinture
CHATIE : Punit
CHATOUILLE : Larve de la lamproie
CHATOYANT : Qui a des reflets brillants
CHATRE : Castre
CHATTEMITE : Personne qui affecte un faux air de douceur
CHAUDE : Ardente
CHAUDRONNIERE : Personne qui fabrique des objets en t�le
CHAUFFARD : Mauvais conducteur
CHAUFFEUSE : Chaise basse
CHAULAIENT : Blanchissaient
CHAULE : Blanchit
CHAUME : Paille
CHAUSSEE : Partie de la voie publique am�nag�e pour la circulation
CHAUSSER : Entourer une plante de terre
CHAUVE : Pel�
CHAUVES : Pel�s
CHAUVINE : Aime son pays
CHAUVINS : Aiment leur pays
CHAVIRAIT : Se retournait
CHAVIRER : Se retourner
CHECHIA : Coiffure
CHEFFERIE : Organisme politique
CHELICERE : Appendice venimeux de l'araign�e
CHEMIN : Passage
CHEMINEMENT : Progression
CHEMISE : V�tement
CHENAUX : R�ceptacles de pluie
CHENEAU : R�ceptacle de pluie
CHENILLE : Larve
CHENUE : Blanchie
CHERBOURGEOIS : Habitant d'une ville de la Manche
CHERCHEUSE : Scientifique
CHERIE : Tendrement aim�e
CHERIF : Descendant de Mahomet
CHERUBIN : Ange
CHEVAL : Mammif�re de l'ordre des ongul�s
CHEVALERIE : Ordre cr�� par un souverain
CHEVALIERE : Bague
CHEVAUCHER : Empi�ter
CHEVECHE : Petite chouette
CHEVEUX : Poil
CHEVILLETTE : Petite pi�ce d'assemblage
CHEVRETTE : Petit ruminant
CHEVRETTES : Petits ruminants
CHEVRIER : Haricot
CHEVROTAIN : Ruminant sans bois d'Afrique et d'Asie
CHEVROTEMENT : Tremblement
CHEVROTER : Trembler
CHEVROTIN : Peau
CHEVROTINE : Plomb
CHIANTI : Vin rouge
CHIASME : Proc�d� stylistique
CHIC : El�gant
CHICANEUR : Aime faire des reproches
CHICHI : Simagr�e
CHICOT : Souche
CHIEN : Mammif�re domestique
CHIENDENT : Graminac�e nuisible aux cultures
CHIFFONNER : Froisser
CHIFFONNIER : Petit meuble
CHIFFREMENT : Codage
CHIGNOLE : Perceuse
CHILI : Pays d'Am�rique du Sud
CHIMERIQUE : Illusoire
CHIMIQUE : Pas naturel
CHIMPANZE : Singe
CHINE : Pays d'Asie
CHINEUR : Brocanteur
CHINOIS : Habitant d'un pays d'Asie
CHIPER : D�rober
CHIPIE : Coquine
CHIPOTANT : Faisant des difficult�s
CHIPOTEUR : Qui fait des difficult�s
CHIQUE : Morceau de tabac
CHIQUER : M�cher
CHIROMANCIEN : Voyant
CHISTERA : Sorte de raquette
CHITINE : Substance organique azot�e
CHLAMYDE : Manteau des anciens Grecs
CHLORALS : Obtenu par action du chlore sur l'alcool
CHLORE : Produit utilis� pour le blanchiment
CHLOROFORME : Anesth�sique
CHLOROPHYLLE : Pigment vert
CHLOROPLASTE : Si�ge de la photosynth�se
CHLORURE : Combinaison du chlore avec un autre corps
CHOCOLAT : P�te alimentaire solidifi�
CHOIR : Tomber
CHOISISSANT : Optant
CHOIX : Option
CHOLERA : Maladie contagieuse
CHOMEUSE : Inoccup�e
CHOPAIENT : Attrapaient
CHOPINE : Environ un demi-litre
CHOQUANTE : Blessante
CHOQUERONT : Blesseront
CHOREE : Danse de Saint-Guy
CHOREGRAPHE : Ballet
CHOREUTE : Choriste
CHORIZO : Saucisse
CHOSE : Etre inanim�
CHOUCAS : Oiseau
CHOUCROUTE : Plat alsacien
CHOUETTE : Oiseau Rapace
CHOURINER : Poignarder
CHREMEAU : Bonnet de toile
CHRETIENNEMENT : Religieusement
CHRISME : Logo
CHRISTIANISANT : Convertissant
CHROMAGE : D�p�t m�tallique
CHROMATOGRAPHIE : M�thode de s�paration
CHROME : Brillant
CHROMISTE : Retoucheur
CHROMOSOME : El�ment contenant les g�nes
CHRONIQUE : Article
CHRONOGRAPHE : Montre
CHRONOMETRER : Mesurer le temps
CHRYSALIDE : Entre chenille et papillon
CHRYSOCALE : Alliage imitant l'or
CHU : Tomb�
CHUCHOTER : Dire � l'oreille
CHUINTEMENT : Crie de la chouette
CHUT : Taisez vous
CHUTE : Vol plan�
CHUTER : Aux cartes, ne pas effectuer les lev�es pr�vues 
CHUTES : Vols plan�s
CHYLE : Liquide blanch�tre
CI : Adverbe de lieu
CIAO : Au revoir
CIBOIRE : Vase sacr�
CICATRICE : Trace permanente
CICATRISATION : Fermeture
CICERO : Unit� de longueur en imprimerie
CIEL : Partie de l'espace
CIF : Abr�viation commerciale anglaise
CIGARIERE : Ouvri�re cubaine
CIGUE : Plante v�n�neuse
CIL : Poil
CILLEMENT : Clin d'oeil
CILS : Poils
CIMENT : Liant
CIMENTER : Lier
CINABRE : Rouge vermillon
CINEMATIQUE : Etude des mouvements
CINERAIRES : Plante ornementale
CINETIQUE : Du mouvement
CINGLE : Fou
CINNAMIQUE : Extrait du baume du P�rou
CINQUANTENAIRE : Anniversaire particulier
CINTRE : Echafaudage
CIRANT : Faisant briller
CIRCONSCRIPTION : Division
CIRCONSCRIVANT : Tra�ant une limite
CIRCONSTANCIEL : Qui exprime les �l�ments secondaires
CIRCONVENAIENT : Cherchaient � tromper par des d�tours artificieux
CIRCONVENIEZ : Cherchiez � tromper par des d�tours artificieux
CIRCONVOISIN : Autour
CIRCUIT : R�seau
CIRCULAIRE : Rond
CIRCULATOIRE : Du syst�me sanguin
CIRCUMNAVIGATION : Tour du monde
CIRON : Animalcule qui vit dans les aliments
CIRQUE : Lieu destin� aux jeux publics
CIRRUS : Nuage
CISAILLES : Gros ciseaux
CISELA : D�coupa
CISELAIS : D�coupais
CISELEES : D�coup�es
CISELERAIENT : D�couperaient
CISELERIONS : D�couperions
CISELEZ : D�coupez
CISELURE : Art du ciseau
CISTE : Corbeille d'osier
CITADIN : Habitant d'une ville
CITERNE : R�servoir
CITHARE : Instrument � cordes
CITRINE : Pierre fine
CITRON : Fruit
CITROUILLE : Esp�ce de courge
CIVETTE : Mammif�re carnivore de la famille des viverrid�s
CIVILISANT : Rendant plus aimable et poli
CIVILISE : Rend plus aimable et poli
CI : Chlore
CLABAUDERIE : M�disance
CLABOTE : Assemble deux arbres
CLAIR : Lumineux
CLAIRETTE : Vin
CLAIRONNE : Annonce avec �clat
CLAIRVOYANT : Perspicace
CLAMER : Manifester par des cris
CLAMP : Pince chirurgicale
CLANDESTINITE : Cachette
CLAPIER : Cabane
CLAPOTANTE : Faisant des bruits d'eau
CLAPOTIS : Bruit de l'eau
CLAQUAGE : Distension
CLAQUEMENT : Bruit sec
CLAQUETTES : Danse
CLARIFIANT : Purifiant
CLARINETTISTE : Musicien
CLASSE : Distinction
CLASSIFIANT : Rangeant par cat�gories
CLASSIFIER : Ranger par cat�gories
CLAUDICANT : Boitant
CLAUSE : Disposition
CLAUSTRA : Grille de pierre
CLAVAIRE : Champignon
CLAVECINISTE : Musicien
CLAVETAGE : Assemblage
CLAVICULE : Os
CLAYON : Cl�ture
CLE : El�ment capital
CLEF : El�ment capital
CLEFS : El�ments capitaux
CLEMENT : Peu rigoureux
CLENCHE : Pi�ce du loquet
CLERGE : Ensemble des pr�tres
CLEROUCHIE : Colonie grecque dans l'Antiquit�
CLES : El�ments capitaux
CLICHAGE : Proc�d� utilis� dans l'imprimerie
CLICK : Bruit sec
CLIGNEMENT : Clin d'oeil
CLIGNOTE : S'allume et s'�teint
CLIMATISANT : Mettant � la bonne temp�rature
CLIMATISE : Met � la bonne temp�rature
CLIMAX : Terme final
CLINIQUE : Etablissement de soins
CLIPPER : Voilier
CLIQUETER : Faire du bruit
CLISSE : Enveloppe
CLIVANT : Fendant
CLOAQUE : Masse d'eau croupie
CLOCHARD : Mendiant
CLOCHETON : Ornement pyramidal
CLOISONNEMENT : S�paration
CLOITRE : Partie d'un monast�re
CLONE : Copie
CLOPINER : Boiter
CLOQUER : Se boursoufler
CLORE : Fermer
CLOSEAU : Petite m�tairie
CLOTURANT : Terminant
CLOU : Pi�ce de fixation
CLOUER : Fixer
CLOWN : Bouffon
CLOWNESQUE : Dr�le
CLUSE : Gorge
CLYSTERE : Lavement
CM : Unit� de longueur
CO : Cobalt
COAGULATION : Prise en masse
COALISER : R�unir
COALTAR : Goudron
COASSOCIE : Un des amis
COATI : Mammif�re d'Am�rique du Sud
COB : Cheval
COBALT : M�tal blanc rouge�tre
COBAYE : Petit mammif�re rongeur
COBEA : Liane du Mexique
COCAGNE : M�t
COCARDIER : Qui aime l'arm�e
COCCINELLE : Insecte col�opt�re
COCHENILLE : Puceron
COCHLEAIRE : Partie de l'oreille interne
COCHONNAILLE : Charcuterie
COCHONNET : Petite boule
COCON : Enveloppe
COCOTERAIE : Plantation d'arbres
COCOTTE : Poule
COCUFIE : Trompe
CODAGE : Action de rendre incompr�hensible
CODEMANDERESSE : Une de celles qui demandent en justice
CODETENU : Compagnon de cellule
CODIFIER : Eriger en syst�me
CODIRECTRICE : Dirigeante associ�e
COEFFICIENT : Partie num�rique d'un mon�me
COEQUIPIERE : Associ�e
COERCIBLE : Qui peut �tre comprim�
COFFRAGE : Moule
COGERANCE : Gestion commune
COGITATION : R�flexion
COGITE : R�fl�chit
COGNAIS : Frappais
COGNEMENT : Choc
COHERENCE : Liaison logique
COHEREUR : Appareil de r�ception
COHERITER : Partager un legs
COHESION : Adh�rence
COHUE : Foule
COIFFANT : Couvrant
COIFFEUSE : Table 
COIN : Lieu retir�
COINCE : Bloque
COINCIDENCE : Superposition
COING : Fruit
COINGS : Fruits
COINS : Poin�ons
COKE : Combustible
COL : Partie r�tr�cie
COLA : Arbre de la famille des sterculiac�es
COLCOTAR : Oxyde ferrique employ� pour polir le verre
COLERE : Irritation
COLIBRI : Oiseau passereaux d'Am�rique
COLINEAIRES : Align�s
COLIS : Paquet
COLLABORATEUR : Tra�tre
COLLAGE : Assemblage
COLLAPSUS : Affaiblissement
COLLATERAL : Bas-c�t� d'une �glise
COLLATIONNANT : Comparant
COLLECTER : R�unir
COLLECTION : Ensemble des mod�les
COLLECTIONNER : R�unir
COLLECTIVISER : Mettre au service du plus grand nombre
COLLEGE : R�union de personnes
COLLEGIENNE : El�ve
COLLETEE : Attraper
COLLEY : Chien de berger
COLLIMATEUR : Appareil de vis�e
COLLOIDALE : Qui a l'apparence de la colle
COLLUSION : Entente secr�te
COLLYBIE : Champignon
COLMATANT : Bouchant
COLOGNE : Ville du Gers
COLOMBE : Oiseau
COLOMBINE : Ordre d'oiseaux
COLONAGE : Bail
COLONEL : Grade d'officier
COLONIE : Territoire occup�
COLONNADE : Rang�e de pile
COLONNES : Supports
COLOPHANE : R�sine pour les archets
COLOQUINTE : Plante voisine de la past�que
COLORIMETRE : Appareil de mesure
COLOSSALE : Immense
COLOSSE : Grande statue
COLPORTEUR : Marchant ambulant
COLS : Parties r�tr�cies
COLT : Pistolet
COLTINE : Porte
COLTS : Pistolets
COLVERT : Canard
COMANDANT : Dirigeant
COMBATIF : Port� � la lutte
COMBATS : Luttes
COMBATTANT : Luttant
COMBATTRE : Lutter
COMBE : Vall�e
COMBIENTIEME : A quel rang
COMBINATEUR : Variateur de vitesse
COMBINE : Moyen
COMBURANT : Permet la combustion
COMEDIE : Pi�ce de th��tre
COMEDON : Point noir
COMIQUE : Dr�le
COMMA : Intervalle musical
COMMANDANT : Officier sup�rieur
COMMANDITAIRE : Bailleur de fonds
COMME : Conjonction
COMMEMORATION : Souvenir
COMMENCE : Entame
COMMENSALES : Qui s'acceptent
COMMENTAIRE : Remarque
COMMENTER : Faire des remarques
COMMERCE : Boutique
COMMERE : Femme bavarde
COMMETTRE : Faire un acte r�pr�hensible
COMMIS : Envoy�
COMMISSIONNAIRE : Personne de confiance
COMMISSURE : Point de jonction
COMMODE : Meuble
COMMODORE : Officier sup�rieur dans certaines marines
COMMOTIONNER : Ebranler
COMMUN : Ordinaire
COMMUNALISER : Confier � la ville
COMMUNARD : Partisan
COMMUNEMENT : Ordinairement
COMMUNICATION : Transmission
COMMUNION : Sacrement
COMMUNISME : Doctrine
COMMUTATEUR : Interrupteur
COMMUTER : Substituer
COMPACTAGE : Pilonnage
COMPACTE : Dense
COMPAGNE : Epouse
COMPARABLES : Semblables
COMPARAISON : Rapprochement
COMPARAISSANT : Se pr�sentant
COMPARATEUR : Instrument de pr�cision
COMPARER : Etablir des ressemblances
COMPARSE : Personnage muet
COMPARTIMENT : Case
COMPAS : Instrument de trac�
COMPASSER : Mesurer
COMPATIBLES : Qui s'accordent
COMPATIR : Etre touch�
COMPENDIUM : Abr�g�
COMPENSATOIRE : Qui remplace
COMPERE : Second
COMPETITEUR : Concurrent
COMPILANT : Rassemblant des morceaux
COMPLAINTE : Chanson
COMPLAISAMMENT : Avec orgueil
COMPLAISENT : Trouvent du plaisir
COMPLAIT : Trouve du plaisir
COMPLEMENT : Ce qu'il faut ajouter
COMPLETER : Ajouter
COMPLETIVE : Subordonn�e
COMPLEXE : Difficile � analyser
COMPLEXION : Temp�rament
COMPLIES : Apr�s v�pres
COMPLIMENTEUSE : Flatteuse
COMPLOTER : Pr�parer en secret
COMPONCTION : Gravit�
COMPORTEMENT : Conduite
COMPORTER : Se Conduire (se)
COMPOSANT : El�ment
COMPOSE : Tout form� de plusieurs parties
COMPOSITRICE : Musicienne
COMPOSTEUR : R�gle de typographe
COMPREHENSIF : Indulgent
COMPRENAIT : Saisissait
COMPRENDRAS : Saisiras
COMPRENDS : Saisis
COMPRENNENT : Saisissent
COMPRESSEUR : Ecraseur
COMPRESSIF : Qui restreint
COMPRIME : Aplati 
COMPRIRENT : Saisissent
COMPRIT : Saisit
COMPROMETS : Nuis
COMPROMETTENT : Nuisent
COMPROMETTIONS : Nuisions
COMPROMIS : Accommodement
COMPROMIT : Nuit
COMPTABILITE : Art de l'addition
COMPTANT : Sur l'heure
COMPTE : D�p�t
COMPULSAIS : Recherchais
COMPULSIEZ : Recherchiez
COMPULSOIRE : D�cision de justice
COMPUT : Calcul du temps
COMTE : Titre de noblesse
CONCASSANT : Broyant
CONCAVE : Creux
CONCEDER : Accorder
CONCEPT : Id�e
CONCERNANT : Au sujet de
CONCERTINO : Ensemble de solistes
CONCERTO : Composition symphonique
CONCESSION : Privil�ge
CONCEVAIENT : Cr�aient
CONCEVOIR : Cr�er
CONCHOIDAUX : QUI ressemblent � une coquille
CONCILE : R�union
CONCILIABULE : R�union secr�te
CONCILIE : R�union d'�v�ques
CONCITOYENS : Qui habitent la m�me ville
CONCLAVE : Assembl� de cardinaux
CONCLUAIENT : Terminaient
CONCLURE : Terminer
CONCLUSION : Arrangement d�finitif
CONCOMBRE : Cucurbitac�e
CONCOMITANCE : Coexistence
CONCORDE : Avion
CONCOURANT : Convergeant
CONCOURIR : Etre en comp�tition
CONCOURS : Coop�ration
CONCRET : R�el
CONCRETISATION : R�alisation
CONCUPISCENCE : Penchant � jouir des plaisirs sensuels
CONCURRENCE : Rivalit�
CONCUSSION : Malversation
CONCUSSIONNAIRE : Coupable de malversation
CONCUSSIONS : Malversations
CONDAMNATION : Peine
CONDENSABLE : Que l'on peut r�sumer
CONDENSEUR : Appareil r�frig�rant
CONDESCENDANT : C�dant
CONDESCENDES : C�des
CONDESCENDIONS : C�dions
CONDESCENDRE : C�der
CONDIMENT : Substance aromatique
CONDITIONNE : Emballe
CONDITIONNEL : Mode
CONDUCTANCE : Inverse de la r�sistance
CONDUCTIVITE : Inverse de la r�sistivit�
CONDUIRE : Mener
CONDUISAIENT : Menaient
CONDUISES : M�nes
CONDUISIEZ : Meniez
CONDUITES : Comportements
CONDYLE : Articulation
CONE : Coquillage
CONFECTIONNE : Fabrique
CONFEDERANT : R�unissant
CONFEDERER : R�unir
CONFERENCIER : Personne que l'on �coute
CONFERER : S'entretenir
CONFESSION : Aveu
CONFETTI : Petite rondelle de papier
CONFIANCE : Assurance
CONFIDENT : Personne de confiance
CONFIER : Dire un secret
CONFIGURER : Donner la forme
CONFINE : Enferm�
CONFINS : Limites
CONFIRMATION : Assurance de la v�racit�
CONFISCABLE : Que l'on peut saisir
CONFISERIE : Sucrerie
CONFISEUR : Qui fait des sucreries
CONFISQUE : Saisi
CONFIT : Morceau de viande conserv� dans la graisse
CONFITES : Conserv�es dans du sucre
CONFITURIER : R�cipient
CONFLUENT : Lieu de rencontre
CONFLUER : Se rejoindre
CONFONDANT : Se trompant
CONFONDIEZ : Vous trompiez
CONFORME : En accord
CONFORMITE : Analogie
CONFORT : El�ment du bien �tre
CONFORTABLE : Qui contribue au bien �tre
CONFRATERNITE : Bons rapports
CONFRONTER : Comparer
CONFUSEMENT : De fa�on brouill�e
CONGE : Permission de s'absenter
CONGEDIER : Renvoyer
CONGELA : Solidifia
CONGELAIS : Solidifiais
CONGELAT : Solidifi�t
CONGELERAI : Solidifierai
CONGELERIONS : Solidifierions
CONGELIONS : Solidifions
CONGENITAL : N� avec
CONGESTIONNE : Produit une accumulation 
CONGLOMERAT : M�lange
CONGLOMERER : M�langer
CONGLUTINER : Rendre gluant
CONGO : Pays africain
CONGRATULATIONS : F�licitations
CONGRATULER : F�liciter
CONGRE : Poisson marin
CONGREER : Surlier
CONGRU : Qui convient � la circonstance
CONGRUENCE : Convenance
CONICINE : Cicutine
CONIFERE : Ordre des gymnospermes
CONIROSTRE : Qui a un bec conique
CONJECTURALE : Repose sur des apparences
CONJOINT : Epoux
CONJOINTS : Epoux
CONJONCTIVE : Qui sert � unir
CONJONCTURE : Situation pr�sente
CONJUGAISON : Action de joindre
CONJUGUANT : Joignant
CONJUNGO : Mariage
CONJURER : Ecarter
CONNAISSAIS : Savais
CONNAISSEMENT : R�c�piss�
CONNAISSIEZ : Saviez
CONNAITRE : Savoir
CONNECTICUT : Un des �tats unis d'Am�rique
CONNEXION : Liaison
CONNOTATION : Sens plus g�n�ral
CONNURENT : Surent
CONOPEE : Voile qui enveloppe le tabernacle
CONQUE : Coquille
CONQUERAIS : Soumettais
CONQUERANT : Fier
CONQUERIEZ : Soumettiez
CONQUERIR : Soumettre
CONQUISTADOR : Aventurier espagnol
CONSACRIONS : D�dions
CONSCIENCIEUSE : Scrupuleuse
CONSCRIPTION : Syst�me de recrutement
CONSECRATEUR : Ev�que qui en sacre un autre
CONSECUTION : Encha�nement
CONSEIL : Avis
CONSEILLER : Recommander
CONSENTEMENT : Accord
CONSENTIES : Accord�es
CONSENTIR : Acquiescer
CONSEQUENCE : Suite
CONSEQUENT : Second terme d'un rapport
CONSERVE : Aliment st�rilis�
CONSERVER : Maintenir en l'�tat
CONSIDERAIENT : Regardaient attentivement
CONSIDERENT : Regardent attentivement
CONSIGNATAIRE : D�positaire
CONSIGNENT : Mettent en d�p�t
CONSIGNER : Mettre en d�p�t
CONSISTANCE : Fermet�
CONSISTOIRE : Assembl�e de cardinaux
CONSOL : Proc�d� de navigation
CONSOLE : Support
CONSOLER : Soulager la peine
CONSOMMATEUR : Client
CONSOMME : Bouillon
CONSOMMER : Boire un verre
CONSOMPTIVE : Amaigrissante
CONSONNE : Type de lettre
CONSORT : Mari de la reine
CONSPIRE : S'accorde dans un mauvais dessein
CONSTABLE : Officier de police
CONSTANTIN : Empereur romain
CONSTAT : Proc�s-verbal
CONSTATE : Prend connaissance
CONSTELLE : Couvre de choses brillantes
CONSTERNATION : Abattement
CONSTERNEE : Abattue
CONSTITUER : Composer un tout avec divers �l�ments
CONSTRICTEUR : Muscle
CONSTRUCTEUR : B�tisseur
CONSTRUCTIF : Propre � cr�er
CONSTRUIRE : B�tir
CONSUL : Magistrat romain
CONSULTE : Cour de justice
CONSULTER : Prendre conseil
CONSUMER : D�truire
CONTACT : Relation
CONTACTEUR : Interrupteur
CONTAGE : Vecteur de maladie
CONTAGIEUX : Communicatif
CONTAINER : Grosse bo�te
CONTE : R�cit
CONTEMPLER : Qui regarde avec soin
CONTEMPORAIN : De notre �poque
CONTENAIS : Renfermais
CONTENIR : Renfermer
CONTENT : Heureux
CONTENTEMENT : Satisfaction
CONTENTIEUX : Litige
CONTENU : Ce qui est � l'int�rieur
CONTESTATION : Conflit
CONTEUSE : Qui aime raconter des histoires
CONTEXTE : Ensemble de circonstances
CONTIENDRAIENT : Renfermaient
CONTIENT : Renferme
CONTIGUITE : Contact
CONTINENT : Vaste �tendue de terre
CONTINENTALITE : Caract�ristique climatique
CONTINGENCE : Eventualit�
CONTINU : Sans division
CONTINUATION : Prolongement
CONTINUELLEMENT : Toujours
CONTINUMENT : Sans cesse
CONTORSION : Grimace
CONTOURNER : Eviter
CONTRACTEE : Nerveuse
CONTRACTUELLE : Aubergine
CONTRADICTION : Incompatibilit�
CONTRAIGNANT : Emb�tant
CONTRAINDRE : Obliger
CONTRAIRE : Qui n'est pas conforme
CONTRALTO : Chanteuse
CONTRAPUNTISTE : Compositeur
CONTRARIETE : Ennui
CONTRAROTATIF : Tournant en sens contraire
CONTRASTE : Opposition
CONTRAVENTION : Infraction
CONTRE : Tout pr�s
CONTREBANDE : Commerce illicite
CONTREBASSE : Instrument � cordes
CONTREBASSISTES : Musiciens
CONTREBASSON : Instrument � vent
CONTREBATTRE : Riposter
CONTRECARRER : S'opposer
CONTRECHAMP : Prise de vue
CONTRECLEF : Pi�ce d'une vo�te
CONTREDANSE : Contravention
CONTREDIRE : Etre en opposition
CONTREFAIRE : Reproduire
CONTREFAITE : Imit�e
CONTREFICHER : Se moquer
CONTREFORT : Pilier de renforcement
CONTREMAITRE : Chef
CONTREMARCHES : Parois verticales d'un escalier
CONTREPARTIE : Echange
CONTREPOIDS : Objet servant � �quilibrer
CONTRESCARPE : Talus
CONTREVENIR : Agir contrairement � une prescription
CONTREVENTEMENT : Assemblage qui renforce une construction
CONTREVERITE : Sorte de mensonge
CONTRIBUANT : Aidant
CONTRIBUTION : Part
CONTROLER : Dominer
CONTROUVE : Invent� de toutes pi�ces
CONTROVERSABLE : Qui peut �tre discut�
CONTUMACE : Absence
CONTUSIONNER : Blesser
CONVAINCANT : Probant
CONVAINCANTE : Probante
CONVAINCRE : Persuader
CONVAINCU : Persuad�
CONVALESCENT : mieux portant
CONVENABLE : Opportun
CONVENANCE : Commodit�
CONVENT : Assembl�
CONVENTION : Accord
CONVERGENCE : Point de rencontre
CONVERSATION : Entretien
CONVERTIBILITE : Propri�t� d'�tre chang�
CONVERTISSANT : Changeant
CONVICT : Criminel
CONVIENDRAIS : Irais
CONVIENDRONS : Irons
CONVIENNENT : Vont
CONVIER : Inviter
CONVIVE : Participant � un repas
CONVOCATION : Rendez-vous
CONVOITER : D�sirer
CONVOLER : Se marier
CONVOQUANT : Donnant rendez-vous
CONVOYEUR : Transporteur
CONVULSION : Contraction
CONVULSIVEMENT : Par contractions
COOPERATION : Aide
COOPERER : Aider
COOPTANT : Admettant
COORDINATION : R�union
COORDONNEES : El�ments permettant de d�terminer la position d'un point
COPAIN : Camarade
COPAL : R�sine
COPEAU : Parcelle de bois ou de m�tal
COPIER : Reproduire
COPIEUX : Abondant
COPILOTE : Second
COPISTE : Auteur sans originalit�
COPRAH : Amande de coco s�ch�e
COPTE : Egyptien ancien
COQ : Oiseau domestique
COQUART : Ecchymose
COQUE : Enveloppe
COQUELUCHE : Maladie contagieuse
COQUET : Qui cherche � plaire
COQUETTEMENT : De fa�on � plaire
COQUILLART : Pierre calcaire renfermant des coquilles
COQUILLIER : Former des boursouflures sur la cro�te du pain
COQUINE : Espi�gle
COR : Durillon
CORAIL : Animal des mers chaudes
CORALLIAIRE : Anthozoaire
CORALLINE : Algue marine
CORBEILLE : Sorte de panier
CORDAGE : Lien servant � une manoeuvre
CORDEAUX : Cordes utilis�es pour aligner
CORDEE : Groupe d'alpinistes
CORDER : Tordre
CORDIALITE : Bienveillance
CORDIFORME : Comme un coeur
CORDITE : Explosif
CORDONNER : Tortiller
CORFOU : Ile grecque
CORINTHE : Ville grecque
CORNAC : Conducteur d'�l�phant
CORNARD : Mari tromp�
CORNEE : Peau transparente
CORNER : Plier
CORNICHE : Moulure
CORNIERE : Pi�ce d'acier profil�e
COROLLAIRE : Cons�quence n�cessaire et �vidente
CORONAIRE : Art�re
CORONARITE : Inflammation
CORONOGRAPHE : Instrument regardant le soleil
CORPORATISME : Doctrine �conomico-sociale
CORPULENCE : Grande taille
CORPUS : Recueil
CORRASION : Usure
CORRECT : Conforme aux r�gles
CORRECTEMENT : De fa�on conforme aux r�gles
CORREGIDOR : Autrefois, officier de justice espagnol
CORRELATIF : Qui est en relation avec une autre chose
CORRELATION : Relation r�ciproque entre deux choses
CORRESPONDANCE : Echange de lettres
CORRESPONDRE : Communiquer
CORREZIEN : Habitant du massif central
CORRIDA : Course de taureaux
CORRIDOR : Passage �troit
CORRIGENT : Rendent meilleur
CORRIGIBLE : Peut �tre am�lior�
CORROBORANT : Confirmant
CORROBORER : Confirmer
CORRODE : Ronge
CORROI : Fa�on donn�e au cuir
CORROMPRE : Pervertir
CORROMPU : G�t�
CORROSIF : Qui ronge
CORROYAGE : Assouplissement du cuir
CORRUPTEUR : Qui pervertit
CORSAGE : Blouse
CORSAIRE : Marin
CORSE : Dialecte m�diterran�en
CORSELET : Cuirasse l�g�re
CORSER : Donner de la consistance
CORSERAIT : Donnait de la consistance
CORSET : Sous-v�tement f�minin
CORSETER : Serrer
CORSO : D�fil� de chars
CORTEX : Ecorce c�r�brale
CORTICALE : De l'�corce
CORTON : Vin de C�te d'Or
CORUSCANT : Brillant
CORVEE : Travail fastidieux
CORVETTE : B�timent de guerre
CORVIDE : Famille d'oiseaux passereaux
CORYBANDE : Pr�tre de Cyb�le
CORYPHEE : Chef de choeur dans le th��tre grec
CORYZA : Inflammation du nez
COSAQUE : Soldat russe
COSINUS : Sinus du compl�ment d'un angle
COSMODROME : Base de lancement
COSMOLOGIE : Science des lois de l'univers
COSMONAUTE : Pilote
COSSARD : Paresseux
COSSETTE : Fragment de betterave � sucre coup� en lamelles
COSSU : Riche
COSTAL : Des c�tes
COSTAUD : Fort
COSTUME : Habit de th��tre
COSY : Enveloppe de th�i�re 
COTE : Mont�e
COTER : Estimer
COTIER : Pr�s de terre
COTISANT : Qui paye
COTONNADE : Etoffe
COTONNEUX : Recouvert de duvet
COTOYER : S'approcher de
COTRE : Bateau
COTYLE : Cavit� d'un os
COTYLEDON : Lobe du placenta des ruminants
COUAC : Canard
COUARD : Poltron
COUARDISE : L�chet�
COUCHANT : Ouest
COUCHER : Etendre
COUCHIS : Lattis d'un plancher
COUDE : Articulation
COUDER : Plier
COUDOYER : Etre en contact
COUFFA : Bateau sur le Tigre
COUFFIN : Cabas
COUINER : Pousser de petits cris
COULEMELLE : Champignon comestible
COULER : Immerger
COULEUVRE : Serpent
COULISSE : Pi�ce de bois pr�sentant une rainure
COULISSEAU : Pi�ce qui se d�place dans une ralingue
COULOIR : Passage
COUMARINE : Substance odorante extraite de la f�ve tonka
COUP : Choc
COUPAGE : M�lange
COUPE : Verre
COUPEE : Acc�s lat�ral
COUPER : Diviser
COUPEROSE : Sulfate
COUPES : Verres
COUPLA : Attacha
COUPLE : Paire
COUPLER : Attacher
COUPLERA : Attachera
COUPLERAIT : Attacherait
COUPLES : Paires
COUPLET : Strophe
COUPLEUR : Dispositif d'accouplement
COUPS : Chocs
COUQUE : G�teau flamand
COUR : Espace clos de murs
COURAGE : Audace
COURAGEUX : Audacieux
COURANT : Jus
COURBATURE : Douleur
COURBETTE : R�v�rence
COURCAILLER : Cri de la caille
COURGE : Plante potag�re
COURGETTE : Fruit allong�
COURIR : Aller rapidement
COURLIS : Oiseau �chassier migrateur
COURONNE : Ornement
COURROUCENT : Mettent en col�re
COURS : Le�on
COURSE : Epreuve de vitesse
COURSIVE : Passage dans un bateau
COURT : Terrain de sport
COURTILIERE : Insecte de l'ordre des orthopt�res
COURTINE : Rideau de lit
COURTISER : Chercher � plaire
COURTOISIE : Politesse
COURU : Recherch�
COUSETTE : Jeune couturi�re
COUSIN : Moustique
COUSINAGE : Parent�
COUSSIN : Sac rembourr�
COUT : Prix
COUTEAU : Instrument tranchant
COUTELAS : Ep�e courte et large tranchante sur un seul c�te
COUTER : Valoir
COUTUME : Habitude
COUTUMIERE : Habitu�e
COUVAIN : Ensemble des oeufs des abeilles
COUVENT : Maison religieuse
COUVERTURE : Tissus protecteur
COUVEUSE : Incubateur
COUVI : Oeuf � demi couv�
COUVOIR : Nid
COUVRENT : Prot�gent
COUVRIR : Prot�ger
COVARIANCE : Moyenne
COXAUX : De la hanche
COYAU : Pi�ce prolongeant le chevron
COYOTE : Mammif�re carnivore d'Am�rique
CR : Chrome
CRABE : Crustac�
CRABIER : Esp�ce de h�ron
CRABOT : Dent d'entra�nement
CRABOTAGE : Dispositif d'embrayage
CRACHE : Projette
CRACHIN : Pluie fine
CRACK : Champion
CRACKING : Proc�d� de raffinage
CRACOVIENNE : Danse polonaise
CRAIE : Calcaire d'origine marine
CRAINDRE : Redouter
CRAINTE : Appr�hension
CRAINTIVEMENT : Avec appr�hension
CRAMOISI : Rouge fonc�
CRAMPE : Contraction involontaire
CRAMPILLON : Clou recourb� � deux pointes
CRANER : Faire le malin
CRANEUSE : Pr�tentieuse
CRAPAUD : Batracien
CRAPAUDINE : Palier de base d'un axe vertical
CRAPOUILLOT : Petit mortier de tranch�e
CRAPULE : Individu tr�s malhonn�te
CRAQUE : Mensonge
CRAQUELANT : Fendillant
CRAQUELIN : Biscuit sec
CRAQUEMENT : Bruit sec
CRASSEUX : Salle
CRAVACHE : Baguette pour stimuler
CRAWL : Nage
CRAYON : Baguette de bois laissant une trace
CREANCE : Cr�dit
CREATINE : Substance azot�e dans le plasma sanguin
CREATURE : Etre
CRECHE : Mangeoire
CREDIRENTIERE : Cr�anci�re
CREDITER : Inscrire au compte
CREDULITE : Facilit� � croire
CREMATION : Incin�ration
CREME : Mati�re grasse
CREMEUX : Onctueux
CREMONE : Verrou
CRENEAU : Ouverture pratiqu�e dans un mur
CRENELURE : Dentelure
CREOLE : Langue des Antilles
CREOSOTER : Rendre le bois plus r�sistant aux moisissures
CREPE : Galette
CREPINE : Filtre
CREPIR : Enduire
CREPITE : P�tille
CREPU : Court et fris�
CRESCENDO : En croissant
CRESYL : Produit d�sinfectant
CRETINISME : Stupidit�
CRETOISE : Habitante d'une �le grecque
CRETONNE : Tissus de coton
CREUSET : R�cipient en terre r�fractaire
CREUX : Vide
CREVAISON : Eclatement
CREVASSES : Fentes
CREVER : Epuiser
CREVERAIENT : Epuiseraient
CREVERIONS : Epuiserions
CREVETTIER : Filet
CRI : Eclat de voix
CRIAILLERIES : Querelles
CRIBLAGE : Triage m�canique
CRIBLURE : Mauvaises graines
CRIC : Appareil de levage
CRICKET : Jeu de balle anglais
CRICOIDE : Cartilage du larynx
CRICRI : Grillon
CRIEE : Vente publique
CRIER : Proclamer
CRIME : Violation grave de la loi morale
CRIMINOLOGIE : Science fond�e sur la psychologie, la sociologie et la statistique
CRIN : Poil long et rude
CRINOIDE : Classe d'�chinodermes
CRINOLINE : Jupon bouffant
CRISE : Mauvais moment
CRISPE : Contracte
CRISS : Poignard malais
CRISSEMENT : Bruit aigu
CRISSER : Faire entendre un bruit aigu
CRISTALLIN : Tr�s transparent
CRISTALLOIDE : Corps dissous pouvant �tre dialys�
CRITERE : Principe auquel on se r�f�re
CRITERIUM : Epreuve sportive
CRITIQUE : Jugement
CROATIE : Pays de l'Est de l'Europe
CROC : Grappin
CROCHETER : Ouvrir une serrure
CROCHU : Recourb� en pointe
CROCODILE : Reptile africain et indien
CROCUS : Plante herbac�e � bulbe
CROISADE : Exp�dition
CROISE : Mode d'entrelacement des fils d'un tissus
CROISEUR : Navire de guerre
CROMLECH : Monument m�galithique
CROMORNE : Ancien instrument de musique � vent
CROQUANT : Paysan
CROQUEMBOUCHE : Pi�ce mont�e en petits choux caram�lis�s
CROQUET : Petit biscuit sec aux amandes
CROQUIGNOLETTE : Mignonne
CROSNE : Plante cultiv�e comme l�gume 
CROSSE : B�ton
CROTTE : Fiente
CROULANT : Tombant
CROUPADE : Saut de cheval
CROUPIERE : Partie du harnais
CROUPION : Base de la queue
CROUSTILLANT : Qui abonde en d�tails piquants
CROUTEUX : Qui a des plaques
CROYANCE : Foi
CRU : Terroir
CRUAUTE : F�rocit�
CRUCHE : Vase � anse
CRUCIAL : Fondamental
CRUCIVERBISTE : Vous l'�tes probablement
CRUE : Gonflement d'un cours d'eau
CRUEL : Qui aime faire souffrir
CRUELS : Qui aiment faire souffrir
CRUENTE : A vif
CRUOR : Partie du sang qui se coagule
CRURALE : Des jambes
CRUZEIRO : Monnaie de Br�sil
CRYOLITHE : Fluorure naturel d'aluminium et de sodium
CRYOSTAT : Appareil de r�frig�ration
CRYPTOGRAMME : Message cod�
CS : Caesium
CU : Cuivre
CUBA : Ile dans la mer des Cara�bes
CUBEBE : Arbuste d'Insulinde voisin du poivrier
CUBISME : Ecole artistique moderne
CUBITIERE : Pi�ce d'armure
CUEILLAIENT : Prenaient
CUEILLENT : Prennent
CUEILLIR : Prendre
CUILLERE : Ustensile de table
CUIR : Peau �paisse
CUIRASSE : Protection de fer
CUIRASSIER : Soldat de cavalerie
CUISEUR : Grande Marmite
CUISINER : Interroger
CUISINIERE : Appareil m�nager
CUISSARD : Culotte
CUISSARDES : Bottes
CUISSEAU : Partie du veau
CUIT : Perdu
CUIVRE : M�tal rouge
CUL : Fond
CULASSE : Partie du canon
CULBUTE : Cabriole
CULER : Aller en arri�re
CULEE : Massif de ma�onnerie
CULERON : Partie de la croupi�re
CULIERE : Sangle attach�e � la naissance de la queue du cheval
CULMINANT : Le plus haut
CULMINE : Est au sommet
CULOTTE : V�tement
CULPABILITE : Complexe
CULTE : Hommage
CULTIVATEUR : Agriculteur
CULTURE : Ensemble des connaissances
CUMEX : Cousin
CUMIN : Graine aromatique
CUMULARD : Personne tr�s occup�e
CUMULER : Entasser
CUPIDITE : Avidit�
CUPULE : Organe enveloppant certains fruits
CURAGE : Nettoyage
CURARE : Poison
CURATEUR : Administrateur de biens
CURE : Traitement m�dical
CURETTE : Instrument chirurgical
CURIE : Physicien fran�ais qui d�couvrit la pi�zo-�lectricit�
CURIEUSE : Avide de conna�tre
CURION : Chef d'une curie romaine
CURIUM : El�ment radioactif
CUSTODE : Panneau lat�ral de la carrosserie
CUTINE : Substance imperm�able
CUVAGE : Fermentation
CUVELAGE : Rev�tement int�rieur d'un puits de mine
CV : Cheval
CX : Coefficient de tra�n�e
CYANOSE : Coloration de la peau
CYBERNETICIENNE : Sp�cialiste en m�canisme de communication
CYCLE : P�riode de r�p�tition
CYCLOIDE : Courbe d�crite par un point d'un cercle qui roule
CYCLONE : D�pression
CYCLOPE : Petit crustac� des eaux douces
CYCLOTHYMIE : Forme d'ali�nation mentale
CYLINDREE : Volume
CYLINDRER : Soumettre au rouleau
CYMBALIER : Percussionniste
CYNIQUEMENT : A la fa�on de Diog�ne
CYON : Chien sauvage d'Asie
CYPHOSE : D�viation
CYRILLIQUE : Type d'alphabet
CYSTOSCOPIE : Examen m�dical
CYTOLOGIE : Etude des cellules
CYTOPLASME : Partie fondamentale de la cellule
D : Pas de d�finition
DA : Particule qui renforce parfois l'affirmation
DACTYLE : Gramin�e fourrag�re
DACTYLOGRAPHIE : Ecriture
DAGUE : Ep�e � lame large et courte
DAHIR : D�cret du roi du Maroc
DAIGNER : Vouloir bien
DAIS : Ouvrage suspendu
DALLEUR : Personne qui pave
DALMATIEN : Chien
DALOT : Trou d'�coulement
DALTONISME : Trouble de la vue
DAM : Pr�judice
DAMAN : Mammif�re ongul� herbivore
DAMAS : Etoffe de laine ou de soie d�cor�e
DAMASQUINAGE : Incrustation de filet d'or dans un objet
DAME : Pion doubl�
DAMER : Doubler un pion
DAMEUR : Rouleau compresseur
DAMIER : Tableau de cent cases
DAMNE : Qui est en enfer
DAMPER : Amortisseur
DAN : Degr� de qualification
DANDINANT : Balan�ant
DANDINEMENT : Balancement
DANGEREUSEMENT : En prenant des risques
DANOIS : Chien � poils ras
DANS : Pr�position de lieu
DANSANTE : Bougeante
DANSE : Mouvement du corps
DANSER : Bouger
DANSEUSE : Position d'un cycliste
DANSEZ : Bougez
DAPHNIE : Petit crustac� des eaux douces
DARDENT : Lancent
DARTROSE : Maladie de la pomme de terre
DARWINISME : Doctrine
DATATION : Action d'indiquer le moment
DATERIE : Tribunal de la chancellerie de la cour de Rome
DATTE : Fruit sucr� Africain
DAUBER : D�nigrer
DAUPHIN : Mammif�re marin
DAVIER : Rouleau mobile autour d'un axe
DB : Unit� d'intensit� du son
DE : Protection du doigt
DEAMBULANT : Se promenant
DEBACHER : D�couvrir
DEBALOURDER : Enlever le d�s�quilibre
DEBAPTISER : Changer de nom
DEBARCADERE : Quai
DEBARDER : D�charger
DEBARQUER : Aller � terre
DEBARRASSER : Enlever
DEBATTAIS : Discutais
DEBATTENT : Discutent
DEBATTRE : Discuter
DEBAUCHER : Renvoyer
DEBET : Reste
DEBILITE : Arri�ration mentale
DEBINER : D�nigrer
DEBITER : Couper en morceaux
DEBITEUR : Celui qui doit
DEBLATERE : Parle avec violence
DEBLAYAGE : Action de d�barrasser
DEBLOQUER : D�gager
DEBOISAGE : Arrachage des arbres
DEBOITER : Sortir d'un alignement
DEBONDER : Ouvrir
DEBONNAIRE : Bon jusqu'� la faiblesse
DEBORDEE : D�pass�e
DEBOSSELE : Redresse
DEBOUCHANT : Sortant
DEBOUCHERAI : Sortirai
DEBOUCLER : D�tacher
DEBOULE : Arrive
DEBOULONNE : D�monte
DEBOURBER : Tirer d'embarras
DEBOURRAGE : Nettoyage de la laine
DEBOURSE : Paye
DEBOUTE : Rejette la demande
DEBOUTONNANT : D�shabillant
DEBRAILLE : Mal habill�
DEBRIDE : Effr�n�
DEBROCHAGE : Extraction
DEBROUILLARD : Malin
DEBROUILLER : Eclaircir
DEBUCHER : Sortir du bois
DEBUSQUER : Faire sortir du bois
DEBUTE : Commence
DECACHETE : Ouvre
DECADE : P�riode
DECAGONALE : A dix angles
DECAISSEMENT : Paiement
DECALAMINE : Nettoie
DECALCIFICATION : Affaiblissement des os
DECALER : D�placer
DECALQUER : Reproduire
DECAMPER : Fuir
DECANILLANT : S'enfuyant
DECANTER : Eclaircir
DECAPANT : Nettoyant
DECAPER : Nettoyer
DECAPITER : Raccourcir
DECAPODES : Crabes
DECAPSULANT : Ouvrant
DECARBURATION : Traitement d'un produit m�tallurgique
DECATHLON : Epreuve sportive
DECATIR : Soumettre � l'action de la vapeur
DECAVE : Qui a tout perdu
DECELA : D�couvrit
DECELER : D�couvrir
DECELERER : Ralentir
DECEMMENT : Raisonnablement
DECENNIE : P�riode
DECENTRAGE : D�calage
DECENTRALISER : Donner de l'autonomie
DECERCLANT : D�montant un tonneau
DECEVANT : Trompeur
DECEVRAIENT : Tromperaient
DECHANTER : Oublier ses esp�rances
DECHARGE : D�potoir
DECHARGER : Vider
DECHAUMER : Enterrer
DECHAUSSEMENT : Mise � nu
DECHAUSSER : D�pouiller par la base
DECHET : Reste
DECHIFFRER : Deviner
DECHIQUETANT : Coupant
DECHIQUETURE : Taillade
DECHIRURE : Rupture
DECHOIR : Tomber
DECHU : Qui a perdu son innocence
DECIDE : Qui n'h�site pas
DECIDEMENT : En d�finitive
DECILITRE : Unit� de volume
DECIMAL : A la base dix
DECIMETRE : Unit� de longueur
DECISIVE : Tranchant
DECLAMATOIRE : Pompeux
DECLARATION : Discours
DECLASSANT : D�rangeant
DECLASSES : D�rang�s
DECLAVETER : D�monter
DECLENCHEUR : Organe de mis en route
DECLINAISON : A l'�quateur, hauteur du soleil � midi
DECLINE : Rejette
DECLIVE : Qui va en pente
DECOCHE : Lance
DECOCHER : Lancer
DECODE : D�chiffre
DECOFFRE : D�moule
DECOIFFENT : Emm�lent
DECOINCE : D�gage
DECOLLER : D�tacher
DECOLLETEUR : Ouvrier
DECOLONISATION : Lib�ration
DECOLOREE : P�le
DECOMBRES : Gravats
DECOMMANDER : Annuler
DECOMPOSER : S�parer
DECOMPRIMER : D�tendre
DECOMPTER : Soustraire
DECONCERTANTE : Surprenante
DECONFITE : D�contenanc�e
DECONGELAIENT : R�chauffaient
DECONGELANT : R�chauffant
DECONGELE : R�chauffe
DECONGELERAIT : R�chaufferait
DECONGESTIONNE : D�gage
DECONSIDERATION : Discr�dit
DECONSIGNER : Affranchir
DECONTENANCER : Embarrasser
DECONTRACTEE : D�tendue
DECORATEUR : M�tier de th��tre
DECORATRICE : M�tier de th��tre
DECORE : Orne
DECORTICATION : Grattage de l'�corce
DECORTIQUER : Gratter l'�corce
DECOUCHER : Dormir hors de chez soi
DECOULE : R�sulte
DECOUPAGE : Division
DECOUPLANT : S�parant
DECOUPURE : Taillade
DECOURAGEMENT : D�moralisation
DECOURS : D�croissance
DECOUSU : Sans liaison
DECOUSURE : Blessure
DECOUVRAIS : Trouvais
DECOUVRENT : Trouvent
DECRASSER : D�grossir
DECREPIR : D�labrer
DECRETER : D�cider
DECRIER : D�pr�cier
DECRIRE : D�peindre
DECRISPER : D�tendre
DECROCHEMENT : Retrait
DECROCHER : D�tacher
DECROISER : s�parer
DECROISSANCE : Diminution
DECROISSENT : Diminuent
DECROTTANT : Nettoyant
DECROTTOIR : Lame de fer pour enlever la boue
DECRUE : Baisse du niveau de l'eau
DECRYPTANT : D�codant
DECUE : Non r�alis�e
DECULASSER : Ouvrir
DECULOTTER : D�shabiller
DECUPLER : Augmenter
DECUVAGE : Transvasement
DEDAIGNER : Repousser
DEDAIN : M�pris
DEDIANT : Consacrant
DEDIE : Consacre
DEDIERENT : Consacr�rent
DEDIT : Somme � payer
DEDOMMAGER : Indemniser
DEDOUANER : Acquitter les droits
DEDOUBLANT : Partageant
DEDUCTIBILITE : Syllogisme
DEDUIRE : Soustraire
DEFAILLANCE : Manque
DEFAILLE : Manque de force
DEFAIRE : D�truire
DEFAISIONS : D�truisions
DEFAITES : Revers
DEFALQUER : D�duire
DEFAUSSER : Se d�barrasser
DEFAVORISANT : Handicapant
DEFECTIF : Qui n'a pas tous ses temps
DEFENDABLE : Plaidable
DEFENDIONS : Prot�gions
DEFENDRE : Prot�ger
DEFENDU : Interdit
DEFENSEUR : Avocat
DEFERER : Traduire devant un tribunal
DEFEUTRAGE : Op�ration qui rend la laine propre � l'�tirage
DEFIANT : Qui craint d'�tre tromp�
DEFICELER : Ouvrir
DEFICIENCE : Insuffisance
DEFIER : Provoquer
DEFIGURER : Rendre m�connaissable
DEFILER : Marcher en rang
DEFINI : Expliqu�
DEFINISSEZ : Expliquez
DEFINITEUR : Religieux
DEFINITION : Nombre de point par unit� de surface
DEFLAGRANT : Explosif
DEFLATION : Baisse
DEFLEXION : Changement de direction
DEFLORAISON : Fl�trissure
DEFONCAGE : Labour profond
DEFONCER : Eventrer
DEFONCEUSE : Charrue
DEFORMATION : Torsion
DEFORMER : Tordre
DEFOULER : Se laisser aller (se)
DEFRAICHIR : Ternir
DEFRICHER : Rendre propre � la culture
DEFRISER : Raidir
DEFRONCER : D�faire les plis
DEFROQUE : Vieux v�tements
DEGAGE : Qui a de l'aisance
DEGARNI : Moins touffu
DEGASOLINAGE : Traitement effectu� sur un gaz naturel
DEGAUCHISSENT : Redressent
DEGAZONNAGE : Tondre
DEGEL : Fonte
DEGELAIT : Fondait
DEGELEZ : Fondez
DEGENERATION : Ab�tardissement
DEGENERESCENCE : Alt�ration
DEGINGANDEE : Comme disloqu�e dans ses mouvements
DEGIVREUR : R�chauffeur
DEGLACER : Dissoudre
DEGLUTIR : Avaler
DEGOMMAGE : Nettoyage
DEGONFLER : Vider
DEGORGEMENT : Ecoulement d'eaux
DEGORGEOIR : Instrument servant � couper le fer � chaud
DEGOTTANT : Trouvant
DEGOULINE : Coule
DEGOURDIR : Rendre le mouvement
DEGOUT : R�pugnance
DEGOUTANT : Qui inspire de la r�pugnance
DEGRADER : Ab�mer
DEGRAISSAIS : Nettoyais
DEGRE : Niveau
DEGRINGOLER : Rouler
DEGRISANT : Dessaoulant
DEGRISER : Dessaouler
DEGROSSIR : Faire une premi�re �bauche
DEGROUILLER : Se h�ter
DEGUENILLE : Mal habill�
DEGUISER : Modifier l'apparence
DEGUSTER : Go�ter
DEHANCHE : Qui s'appuie sur une seule hanche
DEHISCENT : Qui s'ouvre quand il est mur
DEICIDE : Meurtrier de Dieu
DEIFIER : V�n�rer
DEITE : Divinit� mythologique
DEJAUGER : Sortir de l'eau
DEJETE : Courb�
DEJEUNER : Repas
DEJOUER : Faire �chouer
DELABRE : En mauvais �tat
DELABREMENT : Etat de ruine
DELACER : D�nouer
DELAI : Temps d'attente
DELAISSEE : Abandonn�e
DELASSER : Reposer 
DELATION : D�nonciation
DELAVER : Affaiblir une couleur
DELEATUR : Signe de correction typographique
DELECTATION : Plaisir
DELEGATION : Groupe de personnes mandat�es
DELEGUER : Confier
DELETERE : Nuisible � la sant�
DELIBERATION : D�bat
DELIBERE : Discussion entre juges
DELIBEREMENT : Apr�s avoir r�fl�chi
DELICATESSE : Tact
DELICIEUSE : Qui flatte les sens
DELIENT : D�tachent
DELINQUANCE : Ensemble de d�lits
DELIQUESCENCE : Affaiblissement
DELIRE : Confusion des id�es
DELIT : Infraction
DELITESCENCE : D�sagr�gation
DELOGE : Chasse
DELOT : Doigtier de cuir
DELOYAUX : Malhonn�tes
DELTAPLANE : Aile
DELUGE : Pluie torrentielle
DELUREE : Effront�e
DEMAGOGIE : Politique qui flatte la multitude
DEMAIGRISSEMENT : Erosion d'une plage
DEMAILLOTER : D�shabiller
DEMAIN : L'avenir
DEMANDER : Faire conna�tre un souhait
DEMANGEAISON : Picotement
DEMANTELENT : D�molissent
DEMANTELER : D�molir
DEMANTIBULER : D�monter maladroitement
DEMAQUILLANT : Lait
DEMARCATION : Limite
DEMARCHAGE : Recherche de clients
DEMARCHE : Tentative en vue d'obtenir quelque chose
DEMARRAGE : D�but
DEMARREUR : Appareil de mise en route
DEMASQUER : D�voiler
DEMATER : Perdre un mat
DEMELE : Querelle
DEMENAGER : Transporter des meubles
DEMENCE : Conduite d�pourvue de raison
DEMENER : Se d�battre (se)
DEMENTIRENT : Contredirent
DEMERITE : Attire la d�sapprobation
DEMESURE : Outrance
DEMETTRE : Destituer
DEMEURE : Domicile
DEMI : Moiti�
DEMIELLER : R�colter le miel
DEMINER : Retirer les explosifs
DEMISSIONNAIRE : Qui abandonne
DEMISSIONNER : Abandonner
DEMIXTION : Solubilit�
DEMOBILISER : Renvoyer des leurs foyers
DEMOCRATISATION : Mise � la port� de tous
DEMODE : D�suet
DEMOGRAPHIE : Etude des populations
DEMOISELLE : C�libataire
DEMOLISSEUR : Destructeur
DEMONETISER : D�pr�cier
DEMONSTRATION : T�moignage
DEMONTABLE : Dont les morceaux sont s�parables
DEMONTER : D�faire
DEMONTRE : Prouve
DEMORALISER : Oter le courage
DEMORDRE : Abandonner un avis
DEMOTIQUE : Se dit d'une �criture simplifi�e
DEMOUCHETER : Oter le bouton de la pointe d'un fleuret
DEMOULAGE : D�coffrage
DEMULTIPLIER : R�duire
DEMUNIR : D�pouiller
DEMYSTIFIER : Dissiper le mensonge
DENATURALISER : Priver de ses droits
DENATURE : Alt�re
DENDRITE : Arbre fossile
DENEGATION : Action de nier
DENI : Refus
DENIAISER : Rendre moins idiot
DENICHANT : Trouvant
DENICOTINISER : Rendre le tabac moins dangereux pour la sant�
DENIGRER : Attaquer la r�putation
DENIVELEE :  Diff�rence d'altitude
DENIVELLEMENT : Diff�rence de niveau
DENOMINATEUR : Sous la barre de fraction
DENONCER : Rompre
DENONCIATRICE : Qui signale comme coupable
DENOTE : Indique
DENOUEMENT : Fin
DENOUER : Donner une solution
DENREES : Marchandises
DENSIMETRIE : Mesure masse volumique
DENTALE : Mollusque marin
DENTELLE : Tissus l�ger et ajour�
DENTELURE : D�coupure
DENTIER : Proth�se
DENTISTE : Praticien dipl�m�
DENUDER : Enlever l'isolant
DENUEE : D�pourvue
DEPAILLER : D�garnir une chaise
DEPANNAGE : Remise en �tat
DEPAREILLER : S�parer
DEPARER : Nuire
DEPARIER : Enlever un des deux
DEPARTEMENT : Division
DEPARTENT : Attribuent en partage
DEPARTIR : Attribuer en partage
DEPASSER : Devancer
DEPAYSEMENT : D�sorienter
DEPECAGES : D�coupages
DEPECANT : D�coupant
DEPECENT : D�coupent
DEPECER : D�couper
DEPECERAS : D�couperas
DEPECES : D�coupes
DEPECIEZ : D�coupiez
DEPEIGNANTES : D�crivantes
DEPEIGNIEZ : D�criviez
DEPEINDRA : D�crira
DEPEINT : D�crit
DEPENDAIENT : R�sultaient
DEPENDENT : R�sultent
DEPENDIRENT : R�sult�rent
DEPENDRE : R�sulter
DEPENS : Charge
DEPENSANT : Consommant
DEPENSER : Consommer
DEPERDITION : Fuite
DEPERIR : Perdre ses forces
DEPERISSEMENT : Affaiblissement
DEPETRANT : D�barrassant
DEPEUPLER : D�garnir
DEPHASAGE : D�calage
DEPHASE : D�cal�
DEPIAUTE : Ecorche
DEPILATOIRE : Qui rend la peau douce
DEPIQUER : R�cup�rer le grain
DEPISTER : D�celer
DEPLACANT : Bougeant
DEPLACEMENT : Trajet
DEPLAIRE : Ne pas faire l'unanimit�
DEPLAISAIT : Ne faisait pas l'unanimit�
DEPLAIT : Ne fait pas l'unanimit�
DEPLANTOIR : Instrument de jardin
DEPLIER : Etendre
DEPLISSANT : Repassant
DEPLOIEMENT : Etalage
DEPLORABLE : Digne de compassion
DEPLORER : Regretter
DEPLOYER : Etaler
DEPLUME : Nu
DEPLUT : Ne fit pas l'unanimit�
DEPOINTER : Viser ailleurs
DEPOLARISER : D�charger
DEPONENT : Verbe latin
DEPORTATION : Exil
DEPOSER : D�monter
DEPOSITAIRE : Interm�diaire
DEPOSITION : D�claration
DEPOSSEDER : Prendre
DEPOTER : Transvaser
DEPOTOIR : D�charge
DEPOUILLE : Sans ornement
DEPOURVUES : Priv�es
DEPOUSSIERER : Nettoyer
DEPRAVEE : Pervertie
DEPRECIATIF : P�joratif
DEPRECIER : Rabaisser
DEPRENDRE : Se d�tacher (se)
DEPRENDRONT : Se  d�tacheront (se)
DEPRESSION : M�lancolie
DEPRIMER : Affaiblir
DEPURANT : Purifiant
DEPURER : Purifier
DERACINER : Arracher
DERADER : Prendre le large
DERAILLE : D�raisonne
DERANGEANT : Perturbant
DERAPE : Glisse
DERASER : Abaisser le niveau
DERATISATION : Extermination
DERAYER : Tracer le dernier sillon
DERBY : Chaussure
DEREGLEMENT : D�sordre
DERISOIRE : Minime
DERIVE : D�viation
DERMATOLOGIE : Sp�cialit� m�dicale
DERMIQUE : De la peau
DERNY : Cyclomoteur
DEROBADE : Action d'esquiver
DEROBER : Voler
DEROCHAGE : Pr�paration du m�tal
DEROGER : Manquer � son rang
DEROULAGE : Mode de d�bit du bois
DEROULEUSE : Machine � d�biter le bois
DEROUTER : D�vier
DES : Cubes de bois
DESABUSEE : Sans illusions
DESACCORD : Contradiction
DESACCOUPLE : S�pare
DESACCOUTUMER : D�faire d'une habitude
DESAFFECTATION : Changement de destination
DESAFFECTION : Perte de l'attachement
DESAGREGER : S�parer
DESALTERER : Abreuver
DESAMORCER : Interrompre
DESAPPRENDRE : Oublier
DESAPPROBATEUR : Qui n'est pas d'accord
DESARCONNER : Faire tomber
DESARGENTER : Ruiner
DESARME : Retire le mat�riel
DESARRIMER : D�tacher
DESARROI : D�sordre
DESARTICULER : D�bo�ter
DESASSORTIR : S�parer
DESASTRE : Catastrophe
DESASTREUSEMENT : De fa�on catastrophique
DESAVANTAGE : Handicap
DESAVANTAGEUX : Handicapant
DESAXER : Rompre l'�quilibre moral
DESCELLER : D�coller
DESCENDANT : Enfant
DESCENDRE : Abattre
DESCENTE : Irruption
DESCRIPTIF : Repr�sentation
DESECHOUER : Remettre � flot
DESEMBOUTEILLER : R�tablir le trafic
DESEMPARE : Priv� de ses moyens
DESEMPLIR : Vider
DESENCHANTANT : D�cevant
DESENCOMBRER : D�barrasser
DESENFUMER : A�rer
DESENGAGER : Lib�rer
DESENGRENAIENT : D�saccouplaient
DESENGRENER : D�saccoupler
DESENGRENERAIT : D�saccouplerait
DESENIVRA : D�grisera
DESENIVRER : D�griser
DESENRAYER : Remettre en �tat de fonctionnement
DESENSABLER : Draguer
DESENSIBILISE : Calme
DESENSORCELE : D�livre d'un sortil�ge
DESENTORTILLE : D�m�le
DESENVASER : Nettoyer
DESENVENIME : D�truit le poison
DESEQUILIBRER : Faire tomber
DESERT : Peu fr�quent�
DESERTEUR : L�che
DESESPERANT : D�courageant
DESESPERE : D�courag�
DESHABILLE : V�tement d'�toffe l�g�re
DESHABITUER : Casser la routine
DESHERBER : Enlever la v�g�tation d'un chemin
DESHERENCE : Absence de successeur
DESHERITE : Personne d�pourvue de biens
DESHONNETE : Contraire � la pudeur
DESHONORER : Salir
DESHYDRATE : S�che
DESIDERABILITE : Utilit� au sens �conomique
DESIDERATA : Revendication
DESIGNE : Indique
DESILLUSION : D�ception
DESINENCE : Terminaison variable des mots
DESINFECTER : D�truire les germes
DESINTEGRER : D�sagr�ger
DESINTERESSE : Pas concern�
DESINTOXIQUER : D�livrer d'une mauvaise habitude
DESINVOLTE : A l'allure d�gag�e
DESIR : Souhait
DESIRABLE : Qui fait envie
DESIREUX : Envieux
DESMAN : Mammif�re se nourrissant d'oeufs de poisons
DESOBLIGEAMMENT : En causant de la peine
DESOBSTRUANT : D�barrassant
DESODORISER : Assainir l'air
DESOLANT : Affligeant
DESOLER : Causer une affliction
DESOLIDARISER : S�parer
DESORDONNE : Mal rang�
DESORDRE : Tumulte
DESORGANISATION : D�rangement
DESORIENTE : Perdu
DESOXYDATION : R�duction d'un m�tal
DESOXYDER : R�duire
DESPOTAT : Etat gouvern� par un tyran
DESPOTIQUE : Arbitraire
DESQUAMATION : Ecaillage
DESSAISIR : D�poss�der d'un droit
DESSALAGE : Adoucissement
DESSALEMENT : Adoucissement
DESSALER : Adoucir
DESSANGLANT : D�tachant
DESSECHE : D�shydrate
DESSEIN : Projet
DESSERT : Dernier service
DESSERTISSAGE : Extraction de sa monture
DESSERVANT : Nuisant
DESSERVIONS : Nuisions
DESSERVIR : Nuire
DESSERVONS : Nuisons
DESSINER : Repr�senter
DESSOULER : Perdre l'ivresse
DESSOUS : D�savantage
DESSUS : Avantage
DESTIN : Avenir
DESTINATION : But
DESTINER : R�server
DESTITUTION : Sanction
DESTRUCTION : Ruine totale
DESTRUCTURATION : D�sorganisation
DESUET : Surann�
DESUNI : En d�saccord
DESUNION : M�sintelligence
DETACHANT : Nettoyant
DETACHEE : Provisoirement affect�e
DETAILLER : S�parer
DETALER : Fuir
DETARTRER : D�boucher
DETAXATION : Diminution de l'imp�t
DETECTE : D�c�le
DETECTIVE : Enqu�teur
DETEIGNAIENT : Influen�aient
DETEINDRE : Influencer
DETELER : D�crocher
DETENDU : Calme
DETENIR : Poss�der
DETENTE : Diminution de la pression
DETENTION : Peine afflictive
DETERGENT : Nettoyant
DETERIORER : Ab�mer
DETERMINATION : D�cision
DETERMINER : Fixer 
DETERMINISME : Les m�mes causes entra�nent les m�mes effets
DETESTER : Ne pas pouvoir supporter
DETIRE : Pied dans la main
DETONATION : Bruit violent
DETONNER : Choquer
DETORDAIT : Redressait
DETORDES : Redresses
DETORDIT : Redressa
DETORDU : Redress�
DETOUR : Trac� sinueux
DETOURNE : Ecarte
DETOXICATION : Neutralisation
DETRACTEUR : Qui rabaisse le m�rite de quelqu'un
DETRAQUE : D�range le m�canisme
DETREMPE : Proc�d� de peinture
DETRESSE : Sentiment d'abandon
DETRIMENT : Dommage
DETROMPE : Corrige
DETRONE : Chasse de sa place
DETROUSSEUR : Voleur
DETRUISAIENT : Ruinaient
DETRUISENT : Ruinent
DETRUIT : Ruine
DETTE : Engagement
DETUMESCENCE : Diminution
DEUIL : Tristesse
DEUTERIUM : Isotope lourd de l'hydrog�ne
DEUTON : Un proton plus un neutron
DEUX : Adjectif num�ral
DEVADASI : Danseuse sacr�e 
DEVALISANT : Volant
DEVALISER : Voler
DEVALORISER : D�nigrer
DEVALUATION : Diminution du taux
DEVANCER : Pr�c�der
DEVASTATEUR : Destructeur
DEVELOPPABLE : Que l'on peut d�plier
DEVELOPPE : Etale
DEVENIR : Mouvement de transformation
DEVERGONDAGE : Conduite rel�ch�e
DEVERNISSANT : D�capant
DEVERS : Diff�rence de niveau
DEVERSER : R�pandre
DEVERSOIR : Vanne
DEVETIR : D�pouiller
DEVIANCE : Conduite hors la norme
DEVIATION : Ecart
DEVIATIONNISTE : Personne en d�saccord avec la doctrine de son parti
DEVIDOIR : D�rouleur
DEVINER : Pr�dire
DEVINERESSE : Astrologue
DEVINETTE : Jeu
DEVIN : Astrologue
DEVIRER : Tourner en sens contraire
DEVISE : Titre de paiement
DEVISANT : Conversant
DEVITALISER : Tuer
DEVITRIFICATION : Perte de transparence
DEVOILER : R�v�ler
DEVOIR : Obligation
DEVOLUTION : Attribution
DEVON : App�t
DEVONIENNE : De la quatri�me p�riode de l'�re primaire
DEVORE : Regarde avec avidit�
DEVOT : Pieux
DEVOTION : Pi�t�
DEVOUEMENT : Sacrifice
DEVOYEE : D�bauch�e
DEWATTE : En quadrature avec la tension
DEXTERITE : Adresse
DEXTRALITE : Fait d'�tre droitier
DEY : Officier barbaresque
DIABETE : Exc�s de sucre
DIABLEMENT : Excessivement
DIABOLIQUE : Pernicieux
DIABOLO : Bobine � lancer
DIACHRONIE : Caract�re des ph�nom�nes linguistiques
DIACLASE : Fissure
DIACONESSE : Dame de charit�
DIADEME : Parure
DIAGNOSE : Description abr�g�e d'une plante
DIAGNOSTIC : Identification d'un d�faut
DIAGNOSTIQUER : Identifier un d�faut
DIAGONALES : Droites obliques
DIAGRAMME : Courbe
DIAGRAPHIE : Technique de reproduction
DIALECTICIEN : Sp�cialiste de la langue
DIALECTOLOGUE : Linguiste
DIALOGUE : Conversation
DIAMANT : Pierre pr�cieuse
DIAMANTIFERE : Qui contient des pierres pr�cieuses
DIANE : R�veil des soldats
DIAPASON : Instrument de r�f�rence sonore
DIAPEDESE : Migration des globules blancs
DIAPHORETIQUE : Qui provoque la transpiration
DIAPHRAGME : Cloison
DIAPHYSE : Partie de l'os
DIAPRER : Parer de couleur vari�es
DIASCOPE : Instrument d'optique
DIATHERMIE : Th�rapeutique utilisant la chaleur
DIATOMIQUE : Dont la mol�cule est form�e de deux atomes
DICHOTOME : Qui se divise par bifurcation
DICTAIENT : Imposaient
DICTATORIAL : Absolu
DICTENT : Imposent
DICTION : Mani�re de dire
DICTIONNAIRE : Recueil de mots
DIDACTIQUE : Qui instruit
DIENCEPHALE : Partie du cerveau
DIESE : Alt�ration qui hausse d'un demi ton
DIESEL : Moteur � combustion
DIETE : R�gime
DIFFAMANTE : Portant atteinte � la r�putation
DIFFAMER : Porter atteinte � la r�putation
DIFFEREE : Report�e
DIFFERENCIATION : Distinction
DIFFERENCIER : Distinguer
DIFFERENT : Ne se ressemblent pas
DIFFLUENCE : Division
DIFFRACTION : Ph�nom�ne lumineux
DIFFUSER : R�pandre
DIFFUSEUR : Accessoire d'�clairage
DIGERENT : Assimilent
DIGESTIBLE : Assimilable
DIGITALE : Genre de scrofulariac�e
DIGON : Fer barbel�
DIGUE : Obstacle
DIJON : Ville de Bourgogne
DILACERE : D�chire
DILAPIDATRICE : D�pensi�re
DILAPIDER : D�penser
DILATOIRE : Qui tend � gagner du temps
DILIGEMMENT : Avec z�le
DILUE : M�lange
DILUVIENNE : Abondante
DIMENSION : Taille
DIMINUER : R�duire
DINANDERIE : Objet en laiton coul�
DINDE : Fille idiote
DINDONNEAU : Oiseau gallinac�
DINETTE : Petit repas
DINGUER : Econduire brutalement
DINOSAURES : Groupe de reptiles de l'�re secondaire
DIODE : Redresseur
DIOPTRIE : Unit� de vergence
DIPHTERIE : Maladie contagieuse
DIPHTONGUE : Groupe de deux lettres
DIPLOMATIE : Tact
DIPLOME : Titre
DIPLOPIE : Trouble de la vue
DIPNEUSTES : Ordre de poissons d'eau douce
DIPTYQUE : Oeuvre compos�e de deux parties
DIRECTEMENT : Sans d�tour
DIRECTIONNEL : Qui vise un point pr�cis
DIRECTIONNELLE : Qui vise un point pr�cis
DIRECTIVE : Consigne
DIRHAM : Monnaie du Maroc
DIRIGISME : Syst�me politique
DISCERNER : Distinguer
DISCIPLE : Personne qui adh�re � une doctrine
DISCOBOLE : Athl�te
DISCOIDE : Rond
DISCONTINUATION : Interruption
DISCONVENIR : Nier
DISCORDANT : Faux
DISCOUREUSE : Qui aime parler
DISCOURIR : Parler
DISCOURRAIT : Parlerait
DISCOURS : Propos
DISCREDIT : Perte de consid�ration
DISCRETES : R�serv�es
DISCRIMINANTE : Qui s�pare
DISCULPER : Innocenter
DISCUTABLE : Douteux
DISCUTER : Echanger des id�es
DISETTE : Manque de vivres
DISGRACE : Infortune
DISJOIGNANT : S�parant
DISJONCTER : Interrupteur
DISLOQUANT : D�membrant
DISPARAITRE : S'esquiver
DISPARATE : Manque d'harmonie
DISPARU : Introuvable
DISPENDIEUX : Co�teux
DISPENSE : Distribue
DISPERSER : R�pandre
DISPONIBILITE : Fonds
DISPOSE : Arrange
DISPROPORTIONNE : Tr�s diff�rent
DISQUE : Plaque circulaire
DISQUETTE : Support magn�tique
DISSEMINANT : Eparpillant
DISSEQUENT : Analysent
DISSERTE : D�veloppe un sujet
DISSIMILITUDE : D�faut de ressemblance
DISSIMULE : Cache
DISSIPATEUR : Perturbateur
DISSIPE : Perturbe
DISSOCIER : S�parer
DISSOLUTION : Suppression
DISSOLVANT : Produit de nettoyage
DISSUADANT : D�tournant d'une r�solution
DISTANCER : Devancer
DISTANTE : R�serv�e
DISTENDRE : Tirer trop fort
DISTILLATION : Technique utilis�e pour la s�paration des �l�ments
DISTILLER : R�pandre
DISTINCTION : Mani�res �l�gantes
DISTINGUEE : Eminente
DISTIQUE : Groupe de deux vers formant un sens complet
DISTORDANTES : Provoquant des d�formations
DISTORSION : D�formation
DISTRAIT : Peu attentif
DISTRAYANT : Amusant
DISTRIBUTEUR : Machine � sous
DITHYRAMBIQUE : Qui loue d'une mani�re excessive
DIVA : Cantatrice c�l�bre
DIVAGATION : D�placement du lit des cours d'eau
DIVERGER : Etre en d�saccord
DIVERSIFIER : Varier
DIVETTE : Chanteuse
DIVIN : Vient de haut
DIVINATION : Facult� de pr�voir
DIVISIBLE : Partageable
DIVORCE : S�paration
DIVULGATION : R�v�lation
DIVULGUER : R�v�ler
DO : Note
DOCILE : Ob�issant
DOCKER : Manutentionnaire
DOCTORALEMENT : Solennellement
DOCUMENTALISTE : Biblioth�caire
DOCUMENTE : Informe
DODECAPHONISME : Langage musical
DODELINER : Balancer mollement
DOGMATIQUEMENT : Du ton d�cisif
DOGMATISME : Disposition � croire
DOIGTE : Adresse
DOL : Manoeuvre frauduleuse
DOLCE : Avec douceur
DOLENTE : plaintive
DOLOIRE : Instrument � g�cher
DOLS : Manoeuvres frauduleuses
DOM : D�partements lointains
DOMANIALITE : R�gime juridique du domaine public
DOME : Couverture d'un �difice
DOMESTIQUER : Apprivoiser
DOMICILIATION : Indication du domicile
DOMINATEUR : Qui aime � gouverner
DOMINER : Tenir sous son autorit�
DOMINICAIN : Religieux
DOMPTABLE : Peut �tre ma�tris�
DON : Aptitude
DONA : Titre de courtoisie espagnol
DONATISTE : Partisan de Donat
DONC : Indique la cons�quence
DONJON : Grosse tour
DONNE : Distribution
DONT : Pronom relatif
DOPPLER : Physicien autrichien
DORDOGNE : D�partement fran�ais
DORIEN : Un des quatre principaux dialectes de la langue grecque ancienne
DORIQUE : Ancien ordre de l'architecture grecque
DORLOTER : Traiter d�licatement
DORMANT : Partie fixe
DORMEUSE : Boucle d'oreille
DORMITION : Mort de la vierge dans l'ancienne liturgie
DORYPHORE : Insecte col�opt�re
DOS : Verso
DOSE : Quantit� d�termin�e
DOSER : D�terminer la concentration
DOSSARD : Pi�ce d'�toffe port�e sur un maillot
DOT : Apport
DOTAL : R�gime matrimonial
DOTATION : Revenu
DOTER : Fournir
DOUAIRE : Biens assur�s par le mari � la femme survivante
DOUANE : Administration charg�e de percevoir des droits
DOUAR : Agglom�ration de tentes en Afrique du Nord
DOUBLEMENT : Pour deux raisons
DOUBLER : D�passer
DOUBLURE : Rempla�ant
DOUCEREUX : Mielleux
DOUCHANT : Arrosant
DOUCINE : Rabot servant � faire des moulures
DOUELLE : Parement d'un voussoir
DOUILLET : Moelleux
DOUM : Palmier d'Afrique
DOUMA : Assembl�e dans la Russie tsariste
DOURO : Ancienne monnaie Espagnole
DOUVAIN : Bois de ch�ne utilis� pour les tonneaux
DOUZAIN : Ancienne monnaie fran�aise
DOYEN : Administrateur
DRACHME : Monnaie grecque
DRAGEE : Bonbon
DRAGON : Monstre fabuleux
DRAGONNADES : Pers�cutions organis�es par Louvois
DRAGUE : Filet
DRAIN : Conduit souterrain
DRAINER : Attirer
DRALON : Tissus
DRAMATISER : Exag�rer la gravit�
DRAPER : Couvrir
DRAVIDIEN : Langue parl�e dans la Sud de l'Inde
DRAYER : Egaliser l'�paisseur du cuir
DRESSAGE : Domptage
DRESSEUR : Dompteur
DRESSOIR : Meuble � �tag�res
DRIBBLER : Technique utilis�e au football
DRISSE : Cordage
DROGUERIE : Commerce
DROITE : Ligne
DROITURE : Loyaut�
DROLERIE : Bouffonnerie
DROSERA : Plante des tourbi�res
DRU : Serr�
DRUIDISME : Institution religieuse des Celtes
DU : Article contract�
DUALISME : Le bien et le mal
DUBITATIVEMENT : En doutant
DUC : Titre de noblesse
DUCAT : Ancienne monnaie
DUCE : Ancien titre de chef du gouvernement italien
DUCHESSE : Poire
DUEL : Combat
DUELLISTE : Combattant
DUELS : Combats
DUIT : Chauss�e
DULCIFIER : Temp�rer l'amertume
DUNETTE : Superstructure d'un navire
DUO : Morceau de musique
DUODENUM : Partie de l'intestin
DUODI : Deuxi�me jour
DUPANT : Trompant
DUPLEX : Permet la communication dans les deux sens
DUPLICATION : Reproduction
DUR : Difficile � entamer
DURABILITE : Esp�rance de vie
DURCISSEMENT : Prise
DUREE : Temps
DURHAM : Race bovine
DURILLON : Callosit�
DURIT : Tuyau en caoutchouc
DUVETEUX : Doux
DY : Dysprosium
DYKE : Filon de lave
DYN : Symbole de la dyne
DYNAMISME : Energie
DYNAMITER : Faire exploser
DYNAMO : G�n�rateur
DYNAMOMETRIQUE : Qui mesure la force
DYSARTHRIE : Difficult� de parole
DYSGRAPHIE : Difficult� dans l'apprentissage de l'�criture
DYSPEPSIE : Digestion difficile
DYSPNEE : Difficult� � respirer
DYTIQUE : Insecte col�opt�re carnivore
E : Pas de d�finition
EAU : Liquide
EBAHISSEMENT : Etonnement
EBARBE : Enl�ve les parties exc�dantes
EBATS : Divertissements
EBATTRE : Se divertir (S')
EBAUBI : Surpris
EBAUCHANT : Esquissant
EBAUCHOIR : Outil de sculpteur
EBENISTE : Ouvrier du bois
EBLOUIR : Aveugler
EBOUILLANTAGE : Trempage
EBOULER : Faire �crouler
EBOURIFFANT : Incroyable
EBOURRER : Nettoyer la peau
EBOUTE : Coupe
EBRANCHOIR : Serpe � long manche
EBRASEMENT : Biais
EBRECHER : Entamer
EBRIETE : Ivresse
EBROUER : S'�battre 
EBULLIOSCOPE : Appareil de mesure
ECAILLAGE : D�faut d'un vernis
ECAILLEUX : Caract�ristique des poisons
ECALE : Enveloppe
ECARQUILLANT : Agrandissant
ECARTE : Jeu de cartes
ECARTELA : Divisa un �cu en quatre
ECARTER : Rejeter une carte de son jeu
ECARTEUR : Provocateur de taureaux
ECCHYMOSE : Bleu
ECCLESIASTIQUE : Du clerg�
ECHAFAUDAGE : Assemblage provisoire de charpente
ECHALIER : Cl�ture faite de branches
ECHALOTE : Plante potag�re
ECHANGER : Communiquer
ECHANTILLON : Aper�u
ECHAPPATOIRE : Issue
ECHARDE : Epine
ECHARNOIR : Couteau � deux poign�es
ECHARPANT : Taillant en pi�ces
ECHAUDER : Br�ler
ECHAUDOIR : Salle d'abattoir
ECHAUFFOUREE : Combat
ECHEANCE : D�lai
ECHEC : Insucc�s
ECHELONNANT : R�partissant
ECHEVELLENT : D�coiffent
ECHEVIN : Magistrat municipal sous l'Ancien R�gime
ECHINE : Dos
ECHINER : Se fatiguer
ECHO : R�p�tition
ECHOIR : Arriver par hasard
ECHOLALIE : R�p�tition
ECHOPPE : Boutique
ECHOUEMENT : Mise au sec
ECIMER : Couper
ECLABOUSSEMENT : Jaillissement
ECLAIRAGE : Point de vue
ECLAIRCISSEMENT : Explication
ECLAIREUSE : Membre d'une patrouille
ECLATANT : Magnifique
ECLECTIQUE : Pas sectaire
ECLIPSE : Disparition
ECLISSE : Eclat de bois
ECLOPEE : Boiteuse
ECLORE : Se manifester
ECLUSER : Faire passer d'un bief � l'autre
ECMNESIE : Evocation du pass�
ECOBUAGE : Proc�d� archa�que de culture
ECOINCON : Ornement de coins
ECOLE : Ensemble des adeptes
ECOLOGIE : Partie de la biologie
ECONDUIRE : Cong�dier
ECONOME : Personne charg�e des d�penses
ECONOMIQUE : Qui diminue les frais
ECOPER : Vider
ECOPERCHE : Pi�ce de bois dress�e portant une poulie en t�te
ECORCHURE : Petite blessure
ECORNER : Entamer
ECORNURE : Eclat d'un angle
ECOSSAIS : Ray� � carreaux
ECOUMENE : Partie habitable de la surface terrestre
ECOUTES : Cordages
ECOUVILLON : Brosse 
ECRABOUILLEMENT : Ecrasement
ECRASANTE : Accablante
ECREMER : Prendre la meilleur
ECRETAGE : Saturation
ECRETER : Couper le sommet
ECRIN : Coffret
ECRITEAU : Pancarte
ECRITURE : Repr�sentation de la pens�e
ECRIVAIN : Homme de lettre
ECROU : Pi�ce de m�tal perc�e d'un trou
ECROUELLES : Inflammation
ECROUER : Emprisonner
ECROUISSAGE : Action de durcir le m�tal
ECROULEMENT : An�antissement
ECROUTEUSE : Herse utilis�e pour pulv�riser la partie superficielle d'une terre labour�e
ECRU : Brut
ECTHYMA : Infection de la peau
ECTINITE : Roche
ECTOPLASME : Forme �mise par un m�dium en transe
ECU : Ancienne monnaie
ECUEIL : Obstacle
ECUELLE : Assiette
ECUMANTE : En rage
ECUME : Mousse
ECURIE : Equipe
ECUYER : Titre de jeune noble
ECZEMA : Maladie de la peau
EDELWEISS : Plante d'altitude
EDEN : Lieu de d�lices
EDICTANT : Publiant
EDIFICE : Institution
EDILE : Magistrat
EDITER : Publier
EDITORIAL : Article
EDREDON : Couvre-pieds
EDULCORER : Adoucir
EDUQUER : Former
EFFACER : Supprimer
EFFARANTE : Incroyable
EFFAROUCHER : Effrayer
EFFECTIVEMENT : R�ellement
EFFECTUER : Accomplir
EFFERVESCENCE : Agitation
EFFET : R�sultat
EFFICIENCE : Rendement
EFFIGIE : Image
EFFILEE : Mince
EFFILER : Amincir
EFFLEURER : Ne pas passer loin
EFFONDRE : Abattu
EFFONDREMENT : An�antissement
EFFONDRILLES : D�p�ts
EFFRANGER : D�couper les bords
EFFRAYE : Rebute
EFFRAYERAIS : Rebuterais
EFFRAYERONS : Rebuterons
EFFRITER : Action de r�duire en poussi�re
EFFRONTERIE : Sans-g�ne
EFFUSION : Epanchement
EGAILLER : Se disperser (S')
EGALER : Atteindre
EGALISER : Aplanir
EGAREMENT : Erreur
EGARER : Perdre
EGLANTINE : Fleur
EGOCENTRISME : Narcissisme
EGORGEANT : Tuant
EGOSILLER : Crier (s')
EGOUTIER : Ouvrier travaillant sous terre
EGOUTTOIR : Casier en fil m�tallique plastifier
EGRAPPE : D�tache
EGRATIGNER : Blesser
EGRISER : Polir
EGRUGER : R�duire en poudre
EGUEULER : Casser
EH : Interjection
EHONTE : Cynique
EINSTEINIUM : El�ment  chimique de num�ro 99
EJECTION : Appareil servant � l'�vacuation d'un fluide
ELABORER : Pr�parer
ELAGUER : D�pouiller
ELANCEE : Mince et grande
ELARGISSEMENT : Mise en libert�
ELAVE : D�color�
ELDORADO : Pays chim�rique
ELECTION : Choix
ELECTIVE : Qui r�sulte d'un choix
ELECTRICIEN : Personne au courant
ELECTRIFIER : Mettre au courant
ELECTRISANT : Enthousiasmant
ELECTROAIMANT : Bobine attirante
ELECTROCUTE : Electrise
ELECTROLYSE : D�composition chimique
ELECTRON : Petit satellite
ELECTROPHORESE : M�thode de s�paration
ELECTROPOSITIVE : Qui agit en cathode
ELECTROVALVE : Soupape t�l�command�e
ELEGIE : Po�me lyrique
ELEMENTS : Constituants
ELEPHANTIASIQUE : Atteint d'une maladie parasitaire qui rend la peau rugueuse
ELEVANT : Rehaussant
ELEVATION : Formation de la puissance d'un nombre
ELEVE : Candidat � un grade
ELEVERA : Construira
ELEVEREZ : Construirez
ELEVONS : Gouverne
ELIDER : Remplacer par l'apostrophe
ELIMANT : Usant
ELIMINATOIRE : Epreuve pr�alable
ELINGUER : Amarrer
ELITE : Gratin
ELLE : Pronom personnel
ELLIPSOIDE : Surface convexe du second degr�
ELOGE : Compliment
ELOGIEUSEMENT : Avec des louanges
ELOIGNER : Ecarter
ELOQUEMMENT : Avec persuasion
ELU : Choisi
ELUCIDATION : Eclaircissement
ELUDER : Eviter
ELYSEE : S�jour des �mes des h�ros
EMACIER : Maigrir (s')
EMAILLER : Parsemer
EMANANT : D�coulant
EMANCIPER : Affranchir
EMARGEANT : Signant
EMBALLEMENT : R�gime anormal d'un moteur
EMBARBOUILLER : Faire perdre le fil de ses id�es
EMBARCADERE : M�le
EMBARQUEMENT : Inscription sur le r�le
EMBARRASSANT : Ennuyeux
EMBARRER : Placer un levier
EMBASTILLE : Emprisonne
EMBASTILLER : Emprisonner
EMBAUCHER : Engager
EMBAUCHOIR : Forme pour une chaussure
EMBAUMER : Exhaler une odeur suave
EMBELLISSENT : Ornent
EMBETES : Ennuy�s
EMBLAVER : Ensemencer
EMBOBINER : Enrouler
EMBOITAGE : R�union de corps et de la couverture
EMBOLIE : Oblit�ration d'un vaisseau
EMBONPOINT : Exc�s de graisse
EMBOSSAGE : Amarrage
EMBOUCHE : Elevage de bovins
EMBOUCHURE : C�t� o� on souffle
EMBOUQUER : S'engager dans un passage
EMBOURGEOISANT : S'installant dans le confort
EMBOUT : Garniture de m�tal au bout d'une canne
EMBOUTEILLAGE : Ralentissement
EMBOUTIR : Marteler
EMBOUTISSOIR : Marteau
EMBRANCHEMENT : Division
EMBRAQUER : Terme de marine
EMBRASER : Exalter
EMBRASSER : Choisir
EMBRAYAGE : Organe de transmission
EMBREVEMENT : Assemblage oblique de deux pi�ces de bois
EMBRIGADE : Mobilise
EMBROCATION : Application d'un liquide gras
EMBROUILLAGE : Complication
EMBROUILLER : Compliquer
EMBRUMER : Attrister
EMBRYOGENESE : D�veloppement
EMBRYON : Organisme en voie de d�veloppement
EMBRYONNAIRE : A l'�tat rudimentaire
EMBUCHE : Pi�ge
EMBUSCADE : Attaque par surprise
EMECHE : Enivr�
EMERGENCE : Source
EMERI : Roche 
EMERILLON : Esp�ce de faucon
EMERVEILLANT : Fascinant
EMETS : Transmets
EMETTENT : Transmettent
EMETTONS : Transmettons
EMEU : Oiseau d'Australie
EMIETTANT : Eparpillant
EMIETTES : Eparpilles
EMIGRER : Changer de climat
EMINCER : Couper en tranches
EMIR : Titre musulman
EMISE : Transmise
EMISSION : Transmission
EMMAGASINE : Absorbe
EMMAILLOTER : Envelopper
EMMANCHURE : Ouverture d'un v�tement
EMMELER : Semer la confusion
EMMENAGEANT : S'installant
EMMENER : Conduire
EMMENERONT : Conduiront
EMMENTHAL : Fromage
EMMETRER : Disposer en vue de mesurer
EMMIELLER : Adoucir
EMMITOUFLER : Envelopper
EMMURER : Enfermer
EMOLUMENT : R�tribution
EMONDER : Elaguer
EMORFILANT : Ebarbant
EMOTIONNABLE : Impressionnable
EMOTIVITE : Sensibilit�
EMOTTEUSE : Herse
EMOUCHETTE : Protection contre les insectes
EMOUSSER : Epointer
EMOUSTILLER : Exciter
EMOUVANT : Bouleversant
EMPAILLER : Naturaliser
EMPALER : Transpercer
EMPANACHE : Orn�
EMPANNER : Virer de bord
EMPAQUETANT : Emballant
EMPARER : Prendre (s')
EMPATEMENT : Engraissement
EMPATTEMENT : Largeur
EMPAUMURE : Partie d'un gant
EMPECHEUR : G�neur
EMPENNAGE : Partie d'une aile
EMPENNE : Partie d'une fl�che
EMPERLER : Orner
EMPESE : Raide
EMPETRER : Entraver
EMPHATIQUEMENT : Pompeusement
EMPIECEMENT : Partie d'une jupe
EMPIERRER : Caillouter
EMPIETER : Usurper
EMPIFFRANT : Gavant
EMPILE : Petit fil auquel on attache l'hame�on
EMPIRANT : Aggravant
EMPIRISME : Acquisition de l'exp�rience
EMPLATRE : M�dicament externe
EMPLOI : Utilisation
EMPLOYE : Salarie
EMPOCHANT : Touchant
EMPOIGNER : Saisir
EMPOIS : Colle
EMPOISONNEUR : G�neur
EMPOISSER : Rendre collant
EMPORTER : Arracher
EMPOTEE : Maladroite
EMPOURPRER : Colorer
EMPREINTE : Trace
EMPRESSE : Pr�venant
EMPRISE : Influence
EMPRISONNER : Clo�trer
EMPRUNTEUR : D�biteur
EMPUANTISSEMENT : Action de remplir d'une mauvaise odeur
EMULATION : Amour-propre
EMULSION : Mousse
EMULSIONNER : Faire mousser
EN : Pronom adverbial
ENA : Grande �cole
ENANTIOTROPE : Qui existe sous deux formes
ENCADRE : Entoure
ENCADREMENT : Action d'entourer
ENCAGER : Enfermer
ENCAISSER : Emballer
ENCALMINE : Sans vent
ENCANAILLEMENT : Avilissement
ENCAQUER : Entasser
ENCASTELURE : Maladie du pied
ENCASTREMENT : Embo�tage
ENCAUSTIQUAGE : Action de peindre
ENCAVER : Ranger du vin
ENCEINDRE : Enclore
ENCENSE : Honore
ENCEPHALE : Cerveau
ENCEPHALOPATHIE : Mal de t�te
ENCERCLER : Entourer
ENCHAINER : Attacher
ENCHANTEUR : Magicien
ENCHASSER : Sertir
ENCHATONNER : Sertir
ENCHAUSSER : Pailler
ENCHEMISER : Prot�ger
ENCHERISSEMENT : Augmentation
ENCHEVAUCHER : Faire joindre par recouvrement
ENCHEVETRER : Emm�ler
ENCLAVANT : Contenant
ENCLENCHEMENT : Dispositif d'accrochage
ENCLIQUETAGE : Dispositif emp�chant le retour
ENCLITIQUE : Mot qui s'appuie sur un mot pr�c�dent
ENCLORE : Fermer
ENCLOS : Terrain ferm�
ENCLOUAGE : Mise hors service d'un canon
ENCLOUURE : Blessure
ENCLUME : Entre le marteau et l'�trier
ENCOCHE : Petite entaille
ENCOIGNURE : Angle int�rieur
ENCOLLER : Enduire
ENCOMBRANT : Embarrassant
ENCORBELLEMENT : Saillie
ENCORE : Adverbe de temps
ENCORNET : Calmar
ENCOURAGEMENT : Incitation
ENCOURIR : M�riter
ENCOURRAIT : M�riterait
ENCRASSER : Salir
ENCREUR : Rouleau d'une machine � imprimer
ENCRINE : Genre d'�chinodermes crino�des
ENCROUE : Enchev�tr�
ENCUVAGE : Action de mettre dans un r�servoir
ENCYCLIQUE : Lettre du pape
ENCYCLOPEDIE : Ensemble de toutes les connaissances
ENCYCLOPEDIQUE : Qui embrasse l'ensemble des connaissances
ENDEMIE : Maladie particuli�re � une r�gion
ENDEUILLER : Attrister
ENDEVANT : Rageant
ENDIGUANT : Contenant
ENDIMANCHER : Rev�tir ses plus beaux habits
ENDIVE : Esp�ce de chicor�e
ENDOCRINIEN : Relatif � des glandes
ENDOCTRINANT : Cat�chisant
ENDOGAMIE : Obligation de se marier dans sa propre tribu
ENDOLORISSANT : Faisant mal
ENDOMMAGE : Ab�me
ENDOPARASITE : Animal vivant dans un organisme
ENDORMIR : Anesth�sier
ENDOS : Mention port�e sur un titre
ENDOSCOPE : Instrument servant � examiner dans les cavit�s profondes
ENDOSSER : Assumer
ENDUIRE : Recouvrir
ENDURABLE : Supportable
ENDURCIE : Inv�t�r�e
ENDURER : Subir
ENDYMION : Jacinthe des bois
ENERGIE : Dynamisme
ENERGIQUE : Vigoureux
ENERGUMENE : Agit�
ENERVEMENT : Agacement
ENFAITEAU : Fa�ti�re
ENFANTEMENT : Cr�ation
ENFANTILLAGE : Pu�rilit�
ENFANTINE : Pu�rile
ENFER : Lieu destin� au supplice des damn�s
ENFERMER : Clo�trer
ENFIEVRE : Surexcite
ENFILAGE : Action de mettre sur un fil
ENFILER : Mettre 
ENFLAMMER : Allumer
ENFLECHURE : Echelon de cordage
ENFLEURAGE : Op�ration de parfumerie
ENFONCEMENT : Creux
ENFONCURE : Creux
ENFOUISSEMENT : Enterrement
ENFOURCHER : S'asseoir sur le dos
ENFOURNER : Ingurgiter
ENFREIGNENT : D�sob�issent
ENFREINDRE : D�sob�ir
ENFUIR : D�guerpir (s')
ENFUMER : Noircir
ENFUTER : Mettre dans un tonneau
ENGAGEANTE : Aguichante
ENGAINER : Mettre dans un �tui
ENGAZONNEMENT : Ensemencement
ENGEANCE : Cat�gorie de personnes m�prisables
ENGENDRE : Cause
ENGLOBER : Annexer
ENGLUAGE : Enduit protecteur
ENGOBE : Enduit terreux
ENGONCE : Mal habill�
ENGORGEMENT : Encombrement
ENGOUER : Etrangler
ENGOUFFRER : Avaler
ENGOURDISSEMENT : L�thargie
ENGRAISSANT : Faisant grossir
ENGRANGEANT : Emmagasinant
ENGRAVER : Entailler
ENGRENAGE : Syst�me de roues dent�es
ENGRENER : Entra�ner
ENGUEULER : Invectiver
ENHARDIR : Encourager
ENHARNACHER : Accoutrer
ENIGMATIQUE : Myst�rieux
ENIVRE : Grise
ENJAMBEMENT : Empi�tement
ENJEUX : Mise
ENJOINDRE : Imposer
ENJOLER : S�duire
ENJOLIVE : Pare
ENJOUE : Aimable
ENKYSTE : Isol� dans l'organisme
ENLACE : Entoure
ENLAIDIR : D�parer
ENLEVAGES : Op�rations de teinturerie
ENLEVEE : Ex�cut�e avec brio
ENLEVENT : Retirent
ENLEVER : Retirer
ENLIASSER : Mettre en paquets
ENLISANT : Embourbant
ENLISER : Embourber
ENLUMINURE : Ornement d'anciens manuscrits
ENNEAGONE : Polygone
ENNEMIE : Adversaire
ENNOBLIR : Grandir
ENNUYER : Pr�occuper
ENONCER : Exposer
ENORGUEILLIR : Glorifier
ENQUERIR : Informer
ENQUETES : Investigations
ENQUIQUINEMENT : Emb�tement
ENRACINE : Ancre
ENRAGER : End�ver
ENRAYER : Freiner
ENRAYERONS : Freinerons
ENREGIMENTENT : Incorporent
ENREGISTREMENT : Mise en m�moire
ENRHUME : Refroidi
ENRICHISSEMENT : Acquisition
ENROBER : Envelopper
ENROLER : Recruter
ENROULER : Bobiner
ENROULEUR : Dispositif de r�duction de voilure
ENRUBANNER : Orner
ENSABLER : Engraver
ENSACHER : Emballer
ENSANGLANTER : Tacher de sang
ENSEIGNE : Drapeau
ENSELLEE : Qui a le dos creux
ENSEMENCENT : Alevinent
ENSEUILLEMENT : Hauteur d'une fen�tre
ENSEVELIR : Enterrer
ENSILAGE : M�thode de conservation
ENSOLEILLEMENT : Quantit� de beau temps
ENSOMMEILLEE : Mal r�veill�e
ENSORCELE : Charme
ENSUITE : Puis
ENSUIVENT : R�sultent
ENSUIVRE : R�sulter
ENTACHANT : Salissant
ENTAILLE : Coupure
ENTAME : Commence
ENTARTRAGE : Obstruction par le phosphate de calcium
ENTASSEMENT : Accumulation
ENTENDEMENT : Bon sens
ENTENEBRANT : Obscurcissant
ENTENEBRER : Obscurcir
ENTER : Greffer
ENTERINER : Confirmer
ENTERRER : Enfouir
ENTHOUSIASMER : Emballer
ENTICHER : Amouracher
ENTIERE : Compl�te
ENTOLAGE : Vol
ENTOMOPHAGE : Insectivore
ENTONNE : Chante
ENTORTILLANT : Pr�ciosit�
ENTOUR : Abord
ENTOURE : Embrasse
ENTRACTES : Repos
ENTRAILLES : Boyaux
ENTRAIN : Enthousiasme
ENTRAINEMENT : Exercice
ENTRAVER : Emp�cher
ENTREBAILLEUR : Cha�ne de s�curit�
ENTRECHOQUER : Choquer
ENTRECOUPE : Interrompu
ENTRECROISEMENT : Entrelacs
ENTREFAITES : Intervalle de temps
ENTRELACER : Tisser
ENTRELARDENT : Entrem�lent
ENTREMELER : M�langer
ENTREMETS : Plats
ENTREMETTRE : Intervenir
ENTREMISE : Arbitrage
ENTREPOT : Hangar
ENTREPRENANT : Audacieux
ENTREPRENEUR : Constructeur
ENTREPRENNENT : Commencent
ENTREPRISE : Etablissement
ENTRETENIR : Maintenir
ENTRETIEN : Discussion
ENTRETOISER : Maintenir l'�cartement
ENTREVOIR : Deviner
ENTROUVERTES : Mal ferm�es
ENTROUVRE : Entreb�ille
ENTURE : Cheville
ENUMERATION : Compte
ENUMERE : Compte
ENVAHIR : Remplir
ENVASER : Embourber
ENVELOPPE : Etui
ENVENIMANT : Aggravant
ENVERGUER : Attacher une voile
ENVIABLE : Souhaitable
ENVIEUX : Jaloux
ENVIRONNEMENT : Entourage
ENVIRONS : Alentours
ENVOI : Exp�dition
ENVOLEE : Elan
ENVOUTEMENT : Mal�fice
ENVOYER : Exp�dier
EOCENE : Avant l'oligoc�ne
EOLOPILE : Boule qui tourne � l'eau chaude
EOSINE : Colorant
EPAGNEUL : Chien
EPAISSIR : Grossir
EPAMPRAGE : Effeuillage
EPANCHANT : R�pandant
EPANNELER : Tailler
EPANOUI : Radieux
EPANOUISSEMENT : Eclosion
EPARGNANT : Econome
EPARPILLEMENT : Dispersion
EPARVIN : Exostose
EPATEES : Surprises
EPATEMENT : Etonnement
EPAULANT : Soutenant
EPAVE : Loque
EPEE : Arme blanche
EPEICHE : Cul-rouge
EPEICHETTE : Oiseau noir et blanc
EPEIRE : Araign�e
EPELANT : S�parant les lettres
EPENTHESE : Apparition d'un ph�nom�ne non �tymologique
EPERDU : Affol�
EPERON : Rostre
EPERONNER : Aiguillonner
EPHEMERIDE : Table
EPHORE : Magistrat de Sparte
EPI : Partie terminale de la tige
EPICEA : Conif�re
EPICENE : Qui d�signe aussi bien le m�le que la femelle
EPICENTRE : Foyer
EPICURIENNE : Qui ne songe qu'au plaisir
EPIDEMIE : Maladie transmissible
EPIDERME : Enveloppe
EPIERONT : Espionneront
EPIEUX : B�tons
EPIGONE : H�ros grecs
EPIGRAMMATIQUE : Satirique
EPIGRAMME : Petite po�me satirique
EPIGRAPHE : Citation
EPIGRAPHIE : Etude des citations
EPILEPSIE : Maladie nerveuse
EPILOBE : Plante � fleurs roses
EPINCANT : Supprimant des bourgeons
EPINEUX : Difficile
EPINGLER : Agrafer
EPINOCHE : Poisson 
EPINOCHETTE : Petit poisson
EPIQUE : Pourrait figurer dans une �pop�e
EPISCOPAL : Qui appartient � l'�v�que
EPISSER : Assembler
EPISSOIR : Outil de matelot
EPISTEMOLOGIE : Etude des sciences
EPISTOLIERE : Ecrivain
EPITHELIUM : Membrane
EPITRE : Lettre
EPLORE : Larmoyant
EPLUCHE : D�cortique
EPLUCHER : D�cortiquer
EPOINTER : Emousser
EPONGER : Etancher
EPONTILLER : Consolider
EPOPEE : Long po�me
EPOUMONER : S' essouffler (s')
EPOUSER : Embrasser
EPOUSSETER : Nettoyer
EPOUSTOUFLER : Epater
EPOUVANTER : Effrayer
EPOUX : Compagnon
EPSILON : Lettre de l'alphabet grec
EPUISANTE : Fatigante
EPUISEMENT : Appauvrissement
EPULPEUR : Appareil utilis� dans la distillation des betteraves
EPURATOIRE : Qui assainit
EPURGE : Vari�t� d'euphorbe
EQUARRISSEUR : D�coupeur
EQUATION : Formule d'�galit�
EQUATORIAUX : Compris entre les deux tropiques
EQUERRAGE : Angle
EQUERRE : Instrument de mesure
EQUIDES : Famille de mammif�res
EQUILATERAUX : Ont les m�mes c�t�s
EQUILIBRER : Compenser
EQUIMOLECULAIRE : Type de m�lange
EQUINOXE : Se produit deux fois par an
EQUIPARTITION : R�partition
EQUIPIER : Camarade
EQUITABLEMENT : De mani�re int�gre
EQUIVALAIENT : Egalaient
EQUIVALENT : Egalent
EQUIVOQUE : Ambigu
ER : Erbium
ERABLE : Grand arbre
ERAFLER : Ecorcher
ERAILLE : Rauque
ERE : Point de d�part d'une chronologie particuli�re
EREINTEMENT : Grosse fatigue
ERES : P�riodes
ERG : R�gion du Sahara
ERGOTANT : Chicanant
ERGOTERIE : Argument
ERIGE : El�ve
ERODE : Use
EROSION : Frottement
ERRATIQUE : Mal localis�
ERREUR : B�vue
ERS : Plante herbac�e
ERSATZ : Produit de substitution
ERUDIT : Cultiv�
ERUPTION : Pouss�e
ES : En mati�re de
ESBIGNANT : D�campant
ESBROUFEUR : Bluffeur
ESCADRILLE : Groupe
ESCALADER : Gravir
ESCALIER : Suite de marches
ESCAMOTER : Cacher
ESCARBILLE : Fragment incompl�tement br�l�
ESCARGOT : Mollusque
ESCARPEMENT : Versant
ESCARRE : Cro�te
ESCHATOLOGIQUE : Qui concerne l'�tude de la fin du monde
ESCLAFFENT : Pouffent
ESCLAVE : D�pendant
ESCOMPTE : Remise
ESCORTANT : Accompagnant
ESCOURGEON : Orge
ESCRIMEUR : Ep�iste
ESCROQUERIE : Tromperie
ESPACANT : Echelonnant
ESPACER : Echelonner
ESPAGNE : Pays d'Europe
ESPALIER : Mur
ESPERANCE : Confiance
ESPERENT : Attendent
ESPIONNAGE : Surveillance
ESPLANADE : Lieu de promenade
ESQUILLE : Morceau d'os
ESQUINTANT : D�t�riorant
ESQUISSE : Premi�re forme
ESSAI : Tentative
ESSAIME : Disperse
ESSARTER : D�broussailler
ESSAYISTE : Auteur
ESSEULE : D�laiss�
ESSORER : Presser du linge
ESSORILLER : Couper les oreilles
ESSOUFFLEMENT : Anh�lation
ESSUYER : Eponger
EST : Levant
ESTACADE : Digue
ESTAMPAGE : Gravure
ESTAMPILLER : Faire une marque
ESTER : Corps r�sultant de l'action d'un acide sur un alcool
ESTHETIQUE : Harmonieux
ESTHETISME : Doctrine dont Oscar Wilde fut un adepte
ESTIMATION : Appr�ciation
ESTIMER : Appr�cier
ESTIVAUX : De l'�t�
ESTOMAQUE : Epat�
ESTOMPER : Att�nuer
ESTOQUER : Frapper
ESTRAPADE : Supplice
ESTROPIANT : Blessant gravement
ESTROPIER : Blesser gravement
ESTUAIRE : Embouchure
ET : Conjonction de coordination
ETA : Lettre de l'alphabet grec
ETABLIR : Installer
ETABLISSEMENT : Maison
ETAGEMENT : Echelonnement
ETAI : C�ble
ETAIN : M�tal blanc
ETAIS : C�bles
ETAL : Table
ETALAGEANT : Exposant
ETALE : Calme
ETALEES : Expos�es
ETALER : Exposer
ETALON : R�f�rence
ETALONNER : V�rifier par comparaison
ETALS : Tables
ETAMER : Recouvrir de m�tal blanc
ETAMPAGE : Op�ration r�alis�e sur un fer � cheval
ETAMPES : Matrices
ETANCHEITE : Caract�ristique int�ressante pour un bateau
ETANCON : B�quille
ETANCONNEMENT : Action d'�tayer
ETANCONNER : Etayer
ETARQUER : Tendre
ETAT : Condition
ETATISATION : Nationalisation
ETATS : Conditions
ETAU : Presse
ETAUX : Presses
ETC : Et le reste
ETE : Saison
ETEINDRE : Etouffer
ETENDAGE : Fil entre deux poteaux
ETENDARD : Drapeau
ETENDUE : D�ploy�e
ETERNISANT : Immortalisant
ETERNUEMENT : Sternutation
ETESIENS : Vents p�riodiques annuels
ETETER : Ecimer
ETHANE : Gaz combustible
ETHER : Espace
ETHEROMANIE : Toxicomanie
ETHMOIDE : Os du cr�ne
ETHNIE : Population
ETHNOGRAPHIE : Classement des peuples
ETHNOLOGIE : Anthropologie
ETHYLENE : Gaz incolore
ETINCELANTE : Brillante
ETINCELLEMENT : Scintillement
ETIOLEMENT : Affaiblissement
ETIOLOGIE : Etude de l'origine des organes
ETIQUETTE : Protocole
ETIREMENT : Allongement
ETOFFE : Tissus
ETOILE : Plan�te
ETOLE : Bande d'�toffe
ETONNEMENT : Surprise
ETOUFFANT : Asphyxiant
ETOUFFER : Asphyxier
ETOUPILLER : Garnir la lumi�re d'un canon
ETOURDIR : Assommer
ETRANGE : Anormal
ETRANGLEE : Resserr�e
ETRANGLEMENT : Resserrement
ETREINDRE : Serrer
ETREINTE : Enlacement
ETRILLANT : Brossant
ETRIPE : Eventre
ETROITE : petite
ETUDIANT : Universitaire
ETUI : Gaine
ETUVER : S�cher
ETYMOLOGISTE : Linguiste
EU : Europium
EUCLIDIEN : G�om�trique
EUGENIQUE : G�n�tique
EUH : Interjection
EUPATOIRE : Plante herbac�e
EUPHONIQUEMENT : Harmoniquement
EUPHORBIACEES : Famille de plantes phan�rogames
EUPHORISANT : Engendrant l'aise
EUPHUISME : Pr�ciosit�
EURASIEN : M�tis
EUROPE : Continent
EUROPIUM : Corps simple
EUTHANASIQUE : Qui tue
EUX : Pronom compl�ment
EVACUATION : Elimination
EVADEE : Fugitive
EVALUE : Estime
EVANGELISATEUR : Missionnaire
EVANGELISTE : Pr�dicateur
EVANOUISSEMENT : Disparition
EVAPORATION : Cal�faction
EVASEMENT : Agrandissement
EVASURE : Ouverture
EVEILLE : Alerte
EVENTAIL : Choix
EVENTEE : Alt�r�e par l'air
EVENTUEL : Possible
EVERTUER : S'appliquer (s')
EVIDENCE : Certitude
EVINCEMENT : Eviction
EVITAGE : Mouvement du bateau
EVOCATION : Repr�sentation
EVOLUER : Changer
EVOLUTIONNISTE : Transformiste
EX : Ancien
EXACERBANT : Irritant
EXACTEMENT : Fid�lement
EXAGERATION : Amplification
EXAGEREMENT : Avec vantardise
EXAMEN : Investigation
EXAMINER : Consid�rer
EXASPERER : Enerver
EXAUCE : Comble
EXCAVATEUR : Pelle m�canique
EXCEDA : Irrita
EXCEDENTAIRE : En trop
EXCELLENCE : Perfection
EXCENTRER : D�placer le milieu
EXCEPTER : Exclure
EXCEPTION : Singularit�
EXCESSIVE : D�mesur�e
EXCIPIENT : Substance qui entre dans la composition des m�dicaments
EXCITATEUR : Fomentateur
EXCITER : Allumer
EXCLAMER : Crier (s')
EXCLUANT : Rejetant
EXCLUS : Bannis
EXCLUSIVEMENT : Uniquement
EXCOMMUNIANT : Rejetant
EXCORIER : Ecorcher
EXCROISSANCES : Protub�rances
EXCURSIONNE : Visite
EXCUSER : Blanchir
EXECRER : Abhorrer
EXECUTER : R�aliser
EXECUTOIRE : Qui doit �tre fait
EXEMPLAIRE : Echantillon
EXEMPLIFIER : Illustrer
EXEMPTE : Dispens�e
EXERCER : Former
EXERGUE : Epigraphe
EXHALANT : Embaumant
EXHAUSSANT : Elevant
EXHAUSTIF : Complet
EXHEREDE : D�sh�rite
EXHIBITIONNISTE : Qui aime se montrer
EXHORTATION : Incitation
EXIGENCE : Revendication
EXIGUE : Etroite
EXILAIENT : D�portaient
EXINSCRIT : Tangent � un c�t� d'un triangle et au prolongement des deux autres
EXISTENTIALISME : Doctrine philosophique
EXOCET : Poisson des mer chaudes
EXONDE : Emerge
EXONERE : Dispense
EXORCISER : Conjurer
EXORDE : Pr�ambule
EXPANSION : D�veloppement
EXPECTORATION : Toux
EXPEDIENT : Moyen
EXPEDITIONNAIRE : Employ� � la copie d'actes
EXPERIMENTALE : Qui constitue une exp�rience
EXPERIMENTAUX : Qui constituent une exp�rience
EXPERTEMENT : Avec comp�tence
EXPIANT : Payant
EXPIRANT : Mourant
EXPLICABLE : Compr�hensible
EXPLICITER : Formuler
EXPLOITATION : Fermage
EXPLOITEUR : Profiteur
EXPLORATION : D�couverte
EXPLOSER : Eclater
EXPLOSION : Commotion
EXPOSE : Analyse
EXPRESS : Train
EXPRESSIVE : D�monstrative
EXPRIME : Signifie
EXPROPRIATION : Saisie
EXPULSER : Chasser
EXPURGEANT : Epurant
EXSUDATION : R�sultat de la chaleur
EXTASE : Ravissement
EXTATIQUE : Ravi
EXTENSIBILITE : Elasticit�
EXTENSOMETRE : Appareil de mesure
EXTENUANT : Tr�s fatiguant
EXTERIORISE : Exprime
EXTERMINE : D�truit
EXTINCTEUR : Bouteille rouge
EXTIRPATION : Extraction
EXTORQUEUR : Escroc
EXTRADE : Livre
EXTRAVAGANTS : Bizarres
EXTRAVASER : Couler (s')
EXTRAVERTIE : Tourn�e vers le monde ext�rieur
EXTREME : Dernier
EXTREMUM : Maximum ou minimum
EXTRUSION : Proc�der de traitement du m�tal
EXULTER : Jubiler
F : Pas de d�finition
FA : Note
FABLIER : Recueil
FABRIQUANT : Constructeur
FABULEUSE : Fantastique
FAC : Ecole
FACE : C�t�
FACES : C�t�s
FACETIE : Bouffonnerie
FACETTER : Tailler
FACHEUX : Emb�tant
FACIES : Aspect du visage
FACILITER : M�nager
FACON : Fabrication
FACONNER : Elaborer
FACTAGE : Livraison
FACTICE : Artificiel
FACTOTUM : Intendant
FACTURE : Style
FACULTATIF : Pas obligatoire
FADASSE : Plat
FADING : Evanouissement
FAGOTER : Accoutrer
FAIBLARDE : Pas tr�s forte
FAIBLIR : Baisser
FAIENCE : C�ramique
FAILLE : Fissure
FAILLIR : Manquer
FAIM : D�sir
FAINEANTE : Paresseux
FAISABLE : Possible
FAISAN : Oiseau gallinac�
FAIT : B�ti
FAITOUT : R�cipient
FALBALA : Volant
FALLACIEUSEMENT : Avec hypocrisie
FALSIFIER : Truquer
FALUCHE : B�ret
FAMELIQUE : Maigre
FAMILIARISER : Habituer
FAMILISTERE : Coop�rative
FAN : Admirateur
FANAL : Flambeau
FANATIQUE : Exalt�
FANATISME : Intol�rance
FANE : Fl�tri
FANER : Fl�trir
FANFARONNADE : Vantardise
FANGEUSE : Boueuse
FANION : Drapeau
FANTASMAGORIQUE : Fantastique
FANTASTIQUE : Imaginaire
FAON : Petit d'une b�te fauve
FARADAY : Physicien anglais
FARANDOLE : Danse populaire
FARCEUR : Plaisantin
FARDAGE : Fraude
FARDEAUX : Charges
FARFOUILLE : Fur�te
FARIGOULE : Eau de toilette
FARINER : Saupoudrer
FAROUCHE : Timide
FASCICULE : Carnet
FASCINA : Charma
FASCINATION : Charme
FASCISME : Doctrine
FASEYE : Bat au vent
FASTIDIEUSEMENT : De mani�re fatigante
FASTUEUX : Riche
FAT : Fi�rot
FATALES : Funestes
FATIDIQUE : Qui marque une intervention du destin
FATIGUANT : Usant
FATS : Fi�rots
FATUITE : Infatuation
FAUBOURIEN : Banlieusard
FAUCHEE : Ruin�e
FAUCHEUSE : Machine agricole
FAUCON : Oiseau rapace
FAUFILER : S'introduire (se)
FAUSSAIRES : Contrefacteurs
FAUSSET : Voix aigu�
FAUTIF : Coupable
FAUTIVEMENT : De mani�re coupable
FAUVETTE : Petit oiseau
FAVORI : Pr�f�r�
FAVORITISME : N�potisme
FAX : Appareil de communication
FE : Fer
FEBRILE : Excit�
FECONDITE : Fertilit�
FECULE : Substance amylac�e
FEDERALE : Relative au gouvernement central
FEDERANT : R�unissant
FEDERER : R�unir
FEE : Etre imaginaire
FEES : Etres imaginaires
FEIGNANT : Simulant
FEINTANT : Trompant
FELDWEBEL : Adjudant de l'arm�e allemande
FELIBRIGE : Ecole litt�raire
FELIDE : Famille de mammif�res
FELLAGHA : Partisan alg�rien
FELONNE : D�loyale
FEMININE : Femelle
FEMORALE : De la cuisse
FENDAIT : Divisait
FENDILLE : Craquelle
FENDILLER : Craqueler
FENDRE : Diviser
FENDU : Cass�
FENETRANT : Faisant des trous
FENOUIL : Plante aromatique
FENUGREC : Plante utilis�e pour les cataplasmes
FER : M�tal blanc
FERMAIENT : Bouclaient
FERMEMENT : Avec assurance
FERMENTE : L�ve
FERMETE : Duret�
FERMIER : Agriculteur
FEROCEMENT : Sauvagement
FERRADE : Action de marquer le b�tail
FERRAILLE : Vielle t�le
FERRAILLER : Se battre au sabre ou � l'�p�e
FERRATE : Sel de l'acide ferrique
FERRERA : Accrochera
FERROMAGNETISME : Propri�t� d'attirer
FERROPRUSSIATE : M�lange employ� pour la reproduction des plans
FERRUGINEUX : Qui contient du fer
FERTILE : F�cond
FERTILISER : Am�liorer
FERU : Epris
FERUE : Eprise
FERUES : Eprises
FERVENT : D�vot
FESSE : Croupe
FESTIN : Banquet
FESTIVITE : F�te
FESTONNER : D�couper
FETARD : Noceur
FETICHISME : V�n�ration
FEU : Combustion
FEUDATAIRE : Vassal
FEUILLANT : Religieux
FEUILLERET : Rabot
FEUILLETER : Parcourir
FEUILLETONISTE : Ecrivain
FEUTRE : Etoffe
FEUTREE : Ouat�e
FEVE : Graine comestible
FEZ : Calotte de laine
FIANCEE : Promise
FIASQUE : Bouteille
FIAT : D�cision volontaire apr�s d�lib�ration
FIBRILLATION : Contraction
FIC : Verrue
FICELANT : Attachant
FICELLE : Petite baguette
FICHE : Carte
FICHU : Perdu
FICTIVEMENT : De mani�re imaginaire
FIDELISATION : Abonnement
FIEF : Domaine
FIEL : Bile
FIER : Suffisant
FIERS : Suffisants
FIEVREUX : Chaud
FIGEE : Glac�e
FIGUE : Fruit comestible
FIGURATION : Repr�sentation
FIGURINE : Santon
FIL : Tranchant
FILAGE : Op�ration de filature
FILANDIERE : Fileuse
FILE : Queue
FILER : D�camper
FILERA : D�campera
FILET : Morceau de viande
FILEZ : D�campez
FILIAL : Qui �mane d'une enfant
FILIN : Cordage
FILLEUL : Prot�g�
FILM : couche mince
FILMA : Enregistra
FILME : Enregistre
FILMER : Enregistrer
FILON : Veine
FILOUTE : Tricheuse
FILS : H�ritier
FILTRANT : Clarifiant
FILTRER : Clarifier
FIN : Limite
FINALE : Derni�re �preuve
FINALEMENT : En conclusion
FINANCE : Argent
FINAUDERIE : Malice
FINE : Eau de vie
FINES : Charbon en morceau tr�s petits
FINETTE : Etoffe
FINI : Poli
FINIR : Achever
FINISH : Fin d'un combat de boxe
FINISSAGE : Ajustage
FINISTERE : D�partement fran�ais
FINLANDAISE : Finnoise
FION : Bonne tournure
FIORITURES : Ornements
FISC : Administration
FISSURANT : Fendant
FISTON : Fils
FISTULINE : Langue de boeuf
FIXATIF : Pr�paration qui �vite au fusain de s'effacer
FIXER : Assujettir
FLACHE : Creux � l'ar�te d'une poutre
FLACONNAGE : fabrication de bouteilles
FLAGELLATION : Action de fouetter
FLAGEOLE : Tremble
FLAGORNER : Flatter bassement
FLAGRANTE : Evidente
FLAIRE : Deviner
FLAMBAGE : Courbure
FLAMBEAU : Brandon
FLAMBEUR : Joueur
FLAMENCO : Musique
FLAMME : Eclat
FLAMMEROLE : Feu follet
FLANCHANT : Se d�gonflant
FLANDRIN : Grand dadais
FLANERIE : Balade
FLANQUER : Garnir
FLASH : Courte nouvelle
FLATTER : Complimenter
FLATULENCE : Production de gaz
FLAVESCENTE : Qui tire sur le jaune
FLEAU : Catastrophe
FLECHE : Dard
FLECHISSEMENT : Courbure
FLEMMARD : Paresseux
FLET : Poisson plat
FLETRISSENT : Fanent
FLEURANT : Embaumant
FLEURET : Ep�e
FLEURIR : Bourgeonner
FLEURON : Ornement
FLEXION : Fl�chissement
FLEXUEUX : Sinueux
FLIBUSTIER : Corsaire
FLIPOT : Pi�ce servant � dissimuler une fente
FLIRTER : Faire la cour
FLOCHE : L�g�rement torse
FLOCON : Petite masse peu dense
FLORAISON : Epanouissement
FLORALIES : Exposition
FLORENCE : Crin tr�s r�sistant employ� pour la p�che
FLORICULTURE : Branche de l'horticulture
FLORILEGE : Recueil de pi�ces choisies
FLOTTABLE : Insubmersible
FLOTTE : Eau
FLOU : Vague
FLUCTUATION : Variation
FLUETTE : Gracile
FLUORESCENCE : Emission de radiations visibles
FLUORHYDRIQUE : Se dit d'un acide utilis� dans la gravure sur verre
FLUTE : Instrument � vent
FLUX : Emission
FLUXMETRE : Appareil de mesure
FM : Type de modulation
FOCALISER : Concentrer
FOI : Confiance
FOIE : Organe de la digestion
FOIN : Fourrage
FOIRES : Expositions
FOISON : Abondance
FOISONNE : Abonde
FOLATRE : Espi�gle
FOLIE : Psychose
FOLIOTE : Num�rote
FOLKLORE : Ensemble des traditions
FOLLE : Filet de p�che
FOLLICULE : Fruit
FOMENTATEUR : Fauteur
FONCE : File
FONCIERE : Inn�e
FONCTIONNAIRE : Agent
FONCTIONNARISME : Pr�pond�rance de la fonction publique
FONDAIS : Basais
FONDAMENTAL : Essentiel
FONDAMENTAUX : Essentiels
FONDATRICE : Cr�atrice
FONDERIE : Aci�rie
FONDRE : Liqu�fier
FONDUE : D�grad�e
FONGICIDE : Contre le mildiou
FONTAINE : Robinet
FOOTING : Entra�nement
FORAGE : Sondage
FORCE : Vigueur
FORCER : Fracturer
FORCERIE : Serre
FORCIPRESSURE : M�thode d'h�mostase
FORCISSANT : Grossissant
FORCLORE : Exclure
FORE : Perce
FORERAIT : Percerait
FORERONS : Percerons
FORET : Vrille
FORFAIT : Faute
FORFAITURE : F�lonie
FORGE : Atelier
FORGER : Travailler le m�tal
FORJETER : Construire en saillie
FORLANCER : Faire sortir de son g�te
FORMALISER : Offenser
FORMATEUR : Professeur
FORME : Apparence
FORMERET : Arc
FORMIDABLE : Extraordinaire
FORMOLER : D�sinfecter
FORMULATION : Explication
FORNICATRICE : Personne qui commet le p�ch� de la chair
FORT : Puissant
FORTE : Puissante
FORTES : Puissantes
FORTICHE : Balaise
FORTIN : Casemate
FORTS : Puissants
FORTUITE : Impr�vue
FORURE : Trou
FOSSILE : Empreinte
FOSSOYEUR : Naufrageur
FOU : D�ment
FOUAILLER : Battre
FOUDROYANT : Mortel
FOUETTANT : Fouaillant
FOUETTENT : Fouaillent
FOUETTERAIT : Fouaillerait
FOUETTERONT : Fouailleront
FOUGUE : Ardeur
FOUGERE : Plante
FOUGUEUX : Imp�tueux
FOUILLEUR : Chercheur
FOULAGE : Ecrasement
FOULER : Pi�tiner
FOULQUE : Oiseau �chassier
FOUR : D�sastre
FOURBI : Attirail
FOURBURE : Cogestion du pied
FOURCHETTE : Couvert
FOURGON : V�hicule
FOURGUER : Vendre
FOURMILIERE : Habitation
FOURMILLER : Abonder
FOURNI : Dru
FOURNISSANT : Alimentant
FOURRAGE : Nourriture
FOURREAUX : Etuis
FOURRER : Garnir
FOURRIER : Math�maticien fran�ais
FOURS : D�sastres
FOURVOYANT : Egarant
FOUTOIR : D�sordre
FOX : Chien
FR : Francium
FRACASSANT : Brisant
FRACTIONNEL : Qui tend � diviser
FRAGILE : Ch�tif
FRAGMENT : Morceau
FRAGMENTER : Diviser
FRAICHIR : Se lever
FRAIS : D�pense
FRAISER : Usiner
FRAISIER : Plante basse
FRAMBOISE : Fruit
FRANC : Sinc�re
FRANCHE : Sinc�re
FRANCHISE : Droiture
FRANCIQUE : Ancienne langue
FRANCISCAIN : Religieux
FRANCIUM : El�ment radioactif
FRANCOLIN : Oiseau gallinac�
FRANGER : Border
FRANGON : Arbrisseau
FRAPPE : Dactylographie
FRATERNELLEMENT : Avec solidarit�
FRATRICIDE : Meurtrier
FRAUDEUR : Escroc
FRAYANT : Ouvrant
FREDONNE : Chantonne
FREGATE : Oiseau de mer
FREINER : Contrarier
FRELATEE : D�natur�e
FRELON : Grosse gu�pe
FREMISSEMENT : Bruissement
FRENESIE : Fi�vre
FREON : Fluide frigorifique
FREQUENCE : R�p�tition
FREQUENTANT : Hantant
FRERE : Est parfois beau  
FRETANT : Louant
FRETILLANTE : Remuante
FRETTAGE : Location
FREUDISME : Ensemble de th�ories psychanalytiques
FREUX : Esp�ce de corneille
FRIBOURG : Ville de Suisse
FRICASSEE : Gibelotte
FRICHE : Abandon
FRICTION : Frottement
FRIGORIFIER : Refroidir
FRIMAIRE : Troisi�me mois de l'ann�e r�publicaine
FRIMAS : Brouillard
FRIME : Com�die
FRIMOUSE : Minois
FRINGUANT : Alerte
FRIPER : Rider
FRIPONNE : Coquine
FRISE : Boucl�
FRISQUET : Frais
FRISSONNEMENT : Tremblement
FRITE : Morceau de pomme de terre
FRITEUSE : Ustensile de cuisine
FRIVOLEMENT : L�g�ret�
FROIDEMENT : Fra�chement
FROISSEMENT : Heurt
FROLER : Raser
FROMAGER : Arbre tropical
FRONCER : Plisser
FRONDANT : Lan�ant
FRONTIERE : S�paration
FRONTIGNAN : C�page du sud de la France
FROTTEE : Tartine
FROTTOIR : Grattoir
FROUSSARD : Peureux
FRUCTIFIANT : D�veloppant
FRUCTUEUSEMENT : Avec profit
FRUGAUX : Sobres
FRUIT : profit
FRUSTE : Grossier
FRUSTRER : D�savantager
FUCACEES : Famille d'algues
FUCUS : Algue
FUGACE : Eph�m�re
FUGUE : Escapade
FUIR : D�camper
FULGURANTE : Foudroyante
FULIGINEUX : Noir�tre
FULMINATION : Action de s'emporter
FUMEE : Exhalaison
FUMEROLLE : Emanation de gaz
FUMET : Odeur
FUMIGER : Enfumer
FUNERAILLES : Enterrement
FURAX : Pas content du tout
FURETENT : Chassent
FURETER : Chasser
FURETERONT : Chasseront
FUREUR : Violence
FURIEUSE : Acharn�e
FURONCLE : Inflammation de la peau
FUSEAU : Pantalon
FUSEE : Projectile
FUSELAGE : Corps d'un avion
FUSIBLE : Coupe-circuit
FUSILIER : Matelot
FUSIONNER : R�unir
FUSTANELLE : Jupon masculin
FUT : Baril
FUTES : Malins
FUTURISME : Doctrine de Marinetti
FUYANT : Insaisissable
G : Pas de d�finition
GA : Gallium
GABARE : Bateau
GABIER : Matelot
GABON : Pays Africain
GACHEUR : Saboteur
GADOLINIUM : M�tal rare
GAFFER : Accrocher
GAG : Blague
GAGA : G�teux
GAGE : Caution
GAGEURE : Pari
GAGNANTE : Premi�re
GAGS : Blagues
GAI : Joyeux
GAIE : Joyeuse
GAIES : Joyeuses
GAIETE : Joie
GAILLARDISE : Gauloiserie
GAIN : Fruit
GAINE : Etui
GAINER : Prot�ger
GAL : Unit� d'acc�l�ration
GALA : C�r�monie
GALALITHE : Premier plastique
GALANTINE : Charcuterie
GALAS : C�r�monies
GALBER : Cintrer
GALE : Maladie de peau
GALENISME : Doctrine m�dicale
GALET : Roulette
GALETTE : G�teau
GALIBOT : Personne travaillant au service des voies
GALILEEN : Palestinien
GALIOTE : Caboteur
GALLON : Mesure de capacit�
GALOCHE : Chaussure
GALONNER : Border
GALOPER : Courir
GALUCHAT : Peau de poisson
GALVANISE : Electrise
GALVAUDANT : Avilissant
GAMBETTE : Jambe
GAMELLE : Ecuelle
GAMINE : Petite fille
GAMMA : Lettre de l'alphabet grec
GANACHE : M�choire
GANGA : Oiseau galliforme
GANGRENER : Corrompre
GANGSTER : Bandit
GANOIDE : Esturgeon
GARANCE : Plante herbac�e
GARANTIR : Assurer
GARCETTE : Petit cordon
GARCON : Serveur
GARDENIA : Arbuste exotique
GARDER : Conserver
GARE : Endroit o� les bateaux peuvent se croiser
GARGARISANT : Savourant (se)
GARGOTIER : Cuisinier
GARGOUILLER : Produire un bruit d'eau
GARNEMENT : Galopin
GARNISON : Corps de troupe
GARNITURE : Parure
GARROT : Supplice
GASCOGNE : R�gion fran�aise
GASOIL : Carburant
GASPILLANT : Perdant
GASTRALGIE : Douleur de l'estomac
GASTRITE : Inflammation de la muqueuse de l'estomac
GASTROSCOPIE : Examen
GATE : Ch�ri
GATEAU : Dessert
GAUCHEMENT : Maladroitement
GAUCHIR : Voiler
GAUFRE : P�tisserie
GAULE : Canne
GAULIS : Branche
GAULOIS : Grivois
GAUSSANT : Raillant
GAVE : Cours d'eau
GAVIALS : Reptile crocodilien
GAZ : Vapeur invisible
GAZE : Taffetas
GAZEIFICATION : Action de vaporiser
GAZER : Dissimuler
GAZETIER : Journaliste
GAZOLINE : Ether de p�trole
GAZONNER : Rev�tir d'herbe
GAZOUILLEMENT : Murmure
GD : Gadolinium
GE : Germanium
GECKO : Reptile saurien
GEISHA : Chanteuse japonaise
GEL : Cong�lation
GELA : Congela
GELAIENT : Congelaient
GELATINE : Ichtyocolle
GELEES : Congel�es
GELURE : Froidure
GEMELLIPARITE : Etat d'une femelle qui porte des jumeaux
GEMINATION : R�p�tition
GEMISSANT : Plaintif
GEMMATION : D�veloppement des bourgeons
GEMMULE : Bourgeon de l'embryon
GENDARME : Militaire
GENEALOGIE : Ascendance
GENERALISABLE : Qui peut �tre �tendu
GENERALISSIME : G�n�ral en chef
GENERATRICE : Dynamo
GENERIQUE : Commun
GENEROSITE : D�sint�ressement
GENESE : Nom du premier livre de l'Ancien Testament
GENET : Cytise
GENEUR : Emp�cheur
GENEVRIER : Arbrisseau
GENIALEMENT : Magistralement
GENISSE : Jeune vache
GENOCIDE : Destruction 
GENOU : Articulation
GENT : Peuple
GENTILITE : Ensemble des peuples pa�ens
GENTILLESSE : Amabilit�
GENTRY : Noblesse anglaise non titr�e
GEOGRAPHIE : R�alit� physique
GEOLE : Cachot
GEOLOGIE : Science de l'histoire de la terre
GEOMETRAUX : Qui ne tiennent pas compte de la perspective
GEOMORPHOLOGIE : Etude de l'�volution du relief terrestre
GEORGIEN : Langue caucasienne
GEOTRUPE : Insecte col�opt�re
GERANCE : Administration
GERBAGE : Empilage
GERBEUR : Appareil de levage
GERCER : Crevasser
GERE : Administre
GERIATRIE : M�decine
GERMANIQUE : Teuton
GERME : Embryon
GEROME : Fromage
GERONTOLOGIE : Etude de la vieillesse
GERSEAUX : Cordages qui renforcent une poulie
GESSE : Plante l�gumineuse
GESTICULATION : Pantomime
GESTION : Administration
GHETTO : Lieu de quarantaine
GIBBON : Singe
GIBELINE : Partisane italienne des empereurs d'Allemagne
GIBOULEE : Pluie soudaine
GICLANT : Eclaboussant
GICLEUR : Petite pi�ce d'un carburateur
GIGANTESQUE : Enorme
GIGOTER : Remuer
GIGUE : Jambe
GILLE : Personnage niais et na�f
GINGIVITE : Inflammation des gencives
GIRAFE : Grand mammif�re ongul�
GIRAUMONT : Courge d'Am�rique
GIROFLEE : Plante herbac�e
GIRON : Milieu
GISEMENT : Veine
GITAN : Boh�mien
GIVRE : Frimas
GIVRURE : D�faut de la pierre
GLACE : Miroir
GLACIERE : Appareil de conservation
GLACON : Personne froide
GLAIRE : Blanc d'oeuf
GLAISE : Argile
GLANDE : Organe
GLANER : Butiner
GLAPIR : Faire entendre une voix aigre
GLAS : Son de cloche
GLAUQUE : Verd�tre
GLENOIDALE : Re�oit un condyle
GLISSANTE : Dangereuse
GLISSEMENT : D�placement
GLOBAL : Total
GLOBALEMENT : Dans son ensemble
GLOBIGERINE : Protozoaire p�lagique
GLOBULINE : Vari�t� d'albumines
GLORIETTE : Petit pavillon 
GLORIFICATION : Apologie
GLOSSAIRE : Dictionnaire
GLOSSINE : Mouche ts�-ts�
GLOSSITE : Inflammation de la langue
GLOUGLOUTE : Faire un bruit d'eau
GLOUSSERONT : Riront
GLU : Colle
GLUCIDE : Nom g�n�rique des hydrates de carbone
GLUCOSE : Sucre
GLUTINEUX : Adh�sif
GLYCERINE : Tri-alcool provenant de la saponification des graisses
GLYCINE : Plante � fleurs odorantes
GLYCOCOLLE : Acide amin�
GLYCOSURIQUE : Diab�tique
GNEISSIQUE : Compos� principalement de feldspath, de quartz et de mica
GNOMES : Esprits
GNOSTICISME : Doctrine
GOAL : Gardien
GOBELET : R�cipient
GOBER : Avaler
GOBIE : Poisson du littoral
GODAILLER : Faire des faux plis
GODET : R�cipient
GODILLE : Aviron
GODIVEAUX : Boulettes de viande
GOELETTE : Bateau
GOEMON : Algues marines
GOGUENARDISE : Plaisanterie
GOINFRERIE : Gloutonnerie
GOLFE : Echancrure
GOMMER : Effacer
GOMMIER : Famille d'arbre
GONDOLANT : Tordant
GONDOLIER : Batelier
GONFLEMENT : Enflure
GONFLEUR : Compresseur
GONIOMETRIE : Science de la mesure des angles
GONOCHORISME : S�paration compl�te des sexes
GORET : Jeune cochon
GORGER : Gaver
GOSIER : Gorge
GOUACHE : Peinture
GOUAILLER : Plaisanter
GOUAILLEUSE : Fac�tieuse
GOUFFRE : Ab�me
GOUJAT : Mufle
GOUJONNE : Assemble
GOULET : Passage r�tr�ci
GOULUE : Avide
GOUPILLE : Goujon
GOURA : Pigeon � huppe
GOURDE : Bidon
GOURER : Se tromper (se)
GOURMANDER : Gronder
GOURMETTE : Bracelet
GOUTER : Collation
GOUTTE : Petite quantit� de liquide
GOUTTIERE : Rainure
GOUVERNAIL : plan orientable immerg�
GOUVERNEMENTAL : Minist�riel
GOYAVE : Fruit des cara�bes
GR : Grade
GRACE : El�gance
GRACIEUSEMENT : Avec �l�gance
GRACILE : Elanc�
GRADIENT : Variation de pression
GRADUEL : Progressif
GRAFFITI : Dessin
GRAILLON : Mauvaise cuisine
GRAINE : Semence
GRAINETERIE : Commerce de semence
GRAISSER : Lubrifier
GRAMINEE : Herbe
GRAMMATISTE : Enseignant grec
GRAMOPHONE : Appareil de reproduction sonore
GRANDILOQUENCE : Emphase
GRANDIOSE : Imposant
GRANITE : Roche dure
GRANULITE : Roche granito�de
GRANULOMETRIE : M�thode de classement
GRAPHIQUEMENT : Par l'�criture
GRAPHITE : Vari�t� de carbone
GRAPHOMETRE : Instrument de mesure des angles
GRAPPILLER : Gratter
GRAS : Adipeux
GRASSEYER : Mani�re de parler
GRASSOUILLETTE : Potel�e
GRATIN : Plat
GRATIS : Qui ne co�te rien
GRATUITE : Caract�re de ce qui est injustifi�
GRAVATS : D�combres
GRAVE : S�rieux
GRAVELURE : Grivoiserie
GRAVER : Buriner
GRAVIMETRIE : Mesure de la pesanteur
GRAVITATION : Attraction
GRE : Convenance
GREBE : Oiseau aquatique palmip�des
GREC : Pr�hell�nique
GRECE : Etat de la p�ninsule balkanique
GRECQUE : Scie de relieur
GREEMENT : Mature
GREER : Equiper
GREFFANT : Entant
GREFFER : Enter
GREGORIEN : Introduit par le pape au VI �me si�cle
GRELIN : Fort cordage
GRELOT : Clochette
GRELOTTE : Tremble
GRELUCHON : Gigolo
GREMILLE : Petite perche
GRENADILLE : Esp�ce de passiflore
GRENAILLE : Rebut de grain
GRENANT : Emiettant
GRENAT : Pierre pr�cieuse
GRENETIS : Cordon fait de petits gains au bord des monnaies
GRENOUILLE : Batracien
GRENOUILLETTE : Esp�ce de renoncule
GRES : Roche s�dimentaire
GRESER : Polir
GRESILLEMENT : L�ger cr�pitement
GREVER : Imposer
GRIBOUILLAGE : Dessin confus
GRIBOUILLIS : Dessin confus
GRIFFE : Empreinte
GRIFFONNAGE : Gribouillage
GRIFFURE : Rayure
GRIGNANT : Faisant des fronces
GRIGNOTANT : S'appropriant
GRIGNOTIS : Taille en traits courts
GRILLAGE : Moucharabieh
GRILLE : Assemblage de barreaux
GRIMACE : Moue
GRIMER : Rider
GRIMOIRE : Livre de magie
GRIMPEREAU : Oiseau passeriforme
GRINCANT : Crissant
GRINGALET : Homme ch�tif
GRIOTTE : Cerise
GRIPPER : Attraper
GRISANT : Enivrant
GRISER : Enivrer
GRISETTE : Etoffe
GRISOU : Gaz combustible
GRIVELANT : Tirant d'un emploi de profits illicites
GRIVELEE : Tachet�e
GRIZZLI : Ours
GROG : Boisson chaude alcoolis�e
GROGNE : Bougonne
GROGNON : Bougon
GROMMELANT : Bougonnant
GRONDE : Tonne
GRONDIN : Poisson comestible
GROSSE : Volumineuse
GROSSIER : Brut
GROSSIR : Enfler
GROSSISSEMENT : Accroissement
GROUILLANTE : Pullulante
GROUPER : R�unir
GRUAU : Grain d'avoine priv� de son
GRUGER : Duper
GRUMELURE : Soufflure
GRUPPETTO : Ornement musical
GUANO : D�jections d'oiseaux marins
GUENON : Cercopith�que
GUEPARD : Mammif�re carnivore
GUEPE : Insecte hym�nopt�re
GUERISON : R�tablissement
GUERNESEY : Ile au large de la Normandie
GUERROYER : Se battre
GUETRE : Jambi�re
GUETTER : Surveiller
GUEULARD : Ouverture d'une chaudi�re
GUEULES : Bouches
GUEUSE : Lingot
GUICHE : Courroie pour suspendre un bouclier
GUIDANT : Conduisant
GUIDEAUX : Filets en forme de sac
GUIDON : Fanion
GUIGNENT : Lorgnent
GUIGNON : Poisse
GUILLEMETER : Faire ressortir une citation
GUILLERETTE : Gaie
GUILLOCHIS : Traits grav�s entrecrois�s sym�triquement
GUILLOTINENT : D�capitent
GUIMBARDE : Instrument de musique
GUINGUETTE : Caf�
GUIPURE : Dentelle
GUITARE : Instrument de musique
GUPPY : Petit poisson d'aquarium
GYMNASE : Salle de sport
GYMNOTE : Poison d'eau douce
GYPAETE : Grand oiseau rapace diurne
H : Pas de d�finition
HA : Interjection
HABILE : Malin
HABILITE : Autorise
HABILLER : V�tir
HABITABLE : Vivable
HABITATION : Demeure
HABITUDE : Manie
HABITUE : Familier
HABLERIE : Fanfaronnade
HACHER : Couper en petits morceaux
HACHIS : Farce
HACHURANT : Rayant
HADDOCK : Aiglefin
HAIKAI : Po�me classique japonais
HAINEUX : Malveillant
HAIRE : Chemise de poil de ch�vre
HALAGE : Remorquage
HALBRAN : Jeune canard sauvage
HALETANTE : Essouffl�
HALICTE : Insecte hym�nopt�re
HALLEBARDE : Arme d'hast
HALLUCINATIONS : Illusions
HALO : Aur�ole
HALOIR : S�choir
HAMAC : Lit suspendu
HAMEAU : Lieu-dit
HAMECONNER : Accrocher
HAMSTER : Petit mammif�re rongeur
HANDICAP : G�ne
HANGAR : Remise
HANNETON : Insecte col�opt�re
HANSE : Association de marchands
HANTISE : Obsession
HAPPE : Crampon
HARANGUAIT : Sermonnait
HARASSANT : Fatigant
HARCELER : Poursuivre
HARDER : Attacher
HARDIESSE : Audace
HARENG : Poisson de mer
HARGNEUX : Acari�tre
HARMONICA : Instrument de musique
HARMONIEUX : M�lodieux
HARMONISER : Accorder
HARNACHEMENT : Equipement
HARPAIL : Troupe de biches
HARPONNER : Attraper
HART : Corde
HASARDEUX : Risqu�
HASCHISCH : Herbe
HASTEE : Qui a la forme d'un fer de lance
HATER : Presser 
HATIVEMENT : Trop vite
HAUBANAGE : C�bles
HAUSSIERE : Corde
HAUTAIN : Arrogant
HAUTIN : Vigne
HAVANE : Cigare
HAVENEAU : Filet
HAVRE : Refuge
HAVRESAC : Sac � dos
HAYON : Panneau amovible
HE : Interjection
HEBERGEANT : Abritant
HEBETEMENT : Abrutissement
HECATOMBE : Carnage
HEDONISME : Doctrine de la recherche du plaisir
HEGELIANISME : Doctrine de Hegel
HEGEMONIE : Autorit�
HELANT : Interpellant
HELIANTHE : Plante � grands capitules jaunes
HELICICULTURE : Elevage des escargots
HELICOIDAL : En forme d'h�lice
HELICON : Instrument de musique � vent
HELIOGRAPHIE : Proc�d� photographique de gravure
HELIOTROPE : Tournesol
HELIUM : Gaz
HELMINTHE : Ver parasite
HEM : Interjection
HEMARTHROSE : Epanchement de sang
HEMATOLOGIE : Etude du sang
HEMATOPOIESE : Formation des globules sanguins
HEMICYCLE : Gradin
HEMISPHERIQUE : Coupole
HEMOGLOBINE : Colorant
HEMORRAGIE : Effusion de sang
HENDECASYLLABE : Vers qui compte onze syllabes
HENNIN : Coiffure f�minine du Moyen Age
HENRY : Unit� d'inductance
HEP : Interjection
HEPATITE : Affection du foie
HEPTAGONALE : Qui a sept angles
HERALDISTE : Sp�cialiste du blason
HERBE : Petite plante phan�rogame
HERBIER : Trait� de botanique
HERBORISTERIE : Commerce o� l'on trouve des plantes m�dicinales
HERCULE : Homme fort
HERE : Homme mis�rable
HEREDITAIRE : Cong�nital
HERESIE : Sacril�ge
HERISSEMENT : Horripilation
HERITAGE : H�r�dit�
HERMAPHRODISME : R�union des deux sexes
HERMETIQUEMENT : De mani�re �tanche
HERMINE : Mammif�re carnivore
HERNIE : Excroissance
HEROIQUEMENT : Bravement
HERONNEAU : Jeune h�ron
HERPETOLOGIE : Etude des reptiles
HERTZIEN : Qui a rapport � la radio
HESITER : R�fl�chir
HETEROMORPHISME : Caract�re de ce qui pr�sente des formes tr�s diff�rentes
HEU : Interjection
HEUR : Bonheur
HEURE : Unit� de temps
HEURISTIQUE : Qui sert � la d�couverte
HEURT : Choc
HEURTER : Cogner
HEURTERA : Cognera
HEURTS : Chocs
HEXAGONE : France m�tropolitaine
HF : Haute fr�quence
HG : Mercure
HI : Interjection
HIATUS : Solution de continuit�
HIBERNER : Dormir 
HIC : Probl�me
HIDEUR : Laideur
HIE : Instrument servant � enfoncer les pav�s
HIEMAL : Hibernal
HIER : Le jour pr�c�dent
HIERATIQUE : Solennel
HILARE : R�joui
HINDI : Langue de l'Inde
HINTERLAND : Arri�re-pays
HIPPOCAMPE : Petit poisson
HIPPOMOBILE : V�hicule � cheval
HIPPOTECHNIE : Technique de l'�levage des chevaux
HIRONDELLE : Oiseau migrateur
HISPANIQUE : Ib�rique
HISSER : Envoyer
HISTOIRE : Anecdote
HISTOLYSE : Destruction de tissus
HISTORIENNE : Annaliste
HISTORIOGRAPHIE : Ensemble d'ouvrages d'histoire
HISTRION : Bouffon
HITLERIEN : Nazi
HIVERNAGE : Temps de la mauvaise saison
HIVERNER : Passer la mauvaise saison � l'abri
HO : Onomatop�e
HOBEREAU : Oiseau rapace diurne
HOCHEMENT : Mouvement de la t�te
HOCHETS : Jouets
HOLA : Interjection
HOMARDERIE : Elevage de crustac�s
HOMEOPATHE : M�thode th�rapeutique
HOMEOTHERME : Dont la temp�rature est constante
HOMINIENS : Famille de primates
HOMOGENE : Dont les �l�ments sont de m�me nature
HOMOGENEISER : M�langer
HOMOLOGUANT : Ent�rinant
HOMONYMIQUE : De m�me prononciation
HONGKONG : Ile de la baie de Canton
HONGROIERIE : Commerce de cuir
HONGROYEUR : Ouvrier qui pr�pare du cuir
HONNIR : D�noncer
HONORABLEMENT : De mani�re convenable
HONORER : Gratifier
HONTEUX : D�gradant
HOP : Interjection
HOQUETON : Veste de grosse toile
HORAIRE : Programme
HORIZONTALEMENT : A plat
HORLOGER : M�canicien
HORMONOTHERAPIE : Traitement m�dical
HOROSCOPE : Etude de la destin� d'un individu
HORRIBLE : Affreux
HORRIPILANTE : Aga�ante
HORST : M�le
HORTICULTEUR : Jardinier
HOSPITALIER : Accueillant
HOSPODAR : Ancien titre des princes vassaux du sultan de Turquie
HOSTIE : Petite rondelle de pain de froment
HOTELLERIE : Auberge
HOTTENTOT : Relatif � une population de pasteurs nomades de l'Afrique du Sud-ouest
HOU : Interjection
HOUBLONNAGE : Troisi�me op�ration dans la fabrication de la bi�re
HOUE : Pioche
HOUER : Labourer
HOULETTE : B�ton de berger
HOUP : Interjection
HOUPPIER : Sommet d'un arbre �branch�
HOURDIS : Ma�onnerie l�g�re
HOUSEAUX : Jambi�res
HOUSPILLER : Quereller
HOUX : Arbuste piquant
HUBLOT : Petite fen�tre
HUCHET : Petit cor de chasse
HUER : Pousser des cris hostiles
HUGUENOTS : Protestants calvinistes
HUILEUSE : Visqueuse
HUISSERIE : Encadrement d'une porte
HULOTTE : Oiseau rapace nocturne
HUM : Interjection
HUMAINEMENT : Charitablement
HUMANISER : Adoucir
HUMANITARISME : Utopie
HUME : Flaire
HUMECTER : Imbiber
HUMERUS : Os du bras
HUMIDIFIER : Humecter
HUMILIANT : D�gradant
HUMORISTIQUE : Caricatural
HUNIER : Voile carr�e
HURLE : Braille
HURLUBERLU : Ecervel�
HUSSARD : Cavalier de l'arm�e hongroise
HYALITE : Opale
HYBRIDE : Issu d'un croisement
HYDNE : Genre de champignons basidiomyc�tes
HYDRATE : Compos� contenant de l'eau
HYDRE : Animal fabuleux
HYDROCARBONATE : Carbonate hydrat�
HYDROCARBURE : Carburant
HYDROCORTISONE : Hormone naturelle de la cortisone
HYDROFUGER : Imperm�abiliser
HYDROGEOLOGIE : Etude de la recherche et du captage des eaux
HYDROLAT : Parfum
HYDROLYSE : D�composition
HYDROMEL : Boisson au miel
HYDROSPHERE : Ensemble de l'�l�ment liquide de la terre
HYDROXYDE : Base
HYGIENE : Propret�
HYGROMETRIQUE : Qui a rapport � l'humidit�
HYGROSCOPE : Hygrom�tre d'absorption
HYMNE : Chant
HYPERBATE : Inversion des mots
HYPERBOREEN : De l'extr�me-Nord
HYPERFREQUENCE : Fr�quence tr�s �lev�e
HYPERMNESIE : Exaltation de la m�moire
HYPERSENSIBLE : Qui ne supporte rien
HYPERTROPHIE : Exag�ration
HYPNOTISE : Fascine
HYPOCAUSTE : Fourneau souterrain
HYPOTENUSE : C�t� oppos� � l'angle droit
HYPOTHEQUE : Gage
HYSTERIE : N�vrose
HZ : Hertz
I : Pas de d�finition
IBERIQUE : Hispanique
ICHTYOSAURE : Grand reptile fossile de l'�poque secondaire
ICONE : Peinture religieuse
ICONOGRAPHIE : Etude des diverses repr�sentations figur�es d'un sujet
ICONOSCOPE : Dispositif qui analyse l'image
ICTUS : Battement de la mesure dans le vers
IDEALISER : Embellir
IDEALISME : Syst�me philosophique
IDEAUX : Parfaits
IDENTIFIER : Assimiler
IDEOGRAMME : Signe repr�sentatif d'une id�e
IDES : Division du mois
IDIOTIE : B�tise
IDOLATRENT : Adorent
IF : Arbre � fruits rouges
IGNE : Ardent
IGNIPUNCTURE : M�thode de caut�risation
IGNOMINIEUSE : Honteuse
IGNORANTE : Inculte
IL : Pronom personnel
ILE : Terre isol�e
ILIEN : Insulaire
ILLEGALITE : Abus
ILLETTRE : Analphab�te
ILLISIBLE : Ind�chiffrable
ILLUMINE : Eclaire
ILLUSIONNISTE : Prestidigitateur
ILLUSTRE : C�l�bre
ILLUVIUM : Accumulation d'�l�ments dissous dans l'horizon d'un sol
ILS : Pronom personnel
IMAGEE : Figur�e
IMAGINABLE : Concevable
IMAGINE : Suppose
IMBATTABLE : Invincible
IMBIBE : Impr�gne
IMBRIQUE : Embo�te
IMBROGLIO : M�lange
IMITATIF : Onomatop�e
IMITER : Copier
IMMATERIALISME : Doctrine qui nie l'existence de la mati�re
IMMATRICULATION : Inscription
IMMEDIAT : Imminent
IMMENSE : Illimit�
IMMERGE : Sous-marin
IMMEUBLE : Immobile
IMMIGRE : Etranger  
IMMISCER : Intervenir (s')
IMMOBILISANT : Fixant
IMMOBILITE : Inactivit�
IMMODESTE : Impudique
IMMOLER : Massacrer
IMMORALISME : Doctrine qui nie les r�gles de la morale
IMMORTALISAIT : Perp�tuait
IMMORTELLE : Eternelle
IMMUABLEMENT : Invariablement
IMMUNISE : Vaccine
IMPAIR : Gaffe
IMPARDONNABLE : Irr�missible
IMPARTIR : Accorder
IMPASSIBLE : Imperturbable
IMPATIENT : Press�
IMPATRONISER : Faire adopter
IMPAVIDE : Impassible
IMPEDANCE : R�sistance en alternatif
IMPENSABLE : Incroyable
IMPERATIVEMENT : D'une mani�re autoritaire
IMPERCEPTIBLE : Inaudible
IMPERIALISME : Expansionnisme
IMPERISSABLE : Immortel
IMPERTINENCE : Effronterie
IMPERTURBABLE : In�branlable
IMPETRANT : B�n�ficiaire
IMPETUOSITE : Fougue
IMPLACABLE : Impitoyable
IMPLICITE : Tacite
IMPLORANT : Priant
IMPOLITIQUE : Impopulaire
IMPORTANCE : Taille
IMPORTUNE : D�range
IMPOSANT : Majestueux
IMPOSEE : Contribuable
IMPOSTURE : Mensonge
IMPRATICABLE : Irr�alisable
IMPREGNATION : Inhibition
IMPREGNER : Imbiber
IMPRENABLE : Inexpugnable
IMPRESSIONNISTE : Qui ne traduit que des impressions subjectives
IMPREVOYANT : Insouciant
IMPREVU : Inattendu
IMPRIMERIE : Technique de reproduction
IMPROBITE : Malhonn�tet�
IMPRONONCABLE : Ne peut �tre dit
IMPRUDEMMENT : Aveuglement
IMPRUDENCE : T�m�rit�
IMPUDICITE : D�vergondage
IMPULSIF : Violent
IMPUNEMENT : Sans risque
IMPURE : Immonde
IMPUTATION : Accusation
IN : Pr�fixe
INABORDABLE : Exorbitant
INACCEPTABLE : Irrecevable
INACHEVE : Incomplet
INACTIVITE : Inaction
INADMISSIBLE : Intol�rable
INALTERE : Pur
INAMOVIBLE : Eternel
INANITE : Vide
INAPERCUE : Pas vue
INAPPRECIABLE : Inestimable
INAPTITUDE : Incapacit�
INASSOUVIE : Insatisfaite
INATTENTION : Inadvertance
INAUGURATION : Ouverture
INAVOUABLE : Abject
INCANDESCENT : Lumineux
INCAPACITE :  Impuissance
INCARCERENT : Emprisonnent
INCARNAT : Rouge vif
INCARNATION : Personnification
INCENDIE : Feu
INCERTITUDE : Doute
INCHAUFFABLE : Condamn� � �tre froid
INCIDENCE : Effet
INCINERATION : Cr�mation
INCISER : Couper
INCITANT : Encourageant
INCITER : Encourager
INCLASSABLE : Ind�finissable
INCLINATION : Penchant
INCLUSIVEMENT : Compris
INCOERCIBLE : Irr�pressible
INCOLORE : Terne
INCOMBUSTIBLE : Apyre
INCOMMODANT : G�nant
INCOMPATIBILITE : Antagonisme
INCOMPLETE : Il lui manque quelque chose
INCOMPRESSIBLE : Ne peut �tre r�duit
INCONFORT : Incommodit�
INCONGRUE : Mals�ant
INCONNUE : Ignor�e
INCONSEQUENCE : Inattention
INCONSISTANTE : Amorphe
INCONSTANT : Changeant
INCONTINENCE : Absence de retenue
INCONVENANCE : Ind�cence
INCONVERTIBLE : Ne peut �tre �chang�
INCORPORANT : M�langeant
INCORRECT : Faux
INCREE : Qui existe sans avoir �t� cr��
INCRIMINATION : Accusation
INCROYABLEMENT : Excessivement
INCRUSTATION : Nielle
INCUBATEUR : Couveuse
INCUBER : Couver
INCULPATION : Imputation
INCULQUER : Apprendre
INCULTIVABLE : Aride
INCURABLE : Ingu�rissable
INCURSION : Irruption
INDE : Bleu fonc�
INDECENTE : Inconvenante
INDECISION : Doute
INDECROTTABLE : Incorrigible
INDEFINIE : Vague
INDEFINISSABLE : Etrange
INDELICAT : Grossier
INDEMNISANT : Compensant
INDEMNISATION : Compensation
INDENIABLE : Flagrant
INDEPENDANTISTE : Partisan de l'autonomie
INDESIRABLE : Intrus
INDETERMINATION : Doute
INDEX : Doigt
INDICATION : Indice
INDICIBLE : Indescriptible
INDICIBLEMENT : De mani�re indescriptible
INDIFFERENCE : D�sint�ressement
INDIGENE : Natif
INDIGESTE : Lourd
INDIGNER : Scandaliser
INDIQUANT : D�signant
INDIRECTEMENT : Par ricochet
INDISCRETE : Bavarde
INDISCUTABLE : Certain
INDISPOSE : G�ne
INDIVIDUALISANT : Distinguant
INDIVIDUALISME : Lib�ralisme
INDIVIS : Commun
INDIVISIBLE : Qui ne peut �tre partag�
INDOCILITE : D�sob�issance
INDOMPTABLE : Irr�ductible
INDRI : Mammif�re l�murien
INDUCTEUR : Electro-aimant
INDUIRE : Tromper
INDULGENT : Complaisant
INDUSTRIALISER : Installer des usines
INEBRANLABLE : Tr�s solide
INEFFABLE : Indicible
INEFFICACE : Inop�rant
INEGALITE : D�s�quilibre
INELIGIBLE : Ne peut �tre choisi
INELUCTABLEMENT : Infailliblement
INEPROUVE : Pas encore essay�
INEPUISABLE : Infini
INERTIE : R�sistance
INESTIMABLE : Inappr�ciable
INEXACTE : Erron�e
INEXERCE : Inexp�riment�
INEXPERT : pas tr�s habile
INEXPLORABLE : Imp�n�trable
INEXPRESSIF : Terne
INEXTENSIBILITE : Impossible � allonger
INFAILLIBLEMENT : Assur�ment
INFAMANT : D�shonorant
INFANTERIE : Soldats � pieds
INFARCTUS : Infiltration d'un tissu par un �panchement sanguin
INFECT : R�pugnant
INFECTION : Corruption
INFEODER : Ali�ner
INFERENCE : Raisonnement
INFERIORITE : Faiblesse
INFERNAL : D�moniaque
INFESTENT : Envahissent
INFIDELE : D�loyal
INFILTRE : Traverse
INFIME : Minime
INFIRMER : D�mentir
INFIXE : El�ment qui s'ins�re � l'int�rieur d'un mot
INFLECHIR : D�vier
INFLECHISSANT : D�viant
INFLEXION : D�viation
INFLIGER : Donner
INFLUENCER : Peser
INFLUENZA : Grippe
INFORMATEUR : Rapporteur
INFORMATION : Tuyau
INFORMER : Aviser
INFRASTRUCTURE : Fondation
INFRASTRUCTURES : Fondations
INFUSER : Mac�rer
INFUSOIRE : Animal unicellulaire qui vit dans les liquides
INGENIEUSEMENT : Avec astuce
INGENIOSITE : Adresse
INGERENCE : Intrusion
INGREDIENT : El�ment
INGURGITER : Avaler
INHABITE : D�sert
INHALATION : Aspiration
INHERENTE : Essentiel
INHIBER : Emp�cher
INHUMAINEMENT : De mani�re barbare
INIMAGINABLE : Invraisemblable
ININTELLIGENCE : Incompr�hension
ININTERESSANT : Ne vaut pas le d�tour
INIQUITE : D�faut
INITIALE : Originale
INITIAUX : Originaux
INJECTA : Insuffla
INJECTEUR : Dispositif assurant l'alimentation
INJONCTION : Ordre
INJURIER : Traiter de tous les noms
INJUSTICE : Iniquit�
INLASSABLEMENT : Sans fin
INNOCEMMENT : Sans malice
INNOCENTER : Blanchir
INNOMMABLE : D�go�tant
INNOVE : Invente
INOBSERVATION : Inex�cution
INOCULER : Transmettre
INONDE : Immerge
INOPERANTE : Inefficace
INOPPORTUNEMENT : A contretemps
INOUBLIABLE : Grav�
INOXYDABLE : Inalt�rable
INQUIETES : Anxieuses
INQUISITION : Enqu�te
INSALUBRE : Malsain
INSATIABLE : Insatisfait
INSCRITE : Port�e
INSCRIVAIT : Notait
INSECTARIUM : Elevage de petits animaux
INSELBERG : Butte isol�e
INSENSIBILISANT : Anesth�siant
INSENSIBLEMENT : Doucement
INSERE : Ajoute
INSIDIEUX : Trompeur
INSIGNIFIANCE : Inconsistance
INSINUATION : Allusion
INSIPIDE : Fade
INSISTE : Souligne
INSOLENCE : Effronterie
INSOLUBLE : Impossible
INSOUCIANT : Indiff�rent
INSOUMISSION : D�sob�issance
INSPECTER : Contr�ler
INSPIRANTE : Suggestive
INSPIRER : Sugg�rer
INSTALLATION : Am�nagement
INSTALLER : Caser
INSTANTANEITE : Promptitude
INSTAURATION : Fondation
INSTIGATRICE : Meneuse
INSTINCT : Libido
INSTITUER : Fonder
INSTRUCTEUR : Professeur
INSTRUIRE : Former
INSTRUITE : Cal�e
INSTRUMENT : Outil
INSUCCES : Echec
INSUFFLER : Inspirer
INSULAIRE : Ilien
INSULTANT : Offensant
INSULTE : Offense
INSURMONTABLE : Infranchissable
INTACTE : Sauf
INTEGRALEMENT : Compl�tement
INTEGRES : Honn�tes
INTEGRITE : Honn�tet�
INTELLECTUELLE : C�r�brale
INTELLIGENTSIA : Groupe de t�tes
INTEMPERANT : Immod�r�
INTENDANT : Administrateur
INTENSIFICATION : Augmentation
INTENTER : Actionner
INTENTIONNEL : Volontaire
INTERCALATION : Insertion
INTERCEDER : D�fendre
INTERCEPTE : Capte
INTERCONNEXION : Branchement
INTERCOSTAL : Entre deux c�tes
INTERDEPENDANCE : Corr�lation
INTERDIGITAUX : Entre les doigts
INTERDIRE : Proscrire
INTERDIT : Pantois
INTERESSEE : Avide
INTERFERENCE : Intervention contradictoire
INTERFEROMETRE : Instrument de mesure
INTERFLUVE : Relief qui s�pare les vall�es
INTERINDIVIDUEL : Qui concerne les relations entre les gens
INTERIORISER : Ramener au moi
INTERJETER : Faire intervenir
INTERLOCK : Nom d'un tissu ind�maillable
INTERLOQUE : D�contenanc�
INTERLUDE : Passage que l'on joue � l'orgue entre les versets d'un choral
INTERMEDE : Interruption
INTERNATIONAL : Concerne plusieurs pays
INTERNEMENT : Emprisonnement
INTERPLANETAIRE : D'une plan�te � l'autre
INTERPOLATION : Action d'intercaler une valeur dans une s�rie
INTERPRETATION : Explication
INTERROGATIVE : Qui pose une question
INTERROGER : Sonder
INTERROMPRE : Couper
INTERSECTION : Croisement
INTERSTICE : Fente
INTERTRIGO : Maladie de peau
INTERVENIR : S'immiscer
INTERVERTIR : Changer
INTESTIN : Boyau
INTIMEMENT : Etroitement
INTIMER : Notifier
INTIMIDER : Effaroucher
INTITULE : Titre
INTOLERANCE : Fanatisme
INTOXICATION : Empoisonnement
INTOXIQUANT : Empoisonnant
INTRADERMIQUE : Dans l'�paisseur de la peau
INTRAMUSCULAIRE : Dans l'�paisseur du muscle
INTRICATION : Complexit�
INTRINSEQUE : Essentiel 
INTRODUIRE : Pr�senter
INTROIT : Chant destin� � �tre ex�cut� avant la messe
INTROSPECTION : Observation d'une conscience individuelle par elle-m�me
INTROVERTIE : Qui ne s'int�resse qu'� elle
INTUITION : Pressentiment
INTUITIONNISME : Doctrine du pressentiment
INULINE : Compos� voisin de l'amidon
INUSITE : Inutilis�
INUTILISE : Inusit�
INVALIDE : Infirme
INVARIABILITE : Constance
INVECTIVANT : Fulminant
INVENTAIRE : Recensement
INVENTIF : Ing�nieux
INVENTORIER : D�nombrer
INVERSE : Contre-pied
INVERSEUR : Commutateur
INVESTIGATRICE : Chercheuse
INVESTIR : Assi�ger
INVETERE : Enracin�
INVIOLABLE : Intangible
INVITATION : Exhortation
INVITE : Exhorte
INVIVABLE : Insupportable
INVOLONTAIRE : Automatique
INVOQUER : Conjurer
INVULNERABLE : Au dessus de toute atteinte
IODE : M�tallo�de tr�s volatil
IONIE : Ancienne province grecque d'Asie mineure
IONISER : Charger
IOTA : Lettre de l'alphabet grec
IPECA : Nom collectif de racines
IR : Lumi�re chauffante
IRAN : Perse
IRE : Col�re
IRIDIUM : M�tal blanc tr�s dur
IRIS : Membrane
IRLANDAIS : Ga�lique
IRONIE : Sarcasme
IRRADIATION : Rayonnement
IRRATIONALISME : Absence de foi dans la raison
IRREALISABLE : Chim�rique
IRRECEVABLE : Inadmissible
IRREELLE : Imaginaire
IRREFRAGABLE : Irr�cusable
IRREFUTABLE : Formel
IRREGULIER : Discontinu
IRRELIGIEUX : Ath�e
IRREMISSIBLE : Impardonnable
IRREPROCHABLE : Parfait
IRRESOLUTION : Incertitude
IRREVERENCIEUSE : Impolie
IRREVOCABLE : Arr�t�
IRRIGATION : Arrosage
IRRITANT : Aga�ant
IRRITER : Agacer
ISBA : Petite maison russe
ISCHEMIE : An�mie locale
ISLAMIQUE : Musulman
ISLANDE : Ile de l'Atlantique Nord
ISOBARE : Ligne de pression
ISOBATHE : D'�gale profondeur
ISOCARDE : Mollusque
ISOCLINAL : D'�gale inclinaison magn�tique
ISOETE : Petite plante lacustre
ISOGONE : De m�me d�clinaison magn�tique
ISOLABLE : S�parable
ISOLANTE : Qui ne conduit pas
ISOLEES : S�par�es
ISOMORPHE : Qui affecte la m�me forme cristalline
ISOPODE : Dont les pattes sont semblables
ISRAEL : Etat du Proche-Orient
ISTHME : Langue de terre
ITALIE : Pays europ�en
ITALIQUE : Inclin� vers la droite
ITINERAIRE : Parcours
IVOIRE : Partie dure des dents
IVRESSE : Extase
IXODE : Tique
J : Pas de d�finition
JABOT : Ornement d'une chemise
JACASSE : Bavarde
JACASSERIE : Bavardage
JACINTHE : Plante portant une grappe de fleurs color�es et parfum�es
JACOBEE : Esp�ce de s�ne�on
JACQUARD : M�tier
JACQUES : Ancien sobriquet du paysan fran�ais
JACTANCE : Bavardage
JADIS : Autrefois
JAILLISSEMENT : Jet
JALON : Rep�re
JALOUSER : Envier
JALOUX : Envieux
JAMBE : Patte
JAMBON : Cuisse
JANGADA : Bateau br�silien
JAPON : Empire insulaire de l'Asie orientale
JAPPER : Aboyer
JAQUE : Ancien sobriquet du paysan fran�ais
JARDINAGE : Horticulture
JARDINIERE : M�lange de l�gumes cuits
JARGON : Petite pierre rouge ressemblant � l'hyacinthe
JARRET : R�gion post�rieure de genou
JAS : Partie d'une ancre
JASE : Bavarde
JASMIN : Arbuste sarmenteux et vivace
JASPINER : Caqueter
JAUGE : Tonnage
JAUNATRE : Couleur
JAUNE : Couleur
JAVA : Danse
JAVEAU : Ile
JAVELLE : Fagot de sarments
JAZZ : Genre musical
JE : Pronom personnel
JEANNETTE : Narcisse de po�tes
JEREMIADE : Lamentation
JERRICAN : Bidon
JESUITE : Membre de la Compagnie de J�sus
JETE : Lance
JETEE : Digue
JETER : Lancer
JEU : Divertissement
JEUDI : Jour de la semaine
JEUNESSE : Jouvence
JOAILLIER : Bijoutier
JOBARDE : Na�ve
JOINDRE : Unir
JOINTIVE : En contact
JOLIESSE : Beaut�
JONCHER : Parsemer
JONGLER : Lancer des boules
JONQUE : Voilier
JONQUILLE : Fleur jaune
JOUE : Partie lat�rale de la face
JOUER : Parier
JOUISSANCE : Plaisir
JOULE : Travail
JOURNALIER : Quotidien
JOUTE : Combat
JOUVENCE : Jeunesse
JOUXTANT : Avoisinant
JOVIALITE : Gaiet�
JOYAUX : Bijoux
JUBE : Ambon
JUBILER : Se r�jouir 
JUCHOIR : Perchoir
JUDAIQUE : Juif
JUDICIEUSEMENT : Intelligemment
JUDO : Sorte de lutte japonaise
JUGEMENT : Opinion
JUGEOTE : Bon sens
JUILLET : Mois
JUIN : Mois
JULES : Homme
JUMEAU : Besson
JUNIOR : Cadet
JUPON : Cotillon
JURAT : Magistrat municipal
JURE : Blasph�me
JURIDICTION : Circonscription
JURISTE : Homme de loi
JURY : Commission
JUSTESSE : Exactitude
JUSTIFIABLE : Excusable
JUSTIFICATION : Explication
JUTE : Fibre textile
JUVENAT : Stage en usage dans certains ordres religieux
JUXTAPOSER : Accoler
K : Pas de d�finition
KABUKI : Genre th��tral traditionnel au Japon
KACHA : Plat populaire russe
KAKI : Plaqueminier
KAMICHI : Grand oiseau �chassier d'Am�rique du Sud
KANDJAR : Poignard oriental
KANGOUROU : Mammif�re australien
KARATE : Sport de combat
KARMA : Dogme central de la religion hindouiste
KARTING : Sport automobile
KAYAK : Petite embarcation de sport
KENOTRON : Tube �lectronique
KENTIA : Genre de palmier australien
KERMES : Cochenilles
KETCH : Voilier
KETMIE : Arbre des r�gions chaudes
KG : Unit� de poids
KHAN : Titre de souverain mongol
KHEDIVE : Ancien titre port� par le vice roi d'Egypte 
KIDNAPPER : Enlever
KILO : Unit� de poids
KILOMETRE : Unit� de distance
KILT : Jupe courte et pliss�e
KINESITHERAPIE : Mouvements et massages
KIOSQUE : Pavillon de jardin
KIRSCH : Eau-de-vie
KIWI : Apt�ryx
KLAXONNER : Avertir
KM : Unit� de distance
KNICKERS : Pantalons de golf
KOLATIER : Arbre d'Afrique
KONZERN : Forme d'int�gration �conomique
KOUGLOF : G�teau
KR : Krypton
KROUMIR : Chausson
KYRIELLE : S�quelle
L : Pas de d�finition
LA : Note
LABARUM : Etendard romain
LABEUR : Besogne
LABILE : Qui est sujet � tomber
LABORATOIRE : Local pour faire des exp�riences
LABOURER : Retourner
LABOUREUR : Cultivateur
LABRIT : Chien de berger
LAC : Etendue d'eau
LACER : Attacher
LACERER : D�chirer
LACERIE : Fin tissu de paille
LACET : Cordon
LACHER : Desserrer
LACHEUR : Personne qui abandonne
LACIS : R�seau
LACONIQUE : Concis
LACRYMOGENE : Qui fait pleurer
LACS : Noeud coulant
LACTIFERE : Qui produit du lait
LACTOMETRE : Galactom�tre
LACTOSE : El�ment du lait
LACUNE : Omission
LAD : Gar�on d'�curie
LADANUM : Gomme-r�sine aromatique
LADY : Dame
LAGON : Petit lac d'eau sal�e
LAI : Convers
LAIC : Qui ne fait pas partie du clerg�
LAID : Vilain
LAIDE : Vilaine
LAIDES : Vilaines
LAIE : Truie
LAINAGE : V�tement
LAINER : Rendre moelleux
LAIRD : Propri�taire en Ecosse
LAISSER : Abandonner
LAIT : Aliment liquide
LAITANCE : Glandes m�les des poissons
LAITERIE : Cr�merie
LAITON : Cuivre et zinc
LAITUE : Salade
LAIUS : P�re d'Oedipe
LAMA : Mammif�re ongul� d'Am�rique du Sud
LAMANAGE : Aide � l'amarrage des bateaux
LAMARCKISME : Th�orie de l'�volution 
LAMBIN : Tra�nard
LAMBOURDE : Pi�ce de bois
LAMBRIS : Rev�tement
LAMBRUSQUE : Vigne sauvage
LAMELLIBRANCHES : Classe de mollusques aquatiques
LAMENTABLE : Navrant
LAMENTER : Se plaindre (se)
LAMIER : Ortie rouge
LAMINER : Etirer
LAMPANT : Raffin� pour l'�clairage
LAMPEE : Grande gorg�e
LAMPISTE : Personne charg�e de l'entretien de l'�clairage
LAMPYRE : Ver luisant
LANCER : Jeter
LANCINANT : Obs�dant
LANCON : Poisson au corps effil�
LANDAU : Voiture d'enfant
LANGAGIER : Linguistique
LANGOUREUSE : Alanguie
LANGOUSTE : Crustac� marin
LANGUETTE : Lichette
LANGUEUR : Abattement
LANIERE : Courroie
LANSQUENET : Fantassin allemand mercenaire
LANTERNER : Tra�ner
LAPALISSADE : Evidence
LAPIDAIRE : Petite meule
LAPILLI : Petites pierres projet�es par les volcans
LAPIS : Pierre bleu
LAPS : Espace de temps
LAQUE : Peinture
LAQUEE : Vernie
LARCIN : Vol
LARDOIRE : Brochette creuse
LARGE : Ample
LARGEUR : Carrure
LARGUER : L�cher
LARMIER : Saillie d'une corniche
LARRON : Brigand
LAS : Faible
LASAGNES : P�tes italiennes
LASCIVETE : Lubricit�
LASSER : Ennuyer
LATENT : Pas encore d�clar�
LATERAL : Situ� sur le c�t�
LATERALEMENT : De c�t�
LATIFOLIE : Qui a de larges feuilles
LATIFUNDIUM : Grand domaine priv�
LATITUDE : Distance au p�le
LATRIE : Forme la plus �lev�e d'adoration
LATTE : Planche
LAUDANUM : Teinture alcoolique d'opium
LAURE : Monast�re
LAUREAT : Vainqueur
LAVAGE : Nettoyage
LAVANDE : Arbrisseau � fleurs bleues parfum�es
LAVE : Mati�re en fusion
LAVERET : Cor�gone
LAVOIR : Buanderie
LAXISME : Suppression des interdits
LAZARET : Etablissement de contr�le sanitaire
LAZZI : Pantomime
LE : Article d�fini
LEADER : Premier
LEBEL : Fusil � r�p�tition
LECHEFRITE : Ustensile de cuisine
LECON : Cours
LECTURE : D�chiffrage
LEGALISATION : Attestation
LEGATO : Sans d�tacher les notes
LEGENDE : Fable
LEGERETE : Agilit�
LEGIFERER : Dicter des r�gles
LEGISLATIF : Qui fait des lois
LEGISTE : Conseiller juridique
LEGITIMER : Reconna�tre
LEGUER : Transmettre
LEGUME : Plante potag�re
LEITMOTIV : Refrain
LEMMING : Petit mammif�re rongeur
LEMURIEN : Sous ordre de mammif�res primates
LENIFIER : Adoucir
LENTE : Oeuf de pou
LENTICULE : Plante flottante des eaux stagnantes
LENTILLE : Loupe
LEOPARD : Panth�re d'Afrique
LEPIOTE : Champignon
LEPTOCEPHALE : Larve de l'anguille et du congre
LES : Article d�fini
LESE : D�savantage
LESER : D�savantager
LESINE : Avarice
LESION : Blessure
LESSIVANT : Lavant
LEST : Poids
LESTER : Charger
LETHARGIE : Sommeil
LETTRE : Message
LEU : Unit� mon�taire roumaine
LEUCITE : Min�ral du groupe des feldspatho�des
LEUR : Pronom personnel
LEURRER : Abuser
LEURS : Pronom personnel
LEV : Unit� mon�taire bulgare
LEVAGE : Manutention
LEVANTIN : Originaire des c�tes de la M�diterran�e orientale
LEVE : Dresse
LEVEES : Chauss�es
LEVIER : Manette
LEVRAUT : Jeune rongeur
LEVRETTEE : Vari�t� petite d'un grand chien
LEVURE : Ferment
LEXICOGRAPHIE : Dictionnaire
LEXICOLOGIE : Partie de la linguistique
LEZ : A c�t� de
LEZARD : Petit reptile saurien
LIAIS : Pierre calcaire
LIAISON : Association
LIANES : Plantes grimpantes
LIBATION : Offrande
LIBELLER : R�diger dans les formes
LIBERAL : G�n�reux
LIBERALISER : Tol�rer
LIBERATION : Affranchissement
LIBERER : Rel�cher
LIBERTIN : Dissolu
LIBRAIRE : Editeur
LIBRE : Ind�pendant
LICENCE : Autorisation
LICENCIEUSEMENT : En abusant de la libert� qu'on lui laisse
LICHER : Boire
LICHETTES : Languette
LICITE : Permis
LICOU : Pi�ce de harnais
LIE : D�p�t
LIECHTENSTEIN : Principaut� de l'Europe centrale
LIED : Chanson populaire
LIEDS : Chansons populaires
LIEN : Attache
LIENS : Attaches
LIER : Attacher
LIERA : Attachera
LIESSE : All�gresse
LIEU : Endroit
LIEUE : Ancienne mesure de distance
LIEUTENANT : Second
LIEVRE : Rongeur
LIGAMENTS : Faisceau de tissus reliant les �l�ments d'une articulation
LIGATURE : Noeud
LIGNAGE : Famille
LIGNEE : Descendance
LIGNICOLE : Qui vit dans les bois
LIGOT : Petit fagot
LIGUE : Alliance
LIGUER : Allier
LILAS : Arbuste aux fleurs tr�s parfum�es
LILLE : Ville du Nord de la France
LIMACON : Escargot
LIMAN : Estuaire
LIME : Vari�t� de citronnier
LIMICOLE : Qui vit sur la vase
LIMITATION : Restriction
LIMITER : Borner
LIMNEE : Mollusque gast�ropode
LIMON : D�p�t
LIMONAIRE : Orgue
LIMONITE : H�matite brune
LIMOUSINAGE : Ma�onnerie
LIMULE : Crabe des Moluques
LIN : Plante herbac�e
LINCEUL : Suaire
LINEATURE : D�finition
LINGE : Dessous
LINGOT : Bloc de m�tal
LINGOTIERE : Moule
LINIMENT : Baume
LINOLEUM : Rev�tement
LINOTYPISTE : Compositeur
LINSANG : Mammif�re carnivore des �les de la sonde
LION : Grand mammif�re carnivore
LIPPE : L�vre inf�rieure pro�minente
LIQUATION : S�paration par la fusion
LIQUEFIER : Faire fondre
LIQUIDE : Fluide
LIQUIDITE : Disponibilit�
LIRE : D�chiffrer
LIS : Fleur
LISBONNE : Ville du Portugal
LISE : Sable mouvant
LISERER : Border
LISERON : Plante herbac�e
LISIBLE : D�chiffrable
LISSE : Pi�ce longitudinale de la charpente d'une coque
LISTE : Enum�ration
LISTEAUX : Petites moulures
LIE : D�p�t
LITHINE : Oxyde de lithium
LITHODOME : Mollusque qui creuse les roches pour s'y loger
LITHOGRAPHIE : Gravure
LITHOPHAGE : Qui creuse des cavit�s dans les roches pour s'y loger
LITIGE : Dispute
LITOTE : Figure de rh�torique
LITTERAL : Textuel
LITTERATURE : Usage esth�tique d'une langue
LITTORINE : Bigorneau
LIVAROT : Fromage ferment� � p�te mole
LIVRER : D�noncer
LIVRET : Carnet
LLANOS : Plaine herbeuse en Am�rique du Sud
LOBE : Partie arrondie
LOBOTOMIE : Op�ration de neurochirurgie
LOCAL : Pi�ce
LOCALISABLE : Mal cach�
LOCATION : Affermage
LOCH : Appareil de mesure de la vitesse
LOCOMOTION : D�placement
LOCUSTE : Sauterelle verte
LOCUTION : Expression
LOFER : Venir au vent
LOGEABLE : Habitable
LOGEUR : H�telier
LOGIQUE : Coh�rent
LOGOGRIPHE : Devinette
LOI : R�gle
LOIR : Petit mammif�re rongeur
LOMBRIC : Ver de terre
LONGANIMITE : Patience
LONGEVITE : Dur�e
LONGUET : Qui dure un peu trop
LOQUACE : Bavard
LOQUETEUX : Mal habill�
LORDOSE : D�viation
LORETTE : Courtisane
LORGNETTES : Lunettes
LORIS : Mammif�re l�murien
LOT : Assortiment
LOTIER : Herbe annuelle ou vivace
LOTIR : Partager
LOTO : Jeu de hasard
LOUABLE : M�ritoire
LOUANGEUSE : Adulatrice
LOUCHE : Suspect
LOUCHET : B�che � lame �troite
LOUEUSE : Chaisi�re
LOUIS : Ancienne monnaie fran�aise
LOUPANT : Ratant
LOUPIOTE : Petite lampe
LOURDAUD : Balourd
LOUSTIC : Amuseur
LOUTRE : Petit mammif�re carnivore adapt� � la vie aquatique
LOUVETEAU : Jeune scout
LOUVETERIE : Chasse
LOUVOYER : Biaiser
LOVER : Enrouler
LOYALISME : D�vouement
LU : Avant d'�tre approuv� 
LUBIE : Caprice
LUBRIQUE : Luxurieux
LUCARNE : Fa�ti�re
LUCIDITE : Acuit�
LUCILIE : Mouche verte
LUCRE : Gain
LUEUR : Lumi�re
LUFFA : Courge d'Afrique et d'Asie
LUGUBRE : Sinistre
LUI : Pronom personnel
LUIRE : Briller
LUMEN : Unit� de flux lumineux
LUMINAIRE : Source d'�clairage
LUMINESCENT : Phosphorescent
LUMINISTE : Sp�cialiste des effets de lumi�re
LUNDI : Jour
LUNE : Satellite
LUNETIER : Opticien
LUNURE : D�faut du bois
LUPULINE : Vari�t� de luzerne
LURON : Drille
LUSIN : Petit cordage
LUSTRAL : Qui sert � purifier
LUSTRER : Polir
LUTEINE : Pigment jaune
LUTH : Instrument de musique
LUTHIER : Fabriquant d'instruments de musique
LUTIN : Farfadet
LUTRIN : Pupitre pour les livres de chant
LUTTE : Conflit
LUX : Unit� d'�clairement
LUXE : Faste
LUXEMBOURG : Pays europ�en
LUXER : D�bo�ter
LUXUEUX : Fastueux
LUXURIEUX : D�bauch�
LYCEE : Ecole
LYCOPODE : Plante pt�ridophyte � tige gr�le
LYMPHOCYTE : Petit leucocyte immobile
LYNCHAGE : Ex�cution sommaire
LYNX : Mammif�re carnivore
LYRE : Instrument de musique
LYRIQUE : Destin� � �tre chant�
LYS : Fleur
LYSIMAQUE : Plante herbac�e
M : Pas de d�finition
MA : Adjectif possessif
MACACHE : Rien du tout
MACARON : G�teau sec
MACARONIS : P�tes
MACERER : Faire tremper
MACHAON : Papillon
MACHETTE : Coutelas
MACHINAL : Automatique
MACHINATION : Complot
MACHINISME : M�canisme
MACHOIRE : Maxillaire
MACHONNE : Mordille
MACHURE : Barbouille
MACLE : Plante aquatique
MACON : Ville Fran�aise
MACONNERIE : Gros oeuvre
MACREUSE : Oiseau migrateur
MACROPHAGE : Globule blanc
MACROPODE : Qui a de longs pieds
MACULE : Feuille intercalaire
MADAGASCAR : Ile de l'oc�an Indien
MADELEINE : G�teau
MADONE : Vierge
MADRAS : Foulard
MADREPORE : Animal coelent�r�
MADRIGAL : Pi�ce vocale polyphonique sur un texte profane
MAELSTROM : Tourbillon
MAFFIA : Coterie secr�te
MAGAZINE : Revue
MAGHREB : Nord de l'Afrique
MAGIQUE : Surnaturel
MAGISTRALEMENT : Solennellement
MAGNANERIE : S�riciculture
MAGNANIME : Cl�ment
MAGNESIUM : M�tal l�ger blanc argent�
MAGNETIQUE : Attirant
MAGNETISEUR : Gu�risseur
MAGNETOCASSETTE : Enregistreur
MAGNETOPHONE : Enregistreur
MAGNETOSCOPE : Enregistreur
MAGNIFIANT : Glorifiant
MAGNIFIQUEMENT : Superbement
MAGNUM : Grosse bouteille
MAGOT : Tr�sor
MAHARAJA : Titre des princes hindous
MAI : Mois
MAIE : P�trin
MAIES : P�trins
MAIGREUR : Pauvret�
MAIL : Maillet
MAILLAGE : Point
MAILLOCHE : Marteau de carrier
MAILLOTIN : Ancienne arme
MAIN : Battoir
MAINLEVEE : Fin de saisie
MAINT : Plusieurs
MAINTE : Plusieurs
MAINTENANT : Pr�sentement
MAINTENIR : Garder
MAINTENUE : Gard�e
MAIS : Gramin�e
MAISERIE : Fabrique de f�cule
MAISON : B�timent
MAIZENA : Farine
MAJEUR : Plus grand
MAJORAIT : Augmentait
MAJORDOME : Ma�tre d'h�tel
MAJORQUE : Ile de M�diterran�e
MAL : Douleur
MALABAR : Costaud
MALADIE : Trouble
MALADRESSE : B�vue
MALAISE : Embarras
MALAISEMENT : Difficilement
MALANDRE : Partie pourrie dans les bois de construction
MALAVISEES : Imprudentes
MALAXER : Triturer
MALCHANCEUX : Malheureux
MALEFICE : Diablerie
MALFACON : D�faut
MALFAITEUR : Bandit
MALHABILE : Gauche
MALHONNETE : D�loyal
MALICIEUX : Espi�gle
MALIGNE : Mauvais
MALINOIS : Chien
MALLETTE : Valise
MALMENER : Brutaliser
MALODORANT : Puant
MALPIGHIE : Plante tropicale
MALSAINE : Insalubre
MALT : C�r�ale
MALTRAITER : Battre
MALVEILLANCE : Intention de nuire
MALVERSATION : Corruption
MAMELLE : Pis
MAMELONNE : Couvert de pro�minences
MAMOURS : D�monstrations de tendresse
MANAGER : Organiser
MANANT : Vilain
MANCHON : Fourreau
MANDANT : Commettant
MANDARINE : Fruit
MANDATE : D�l�gue
MANDEMENT : Instruction
MANDER : Convoquer
MANDORE : Ancien instrument de musique
MANDRILL : Grand singe
MANECANTERIE : Ecole de chant
MANGANESE : M�tal
MANGEABLE : Assez bon
MANGEOIRE : Auge
MANGER : D�jeuner
MANGLIER : Pal�tuvier
MANGOUSTE : Petit mammif�re carnivore
MANIABLE : Manoeuvrable
MANICHORDION : Ancien instrument de musique
MANIER : Manipuler
MANIFESTATION : Expression
MANIFESTE : Proclamation
MANIGANCER : Tramer
MANIOC : Arbrisseau des r�gions tropicales
MANIPULER : Manier avec soin
MANITOU : Personnage important et puissant
MANNEQUIN : Mod�le
MANOQUE : Petite botte de feuilles de tabac
MANQUANT : Absent
MANQUER : S�cher
MANSARDE : Chambrette
MANTE : Manteau
MANTELET : Habit de pr�lat
MANTILLE : Echarpe
MANUEL : Cours
MANUFACTURE : Atelier
MANUSCRIT : Original
MANUTERGE : Linge d'�glise
MAPPEMONDE : Carte
MAQUETTE : Ebauche
MAQUIGNON : N�gociant
MAQUILLER : Falsifier
MARAICHER : Jardinier
MARASQUIN : Liqueur
MARATHONIEN : Coureur
MARAUDER : Voler
MARBRE : Roche calcaire
MARCASSITE : Bisulfure de fer naturel
MARCESCENT : Qui se fl�trit
MARCHANDAGE : Discussion
MARCHANDISE : Fret
MARCHE : Degr�
MARCHER : Avancer
MARCOTTAGE : Provignage
MARDI : Jour
MARECAGEUX : Bourbeux
MARECHAUSSEE : Gendarmerie
MAREMME : Terrain mar�cageux
MARGARINE : Substance grasse
MARGELLE : Rebord
MARGINAL : Secondaire
MARGOTIN : Petit fagot
MARGOUILLIS : Boue
MARGUERITE : Fleur
MARIAGE : Association
MARIGOT : Marais
MARIN : Matelot
MARINGOUIN : Moustique
MARIONNETTE : Automate
MARITIME : Naval
MARIVAUDER : Badiner
MARLI : Bord int�rieur d'une assiette
MARMAILLE : Groupe d'enfant
MARMELADE : Confiture
MARMONNER : Bredouiller
MARMOREEN : Froid
MARMOTTE : Mammif�re rongeur
MARMOTTER : Murmurer
MARNE : M�lange d'argile et de calcaire
MARNIERE : Carri�re
MAROILLES : Fromage rectangulaire
MARONNE : Rage
MAROQUINERIE : Tannage
MAROUETTE : Plante � odeur f�tide
MAROUFLE : Colle
MARQUANTE : M�morable
MARQUETEUR : Ouvrier �b�niste
MARQUISE : V�randa
MARRANT : Dr�le
MARRANTE : Dr�le
MARRI : Contrit
MARS : Mois
MARSOUIN : Mammif�re c�tac�
MARTEAU : Outil
MARTELAIENT : Frappaient
MARTELENT : Frappent
MARTELER : Frapper
MARTIALES : Relatives � la guerre
MARTINET : Oiseau passereau
MARTINIQUE : Ile des Antilles
MARTYRISANT : Torturant
MARTYROLOGE : Liste de ceux qui ont souffert
MARYLAND : Tabac
MAS : Maison
MASCOTTE : Porte-bonheur
MASOCHISTE : Qui aime souffrir
MASQUEE : Cach�e
MASSACRER : D�truire
MASSAGE : Friction
MASSER : Frictionner
MASSEUR : Soigneur
MASSICOTER : Rogner
MASSIER : Huissier
MASSIVEMENT : Lourdement
MASTABA : Tombeau de l'ancienne Egypte
MASTIQUER : M�cher
MASTODONTE : Gigantesque mammif�re fossile
MASTROQUET : Cafetier
MAT : En �chec
MATADOR : Torero
MATCH : Combat
MATELASSER : Rembourrer
MATELOT : Marin
MATER : Dompter
MATERIALISER : Symboliser
MATERIELLE : Physique
MATERNER : Prendre soin de quelqu'un
MATHEMATICIEN : Analyste
MATHEMATIQUE : Pr�cis
MATHUSALEM : Patriarche biblique
MATIN : Aube
MATINEE : Demi-journ�e
MATOIS : Rus�
MATOISES : Rus�es
MATRAQUER : Frapper
MATRAS : R�cipient florentin
MATRIARCAL : Sous le r�gne de la m�re
MATRICER : Forger
MATRICULE : Num�ro d'inscription
MATRIMONIAUX : Conjugaux
MATS : Ternes
MATURE : Gr�ement
MAUDIT : Damn�
MAUGREER : Pester
MAURE : Berb�re
MAURITANIE : Pays africain
MAUVAISE : N�faste
MAUX : Douleurs
MAXIME : Principe
MAYONNAISE : Sauce
MAZDEISME : Religion de l'Iran antique
MAZURKA : Danse
ME : Pronom personnel
MEANDRE : Courbe
MEC : Homme
MECANICIEN : Conducteur
MECANISER : Industrialiser
MECANISME : Syst�me
MECANOGRAPHIQUE : Qui a recours une machine � �crire
MECHAMMENT : Cruellement
MECHOUI : Mouton r�ti
MECOMPTE : D�ception
MECONNAITRE : Ignorer
MECONNUES : Anonymes
MECREANT : Incr�dule
MEDAILLEUR : Graveur
MEDECIN : Docteur
MEDIAN : Au milieu
MEDIAT : Indirect
MEDIATION : Arbitrage
MEDICAMENT : Drogue
MEDICAMENTEUX : Qui a des propri�t�s th�rapeutiques
MEDICINAL : Qui a des propri�t�s curatives
MEDIEVAUX : Moyen�geux
MEDIOCREMENT : Assez mal
MEDIRE : D�crier
MEDISANT : Diffamatoire
MEDITER : R�fl�chir
MEDITERRANEE : Au milieu des terres
MEDOC : R�gion viticole
MEDUSER : Stup�fier
MEFIANCE : Doute
MEFIER : Douter (se)
MEGAHERTZ : Unit� de fr�quence
MEGALOMANE : Orgueilleux
MEGARDE : Inattention
MEGERE : Harpie
MEGIS : Bain pour tanner les peaux
MEGISSER : Tanner
MEGOTER : L�siner
MEIJI : Ere de la chronologie japonaise
MEILLEUR : Gratin
MEJUGER : M�sestimer
MELAMPYRE : Parasite des c�r�ales
MELANCOLIE : Cafard
MELANINE : Pigment de la peau
MELASSE : Brouillard �pais
MELE : Composite
MELISSE : Plante aromatique
MELLIFICATION : Travail des abeilles
MELODIEUSE : Harmonieuse
MELODRAME : Drame populaire
MELON : Plante dicotyl�done
MEMBRURE : Pi�ce de charpente
MEMOIRE : Souvenir
MEMORABLE : Historique
MEMORISE : Enregistre
MENACANTE : Intimidante
MENAGERIE : Zoo
MENAIT : Entra�nait
MENDELISME : Th�orie de l'h�r�dit�
MENDIER : Demander
MENEES : Intrigue
MENINGE : Membrane qui entoure le cerveau
MENINGOCOQUE : Agent pathog�ne de la m�ningite
MENISQUE : Lentille
MENSE : Revenu eccl�siastique
MENSUEL : Douze fois par an
MENTALEMENT : Int�rieurement
MENTEUR : Trompeur
MENTEUSE : Trompeuse
MENTHE : Plante aromatique
MENTIONNE : Nomme
MENTISME : Fuite des id�es
MENTONNIERE : Jugulaire
MENUE : Mince
MENURE : Grand oiseau passereau vivant en Australie
MEPRENDRE : Faire une erreur (se)
MEPRISE : Confusion
MEPRISER : D�daigner
MER : Etendue d'eau
MERCANTI : Commer�ant malhonn�te
MERCANTILE : Commercial
MERCENAIRE : Qui n'agit que pour un salaire
MERCURE : Plan�te chaude
MERE : Moule
MERES : Moules
MERIDIONAL : Au sud
MERINOS : Mouton
MERISIER : Bois
MERITER : Encourir
MERLAN : Poisson
MERLE : Oiseau passereau
MERLIN : Hache
MERLU : Poisson
MERLUCHE : Morue
MEROSTOMES : Arthropodes aquatiques
MES : Adjectif Possessif
MESAVENTURE : Accident
MESESTIMER : M�conna�tre
MESS : Cantine
MESSAGERIE : Service de transport
MESSE : Service
MESSIE : Lib�rateur
MESSIRE : Ancienne d�nomination honorifique
MESURAIENT : Sondaient
MESURANT : Sondant
MESURER : Sonder
METALLISE : Etame
METALLURGISTE : Fondeur
METAMORPHOSE : Changement
METEO : Temps
METEORITE : A�rolithe
METHANE : Carbure d'hydrog�ne
METHODOLOGIE : Epist�mologie
METICULEUSE : Pointilleuse
METISSAGE : Croisement
METOPE : Intervalle
METRER : Mesurer
METRO : Chemin de fer
METRONOME : Instrument � pendule
METS : Plat
METTABLE : Passable
METTRE : Poser
MEUBLER : Garnir
MEUGLER : Mugir
MEULAGE : Ajustage
MEULON : Tas de sel
MEURTRE : Crime
MEURTRIR : Contusionner
MEUTE : Troupe
MEXIQUE : Pays d'Am�rique centrale
MG : Magn�sium
MI : Note
MIASME : Gaz putride
MICA : Minerai � structure feuillet�e
MICELLE : Particules en suspension dans une solution collo�dale
MICMAC : Manigance
MICROBE : Bacille
MICROBICIDE : Antiseptique
MICROCEPHALE : Petite t�te
MICROCOSME : Image r�duite du monde
MICROFARAD : Unit� de capacit�
MICROMETRE : Instrument de mesure tr�s pr�cis
MIE : Partie du pain
MIEL : Substance sirupeuse et sucr�e
MIELLEE : Exsudation sucr�e
MIEN : Possessif
MIENNE : Possessif
MIENS : Possessif
MIEVRERIE : Espi�glerie
MIGNARDISE : D�licatesse
MIGNONNE : Poire
MIGRAINE : Mal de t�te
MIJAUREE : Pimb�che
MIL : C�r�ale
MILDIOU : Maladie 
MILE : Mesure de longueur
MILICIEN : Soldat
MILITAIRE : Soldat
MILITARISME : Bellicisme
MILLE : Adjectif num�ral
MILLENAIRE : P�riode
MILLET : C�r�ale
MILLIAMPERE : Unit� de courant
MILLIARDAIRE : Riche
MILLIMETRE : Unit� de longueur
MILOUIN : Oiseau palmip�de
MIMER : Faire des gestes
MIMETISME : Ressemblance
MIMOGRAPHE : Compositeur de mimes
MINABLE : Pitoyable
MINARET : Tour
MINAUDIER : Poseur
MINCE : Etroit
MINERALIER : Cargo
MINERVE : Appareil orthop�dique
MINEUR : Moindre
MINIATURISANT : R�duisant
MINIMAUX : Infimes
MINIME : Infime
MINIMUM : Plus petite valeur
MINISTRE : Pr�tre
MINIUM : Oxyde de plomb
MINNESOTA : Etat d'Am�rique
MINOIS : Frimousse
MINORQUE : Ile de M�diterran�e
MINUTER : Organiser
MINUTIEUSE : M�ticuleuse
MIR : Organisme de propri�t� collective rurale russe
MIRABELLE : Prune
MIRACLE : Prodige
MIRADOR : Belv�d�re
MIRAGE : Chim�re
MIRE : Cible
MIREPOIX : Pr�paration pour corser une viande
MIRIFIQUE : Mirobolant
MIRLITON : Fl�teau
MIROITAIENT : Brillaient
MIROITERIE : Industrie des glaces
MISANTHROPE : Sauvage
MISCIBLES : Peuvent �tre m�lang�s
MISERABLE : Malheureux
MISERE : D�tresse
MISEREUX : Pauvre
MISSILE : Fus�e de combat
MISSIVE : Message
MITEUX : Minable
MITHRIDATISE : Immunise
MITIGER : Adoucir
MITOSE : Caryocin�se
MITRAILLEUSE : Arme automatique
MITRON : Gar�on boulanger
MIXE : M�lange
MIXTION : M�lange
MM : Millim�tre
MN : Minute
MOBILISABLE : peut �tre appel�
MOBILITE : Instabilit�
MODALITE : Particularit�
MODE : Moeurs
MODELE : Etalon
MODELER : Fa�onner
MODELEUR : Sculpteur
MODENATURE : Profil des moulures
MODERATION : Retenue
MODERER : Adoucir
MODERNE : Contemporain
MODERNISER : Rajeunir
MODESTEMENT : Humblement
MODIFICATEUR : Transformateur
MODILLON : Ornement
MODULATION : Inflexion
MODULE : Coefficient
MODULER : Articuler
MOELLON : Pierre de construction
MOI : Pronom personnel
MOINDRE : Plus petit
MOINS : Comparatif d'inf�riorit�
MOIRER : Calandrer
MOIRURE : Reflet
MOIS : Division de l'ann�e
MOISER : Assembler
MOISI : G�t�
MOISISSURE : V�g�tation cryptogamique
MOISSONNER : R�colter
MOITIE : Demi
MOLAIRE : Dent
MOLE : Digue
MOLECULE : Particule
MOLES : Digues
MOLESTER : Brutaliser
MOLETTE : Petit pilon de pharmacien
MOLLAH : Savant docteur en droit canonique
MOLLASSONNE : Indolente
MOLLESSE : Apathie
MOLLETIERE : Jambi�re de cuir
MOLLETONNER : Rembourrer
MOLLUSCUM : Tumeur de la peau
MOLOCH : Reptile saurien
MOMERIE : Mascarade
MOMIFIER : Fossiliser
MON : Adjectif possessif
MONARCHIE : Royaut�
MONARCHISTE : Royaliste
MONASTERE : Clo�tre
MONCEAUX : Accumulations
MONDER : D�cortiquer
MONDIALISATION : Universalisation
MONDOVISION : Transmission globale
MONEL : Alliage
MONGOLISME : Affection cong�nitale
MONIALE : Religieuse
MONITEUR : Entra�neur
MONITION : Avertissement
MONITOR : Navire de guerre cuirass�
MONNAYER : Vendre
MONOCHROME : Noir et blanc
MONOCLE : Lorgnon
MONOCOTYLEDONES : Classe de v�g�taux
MONODIE : Chant � une seule voix
MONOGRAPHIE : Etude sur un sujet pr�cis
MONOIDEISME : Id�e fixe
MONOLOGUE : Soliloque
MONOME : Expression alg�brique
MONONUCLEAIRE : Qui n'a qu'un noyau
MONOPHASE : Alternatif simple
MONOPHONIE : Qui n'a qu'un canal
MONOPOLISATION : Accaparement
MONOPTERE : Temple circulaire � coupole  entour� d'une seule rang�e de colonnes
MONOSACCHARIDE : Sucre
MONOSTYLE : Qui n'a qu'un f�t
MONOTHEISTE : Qui n'a qu'un Dieu
MONOTONIE : Ennui
MONSEIGNEUR : Messire
MONSTRE : Animal fantastique et terrible
MONT : Butte
MONTAGE : Trucage
MONTAISON : Migration des saumons
MONTANT : Total
MONTEE : C�te
MONTEES : C�tes
MONTER : Grimper
MONTGOLFIERE : Ballon
MONTICULE : Butte
MONTMARTRE : Quartier de Paris
MONTMORENCY : Vari�t� de cerise
MONTRER : Pr�senter
MONTS : Collines
MONUMENT : Mausol�e
MONUMENTAL : Colossal
MOQUE : R�cipient servant de mesure
MOQUETTE : Tapis
MORAILLE : Tord-nez
MORAINE : D�bris de roche
MORALE : Ethique
MORALISATEUR : Edifiant
MORALISER : Cat�chiser
MORASSE : Derni�re �preuve
MORATOIRE : Suspension
MORCELER : Partager
MORCELLEMENT : Division
MORDANT : Incisif
MORDICUS : Obstin�ment
MORDRE : Croquer
MORE : Berb�re
MORFONDRE : Se languir (se)
MORGUE : Arrogance
MORIBOND : Agonisant
MORICAUD : Noiraud
MORILLE : Champignon
MORILLON : Raisin noir
MORIO : Papillon
MORION : Ancien casque l�ger
MORMON : Membre d'une secte am�ricaine
MORNE : Triste
MOROSES : Mornes
MORPHINE : Principal alcalo�de de l'opium
MORPHOGENE : Qui intervient dans la gen�se d'une forme organique
MORSE : Mammif�re marin des r�gions arctiques
MORTADELLE : Gros saucisson
MORTAISE : Entaille
MORTAISEUSE : Machine outil de menuisier
MORTIER : M�lange de ciment et de sable
MORTIFIER : Faire souffrir cruellement
MORUTIER : Bateau de p�che
MORVEUX : Sale gamin
MOSAIQUE : Assemblage d�coratif de petites pierres
MOSQUEE : Sanctuaire consacr� au culte musulman
MOT : Message
MOTEL : G�te pour automobilistes
MOTIVER : Causer
MOTO : V�hicule � deux roues
MOTOCYCLE : V�hicule � deux roues
MOTONAUTISME : Navigation rapide
MOTORISANT : M�canisant
MOTRICE : Locomotive
MOTS : Messages
MOTTE : Gros morceau de beurre
MOU : Tendre
MOUCHARABIEH : Balcon arabe
MOUCHARDAGE : D�nonciation
MOUCHER : Rembarrer
MOUCHERONNER : Sauter hors de l'eau
MOUCHETEE : Tachet�e
MOUCHOIR : Petite pi�ce de linge
MOUDRE : Ecraser
MOUE : Grimace
MOUFLE : Mitaine
MOUILLAGE : Ancrage
MOUILLE : Avarie d'une cargaison
MOUILLETTE : Morceau de pain long
MOUISE : Panade
MOULER : Reproduire la forme
MOULIERE : Elevage de moules
MOULINANT : Ecrasant
MOULINETTE : Broyeur m�nag�
MOULURES : Baguettes
MOUMOUTE : Perruque
MOURANT : Moribond
MOURIR : Partir
MOURON : Souci
MOUSME : Jeune fille japonaise
MOUSQUETAIRE : Fantassin arm� d'un mousquet
MOUSQUETON : Crochet � ressort
MOUSSE : Ecume
MOUSSELINE : Toile de coton claire, fine et l�g�re
MOUSSON : Vent saisonnier
MOUSTACHES : Longs poils tactiles
MOUT : Jus de raisin
MOUTARDE : Condiment
MOUTON : Mammif�re domestique ruminant
MOUTONNEUSE : Agit�e
MOUTURE : Op�ration de meunerie
MOUVANCE : D�pendance d'un fief par rapport � un autre
MOUVANT : Anim�
MOUVEMENTE : Accident�
MOUVOIR : Remuer (se)
MOYENAGEUX : Ag� d'environ deux mille ans
MOYENNEMENT : A demi
MOYETTE : Petite meule
MOYEUX : Partie centrale d'une roue
MS : Mili-seconde
MU : Lettre de l'alphabet grec
MUCILAGINEUX : Visqueux
MUCOR : Champignon
MUER : Changer de peau
MUET : Silencieux
MUETTES : Discr�tes
MUFLE : Individu mal �lev�
MUGIR : Beugler
MUGISSEMENT : Beuglement
MULARDE : Canard
MULATRESSE : M�tisse
MULE : Hybride de l'�ne et de la jument
MULETTE : Mollusque d'eau douce
MULOT : Rat des champs
MULTICOLORE : Polychrome
MULTIFILAIRE : A plusieurs conducteur
MULTIMETRE : Appareil de contr�le
MULTIPLACE : Dans lequel on peut monter � plusieurs
MULTIPLEX : Transmission de plusieurs communications sur une seule voie
MULTIPLICATION : Reproduction
MULTIPLIER : Reproduire
MULTITUDE : Foule
MUNICIPALITE : Mairie
MUNIR : Equiper
MUNSTER : Fromage ferment�
MUR : Adulte
MURAILLE : Rempart
MURE : Fruit
MURENE : Poisson physostome
MURENIDES : Famille de poissons
MURER : Boucher
MURERA : Condamnera
MURES : Adultes
MUREX : Mollusque gast�ropode
MURMURE : Faible bruit
MUSARDANT : Fl�nant
MUSARDERIE : Fl�nerie
MUSCADES : Graines aromatiques
MUSCARINE : Alcalo�de de certains champignons v�n�neux
MUSCULATION : Exercices physiques
MUSE : D�esse
MUSEAU : Truffe
MUSELER : B�illonner
MUSER : Fl�ner
MUSEUM : Conservatoire
MUSICIEN : Concertiste
MUSICOGRAPHIE : Description des oeuvres musicales
MUSIQUE : M�lodie
MUSSIF : Bisulfure d'�tain
MUSULMAN : Islamique
MUTABLE : Sujet au changement
MUTATION : Changement
MUTILATIONS : D�gradations
MUTILER : D�grader
MUTINER : Se rebeller (se)
MUTITE : Aphasie
MUTUELLE : R�ciproque
MYCENIENNE : Relatif � la civilisation pr�hell�nique
MYCOLOGIE : Etude des champignons
MYELINE : Substance qui entoure la fibre nerveuse
MYGALE : Grande araign�e
MYOGRAPHE : Appareil qui enregistre les contractions musculaires
MYOPATHIE : Affection des muscles
MYOPE : Am�trope
MYOSOTIS : Plante � fleurs bleues
MYRIAPODES : Mille-pattes
MYSTERE : Esot�risme
MYSTIFICATION : Farce
MYSTIFIE : Abuse
MYTHIQUE : Illumin�
MYTHOMANE : Menteur
MYXOMYCETES : Ordre de champignons
N : Pas de d�finition
NA : Interjection
NABOT : Avorton
NACELLE : Panier
NADIR : Oppos� au z�nith
NAGEOIRE : Propulseur
NAGEUSE : Rameuse
NAIN : Petit
NAISSAIN : Embryons d'hu�tre
NAISSANCE : Commencement
NAIVETE : Candeur
NANDOU : Genre d'autruche
NANISME : Petitesse
NANTI : Riche
NANTISSEMENT : Gage
NAPHTALINE : Antimite
NAPPE : Vaste couche
NAPPERON : Petit linge d�coratif
NARCISSISME : Egotisme
NARCOSE : Torpeur pathologique
NARCOTIQUE : Calmant
NARGUILE : Pipe
NARRATION : R�cit
NARTHEX : Vestibule de l'�glise
NASARDE : Chiquenaude
NASILLARD : Qui vient du nez
NASIQUE : Couleuvre de l'Inde
NASITORT : Cresson al�nois
NASSE : Casier
NATIFS : Originaires
NATION : Peuple
NATIONALISATION : Transfert de biens � la collectivit�
NATIVISME : Th�orie qui s'oppose au g�n�tisme
NATTE : Tapis
NATTIER : Tresser
NATURALISTE : Botaniste
NATUREL : Pur
NAUFRAGEUR : Pillard
NAUMACHIE : Repr�sentation d'un combat naval
NAUTILE : Mollusque c�phalopode
NAVAJA : Long couteau espagnol
NAVARQUE : Commandant d'un vaisseau ou d'une flotte
NAVICERT : Permis de naviguer
NAVIGATEUR : Marin
NAVIRE : B�timent
NAVRANT : D�solant
NAZI : Membre du parti national-socialiste allemand
NB : Niobium
ND : N�odyme
NE : N�on
NEANDERTALIEN : Type de pal�anthropien
NEANT : Vide
NEBULEUSE : Corps c�leste
NECESSAIRE : Indispensable
NECESSITEUX : Pauvre
NECROLOGUE : Liste de morts
NECROPOLE : Vaste cimeti�re
NECROSE : Gangr�ne
NECTARINE : P�che
NEE : Apparue
NEES : Apparues
NEF : Grand navire � voiles
NEFASTE : Nuisible
NEGATIF : Cathode
NEGLIGENCE : Nonchalance
NEGOCIABLE : Cessible
NEGOCIATION : Tractation
NEGONDO : Arbre ornemental
NEGUS : Titre port� par les souverains �thiopiens
NEIGE : Eau congel�e
NENUPHAR : Plante aquatique
NEOCOLONIALISME : Domination �conomique
NEOLITHIQUE : Pr�historique
NEOLOGISME : Mot nouveau
NEON : Gaz rare
NEOPHYTE : Novice
NEPE : Insecte des eaux stagnantes
NEPETE : Plante � odeur forte
NEPOTISME : Favoritisme
NEPTUNIUM : El�ment radioactif
NERPRUN : Arbrisseau vivace � fruits noirs
NERVURE : Ligne saillante sur une surface
NET : Propre
NETS : Propres
NETTEMENT : Distinctement
NETTOYAGE : Lavage
NEUFCHATEL : Fromage
NEUROLOGIE : M�decine du syst�me nerveux
NEUTRALISANTE : Annihilante
NEUTRALITE : Abstention
NEUTRON : Particule �l�mentaire
NEUVAINE : S�rie d'exercices de pi�t� et de pri�res
NEUVIEME : Qui bat le dixi�me
NEVRALGIE : Mal de t�te
NEVROSE : Affection nerveuse
NEWTON : Acc�l�ration de 1 m/s communiqu�e � une masse de 1 Kilo
NEZ : Proue
NI : Conjonction n�gative
NIAIS : Na�f
NIAISE : Na�ve
NIAOULI : Arbrisseau exotique
NICARAGUA : Pays d'Am�rique centrale
NICHE : Cavit�
NICHEE : Couv�e
NICKEL : Impeccable
NICOL : Prisme
NICOTINE : Alcalo�de du tabac
NID : Abri
NIDIFIER : Nicher
NIDS : Abris
NIELLE : Incrustation d'�mail noir
NIELLURE : Proc�d� de gravure
NIGAUD : Ben�t
NIGELLE : Herbe � graines parfum�es
NIMBANT : Aur�olant
NIOBIUM : Colombium
NIPPANT : Habillant
NIPPES : Frusques
NIRVANA : Extinction du karman
NITESCENCE : Lueur
NITRATE : Salp�tre
NITRURATION : Durcissement superficiel de l'acier
NIVEAU : Hauteur
NIVELE : Egalise
NIVELLE : Niveau � bulle
NO : Drame lyrique japonais
NOBLAILLON : Personne de petite noblesse
NOBLEMENT : Dignement
NOCIF : Nuisible
NOCTUELLE : Papillon nocturne
NODULE : Concr�tion pierreuse
NOESE : Pens�e
NOIRAUDE : Basan�e
NOIRCISSEMENT : Assombrissement
NOISETIER : Arbrisseau des bois et des haies
NOLISEMENT : Affr�tement
NOM : D�signation
NOMADE : Ambulant
NOMBRE : Quantit�
NOME : Division administrative de l'ancienne Egypte
NOMENCLATURE : Liste
NOMINALEMENT : Par son nom
NOMINATION : Mention
NOMME : D�sign�
NOMOGRAPHIE : Trait� sur les lois et leur interpr�tation
NON : Refus
NONANTE : Quatre-vingt-dix
NONCE : Agent diplomatique du Saint-Si�ge
NONOBSTANT : En d�pit de
NORD : Point cardinal
NORIA : Machine hydraulique �  godets
NORMALE : Ordinaire
NORMALISATION : Standardisation
NORME : R�gle
NORVEGE : Pays du Nord de l'Europe
NOSOGRAPHIE : Description et classification m�thodique des maladies
NOTABLE : Remarquable
NOTAIRE : Officier public
NOTAMMENT : Particuli�rement
NOTE : Noire ou blanche
NOTIFICATIVE : Annonce
NOTOIRE : Connu
NOUAGE : Op�ration de tissage
NOUAISON : Transformation de l'ovaire de la fleur en fruit
NOUGAT : Confiserie
NOURRI : Dense
NOURRIR : Alimenter
NOURRITURE : Alimentation
NOUVEAUTE : Innovation
NOUVELLISTE : Journaliste
NOVATEUR : Cr�ateur
NOVICE : D�butant
NU : Lettre de l'alphabet grec
NUANCE : Tonalit�
NUBIE : R�gion d'Afrique du Nord
NUBILE : En �ge d'�tre mari�
NUCLEAIRE : Atomique
NUCLEOLE : Petit corps sph�rique qui se trouve dans les noyaux cellulaires
NUCLEUS : Rognon de silex
NUEE : Nuage
NUIRE : Faire du tort
NUISIBLES : N�fastes
NUIT : Obscurit�
NUL : Qui se r�duit � rien
NULLEMENT : Point
NULS : Qui se r�duisent � rien
NUMENT : Cr�ment
NUMERAIRE : Qui sert � compter
NUMERATEUR : Nombre sup�rieur d'une fraction
NUMEROTER : Chiffrer
NUMISMATE : Sp�cialiste en m�dailles et monnaies anciennes
NUPTIALE : Relatif � la c�l�bration du mariage
NURSERY : Pi�ce r�serv�e aux enfants
NUS : D�pouill�s
NUTRITION : Alimentation
NYCTAGINACEES : Famille de plantes dicotyl�dones
NYMPHE : D�esses
O : Pas de d�finition
OBEDIENCE : D�pendance
OBEISSANTE : Disciplin�e
OBERER : Charger de dettes
OBIER : Arbuste � fleurs blanches
OBJECTANT : R�torquant
OBJECTION : Critique
OBJECTIVITE : Impartialit�
OBLATION : Offrande
OBLIGATOIRE : Forc�
OBLIGER : Contraindre
OBLIQUER : D�vier
OBLITERER : Apposer un cachet
OBLONGUE : Allong�e
OBSCENE : Licencieux
OBSCURCIR : Noircir
OBSCUREMENT : De mani�re � peine visible
OBSEDE : En proie � une id�e fixe
OBSEQUIEUSEMENT : En rampant
OBSERVATEUR : T�moin
OBSERVER : Regarder
OBSESSION : Hantise
OBSTINATION : Ent�tement
OBSTRUCTION : Engorgement
OBSTRUE : Bouch�
OBTENAIENT : D�crochaient
OBTURANT : Bouchant
OBTURER : Boucher
OBUS : Projectile
OC : Ondes courtes
OCARINA : Petit instrument � vent
OCCASIONNEL : Fortuit
OCCIDENT : Couchant
OCCIDENTALE : A l'Ouest
OCCIRE : Tuer
OCCLUAIENT : Fermaient
OCCULTENT : Eclipsent
OCCULTER : Eclipser
OCCUPATION : Ouvrage
OCCURRENCE : Circonstance
OCEANIDE : Chacune des filles d'Ok�anos et de T�thys
OCEANIQUE : En bord de mer
OCTAEDRE : Poly�dre
OCTAVIA : Petite fl�te
OCTOBRE : Mois
OCTOGENAIRE : Personne �g�e
OCTROYER : Conc�der
OCTUOR : Oeuvre musicale
OCULUS : Oeil-de-boeuf
ODEON : Nom de divers �difices consacr�s aux chants et � la musique
ODIEUX : D�testable
ODONATES : Ordre d'insectes
ODONTOLOGIE : Traitement des dents
ODORAT : Flair
OFFENSE : Affront
OFFENSIVE : Attaque
OFFICIANT : C�l�brant
OFFICINAL : Utilis� en pharmacie
OFFICINE : Boutique
OFFRANDE : Sacrifice
OFFRE : Proposition
OFFRIR : Donner
OFFUSQUER : Choquer
OGIVE : Arc diagonal
OH : Interjection
OHE : Appel
OHM : Unit� de r�sistance
OIE : Oiseau palmip�de
OIGNON : Plante potag�re
OILLE : Rago�t
OINDRE : Enduire
OISEAU : Vert�br� � plumes
OISEUX : Inutile
OISIVE : Inactive
OK : D'accord
OKLAHOMA : Etat d'Am�rique
OLEAGINEUX : Huileux
OLEICULTEUR : Cultivateur grec
OLEODUC : Tuyau
OLFACTION : Flair
OLIGARCHIE : R�gime politique
OLIGOCHETES : Lombric
OLIVAIE : Verger
OLIVE : Fruit
OLIVETAIN : Moine
OLOGRAPHE : Manuscrit
OLYMPIADE : Comp�tition
OMBELLIFERE : Famille de plantes
OMBLE : Saumon de fontaine
OMBRAGEUSE : Inqui�te
OMBRE : Zone sombre
OMBRELLE : Parasol
OMELETTE : Plat aux oeufs
OMETTRE : Oublier
OMISSION : Oubli
OMNIPOTENCE : Domination
OMNIPRESENCE : Ubiquit�
OMNIVORE : Facile � nourrir
ON : Pronom ind�fini
ONCE : Mesure de poids anglaise
ONCTION : Rite
ONDATRA : Mammif�re rongeur
ONDINE : D�esse des eaux
ONDULEUX : Sinueux
ONEREUX : Cher
ONGLETTE : Petit outil de graveur
ONGLON : Sabot
ONOMASIOLOGIE : Inverse de la s�masiologie
ONOMATOPEE : Interjection
ONTARIO : Etat d'Am�rique
ONYX : Vari�t� d'agate
OOLITHE : Calcaire form� de grains sph�riques
OPALE : Pierre pr�cieuse
OPERA : Genre musical
OPERATEUR : Manipulateur
OPERCULE : Couvercle
OPERER : Intervenir
OPHICLEIDE : Gros instrument � vent
OPHTALMIE : Conjonctivite
OPHTALMOLOGISTE : M�decin sp�cialiste
OPINER : Enoncer son opinion
OPINION : Id�e
OPIUM : Stup�fiant
OPPORTUNEMENT : A point nomm�
OPPOSANT : Adversaire
OPPOSITION : Antagonisme
OPPRESSE : Etouffe
OPPRIMER : Asservir
OPTER : Choisir
OPTIMAL : Le meilleur possible
OPTIMISME : Espoir
OPULENT : Riche
OR : M�tal jaune
ORAISON : Pri�re
ORANGEADE : Boisson
ORANGES : Fruit comestible
ORANTE : Personnage repr�sent� en pri�re
ORATOIRE : Lieu destin� � la pri�re
ORBITE : Trajectoire
ORCHESTRATION : Arrangement
ORCHESTRE : Groupe de musicien
ORDINAIRE : Courant
ORDO : Calendrier liturgique
ORDONNATEUR : Autorit� comp�tente
ORDONNEE : Coordonn�e verticale
ORDURIERE : Grossi�re
OREE : Bordure
OREILLER : Coussin
OREMUS : Invitation � la pri�re
ORFRAIE : Oiseau de proie
ORGANEAU : Anneau d'une ancre
ORGANIGRAMME : Tableau sch�matique
ORGANISATEUR : Dirigeant
ORGANISER : Agencer
ORGANISTE : Musicien
ORGELET : Bouton
ORGUEILLEUSE : Fi�re
ORIENTABLE : Qui tourne
ORIENTANT : Dirigeant
ORIENTER : Diriger
ORIGAN : Plante aromatique
ORIGINALITE : Excentricit�
ORIGINELLE : Initiale
ORLE : Bordure
ORMEAU : Haliotide
ORNE : Vari�t� de fr�ne
ORNEMENTATION : D�coration
ORNIERE : Trou
ORNITHORYNQUE : Mammif�re australien
OROGRAPHIQUE : Qui d�crit les montagnes
ORPHELINAT : Etablissement pour les enfants d�favoris�s
ORPHIE : B�cassine de mer
ORQUE : Mammif�re marin
ORTHODOXIE : Conformisme
ORTHODROMIE : Route directe
ORTHOGRAPHE : Mani�re d'�crire un mot
ORTHOPEDIE : Correction des difformit�s
ORTHOSCOPIQUE : Qui ne d�forme pas l'image
ORTIE : Plante piquante
ORVET : Reptile saurien
OS : Probl�me
OSA : Risqua
OSANT : Risquant
OSCILLATION : Balancement
OSCILLER : Balancer
OSCILLOGRAMME : Courbe
OSE : Risque
OSER : Risquer
OSERA : Risquera
OSERAIT : Risquerait
OSMIUM : M�tal dur en cristaux blancs
OSSATURE : Charpente
OSSEUX : Maigre
OSSIFIER : Endurcir
OSTEITE : Carie
OSTENTATION : Etalage
OSTEOMALACIE : Ramollissement des os
OSTEOSYNTHESE : R�paration d'un os
OSTRACISME : Exclusion
OSTROGOT : Personnage extravagant
OTALGIE : Douleur d'oreille
OTITE : Inflammation de l'oreille
OTOLOGIE : M�decine de l'oreille
OU : Conjonction
OUAILLES : Brebis
OUATE : Garniture de doublure
OUATINE : Etoffe de doublure
OUBLIANT : Laissant
OUBLIER : Laisser
OUCHE : P�turage
OUGANDAIS : Africain
OUI : Certes
OUIE : Ouverture d'une table
OUILLANT : Remplissant
OUILLER : Remplir
OUIR : Entendre
OURDIR : Tramer
OURDOU : Langue  du Pakistan
OURLET : Bordure
OURS : Mammif�re carnivore plantigrade
OUT : Terme de tennis
OUTILLANT : Equipant
OUTRAGEUSEMENT : Excessivement
OUTRE : Gourde
OUTREE : Indign�e
OUTRIGGER : Embarcation l�g�re � rames
OUVRABLE : Normalement consacr� au travail
OUVRANT : Battant
OUVRER : Elaborer
OUVRIR : D�plier
OUZBEK : Langue turque
OVALISATION : D�faut d'une pi�ce
OVATIONNE : Acclame
OVIDES : Groupe de mammif�res ongul�s ruminants
OVIPARE : Qui pond des oeufs
OVOIDAL : En forme d'oeuf
OXFORD : Tissu dont les fils de trames et de cha�nes sont de couleurs diff�rentes
OXYACETYLENIQUE : Qui utilise un m�lange d'oxyg�ne et d'ac�tyl�ne
OXYDATION : Rouille
OXYGENE : Gaz invisible et inodore
OYAT : Gramin�e employ�e � fixer les sables des dunes
OZONE : Forme allotropique de l'oxyg�ne
P : Pas de d�finition
PA : Pascal
PACAGER : Faire pa�tre
PACIFIANT : Calmant
PACIFIER : Calmer
PACK : Banquise
PACOTILLE : Camelote
PACTE : March�
PADDY : Riz non d�cortiqu�
PAF : Interjection
PAGAIE : Aviron
PAGANISANT : Agissant comme un pa�en
PAGAYER : Ramer
PAGE : C�t� d'une feuille
PAGINER : Num�roter
PAIEMENT : R�compense
PAILLARD : Libertin
PAILLASSON : Tapis
PAILLE : Chaume
PAILLETANT : Ornant
PAILLON : Petite lamelle de m�tal
PAIR : Divisible par deux
PAISIBLE : Calme
PAITRE : Brouter
PAL : Pieu
PALABRE : Discours
PALAIS : Ch�teau
PALANQUE : Mur de retranchement
PALASTRE : Bo�tier de serrure
PALATIN : Gouverneur d'une province de l'ancienne Pologne
PALE : Partie d'un aviron
PALEE : Poteaux r�unis par des liens
PALEFROI : Cheval de parade
PALEOECOLOGIE : Etude du mode de vie des animaux fossiles
PALEOGRAPHIQUE : Relatif au d�chiffrage des anciennes �critures
PALEONTOLOGISTE : Sp�cialiste en fossiles
PALES : Ternes
PALESTRE : Lieu public pour les exercices du corps
PALETOT : V�tement
PALETTE : Plateau de chargement
PALETTISATION : Organisation des plateaux de chargement
PALEUR : Blancheur
PALI : Ancienne langue religieuse de l'Inde
PALIMPSESTE : Manuscrit effa�able
PALINGENESIE : Th�orie philosophique et religieuse
PALIR : Blanchir
PALIS : Pieu
PALISSADE : Cl�ture
PALISSANT : Blanchissant
PALISSONNER : Assouplir une peau
PALLADIUM : Objet sacr�
PALLIATIVE : Qui n'a qu'une efficacit� incompl�te ou momentan�e
PALMAS : Battement rythm� des paumes des mains
PALMETTE : Ornement stylis�
PALMIPEDES : Groupe d'oiseaux
PALOIS : De Pau
PALOT : B�che
PALPER : Toucher
PALPITANT : Emouvant
PALTOQUET : Homme grossier insignifiant et pr�tentieux
PALUDISME : Maladie
PALUS : Terre d'alluvions au fond des vall�es
PALYNOLOGIQUE : Relatif � l'�tude des pollens
PAMPA : Vaste prairie
PAMPLEMOUSSE : Fruit comestible
PAN : Partie d'un v�tement
PANACEE : Rem�de universel
PANACHE : Assemblage de plumes
PANAMA : Chapeau
PANARABISME : Doctrine politique
PANAX : Genre d'araliac�es
PANCARTE : Panneau
PANCREAS : Glande abdominale
PANDEMIES : Extensions d'une maladie contagieuse
PANDORE : Gendarme
PANEL : Enqu�te
PANETIER : Officier charg� du pain
PANGOLIN : Mammif�re d'Afrique et d'Asie
PANICUM : Millet
PANIERE : Corbeille
PANISLAMISME : Mouvement religieux
PANNEAU : Pancarte
PANNETON : Partie d'une clef
PANOPLIE : D�guisement
PANORPE : Insecte de l'ordre des n�vropt�res
PANOSSE : Serpilli�re
PANSE : Partie d'une cloche
PANSER : Faire la toilette d'un animal domestique
PANSU : Renfl�
PANSUE : Renfl�es
PANTALONNADE : Bouffonnerie
PANTELANT : Haletant
PANTIN : Marionnette
PANTOMIME : Pi�ce mim�e
PANTOUFLER : Passer au service d'une entreprise priv�e
PANURE : Chapelure
PAPAYER : Arbre d'Am�rique tropicale
PAPELARDISE : Hypocrisie
PAPERASSE : Ecrit sans valeur
PAPILIONACEE : Plante de l'ordre des l�gumineuses
PAPILLON : Insecte volant
PAPILLOTAGE : Mouvement involontaire des paupi�res
PAPOTAGE : Bavardage
PAPRIKA : Piment tr�s fort
PAPYROLOGUE : Sp�cialiste en papyrus
PAQUETAGE : Ensemble des effets d'un militaire
PAR : Pr�position
PARA : Partie du Dinar
PARABELLUM : Pistolet automatique
PARACHEVER : Mener � bout
PARACHUTISTE : Sportif ou militaire
PARADER : Se donner un air avantageux pour attirer l'attention
PARADISIER : Oiseau passereau
PARADOXAUX : Qui tiennent de la contradiction
PARAFER : Signer
PARAGE : Voisinage
PARAGUAYEN : Habitant d'un pays d'Am�rique du sud
PARAITRE : Sembler
PARALITTERATURE : Litt�rature en marge
PARALLELEPIPEDE : Poly�dre � six faces
PARALLELOGRAMME : Quadrilat�re
PARALYSER : Neutraliser
PARAMECIE : Protozoaire de l'embranchement des cili�s
PARAMETRE : Constante
PARANGONNAGE : Assemblage
PARANOIDE : D�lire
PARAPHER : Signer
PARAPHRASE : Explication �tendue d'un texte
PARAPLEGIQUE : Handicap�
PARAPSYCHOLOGIE : Etude des ph�nom�nes paranormaux
PARASITE : Perturbation
PARASOL : Grand parapluie
PARATAXE : Proc�d� syntaxique
PARC : Enclos bois�
PARCELLARISER : Diviser
PARCELLE : Pi�ce de terrain
PARCHEMIN : Peau d'animal
PARCIMONIEUSE : Econome
PARCOURIR : Visiter dans toute son �tendue
PARDON : R�mission
PAREDRE : Divinit�
PAREIL : Identique
PAREILLEMENT : Aussi
PAREMENT : Revers des manches
PARENTE : Lien
PARENTS : Qui ont des traits communs
PARER : Embellir
PARESSE : R�pugnance � l'effort
PARFAITE : Qui r�unit toutes les qualit�s
PARFILER : Entrem�ler
PARFONDRE : Colorer le verre
PARFUMER : Aromatiser
PARHELIE : Ph�nom�ne lumineux
PARI : Jeu d'argent
PARIA : Exclu
PARIAGE : Convention du droit f�odal fran�ais
PARIDE : Oiseau passereau
PARIER : Soutenir
PARIETAIRE : Perce-muraille
PARIS : Ville europ�enne
PARISIENNE : Habitante d'une ville fran�aise
PARJURE : Faux serment
PARKA : Manteau
PARLEMENTARISME : R�gime politique
PARLEUSE : Qui aime faire de belles phrases
PARLOTE : Conversation insignifiante
PARNASSIEN : Papillon
PARODIQUE : Qui imite de fa�on ironique
PARODONTE : Ensemble des tissus de soutien de la dent
PAROI : Cloison
PAROISSE : Territoire d'un cur�
PAROISSIEN : Habitant du territoire d'un cur�
PAROLIER : Auteur de textes
PAROXYSMALE : Qui rel�ve du plus haut degr�
PARPAING : El�ment de construction
PARQUEUR : Personne qui s'occupe des hu�tres
PARRAINE : Patronne
PARSEMANT : Jetant �� et l�
PARSIE : Mazd�iste de l'Inde
PART : Portion
PARTAGEANT : Divisant
PARTENAIRE : Associ�
PARTI : Groupe de personnes unies par la m�me opinion
PARTIAL : Qui favorise quelqu'un
PARTICIPANT : Acteur
PARTICIPE : Forme adjective du verbe
PARTICULARISER : Diff�rencier
PARTICULIER : Qui appartient en propre � quelqu'un
PARTIE : Portion
PARTIEL : Qui fait partie d'un tout
PARTIR : Mourir un peu
PARURE : Garniture
PARURIER : Fabricant d'accessoires pour la haute couture
PARUTION : Publication
PARVENIR : Arriver
PARVIENDRA : Arrivera
PAS : Trace
PASCAL : Unit� de mesure de pression
PASSABLE : De qualit� moyenne
PASSADE : Caprice
PASSAGER : Qui ne dure pas
PASSAVANT : Partie du pont d'un bateau
PASSE : Chenal navigable entre deux bancs
PASSEPOIL : Lis�r� qui borde la couture d'un uniforme
PASSEREAU : Oiseau
PASSERELLE : Pont
PASSIFLORE : Fleur de la passion
PASSIONISTE : Membre d'une congr�gation cl�ricale
PASSIONNER : Int�resser
PASSOIRE : Tamis
PASTEQUE : Cucurbitac�e
PASTEURISATION : St�rilisation
PASTICHANT : Imitant
PASTICHEUR : Auteur d'imitations
PASTORAL : Qui �voque la vie des champs
PASTOUREAU : Petit berger
PAT : Terme utilis� aux �checs
PATACHE : Voiture publique peu confortable
PATATE : Pomme de terre
PATAUGER : Marcher dans la boue
PATCHOULI : Plante aromatique
PATE : Farine d�tremp�e et p�trie
PATEE : Nourriture pour les animaux
PATELIN : Village
PATENE : Plat destin� � recevoir l'hostie
PATER : Pri�re
PATERE : Support mural
PATERNE : D'une bienveillance doucereuse
PATHOGENE : Qui provoque des maladies
PATHOLOGIE : Maladie
PATIBULAIRE : Peu recommandable
PATIENTER : Attendre
PATINER : Glisser
PATIR : Subir un dommage
PATISSERIE : G�teau
PATOCHE : Grosse main
PATON : Aliment pour l'engraissement des volailles
PATOUILLER : Patauger
PATRIARCAT : Pr�pond�rance du p�re
PATRIE : Pays
PATRIMOINE : Bien commun
PATRIOTE : Qui aime son pays
PATRON : Mod�le
PATRONAGE : Protection
PATRONNER : Prot�ger
PATROUILLE : Petite formation militaire
PATURE : Nourriture des animaux
PATURER : Pa�tre
PAUMELLE : Gant de voilier
PAUPERISATION : Appauvrissement
PAUVRE : Qui a peu de ressources
PAVANANT : Marchant fi�rement (se)
PAVIE : P�che
PAVILLON : Maison
PAVOIS : Bouclier
PAYER : Acquitter
PAYSAGE : Vue d'ensemble d'une r�gion
PAYSAGISTE : Jardinier
PB : Plomb
PC : Ordinateur
PDG : Patron
PEAGISTE : Personne qui per�oit un droit de passage
PEAUFINER : Fignoler
PECARI : Cochon sauvage d'Am�rique
PECHER : Manquer � une r�gle morale
PECHETTE : Filet rond
PECTINE : Substance utilis�e dans la fabrication des confitures
PECTORAUX : Qui concernent la poitrine
PEDAGOGIE : Science de l'�ducation
PEDALE : Organe de commande d'un m�canisme
PEDANT : Pr�tentieux
PEDIATRIE : Branche de la m�decine
PEDICULE : Support propre � certaines plantes
PEDIGREE : G�n�alogie d'un animal
PEDOLOGIE : Science des sols
PEDONCULE : Queue d'une fleur
PEELING : Intervention esth�tique
PEIGNER : D�m�ler
PEINANT : Causant du chagrin
PEINE : Punition
PEINTRE : Artiste
PEINTURLURANT : Peignant sans go�t
PEJORATIVE : Qui ajoute une id�e d�favorable
PEKINOIS : Petit chien � longs poils
PELAGE : Poils
PELE : Sans v�g�tation
PELIADE : Vip�re
PELISSE : Manteau garni de fourrure
PELLE : Outil de terrassement
PELLETIER : Qui pr�pare, travaille ou vend des fourrures
PELLICULE : Peau tr�s mince
PELOPONNESIEN : Grec
PELOTE : Coussinet pour piquer des aiguilles
PELOTONNANT : Blottissant (se)
PELOUSE : Etendue d'herbe
PELURE : Papier tr�s mince
PENALISATION : D�savantage
PENALITE : Sanction
PENCE : Unit� mon�taire anglaise
PENDAGE : Pente
PENDAISON : Supplice
PENDARD : Vaurien
PENDERIE : Placard
PENDOIR : Crochet � viande
PENDRE : Attacher par le haut
PENDULER : Se balancer
PENETRABLE : Intelligible
PENIBLE : Fatiguant
PENICHE : Bateau
PENITENCIER : Prison
PENITENT : Candidat au pardon
PENNE : Plume
PENNON : Flamme
PENOMBRE : Demi-jour
PENSER : Imaginer
PENSIONNAT : Etablissement d'enseignement priv�
PENSUM : Punition
PENTAEDRE : Solide � cinq faces
PENTAGONE : Polygone
PENTARCHIE : Gouvernement de cinq chefs
PENTECOTE : F�te juive et chr�tienne
PENTURE : Soutien de porte
PEPERE : Tranquille
PEPINIERE : Plant de jeunes arbres
PEPITE : Masse d'or
PEPTIDE : Mol�cule constitu� de plusieurs mol�cules d'acides amin�s
PERBORATE : D�tergent
PERCANTE : Qui p�n�tre profond�ment
PERCEE : Ouverture
PERCEPTEUR : Fonctionnaire
PERCEPTION : Recouvrement
PERCER : Perforer
PERCEVANT : Recueillant
PERCHERON : Race de cheval
PERCHLORATE : Sel d'un acide
PERCLUSE : Priv�e de la facult� de mouvoir ses membres
PERCOLATION : P�n�tration lente des eaux m�t�oriques dans le sol
PERCUTANTE : Qui produit un choc
PERCUTER : Heurter
PERDENT : Egarent
PERDRE : Egarer
PERDRIX : Oiseau gallinac�
PERE : Cr�ateur
PEREMPTOIRE : Cat�gorique
PEREQUATION : R�partition des charges
PERFECTIONNE : Am�liore
PERFECTIONNISME : Recherche excessive de la qualit�
PERFORATION : Trou
PERFORE : Perce
PERFORMANT : D'un bon rendement
PERIARTHRITE : Inflammation autour d'une articulation
PERICLITER : D�cliner
PERIDOTITE : Roche
PERIGEE : Point de l'orbite d'un astre
PERIHELIE : Point de l'orbite d'une plan�te
PERIME : D�pass�
PERIMETRE : Contour
PERIODE : Espace de temps
PERIOSTE : Membrane qui entoure les os
PERIPHERIE : Surface ext�rieure d'un solide
PERIPHRASTIQUE : Qui tient de la circonlocution
PERISSABLE : Qui n'est pas �ternel
PERISTYLE : Colonnade
PERLE : Petite boule
PERLECHE : Inflammation de la commissure des l�vres
PERLIMPINPIN : Poudre magique
PERMANENTE : Qui dure
PERMEABLE : Qui se laisse traverser
PERMETTRE : Autoriser
PERMIEN : Derni�re p�riode de l'�re primaire
PERMISES : Autoris�es
PERMISSIONNAIRE : Militaire en repos
PERMUTER : Intervertir
PERONE : Os
PERONNELLE : Fille sotte et bavarde
PERORER : Discourir avec emphase
PERPETUANT : Faisant durer
PERPETUER : Faire durer
PERQUISITION : Recherche
PERRON : Escalier ext�rieur
PERRUCHE : Oiseau grimpeur
PERRUQUIER : Fabricant de postiches
PERSE : Langue du groupe iranien
PERSECUTE : Opprime
PERSEVERER : S'obstiner
PERSIENNE : Dispositif de fermeture
PERSIFLE : Tourne en ridicule
PERSIL : Plante potag�re aromatique
PERSILLERE : Vase rempli de terre et perc� de trous
PERSISTE : Dure
PERSONNAGE : Personne en vue
PERSONNALISER : Donner un caract�re original
PERSONNEL : Propre
PERSUADER : Convaincre
PERSUASIVE : Convaincante
PERTINENT : Qui convient
PERTURBATEUR : Qui cause du trouble
PERUVIEN : Habitant d'Am�rique du Sud
PERVERSION : Corruption
PESANT : Lourd
PESER : Appuyer
PESSIMISTE : Qui pense que tout va mal
PESTICIDE : Produit contre les parasites
PESTILENTIEL : Qui r�pand une mauvaise odeur
PETANQUE : Jeu de boules
PETARADER : Faire du bruit
PETASE : Chapeau
PETIOT : Tout petit
PETITESSE : Acte mesquin
PETITIONNE : Adresse une plainte
PETONCLE : Mollusque bivalve
PETREL : Oiseau palmip�de
PETRIFIER : Changer en pierre
PETRIN : Outil de boulanger
PETROCHIMISTE : Sp�cialiste en hydrocarbures
PETROGRAPHIE : Branche de la g�ologie
PETROLIER : Navire
PETULANCE : Vivacit�
PEU : Petite quantit�
PEUPLEE : Habit�e
PEUR : Sentiment d'inqui�tude
PH : Coefficient d'acidit�
PHAETON : Voiture hippomobile
PHALANGE : Os
PHALANSTERE : Association de production
PHALENE : Papillon
PHALLINE : Principe toxique
PHANATRON : Redresseur � vapeur de mercure
PHANEROGAMES : Plantes se reproduisant par les fleurs et les graines
PHARE : Ensemble des voiles d'un mat
PHARISIEN : Homme hypocrite ou orgueilleux
PHARMACOPEE : Recueil d'indications concernant les m�dicaments
PHASIQUE : Se dit de ph�nom�nes neurologiques ayant une activit� p�riodique
PHENIX : Oiseau mythologique
PHENOLS : D�riv� oxyg�n� du benz�ne
PHENOMENE : Ev�nement
PHENYLALANINE : Acide amin� essentiel
PHEOPHYCEE : Algue marine
PHILATELISTE : Collectionneur
PHILISTIN : Personne � l'esprit vulgaire
PHILOLOGIE : Science des documents �crits
PHILOSOPHER : Raisonner
PHILTRE : Breuvage magique
PHLEBOTOMIE : Incision d'une veine
PHOBIE : Peur
PHONEME : El�ment sonore du langage
PHONETIQUE : Etude des sons du langage
PHONOGENIQUE : Dont la voix se pr�te � de bonnes reproductions
PHONOGRAPHIQUE : Relatif � l'enregistrement m�canique des sons
PHOSPHATAGE : Addition d'engrais
PHOSPHATER : Amender une terre avec des engrais
PHOSPHENE : Sensation lumineuse
PHOSPHORE : Corps lumineux
PHOTOCOPIE : Reproduction
PHOTOGENESE : Production de lumi�re
PHOTOGRAPHIER : Obtenir une image
PHOTOMETRE : Cellule
PHOTOMONTAGE : Trucage
PHOTOPERIODE : Dur�e du jour
PHOTOPILE : Panneau solaire
PHOTOSTYLE : Crayon optique
PHRASE : Groupe de mots
PHTISIE : Tuberculose
PHYLACTERE : Bulle
PHYLLOXERA : Puceron
PHYSALIS : Amour-en-cage
PHYSOSTIGMA : Plante � graines toxiques
PHYTOHORMONE : Hormone v�g�tale
PHYTOPLANCTON : Plancton v�g�tal
PHYTOTHERAPIE : Traitement des maladies par les plantes
PI : Lettre de l'alphabet grec
PIAFFEMENT : Tr�pignement
PIAILLER : Crier sans cesse
PIAILLERIE : Criaillerie
PIANOTER : Tapoter
PIAULE : Chambre
PIBLE : D'une seule pi�ce (�)
PIC : Partie ext�rieure de la corne d'artimon
PICADOR : Cavalier
PICAILLONS : Argent
PICAREL : Poisson de la M�diterran�e
PICCOLO : Petite fl�te
PICHENETTE : Petit coup
PICORER : Chercher sa nourriture
PICOT : Petite pointe
PICPOUL : C�page blanc du Midi
PIE : Oiseau
PIECE : Espace habitable
PIED : Support
PIEDOUCHE : Pi�destal
PIERIDE : Papillon
PIERREE : Conduit pour l'�coulement des eaux
PIERRIER : Machine de guerre
PIETAILLE : Ensemble de soldats qui se d�pla�aient � pied
PIETINE : Tr�pigne
PIETONNIERE : Interdite aux voitures
PIETRAIN : Porc belge
PIF : Instrument de mesure approximatif
PIFOMETRE : Instrument de mesure approximatif
PIGEON : Oiseau granivore et sociable
PIGER : Comprendre
PIGMENTATION : Coloration
PIGNOCHANT : Manger sans app�tit
PIGNON : Graine
PILAF : Riz
PILER : Broyer
PILLEUR : Voleur
PILOCARPE : Plante d'Am�rique du Sud
PILOSELLE : Epervi�re
PILOT : Pieu
PILOTIS : Ensemble de pieux
PIMBECHE : Femme pr�tentieuse
PIMPANTE : D'une coquetterie pleine d'�l�gance
PIN : Arbre
PINAILLAGE : Ergotage
PINASTRE : Pin maritime
PINCEAU : Faisceau lumineux
PINCETTES : Ustensiles � deux branches
PINCHARDE : Se dit d'une robe
PINEDE : Terrain plant� d'arbres
PINGOUIN : Oiseau palmip�de
PINNIPEDE : Phoque
PINOT : C�page de Bourgogne
PINTADE : Oiseau gallinac�
PINTE : Ancienne mesure fran�aise de capacit�
PIOCHER : Remuer la terre
PIONCER : Dormir
PIPA : Gros crapaud
PIPELINE : Canalisation
PIPER : Truquer
PIPIT : Oiseau passereau
PIQUER : Voler
PIQUETTE : Mauvais vin
PIQURE : Trou de ver
PIRANHA : Poisson carnassier
PIROGUE : Embarcation l�g�re
PIROUETTE : Changement brusque d'opinion
PIS : Mamelle
PISCIFORME : En forme de poisson
PISE : Mat�riau de construction rudimentaire
PISTACHIER : Arbre des r�gions chaudes
PISTE : Pente balis�e
PISTOLET : Pulv�risateur
PISTOU : Potage
PITHECANTHROPE : Type d'archanthropien
PITIE : Sentiment de compassion
PITOYABLEMENT : En excitant la piti�
PIU : Plus
PIVOT : Palier � axe vertical
PIZZA : Tarte italienne
PK : Dissociation ionique d'un �lectrolyte
PLACARDANT : Affichant
PLACEBO : Substance inactive
PLACER : Confier
PLACIDE : Calme
PLAFOND : Limite sup�rieure qu'on ne peut d�passer
PLAFONNER : Atteindre son maximum
PLAGAL : Mode musical m�di�val
PLAGIAT : Copie
PLAIDABLE : D�fendable
PLAIDER : D�fendre sa cause
PLAIDOYER : D�fense
PLAINE : Etendue plate
PLAINTE : M�contentement
PLAISAMMENT : Avec contentement
PLAISANCE : Que l'on pratique pour son agr�ment
PLANAIRE : Ver plat
PLANCTON : El�ments microscopiques en suspension dans l'eau
PLANE : Outil pour d�grossir les planches de bois
PLANETAIRE : Un des pignons d'un m�canisme diff�rentiel
PLANIFICATION : Organisation
PLANIMETRIE : Partie de la g�om�trie
PLANISPHERE : Carte d'un astre
PLANQUE : Cachette
PLANT : Jeune plante
PLANTER : Enfoncer
PLANTOIR : Outil de jardinier
PLANTUREUX : Abondant
PLAQUER : Saisir aux jambes
PLAQUIS : Rev�tement de pierres
PLASTIC : Explosif
PLASTIFIER : Recouvrir
PLASTIQUER : Faire sauter
PLASTRONNER : Prendre une attitude fi�re
PLATEAU : Support plat
PLATHELMINTHE : Ver � corps aplati
PLATINE : M�tal pr�cieux
PLATINITE : Alliage de fer et de nickel
PLATONIQUE : Sans effet
PLATRER : Immobiliser
PLATYRHINIEN : Ouistiti
PLEBISCITER : Elire � une tr�s forte majorit�
PLEIN : Complet
PLENIERE : O� tout les membres sont convoqu�s
PLEONASME : R�p�tition
PLEURE : Suinte
PLEURNICHERIE : Plainte
PLI : Lettre
PLIABLE : Flexible
PLIE : Poisson plat
PLIER : Mettre en double
PLOCEIDE : Oiseau passereau de l'Ancien Monde
PLOMB : M�tal dense
PLOMBEE : Scell�e
PLOMBURE : Partie d'un vitrail
PLONGEON : Saut
PLOT : Bille de bois
PLOUTOCRATIE : Gouvernement o� le pouvoir appartient aux classes riches
PLOYER : Etre accabl�
PLUIE : Ce qui est r�pandue en abondance
PLUMER : D�pouiller
PLUMETIS : Point de broderie
PLURALITE : Fait d'exister � plusieurs
PLURICAUSAUX : Qui ont plusieurs causes
PLURIEL : Caract�re particulier de la forme d'un mot
PLUS : Indique un degr� sup�rieur
PLUTON : Masse de magma qui s'est solidifi� lentement
PLUTOT : De pr�f�rence
PLUVIAN : Oiseau �chassier de la vall�e du Nil
PM : Prom�th�um
PNEUMATIQUE : Protection de jante
PNEUMOLOGUE : M�decin sp�cialis�
PO : Polonium
POCHADE : Oeuvre sans pr�tention
POCHE : Sac
POCHETTE : Enveloppe
PODAGRE : Qui a la goutte aux pieds 
PODOMETRE : Compteur de pas
POELE : Drap mortuaire
POELON : Petite casserole en terre
POGNON : Argent
POGONOPHORE : Animal marin filamenteux
POIGNARD : Arme
POIGNET : Extr�mit� d'une manche
POILER : Rire (se)
POINCONNER : Perforer
POINDRE : Appara�tre
POINTE : Bout piquant
POINTILLEUX : Exigeant
POINTURE : Taille
POIRE : Fruit
POIREAUTER : Attendre
POIRIER : Arbre fruitier
POISSER : Souiller
POISSEUSE : Collante
POITRAIL : Devant du corps du cheval
POIVRIER : Plante sarmenteuse des r�gions tropicales
POLAIRE : Courbe utilis�e en a�ronautique
POLARIMETRIE : M�thode d'analyse chimique
POLEMIQUE : Discussion
POLEMOLOGIE : Etude de la guerre
POLICE : Contrat
POLIORCETIQUE : Relatif � l'art d'assi�ger les villes
POLISSOIR : Instrument pour faire briller
POLISSONNERIE : Espi�glerie
POLJE : Vaste d�pression ferm�e
POLKA : Danse
POLLICITATION : Proposition de contrat
POLLUANT : Produit salissant
POLOCHON : Traversin
POLONIUM : M�tal radioactif
POLYCHROME : En couleur
POLYCOPIER : Reproduire
POLYESTER : Copolym�re moul�
POLYGLOTTE : Dou� pour les langues
POLYMERISATION : R�action chimique
POLYNOME : Somme de mon�mes
POLYNUCLEAIRE : A plusieurs noyaux
POLYPHONIE : Musique contrapuntique
POLYPODE : Foug�re
POLYSEMIQUE : Qui a plusieurs sens
POLYTECHNICIEN : El�ve d'une grande �cole
POMELOS : Pamplemousse
POMME : Fruit comestible
POMMELEE : Marqu�e de taches rondes
POMMERAIE : Verger
POMOLOGIE : Partie de l'arboriculture
POMPER : Puiser
POMPEUSEMENT : Avec emphase
POMPON : Vari�t� de rose
PONCEUSE : Machine � polir
PONCHO : Manteau de l'Am�rique du Sud
PONCTIONNER : Pr�lever
PONCTUEL : Qui ne concerne qu'un d�tail
PONDERATION : Juste �quilibre de forces
PONDEREUX : Tr�s lourd
PONT : Ouvrage de communication
PONTER : Mettre de l'argent contre le banquier
PONTIFIER : Prendre des airs d'importance
PONTONS : Constructions flottantes plates
POOL : Groupement de producteurs
POPOTE : Cuisine
POPULAIRE : Connu et aim� du grand nombre
POPULEUM : Onguent calmant
POQUER : Jeter sa boule en l'air de mani�re � ce qu'elle reste o� elle tombe
PORCELAINE : Mollusque gastropode des mers chaudes
PORCHERIE : Lieu tr�s sale
PORE : Ouverture des tubes de certain champignons
PORPHYRE : Roche volcanique
PORRIDGE : Bouillon de flocons d'avoine
PORT : Abri
PORTE : Ouverture
PORTEFEUILLE : D�partement minist�riel
PORTEMINES : Instruments de dessin
PORTEURS : D�tenteurs d'une valeur mobili�re
PORTIQUE : Appareil de lavage
PORTRAITISTE : Dessinateur
PORTUGAISE : Hu�tre
POSE : Calme
POSITIF : Qui repose sur les faits
POSITIONNEURS : Organe de mise en place
POSITON : Coordonn�es
POSSEDER : Avoir
POSSESSIF : Qui �prouve un d�sir de domination
POSSESSION : Bien
POSTE : Emploi
POSTER : Affiche
POSTERIEURE : Qui est plac� derri�re
POSTICHE : Artificiel
POSTILLON : Conducteur de la poste
POSTULE : Sollicite
POSTURAL : Li� � la position du corps dans l'espace
POT : R�cipient
POTACHE : Coll�gien
POTARD : Pharmacien
POTASSE : Hydroxyde de potassium
POTE : Ami
POTEE : Plat de l�gumes
POTENCE : Instrument de supplice
POTENTIEL : Puissance
POTERNE : Porte d�rob�e donnant sur un foss�
POTES : Amis
POTIN : Comm�rage
POTION : Rem�de
POU : Insecte parasite
POUCE : Doigt
POUDRE : Substance solide pulv�ris�
POUF : Fauteuil
POUFFER : Eclater de rire
POUILLERIE : Extr�me salet�
POUILLOT : Oiseau passereau
POULAINE : Partie extr�me avant d'un navire
POULET : Policier
POULIE : Boite � r�a
POULIOT : Esp�ce de menthe
POULS : Battement
POUPONNER : Dorloter
POURBOIRE : Gratification
POURCHASSANT : Recherchant avec ardeur
POURFENDRE : Couper en deux d'un coup de sabre
POURPARLERS : Conversations
POURPRE : Mati�re colorante
POURRIE : G�t�e
POURSUITE : Course
POURVOIR : Munir
POUSSAH : Homme gros et gras
POUSSETTE : Voiture d'enfant
POUSSIEREUSE : Sale
POUSSIVE : Fatigu�e
POUTRE : Pi�ce de charpente
POUVOIR : Autorit�
PR : Pras�odyme
PRAESIDIUM : Pr�sidence du Conseil supr�me des Soviets
PRAGMATISME : Doctrine qui prend pour crit�re de la v�rit� la valeur pratique
PRALINE : Confiserie
PRAO : Bateau de Malaisie
PRATICIENNE : Personne qui exerce un m�tier
PRATIQUEMENT : A peu pr�s
PRE : Petite prairie
PREAMBULE : Introduction
PRECAIRE : Instable
PRECARITE : Instabilit�
PRECAUTIONNEUX : Tr�s prudent
PRECEDE : Devance
PRECEDENT : Exemple
PRECEDER : Devancer
PRECEPTE : R�gle
PRECESSION : Mouvement conique de l'axe de rotation de la terre 
PRECHE : Discours moralisateur
PRECIEUSE : Femme du monde
PRECIPITANT : Jetant
PRECISER : Ajouter un d�tail
PRECITE : D�j� dit
PRECOCITE : Avance
PRECOMPTER : Retenir
PRECONISER : Conseiller
PRECONTRAINTE : Technique de mise en oeuvre d'un mat�riau
PREDECOUPE : Dont les �l�ments sont facilement s�parables
PREDESTINATION : D�termination immuable d'�v�nements futurs
PREDICATION : Sermon
PREDILECTION : Pr�f�rence
PREDIRE : Annoncer
PREDISPOSITION : Don
PREDOMINANCE : Sup�riorit�
PREELECTORAUX : Avant les �lections
PREENCOLLE : Facile � appliquer
PREFABRIQUE : En kit
PREFINANCEMENT : Cr�dit
PREFIXE : Modificateur de sens
PREFLORAISON : Disposition des pi�ces florales dans le bouton
PREFORMER : Cr�er d'avance dans ses �l�ments essentiels
PREHENSION : Prise
PREHOMINIEN : Australopith�que
PREJUDICE : Dommage
PRELASSER : S'abandonner avec nonchalance (se)
PRELAT : Dignitaire eccl�siastique
PRELE : Plante des lieux humides
PRELEVER : Prendre
PREMATUREMENT : Avant
PREMISSE : Fait d'o� d�coule une cons�quence quelconque
PREMONITOIRE : Qui pr�c�de un �v�nement
PRENDRE : Saisir
PREOCCUPATION : Souci
PREPONDERANT : Primordial
PREPOSE : Personne charg�e d'une fonction sp�ciale
PREPSYCHOSE : Organisation pathologique de la personnalit�
PREROGATIVE : Avantage particulier
PRES : Indique la proximit�
PRESAGE : Signe
PRESBYOPHRENIE : Forme de d�mence s�nile
PRESCRIPTEUR : Personne ayant une influence sur le choix d'un produit
PRESELECTION : Choix
PRESENTABLE : Propre
PRESENTEMENT : Maintenant
PRESERVER : Garantir d'un mal
PRESIDER : Occuper la premi�re place
PRESIDIAL : Tribunal cr�� par Henri II
PRESOMPTUEUSE : Qui a une trop haute opinion d'elle
PRESSANT : Urgent
PRESSENTIR : Pr�voir
PRESSURISANT : Maintenant une pression normale
PRESTATION : Service fourni
PRESTIGE : S�duction
PRESUMER : Consid�rer comme probable
PRESUPPOSER : N�cessiter l'hypoth�se de
PRET : Dispos�
PRETENDANTE : Candidate
PRETENDU : Suppos�
PRETER : Confier
PRETES : Dispos�es
PRETEXTE : Toge bord�e de pourpre
PRETRISE : Premier degr� du sacerdoce
PREVALOIR : Avoir l'avantage
PREVENANTE : Pleine de sollicitude
PREVENTIF : Par pr�caution
PREVENTORIUM : Etablissement de soins
PREVIENDRAIENT : Avertiraient
PREVISIONS : Conjectures
PREVOIR : Conjecturer
PREVOT : Magistrat
PREVOYANT : Conjecturant
PRIER : Demander
PRIERE : Demande instante
PRIMAT : Titre honorifique attach� � un si�ge �piscopal
PRIMAUTE : Sup�riorit�
PRIME : R�compense
PRIMESAUTIERE : Qui agit spontan�ment
PRIMITIF : Rudimentaire
PRINCE : Titre de noblesse
PRINCIPAL : Directeur
PRINCIPAUX : Les plus importants
PRIORAT : Fonction de prieur
PRISANT : Appr�ciant
PRISER : Appr�cier
PRISME : Triangle de verre
PRIVATDOCENT : Professeur libre
PRIVAUTES : Trop grandes familiarit�s
PRIVE : Ote
PRIX : Valeur
PROBABLE : Vraisemblable
PROBATIONNAIRE : Condamn� soumis � la suspension provisoire de sa peine
PROBLEME : Question � r�soudre
PROCEDER : Ex�cuter une t�che
PROCEDURIERE : Qui aime la chicane
PROCESSION : Cort�ge
PROCHAIN : Suivant
PROCHES : Amis
PROCLAMER : R�v�ler publiquement
PROCORDE : Animal voisin des vert�br�s inf�rieurs
PROCURATION : Pouvoir
PROCURER : Obtenir pour quelqu'un
PRODIGUANT : Donnant g�n�reusement
PRODUCTIBILITE : Capacit� � cr�er
PRODUIRE : Cr�er
PROEMINENCE : Relief
PROFANATRICE : Qui ne respecte pas le caract�re sacr�
PROFERENT : Prononcent
PROFESSER : D�clarer
PROFILAGE : Forme de carrosserie
PROFILE : Produit m�tallurgique de grande longueur
PROFITEROLE : Petit chou
PROFONDEUR : Une des trois dimensions d'un solide
PROFUSION : Abondance
PROGRAMMATEUR : Organe d'automatisation
PROGRESSE : Avance
PROGRESSIVE : Forme verbale
PROHIBE : D�fendu
PROHIBITIF : Trop �lev�
PROJECTILE : Objet jet�
PROJETANT : Jetant avec force
PROLACTINE : Hormone hypophysaire
PROLETAIRE : Salarier aux revenus modestes
PROLIFERER : Se multiplier
PROLIGERE : Qui porte un germe
PROLOGUE : Introduction
PROLONGE : Longue corde munie d'un crochet
PROMENADE : Lieu am�nag� pour la marche
PROMENER : Conduire � l'ext�rieur
PROMETHEUM : M�tal du groupe des terres rares
PROMETTRE : S'engager
PROMISE : Fianc�e
PROMOTEUR : Celui qui donne l'impulsion
PROMOUVOIR : Donner l'impulsion
PROMPT : Rapide
PROMU : Elev�
PROMULGUER : Rendre applicable
PRONE : Vante
PRONOMINAL : Qui se conjugue avec deux pronoms de la m�me personne
PRONONCE : Accentu�
PROPAGATEUR : Diffuseur
PROPAGE : Diffuse
PROPERGOL : Corps produisant du gaz chaud
PROPHETIE : Pr�diction
PROPHYLACTIQUE : Qui emp�che le propagation
PROPOLIS : Substance r�sineuse r�colt�e par les abeilles
PROPORTIONNEL : En rapport
PROPOS : Paroles
PROPOSITIONNEL : Qui concerne un choix
PROPRE : Net
PROPRIOCEPTION : Sensibilit�
PROPYLEE : Entr�e monumentale d'une citadelle
PROROGATION : Report
PROSAIQUEMENT : Vulgairement
PROSCRIRE : Rejeter
PROSELYTE : Pa�en converti au juda�sme
PROSODIE : Ensemble des ph�nom�nes d'intonation d'une langue
PROSPECTEUR : Enqu�teur
PROSPERER : R�ussir
PROSTERNER : Se courber (se)
PROTACTINIUM : M�tal radioactif
PROTECTEUR : Garde du corps
PROTECTORAT : Situation d'un �tat plac� sous l'autorit� d'un autre
PROTEGE : Met � l'abri
PROTEGENT : Mettent � l'abri
PROTESTATAIRE : Opposant
PROTHALLE : Petite lame verte r�sultant de la germination des spores de la foug�re
PROTIDE : Substance organique azot� englobant les acides amin�s
PROTOCOLE : Formulaire pour dresser les actes publics
PROTOHISTOIRE : P�riode entre la pr�histoire et l'histoire
PROTOPHYTE : V�g�tal unicellulaire
PROTOTYPE : Premier exemplaire
PROTOXYDE : Oxyde le moins oxyg�n� d'un �l�ment
PROTUBERANTE : En saillie
PROUESSE : Performance
PROVENDE : M�lange de grains et de fourrages hach�s
PROVERBIALES : Exemplaires
PROVIGNER : Marcotter la vigne
PROVINCE : Division territoriale
PROVINCIALISME : Locution particuli�re � une contr�e
PROVISIONNELLE : En attendant le r�glement d�finitif
PROVISOIRE : Qui ne dure pas
PROXIMITE : Alentour
PRUDENTE : Avis�e
PRUNELLE : Liqueur
PRURIGINEUSE : Qui cause la d�mangeaison
PSALMODIER : D�biter d'une mani�re monotone
PSAUME : Chant liturgique
PSCHENT : Coiffure des pharaons
PSI : Lettre de l'alphabet grec
PSITTACISME : R�p�tition
PSYCHE : Grand miroir
PSYCHOGENE : Dont l'origine est dans le fonctionnement mental
PSYCHOLOGISME : R�duction de la th�orie de la connaissance
PSYCHOMETRIE : Tests
PSYCHOPATHIE : Trouble de la personnalit�
PSYCHROMETRE : Appareil de mesure de l'�tat hygrom�trique de l'air
PT : Platine
PTOSE : Chute des organes
PU : Plutonium
PUANTEUR : Mauvaise odeur
PUBLIC : Tout le monde
PUBLICATION : Ouvrage imprim�
PUCCINIE : Champignon microscopique
PUCERON : Petit insecte
PUDDLAGE : Ancien proc�d� m�tallurgique
PUDIBOND : Qui pousse la pudeur � l'exc�s
PUER : Exhaler une mauvaise odeur
PUERIL : Enfantin
PUGILAT : Combat
PUISARD : Egout vertical
PUISER : Prendre � la r�serve
PULL : Tricot
PULLULEMENT : Grouillement
PULMONE : Mollusque gastropode
PULSAR : Source de rayonnement radio�lectrique
PULSATION : Battement
PULSION : Force
PULVERISER : D�truire compl�tement
PULVERULENT : A l'�tat de poudre
PUNAISE : Insecte de l'ordre des h�t�ropt�res
PUNCH : Boisson � base de rhum
PUNCTUM : Point en de�� duquel la vision est indistincte
PUNK : Mouvement caract�ris� par l'agressivit� et la d�rision
PUNTARELLE : Fragment de corail
PUPITRE : Petit meuble
PUR : Sans d�faut
PURE : Sans d�faut
PUREE : Pr�paration culinaire
PURGEUR : Appareil permettant d'�liminer un fluide d'un tuyau
PURIFIER : Assainir
PURIN : Engrais
PUSILLANIMITE : Manque de courage
PUTIET : Merisier � grappes
PUTOIS : Mammif�re carnassier des bois
PUTRESCIBLE : Susceptible de pourrir
PUTTO : B�b� nu
PUY : Montagne volcanique
PV : Amende
PYCNOMETRE : Petit flacon pour mesurer la densit�
PYLONE : Support de c�bles
PYRAMIDE : Monument fun�raire
PYRIDOXINE : Vitamine
PYROGRAPHE : Appareil d'�criture � chaud
PYROLIGNEUX : Obtenu par distillation du bois
PYROMETRIE : Mesure de temp�rature
PYROPHYTE : Plante r�sistant aux incendies
PYRRHONISME : Scepticisme
PYTHIE : Proph�tesse rendant des oracles au nom d'Apollon � Delphes
PYTHON : Serpent
Q : Pas de d�finition
QUADRAGESIMALE : Qui appartient au car�me
QUADRATURE : Phase du premier ou dernier quartier de la Lune
QUADRIENNAUX : Qui reviennent tous les quatre ans
QUADRILATERE : Polygone
QUADRILLE : Ancienne danse
QUADRIPARTITE : A quatre
QUADRIQUE : Repr�sent� par une �quation du second degr�
QUALIFICATION : Attribution d'un titre
QUALIFIE : Comp�tent
QUAND : Adverbe de temps
QUANTIFIE : Compte
QUANTIFIER : Compter
QUARANTAINE : Herbe ornementale voisine de la girofl�e
QUARTANNIER : Sanglier
QUARTE : Deux pintes
QUARTETTE : Groupe de musiciens
QUARTIER : Portion
QUARTZ : Silice cristallis�
QUASI : Presque
QUATERNE : Quatre num�ros d'une m�me ligne horizontale
QUATRAIN : Strophe
QUATRILLION : Dix puissance vingt-quatre
QUECHUA : Langue indienne du P�rou et de la Bolivie
QUELQUE : Un petit nombre
QUEMANDEUSE : Qui sollicite
QUENOTTE : Dent
QUERELLE : Dispute
QUERELLER : Se disputer (se)
QUESTION : Interrogation
QUETE : Inclinaison d'un m�t sur l'arri�re
QUETER : Rechercher
QUICONQUE : Toute personne
QUIETUDE : Tranquillit�
QUINCAILLE : Ustensile m�tallique pour usage domestique
QUINOA : Plante cultiv�e en Am�rique centrale pour ses graines alimentaires
QUINTAINE : Mannequin
QUINTEFEUILLE : Rosace
QUINTETTE : Morceau de musique
QUINTUPLANT : Multipliant
QUINZAINE : Deux semaines
QUIRATAIRE : Propri�taire d'une part de navire
QUITTANT : Laissant
QUOI : Pronom relatif
QUOTA : Contingent
QUOTIDIEN : Journal
R : Pas de d�finition
RA : Radium
RABACHEUR : Qui dit toujours la m�me chose
RABAISSER : D�pr�cier
RABANE : Tissus de fibre de raphia
RABATTRE : Consentir un rabais
RABBIN : Docteur de la Loi juive
RABIBOCHER : Raccommoder
RABLER : Eliminer les impuret�s
RABONNIR : Devenir meilleur
RABOTER : Aplanir
RABOUGRIR : Se recroqueviller (se)
RABOUTER : Assembler
RABROUENT : Repoussent
RACAILLE : Rebut
RACCOMMODER : R�parer
RACCOMPAGNER : Reconduire
RACCORDER : Relier
RACCROCHER : Terminer la communication
RACEE : El�gante
RACHETER : Acqu�rir � nouveau
RACISME : S�gr�gation
RACKET : Extorsion
RACLURE : D�chet
RACOLEUSE : Attirante
RACONTER : Rapporter
RACOON : Raton laveur
RADAR : Appareil de d�tection
RADIAL : En rayon
RADIAN : Unit� de mesure d'angle
RADICALISER : Rendre intransigeant
RADIER : Rayer
RADIEUSE : Lumineuse
RADINERIE : Avarice
RADIOALIGNEMENT : Dispositif de guidage
RADIOBALISE : Dispositif de guidage
RADIODIAGNOSTIC : Application des rayons X
RADIOGONIOMETRE : Appareil de navigation
RADIOGRAPHIE : Technique photographique
RADIOLAIRE : Protozoaire des mers chaudes
RADIOLARITE : Roche s�dimentaire
RADIONAVIGATION : Gonio
RADIOPHONIE : Syst�me de transmission des sons
RADIOSONDE : D�tecteur
RADIOTELESCOPE : Longue-vue
RADIOTHERAPIE : Traitement par des radiations
RADON : El�ment gazeux radioactif
RADOTEUSE : Qui r�p�te toujours la m�me chose
RADOUCIR : Rendre plus conciliant
RAFFERMIR : Consolider
RAFFINEE : Qui a du go�t
RAFFINEMENT : Ce qui marque une grande recherche
RAFFUTER : Terme de rugby
RAFISTOLER : Raccommoder
RAFLER : Tout emporter
RAFRAICHISSANT : Qui calme la soif
RAGEUSE : Sujet � des col�res
RAGOT : Bavardage
RAGREER : Racler
RAGUANT : Usant
RAI : Rayon
RAID : Op�ration militaire
RAIDE : Tendu
RAIDES : Tendus
RAIDISSEUR : Renfort
RAIE : Poisson
RAIL : Guide
RAILLER : Ridiculiser
RAILLERIE : Plaisanterie
RAILS : Guides
RAINETTE : Grenouille
RAINURES : Entaille
RAIS : Chef d'�tat arabe
RAISONNABLE : Conforme au bon sens
RAISONNER : R�fl�chir
RAJA : Prince
RAJEUNIR : Donner de la fra�cheur
RAJUSTER : Remettre en place
RALENTI : Artifice de prise de vues
RALER : Protester
RALLIER : Rejoindre
RALLIFORME : Oiseau �chassier
RAMADAN : Neuvi�me mois du calendrier islamique
RAMAGE : Chant
RAMASSER : R�colter
RAMASSOIRE : Petite pelle
RAME : Branche
RAMEAU : Petite branche
RAMENDER : Raccommoder
RAMENER : Op�ration de dressage
RAMEQUIN : R�cipient
RAMIE : Plante de la famille des urticac�es
RAMIFICATION : Division
RAMOLLIE : Qui manifeste un certain degr� de d�t�rioration intellectuelle
RAMPE : Pente
RAMPONNEAU : Coup violent
RANATRE : Insecte des eaux stagnantes
RANCH : Ferme
RANCIO : Vin de liqueur
RANCON : Prix de la libert�
RANCONNER : Exiger de force ce qui n'est pas d�
RANDOMISER : Introduire un �l�ment de hasard
RANGER : Mettre en ordre
RANIME : R�veille
RANIMER : R�veiller
RAPACE : Vorace
RAPATRIER : Ramener dans son pays
RAPER : User
RAPETISSER : R�duire
RAPIDE : Train
RAPIECER : Raccommoder
RAPINE : Vol
RAPPELER : Faire revenir
RAPPOINTIS : Pointe pour retenir le pl�tre
RAPPORTER : Ramener
RAQUAIENT : Payaient
RAQUER : Payer
RAREFIER : Diminuer la pression
RAREMENT : Pas souvent
RAS : Chef �thiopien
RASADE : Verre plein
RASIBUS : Tout pr�s
RASSASIER : Satisfaire les d�sirs
RASSEOIR : Replacer
RASSERENER : Rendre le calme
RASSURER : Remettre en confiance
RAT : Mammif�re rongeur
RATATINEE : Rapetiss�e par l'�ge
RATE : Coup pour rien
RATEAU : Outil agricole
RATEL : Mammif�re carnassier de l'Afrique et de l'Inde
RATER : Echouer
RATERA : Echouera
RATIER : Chien
RATINE : Etoffe de laine
RATIOCINER : Raisonner de fa�on trop subtile
RATIONALISER : Justifier ce qui rel�ve de motivations inconscientes
RATIONNELLE : Qui n'a rien d'empirique
RATIONNER : R�duire la consommation
RATISSER : Fouiller m�thodiquement
RATON : Mammif�re carnassier d'Am�rique
RATURER : Rayer
RAUCHEUR : Ouvrier mineur
RAVAGER : D�vaster
RAVALEUR : Sp�cialiste dans les travaux de fa�ade
RAVAUDER : Raccommoder
RAVIERE : Petit plat oblong
RAVINER : Creuser
RAVINES : Foss�s
RAVISER : Changer d'avis (se)
RAVITAILLER : Faire le plein
RAY : Culture sur br�lis
RAYER : Barrer
RAYERE : Ouverture dans un mur
RAYONNAGE : Etag�re
RAZ : Courant
RAZZIA : Pillage
RB : Rubidium
RD : Rad
RE : Note
REA : Roue
REACCOUTUMER : R�adapter
REAFFIRMER : Redire
REAL : Ancienne monnaie d'Espagne
REALESAGE : R�paration d'un cylindre
REALESER : R�parer un cylindre
REANIME : R�veille
REAPPARAITRE : Revenir
REAPPARUS : Revenus
REAS : Roues
REASSURANCE : Couverture
REBAPTISER : Changer le nom
REBATIR : Reconstruire
REBATTISSENT : Reconstruisent
REBATTRE : R�p�ter
REBELLANT : Refusant d'ob�ir (se)
REBELLER : Refuser d'ob�ir (se)
REBIQUE : Se dresse
REBOISER : Planter des arbres
REBONDIES : Gonfl�es par l'embonpoint
REBONDISSEMENT : Cons�quence impr�vue
REBOT : Pelote basque
REBOUCHANT : Refermant
REBUT : D�chet
REBUTER : D�courager
RECACHETE : Referme
RECALCITRANT : Rebelle
RECALER : Synchroniser
RECEDER : Rendre
RECELER : Contenir
RECEMMENT : Depuis peu
RECENSER : Compter
RECEPER : Couper pr�s du sol
RECEPTIF : Susceptible de recevoir des impressions
RECEPTIONNE : Prendre livraison
RECESSION : Crise �conomique
RECEVABLE : Admissible
RECEVEUR : Employer qui per�oit la recette
RECHAMPIR : Faire ressortir un ornement
RECHAPER : Reconstituer la bande de roulement
RECHARGER : Rajouter du m�tal
RECHAUFFE : Trop connu
RECHERCHE : Enqu�te
RECHIGNER : T�moigner de la mauvaise humeur
RECIDIVE : Rechute
RECIF : Rocher
RECIPROQUE : Qui a lieu entre deux personnes
RECITATION : Texte � apprendre
RECLAME : Publicit�
RECLUSION : Emprisonnement
RECLUSIONNAIRE : Prisonnier
RECOIN : Cachette
RECOLLAGE : R�paration
RECOLTE : Ramassage
RECOMMANDATION : Conseil
RECOMMANDER : Conseiller
RECOMPTANT : V�rifiant
RECONCILIER : Mettre d'accord
RECONFORT : Consolation
RECONFORTER : Redonner du courage
RECONNAITRE : Admettre
RECONNU : C�l�bre
RECOPIER : Mettre au propre
RECORD : Exploit sportif
RECOUDRE : Raccommoder
RECOURBER : Tordre
RECOURIR : S'adresser � quelqu'un pour obtenir de l'aide
RECOUVREMENT : Perception
RECREATIONS : Interruptions
RECREATIVE : Qui divertit
RECREER : Reconstituer
RECRIER : Pousser une exclamation (se)
RECRIMINER : Critiquer
RECROQUEVILLE : Ramass�
RECRUDESCENCE : Augmentation
RECRUE : Nouveau membre
RECRUTER : Engager
RECTANGULAIRE : Presque carr�
RECTEUR : Haut fonctionnaire de l'�ducation nationale
RECTIFIER : Rendre droit
RECTIFIEUSE : Machine-outil
RECTO : Premi�re page d'une feuille
RECUEIL : R�union de divers actes
RECUEILLIR : Obtenir
RECUES : Obtenues
RECUIRE : Am�liorer les qualit�s d'un m�tal
RECULE : Isol�
RECULEE : Isol�e
RECUPERATEUR : Ferrailleur
RECURER : Nettoyer
RECUSATION : Rejet de l'autorit�
REDACTION : Mani�re de r�diger
REDAN : Ornement
REDEMARRER : Se remettre en route
REDEMPTRICE : Qui rach�te
REDESCENDRE : Retomber
REDIGER : Ecrire
REDIRE : R�p�ter
REDITE : R�p�tition inutile
REDONDANT : De trop
REDONNER : Rendre
REDOUBLER : Recommencer
REDOUTE : Petit ouvrage de fortification isol�
REDRESSER : D�tordre
REDUCTIBLE : Non premier
REDUIRE : Diminuer
REDUPLICATION : R�p�tition
REDUVE : Punaise
REEDIFIER : Reb�tir
REEL : Qui existe
REESSAYERIEZ : Tenteriez � nouveau
REEVALUATION : Augmentation du cours
REEXPEDIER : Renvoyer
REFAIRE : Recommencer
REFEND : Rainure
REFERE : Proc�dure d'urgence
REFERENCE : Recommandation
REFERENTIEL : Syst�me de coordonn�es
REFILER : Vendre
REFLECHIE : Pond�r�e
REFLET : Image
REFLEXE : R�action
REFLUX : Retour en arri�re
REFONDRE : R�nover
REFONTE : R�novation
REFORMAGE : Proc�d� de raffinage
REFORME : Changement
REFOULER : Repousser
REFRACTION : Changement de direction
REFRAIN : Rengaine
REFRIGERANT : D'un abord glacial
REFRIGERES : froids
REFROIDIR : Tuer
REFUGE : Asile
REFUSER : S'arr�ter devant un obstacle
REG : Vaste espace caillouteux
REGAGNER : Rejoindre
REGAL : Grand plaisir
REGARDANTE : Avare
REGATE : Course
REGENERATION : Reconstitution naturelle
REGENT : C�l�bre diamant
REGGAE : Style musical
REGIMBER : R�sister
REGIMENT : Unit� militaire
REGLABLE : Ajustable
REGLE : Loi
REGLEMENTER : Soumettre � une loi
REGNER : Gouverner
REGORGER : Avoir en abondance
REGRESSER : Reculer
REGRET : Repentir
REGROS : Ecorce de ch�ne
REGROUPER : Rassembler
REGULARISER : Rendre conforme � la loi
REGULE : Alliage antifriction
REHABILITER : Faire recouvrer l'estime d'autrui
REHAUSSER : Faire valoir
REIFICATION : Transformation en chose
REIN : Partie inf�rieure ou centrale de la mont� d'une vo�te
REINSERER : R�introduire dans un groupe social
REITERE : R�p�te
REJAILLIR : Atteindre en retour
REJETER : Refuser
REJOINDRE : R�unir des parties s�par�es
REJOINTOIEMENT : Action de refaire les joints
REJOUIE : Contente
RELACHEMENT : Ralentissement de l'activit�
RELANCE : Nouvel enjeu
RELATER : Raconter
RELATIVISATION : Action de faire perdre � quelque chose son caract�re absolu
RELAXER : Lib�rer
RELAYER : Retransmettre
RELENT : Mauvaise odeur
RELEVER : Epicer
RELIGIEUSE : Membre d'un ordre
RELIGIEUX : Membre d'un ordre
RELIQUE : Vieil objet
RELIURE : Couverture
RELUIRE : Briller
RELUQUER : Regarder avec convoitise
REMAILLER : R�parer un filet
REMAKE : Nouvelle version
REMANENCE : Persistance
REMANIER : Changer la composition
REMARQUABLEMENT : De fa�on extraordinaire
REMBALLER : Remettre dans sa bo�te
REMBARQUER : Revenir � bord
REMBARRER : Remettre � sa place
REMBLAYER : Combler
REMBOITER : Remettre en place
REMBOURRER : Garnir d'une mati�re compressible
REMBOURSER : Rendre
REMEDE : M�dicament
REMEDIABLE : R�parable
REMEMBREMENT : Am�nagement
REMEMORER : Rappeler
REMETTRE : Replacer
REMILITARISER : R�installer une arm�e
REMISE : R�duction
REMISSION : Pardon
REMIZ : Oiseau passereau
REMODELER : Am�liorer l'esth�tique
REMOISE : Habitante d'une ville de la Marne
REMONTER : Aller vers la source
REMONTRANCE : R�primande
REMORQUAGE : Action de tirer
REMORQUEUR : B�timent d'assistance
REMOULAGE : Issues provenant de la mouture des semoules
REMOULEUR : Aiguiseur
REMPAILLEUR : R�parateur de chaises
REMPILER : Rengager
REMPLACANT : Int�rimaire
REMPLIR : Occuper enti�rement
REMPLOYER : R�utiliser
REMPLUMER : Reprendre des forces (se)
REMPORTER : Gagner
REMUANT : Turbulent
REMUGLE : Mauvaise odeur
REMUNERE : Pay�
RENARD : Mammif�re carnassier
RENAUDER : Se plaindre
RENCARDANT : Renseignant
RENCHERIR : Augmenter le prix
RENCOGNANT : Serrant dans un coin
RENDEMENT : Rapport total
RENDRE : Restituer
RENEGATE : Qui trahit sa patrie
RENFERMER : Comprendre
RENFLER : Rendre convexe
RENFLOUER : Fournir des fonds pour r�tablir une situation financi�re
RENFONCEMENT : Partie en retrait
RENFORCEMENT : Accroissement de l'intensit� du noir
RENFROGNER : Manifester son m�contentement (se)
RENGAINE : Chanson
RENIER : Renoncer �
RENIFLER : Flairer
RENNE : Mammif�re ruminant de la famille des cervid�s
RENOMME : C�l�bre
RENONCER : Abandonner
RENONCULE : Petite grenouille
RENOUVEAU : Retour du printemps
RENOUVELE : Change
RENOVATEUR : Qui donne une nouvelle forme
RENSEIGNE : Donne des indications
RENTAMER : Recommencer
RENTE : Revenu annuel
RENTRAYER : R�parer une tapisserie � l'aiguille
RENTREE : Fin des vacances
RENVERSE : Sur le dos
RENVIDE : Enroule l'aiguill�e sur les bobines
RENVOYER : R�fl�chir
REORCHESTRATION : Nouvelle adaptation
REORIENTER : Changer de direction
REPAITRE : Rassasier
REPANDU : Courant
REPARER : Faire dispara�tre les traces du moule
REPARTIE : R�ponse
REPARTITION : Distribution
REPASSER : D�friper
REPENTIR : Regret
REPERCUTANT : R�fl�chissant
REPERE : Marque
REPERTORIER : Classer
REPETER : Redire
REPIQUAGE : Copie
REPLAT : Adoucissement de la pente
REPLETIF : Qui sert � remplir
REPLI : Retraite
REPLIQUER : R�pondre
REPONDANT : Caution
REPORTER : Journaliste
REPOSER : Remettre en place
REPOUSSANT : Tr�s laid
REPOUSSER : Faire reculer
REPRENDRE : Retrouver son sang froid (se)
REPRESENTANT : D�l�gu�
REPRESENTER : Dessiner
REPRIMANDE : Reproche
REPRISER : Raccommoder
REPROBATION : Jugement
REPRODUCTEUR : Gabarit
REPROUVEE : Damn�e
REPTILE : Animal rampant
REPUBLICAIN : Oiseau passereau africain
REPUDIER : Rejeter
REPUGNANCE : Aversion
REPUTE : Connu
REQUERANTE : Qui demande justice
REQUIEMS : Pri�re
REQUINQUER : Redonner des forces
REQUIS : N�cessaire
REQUISITOIRE : Reproches
RESCINDABLE : Cassable
RESCISION : Annulation
RESERVE : Prudence
RESERVOIR : R�cipient
RESIDER : Demeurer
RESIDU : Reste
RESIGNE : Qui supporte une chose p�nible
RESILIATION : Annulation
RESIPISCENCE : Reconnaissance de sa faute
RESOLU : D�cid�
RESOLUMENT : Sans h�sitation
RESOLUTION : D�cision
RESONANCE : Echo
RESORBER : Faire dispara�tre peu � peu
RESPLENDIR : Briller
RESPONSABLE : Personne qui a la capacit� de prendre des d�cisions
RESQUILLER : Entrer sans payer
RESSASSER : R�p�ter
RESSEMBLER : Avoir des points communs
RESSERRER : Rendre plus �troit
RESSERVI : R�chauffer
RESSORTISSANTE : Personne qui rel�ve d'un �tat dont elle n'a pas la nationalit�
RESSUSCITER : Ramener � la vie
RESTAURER : R�parer
RESTE : R�sidu
RESTITUER : Rendre
RESTOROUTE : Restaurant
RESTRICTION : Limitation
RESULTAT : R�ussite ou �chec
RESULTER : S'ensuivre
RETABLIR : Remettre en �tat
RETAILLE : Recoupe
RETAPAGE : Action de restaurer
RETARDANT : Retenant
RETENDOIR : Outil d'accordeur
RETENIR : Freiner
RETENTIR : Avoir des r�percussions
RETERCER : Donner un nouveau labour � la vigne
RETICULAIRE : Qui a la forme d'un r�seau
RETIF : Difficile � conduire
RETINE : Membrane sensible
RETIRATION : Impression du verso
RETIRER : Oter
RETIVE : Difficile � conduire
RETORS : Rus�
RETOUCHEUR : Arrangeur
RETOURNEMENT : Changement de situation
RETRACTABILITE : Aptitude � changer de dimensions
RETRACTER : Revenir sur ce qu'on a dit (se)
RETRAIT : Diminution de volume
RETRANCHER : Oter
RETRANSCRIRE : Traduire
RETRANSMETTRE : Diffuser
RETRAYES : Personne contre laquelle s'exerce le retrait successoral
RETREINDRE : Marteler
RETREMPE : Traitement thermique
RETROACTION : Contre-r�action
RETROGRADER : Changer de vitesse
RETROUSSE : Rel�ve
RETROUVER : Mettre la main dessus
RETS : Filet
REUNION : Rassemblement
REUSSIR : Parvenir
REUSSITE : Succ�s
REVALOIR : Rendre la pareille
REVALORISER : Augmenter le prix
REVANCHE : Seconde partie
REVASSER : Somnoler
REVECHE : Bourru
REVEE : Id�ale
REVEILLER : Faire rena�tre
REVEILLON : F�te
REVELER : D�voiler
REVENDICATION : R�clamation
REVENDIQUER : R�clamer son bien
REVENIR : Se pr�senter � l'esprit
REVERBERER : R�fl�chir
REVERCHER : Boucher les trous
REVERDOIR : R�servoir � mo�ts
REVERENCE : Respect profond
REVERER : Honorer
REVERRONS : Retrouverons
REVERS : Dos
REVERSI : Jeu de cartes
REVETIR : Mettre sur soi
REVIF : Entre la morte-eau et la vive-eau
REVIGORANT : Redonnant des forces
REVIREMENT : Changement
REVISION : Contr�le
REVITALISER : Donner une force nouvelle
REVOICI : Pr�position
REVOIR : Revenir dans un lieu
REVOLTANT : Qui indigne
REVOLTE : Soul�vement
REVOLUE : Qui n'existe plus
REVOLUTION : Changement brusque et violent
REVOQUER : Oter le pouvoir
REVUISTE : Auteur
REVULSION : Irritation locale
RF : Radiofr�quence
RH : Rhodium
RHEOMETRE : Instrument de jaugeage pour les fluides
RHINOCEROS : Mammif�re p�rissodactyle des r�gions chaudes
RHIZOME : Tige souterraine
RHODAMINE : Mati�re colorante
RHODOID : Mati�re thermoplastique
RHOMBENCEPHALE : Structure nerveuse de l'embryon
RHOMBOIDAL : En forme de losange
RHOVYL : Fibre synth�tique
RHUMATISME : Maladie des articulation
RHUMB : Onze degr�s et quinze minutes
RIA : Partie aval d'une vall�e
RIAIS : Etais gai
RIBAUD : D�bauch�
RIBOFLAVINE : Vitamine
RICANER : Rire sottement
RICHARD : Personne tr�s riche
RICHESSE : Abondance
RICIN : Plante Euphorbiac�e
RICTUS : Contraction
RIDE : Ondulation
RIDICULE : Qui incite � la moquerie
RIEL : Unit� mon�taire du Cambodge
RIEN : Chose sans importance
RIEUSE : Sorte de mouette
RIFIFI : Bagarre
RIFLE : Carabine
RIGAUDON : Danse � deux temps
RIGIDE : Raide
RIGOLO : Dr�le
RIGOUREUSE : P�nible
RIMAILLEUR : Mauvais po�te
RIMMEL : Fard
RINCEAU : Ornements
RINCER : Nettoyer
RINGARDAGE : Brassage du combustible
RIPAILLE : Exc�s
RIPE : Outil de tailleur de pierre
RIPOSTER : R�pondre
RIPUAIRE : Se dit des anciens peuples germaniques des bords du Rhin
RIS : R�duction de surface
RISEE : Moquerie collective
RISQUE : Danger
RISS : La troisi�me des grandes glaciations de l'�re quaternaire
RISTOURNE : R�duction
RITE : C�r�monial
RITES : C�r�monials
RITUALISME : Tendance � exag�rer l'importance des c�r�monies du culte
RIVAL : Concurrent
RIVALITE : Concurrence
RIVETAGE : Op�ration d'assemblage
RIVETEUSE : Machine � assembler
RIVOIR : Marteau
RIZ : Graminac�e cultiv� dans les terrains humides et chauds
RN : Radon
ROB : Suc �pur� d'un fruit cuit, �paissi jusqu'� consistance de miel
ROBIN : Magistrat
ROBOT : Appareil automatique
ROBUSTESSE : Solidit�
ROCAILLEUR : Cimentier sp�cialis�
ROCHAGE : D�gagement de gaz
ROCHE : Mat�riau constitutif de l'�corce terrestre
ROCHER : Petit g�teau
ROCOU : Mati�re tinctoriale rouge
ROCOUER : Teindre
RODE : Use
RODEUR : Vagabond
ROGATIONS : Pri�re
ROGNE : Mauvaise humeur
ROGNURE : D�chet
ROGUE : App�t
ROITELET : Petit oiseau passereau insectivore
ROLLIER : Oiseau � plumage bleut�
ROMAN : Oeuvre d'imagination
ROMANCE : Chanson
ROMANEE : Vin rouge de Bourgogne
ROMANTISME : Mouvement intellectuel et artistique
ROMPRE : Briser
RONCE : Rosac�e �pineuse
RONCHONNER : Grogner
RONCHONNEUR : M�content
RONDACHE : Bouclier
RONDEMENT : Promptement
RONDOUILLARDE : Grassouillette
RONEO : Machine servant � reproduire un texte ou un dessin
RONFLEMENT : Sonorit� sourde et prolong�e
RONGER : Grignoter
ROOKERIE : Rassemblement de manchots
ROQUEFORT : Fromage
RORQUAL : Bal�nopt�re
ROSACE : Ornement circulaire
ROSALBIN : Esp�ce de cacato�s
ROSE : Fleur
ROSEAUX : Plantes vivant au bord des eaux
ROSETTE : Noeud de ruban
ROSIER : Arbrisseau �pineux
ROSSARD : Homme pr�t � faire des mauvais tours
ROSSER : Battre violemment
ROSSIGNOL : Oiseau passereau
ROSTRE : Eperon
ROT : Maladie cryptogamique des plantes
ROTATION : Mouvement autour d'un axe
ROTENGLE : Gardon aux yeux et aux nageoires rouges
ROTIN : Tige utilis�e pour faire des cannes
ROTISSOIRE : Sorte de four
ROTULE : Articulation
ROUAGES : Pi�ces d'une m�canique
ROUBLARD : Rus�
ROUCOULER : Tenir des propos tendres
ROUE : Supplice
ROUET : Machine � filer le chanvre et le lin
ROUGEATRE : Qui tire sur le rouge
ROUGEOIEMENT : Lueurs
ROUGIR : Eprouver de la honte
ROUILLE : Oxydation
ROUIR : Isoler les fibres textiles des tiges
ROULAGE : Transport du charbon dans une mine
ROULER : Duper
ROULIS : Mouvement d'oscillation
ROULOTTE : Caravane
ROUPILLER : Dormir
ROUSCAILLE : Proteste
ROUSPETE : Proteste
ROUSSEROLLE : Passereau voisin des fauvettes
ROUSSIR : Br�ler
ROUTARD : Jeune voyageur
ROUTINE : Habitude
ROUVIEUX : Sorte de gale
ROUVRE : Ch�ne
ROUX : Pr�paration faite avec de la farine roussie dans le beurre
ROYALE : Petite touffe de barbe sous la l�vre inf�rieure
ROYAUTE : R�gime monarchique
RU : Petit ruisseau
RUBAN : Bande de tissus
RUBEOLE : Maladie virale �ruptive
RUBIDIUM : M�tal alcalin
RUBIS : Pierre pr�cieuse
RUBRIQUE : Article
RUDENTURE : Ornement
RUDESSE : Duret�
RUDOYANT : Traitant durement
RUE : Voie publique
RUEE : Mouvement rapide d'un grand nombre de personnes
RUEES : Mouvements rapides d'un grand nombre de personnes
RUER : Se pr�cipiter en masse
RUES : Voie publique
RUGIR : Pousser des cris de fureur
RUILER : Raccorder avec du pl�tre
RUINER : D�truire
RUISSEAU : Petit cours d'eau
RUISSELET : Petit cours d'eau
RUMEX : Oseille
RUMINER : Rem�cher
RUNE : Caract�re des plus anciens alphabets germaniques et scandinaves
RUOLZ : Alliage utilis� en orf�vrerie
RUPIAH : Unit� mon�taire principale de l'Indon�sie
RUPIN : Luxueux
RURAL : Campagnard
RUSE : Astuce
RUSH : Afflux de foule
RUSSULE : Champignon
RUSTIQUE : Hache de tailleur de pierre
RUTABAGA : Chou-navet
RUTHENE : Eglise d�pendant de l'ancienne m�tropole de Kiev
RUZ : Vall�e creus�e sur le flanc d'un anticlinal
RYTHME : Cadence
S : Pas de d�finition
SA : Adjectif possessif
SABAYON : Cr�me
SABBAT : Repos
SABLAGE : D�capage
SABLER : D�caper
SABLON : Sable � grains fins
SABORDAGE : Destruction volontaire
SABOTAGE : D�t�rioration volontaire
SABRE : Arme blanche
SAC : Pillage
SACCADE : Secousse
SACCAGER : Mettre � sac
SACCHAROIDE : Qui a l'apparence du sucre
SACCHAROSE : Glucide du groupe des osides
SACCULE : Petite cavit� de l'oreille interne
SACHEM : Membre du conseil de la nation chez certains Am�rindiens
SACHET : Pochette
SACRE : Cons�cration
SACRIFICE : Renoncement
SACRISTAIN : Employ� charg� de l'entretien d'une �glise
SACS : Pillages
SADDUCEEN : Membre d'une secte juive rivale des pharisiens
SADUCEEN : Membre d'une secte juive rivale des pharisiens
SAFRAN : Surface du gouvernail
SAGACE : Critique
SAGESSE : Conduite r�fl�chie
SAGITTAL : En forme de fl�che
SAGOUIN : Petit singe d'Am�rique du Sud
SAI : Petit singe am�ricain
SAIE : Manteau court en laine
SAILLIE : Partie qui avance
SAINBOIS : Garou
SAINT : Souverainement parfait
SAISON : P�riode de l'ann�e
SALADE : Casque en usage du XV �me au XVII �me si�cle
SALAIRE : R�mun�ration
SALAMANDRE : Amphibien urod�le de l'Europe
SALAMI : Gros saucisson sec
SALAUD : Personnage d�loyal
SALERS : Fromage
SALICACEE : Arbre aux fleurs sans p�tales
SALICAIRE : Plantes dont diverses esp�ces croissent dans les lieux humides
SALICYLIQUE : Se dit d'un acide dou� de propri�t�s antiseptiques et anti-inflammatoires
SALIFIABLE : Qui peut fournir un sel
SALIGAUD : Personne r�pugnante physiquement ou moralement
SALISSURE : Souillure
SALIVATION : S�cr�tion
SALLE : Pi�ce
SALMIS : Rago�t de pi�ces de gibier ou de volailles d�j� cuites � la broche
SALMONELLE : Bact�rie
SALOL : Antiseptique
SALONNARDE : Personne du monde
SALOON : Bar
SALOPER : Salir
SALPETRE : Nitrate de potassium
SALTATION : Technique des sauts
SALUBRE : Sain
SALURE : Teneur en sel
SALVATEUR : Sauveur
SAMARITAIN : Secouriste
SAMOA : Archipel d'Oc�anie
SAMPAN : Bateau
SANCERRE : Vin blanc
SANCTION : Cons�quence
SANDALE : Chaussure
SANDWICH : Mets de pique-nique
SANGLOTER : Pleurer
SANICULE : Plante vivace 
SANS : Pr�position
SANSKRIT : Langue sacr�e et litt�raire de la civilisation brahmanique
SANTAL : Arbuste d'Asie
SANTON : Figurine
SAPE : V�tement
SAPEUR : Soldat du g�nie
SAPIDE : Qui a de la saveur
SAPIN : Arbre r�sineux
SAPITEUR : Expert
SAPONACE : De la nature du savon
SAPONAIRE : Plante � fleurs roses
SAPONIFIER : Transformer en savon
SAPROPHAGE : Qui se nourrit de mati�res organiques en d�composition
SAQUER : Punir s�v�rement
SARCASTIQUE : Moqueur et m�chant
SARCLER : Enlever les mauvaises herbes
SARDE : Habitant d'une �le m�diterran�enne
SARDINIER : Bateau de p�che
SARIGUE : Mammif�re de la sous-classe des marsupiaux
SARONG : Jupe
SARRASIN : Bl� noir
SARRIETTE : Labiac�e aromatique
SAS : Chambre de communication
SATANISME : Culte du mal
SATELLISER : Mettre en orbite
SATINE : Demi-brillant
SATIRE : Pamphlet
SATIRIQUEMENT : Avec raillerie
SATISFAIT : Content
SATISFAITE : Contente
SATRAPE : Gouverneur d'une province dans l'empire perse
SATURER : Remplir � l'exc�s
SATURNIE : Paon de nuit
SATURNISME : Intoxication
SAUCE : Pr�paration liquide accompagnant un mets
SAUCISSONNER : Prendre un repas froid sur le pouce
SAUGRENUE : Absurde
SAUMONE : A la chair rose-orang�
SAUMURE : Pr�paration liquide tr�s sal�e
SAUNAGE : Fabrication et vente du sel
SAUPIQUET : Sorte de sauce piquante
SAUPOUDRER : Parsemer
SAUT : Chute d'eau
SAUTERNES : Vin blanc
SAUVAGE : Qui n'est pas civilis�
SAUVAGINE : Gibier d'eau
SAUVEGARDER : Prot�ger
SAUVER : Pr�server de la perte
SAVAMMENT : Adroitement
SAVARIN : G�teau
SAVART : Unit� d'intervalle musical
SAVON : Produit obtenu par l'action d'une base sur un corps gras
SAXIFRAGE : Plante qui pousse au milieu des pierres
SAYNETE : Sketch
SB : Antimoine
SC : Scandium
SCABREUSE : Dangereuse
SCALDE : Nom des anciens po�tes scandinaves
SCALP : Chevelure
SCANDALEUSE : Honteuse
SCANDER : Souligner fortement
SCANDIUM : Corps simple m�tallique
SCAPHANDRIER : Plongeur
SCAPULAIRE : Pi�ce du costume monastique
SCARIFICATEUR : Instrument chirurgical
SCAROLE : Sorte de chicor�e
SCEAU : Caract�re distinctif
SCELLANT : Fermant
SCENE : Lieu o� se passe une action
SCHEIDER : Fragmenter au marteau
SCHEMATISER : Simplifier
SCHEME : Structure d'ensemble d'un processus
SCHILLING : Unit� mon�taire principale de l'Autriche
SCHISTE : Roche s�dimentaire 
SCHLITTAGE : Transport du bois
SCHNAPS : Eau de vie
SCIE : Outil de menuisier
SCILLE : Plant bulbeuse
SCINTIGRAPHIE : Gammagraphie
SCINTILLE : Brille
SCIOTTE : Scie � main
SCIURIDE : Famille de mammif�res rongeurs de petite taille
SCLEREUSE : Epaissie
SCLEROPHYLLE : Qui a des feuilles dures
SCLEROSE : D�faut d'adaptation
SCOLAIRE : Livresque
SCOLIE : Note de grammaire ou de critique sur les auteurs anciens
SCOPOLAMINE : Alcalo�de extrait de la mandragore
SCORIE : Sous produit m�tallurgique
SCOTCH : Boisson Ecossaise
SCOTOMISATION : Action de faire dispara�tre du champ de la conscience
SCRABBLE : Jeu
SCRIBAN : Secr�taire
SCRIPT : Sc�nario
SCROFULARIACEE : Plante gamop�tale
SCRUBBER : Tour o� se fait l'�puration du gaz
SCRUTER : Examiner attentivement
SCULL : Rame en couple
SCULPTEUR : Artiste
SE : Pronom personnel
SEANCE : R�union d'une assembl�e
SEBASTE : Poisson
SEBUM : S�cr�tion grasse
SEC : Brusque
SECATEUR : Ciseaux � ressort
SECESSIONNISTE : Qui rompt l'union
SECOND : Rempla�ant d�sign�
SECONDER : Assister
SECOURISME : Sauvetage
SECOUSSE : Choc
SECRETAIRE : Meuble
SECTION : Division
SECTIONNE : Divise
SECULARISER : La�ciser des biens d'Eglise
SECULIER : Se dit du clerg� qui n'appartient pas � un ordre religieux
SEDATIF : Qui calme
SEDENTAIRE : Casanier
SEDIMENTOLOGIE : Etude de la gen�se des s�diments
SEDUCTION : Charme
SEGMENTE : Divise
SEICHE : Mollusque vivant pr�s des cotes
SEIGNEUR : Ma�tre absolu
SEISME : Secousse
SEL : Piquant
SELECTION : Choix
SELECTIONNER : Choisir
SELENITE : Habitant imaginaire de la Lune
SELENIUM : M�tallo�de dont la conductivit� augmente avec la lumi�re
SELF : Bobine
SELFS : Bobines
SELLE : Si�ge
SELON : Conform�ment �
SEMAPHORE : T�l�graphe a�rien
SEMBLER : Avoir une certaine apparence
SEMELLE : El�ment d'assise
SEMESTRIELLE : Deux fois par an
SEMILLANT : Tr�s vif et gai
SEMIOTIQUE : Th�orie des signes
SEMONCE : Avertissement
SEMPERVIVUM :  Plante de la famille de crassulac�es
SEN : Unit� mon�taire divisionnaire dans divers pays d'Extr�me-Orient
SENAT : Assembl�e politique
SENE : Nom donn� � diverses esp�ces de cassier
SENEGAL : Pays africain
SENIOR : Ag� de vingt ans ou plus
SENS : Mode de perception
SENSE : Raisonnable
SENSEE : Raisonnable
SENSEES : Raisonnables
SENSIBLE : Facilement �mu
SENTE : Petit chemin
SEP : Pi�ce d'une charrue
SEPARER : D�sunir
SEPIOLE : Petite seiche
SEPS : L�zard � pattes tr�s courtes
SEPT : Adjectif num�ral
SEPTANTE : Adjectif num�ral
SEPTENTRION : Les sept �toiles de la Petite Ourse
SEPULCRE : Tombeau
SEQUIN : Monnaie d'or
SERAIL : Palais
SERANCER : Partager les fils du lin pour pouvoir les filer
SEREINES : Calmes
SERFOUIR : Sarcler
SERGE : Tissu de laine
SERIE : Suite
SERIN : Petit oiseau des �les Canaries
SERINGUE : Petite pompe
SERMON : Remontrance longue et ennuyeuse
SERPENTEAU : Pi�ce d'artifice
SERPETTE : Outil tranchant
SERRE : Espace clos ferm� par des parois translucides
SERRISTE : Agriculteur
SERTE : Ench�ssement des pierres fines
SERVALS : Grand chat
SERVANT : Militaire affect� au service d'une arme
SERVIR : S'acquitter de certaines fonctions
SERVITUDE : Charge
SES : Adjectif possessif
SET : Terme de tennis
SEULE : Isol�e
SEVRES : Porcelaine
SEXTUOR : Composition � six parties
SEYANTE : Qui va bien
SHAMPOOING : Savon liquide
SHANTUNG : Etoffe de soie
SHERRY : Vin de X�r�s
SHINTOISME : Religion du Japon
SHUNT : D�rivation
SI : Conjonction
SIALIS : Insecte abondant pr�s des eaux
SIAMOIS : Langue tha�
SIBYLLE : Femme qui transmettait les oracles des dieux
SIC : Indique que l'on cite textuellement
SICCATIF : Qui acc�l�re le s�chage
SIDERAL : Qui concerne les astres
SIDERER : Frapper de stupeur
SIDERITE : M�t�orite
SIEGE : Chaise
SIESTE : Repos
SIFFLET : Appareil de signalisation sonore
SIGILLE : Marqu� d'un sceau
SIGMA : Lettre de l'alphabet grec
SIGNALANT : Annoncer
SIGNALE : Annonce
SIGNIFIER : Notifier
SIL : Argile
SILENCIEUSEMENT : Sans bruit
SILEX : Roche tr�s dure
SILIQUE : Fruit sec
SILLON : Rigole
SILO : R�servoir
SILOS : R�servoirs
SILVES : Recueil de pi�ces po�tiques
SIMIEN : Singe
SIMILICUIR : Toile enduite
SIMULACRE : Fausse apparence
SIMULE : Feint
SINCERE : Franc
SINCIPUT : Sommet de la t�te
SINGER : Imiter
SINGULARISER : Distinguer des autres
SINGULIER : Etrange
SINISATION : Expansion de la civilisation chinoise
SINISTRE : De mauvais augure
SINUEUX : Qui fait des d�tours
SIPHONNER : Transvaser
SIRENIEN : Mammif�re herbivore marin et fluvial � nageoires
SIROTER : D�guster
SIRTAKI : Danse
SIS : Situ�
SISAL : Agave du Mexique
SISE : Situ�e
SISES : Situ�es
SISMOGRAPHE : Enregistreur de secousses
SISMOMETRIE : Mesure des secousses
SISTRE : Instrument de musique
SITUATION : Position
SIX : Adjectif num�ral
SIXTE : Intervalle de six degr�s
SKAI : Mat�riau synth�tique
SKI : Sport de glisse
SKIPPER : Chef de bord
SLOUGHI : L�vrier d'Afrique
SMALA : Ensemble des �quipages de la maison d'un chef arabe
SMICARD : Travailleur mal pay�
SMOCKS : Fronces
SN : Etain
SOC : Partie d'une charrue
SOCIALISME : Doctrine �conomique et sociale
SOCIOMETRIE : Etude des relations interindividuelles des membres d'un m�me groupe
SOCQUE : Chaussure
SODA : Boisson
SOFFITE : Face int�rieure d�gag�e d'un linteau
SOIF : D�sir
SOIGNER : Prendre soin
SOIN : Attention
SOL : Unit� mon�taire principale du P�rou
SOLDANELLE : Genre de primulac�es � fleurs violettes
SOLDER : Acquitter une dette
SOLENNEL : Pompeux
SOLENOIDE : Electro-aimant
SOLFIER : Chanter en nommant les notes
SOLIDARITE : D�pendance mutuelle entre les hommes
SOLIFLUXION : Glissement de terrain
SOLIPEDE : Equid�
SOLITAIRE : Diamant
SOLLICITATION : Demande
SOLUBLE : Qui peut �tre r�solu
SOLUTION : D�nouement d'une difficult�
SOMMATION : Mise en demeure
SOMMEILLE : Existe � l'�tat latent
SOMNAMBULE : Promeneur de la nuit
SOMNOLENCE : Mollesse
SOMPTUEUSE : Magnifique
SONAGRAPHE : Appareil permettant d'�tudier les sons
SONDAGE : Enqu�te
SONGER : Penser
SONIE : Intensit� de la sensation sonore
SONNAILLE : Clochette
SONNET : Po�me � quatorze vers
SONOMETRE : Appareil de mesure du son
SOPHISTIQUE : Tr�s perfectionn�
SOPHORA : Arbre ornemental
SOPRANO : Voix de femme
SORBETIERE : Appareil pour pr�parer les glaces
SORCIERE : Personne en relation avec le diable
SORT : D�cision par le hasard
SOTIE : Genre dramatique m�di�val
SOTTISE : Manque d'intelligence
SOUBRESAUT : Mouvement brusque et impr�vu
SOUCHETTE : Champignon
SOUCIEUX : Inquiet
SOUDER : Unir
SOUDURE : Assemblage
SOUFFLE : Agitation de l'air
SOUFFRIR : Avoir mal
SOUILLER : Salir
SOUILLON : Personne malpropre
SOULAGER : D�barrasser d'un fardeau
SOULANTE : Fatigante
SOULARD : Ivrogne
SOULIGNER : Attirer l'attention
SOUMAINTRAIN : Fromage
SOUMISE : Dispos�e � l'ob�issance
SOUMISSION : Disposition � ob�ir
SOUPAPE : Obturateur
SOUPCON : Petite quantit�
SOUPIERE : R�cipient
SOUPIRER : D�sirer ardemment
SOUQUER : Raidir
SOURCIER : Chercheur d'eau
SOURCILLEUSE : Pointilleuse
SOURDEMENT : Secr�tement
SOURDRE : Jaillir
SOURIS : Petit mammif�re rongeur
SOURNOIS : Dissimul�
SOUTANE : V�tement port� par les eccl�siastiques
SOUTERRAIN : Cach�
SOUTIEN : Appui
SOUTIRER : Obtenir par la ruse
SOUVERAIN : Monnaie d'or d'Angleterre
SOVKHOZE : Grande ferme russe
SPADASSIN : Personne qui recherche des duels
SPALAX : Rat-taupe
SPALTER : Brosse plate
SPARTE : Alfa
SPEAKER : Pr�sident de la Chambre des communes
SPECIAL : Particulier
SPECIEUX : Sans valeur
SPECIFIER : D�terminer en d�tail
SPECTACULAIRE : Qui fait sensation
SPECTRE : Fant�me
SPECULER : Compter sur quelque chose
SPEECH : Petit discours
SPERGULE : Petite plante � feuilles en lani�res
SPHAIGNE : Mousse
SPHENODON : Hatt�ria
SPHERE : Surface dont tous les points sont � �gale distance du centre
SPHEX : Insecte voisin des gu�pes
SPHYRENE : Barracuda
SPIDER : Coffre � bagages
SPIN : Moment cin�tique propre d'une particule
SPINNAKER : Voile l�g�re
SPIRAL : Petit ressort
SPIRIFER : Branchiopode de l'�re primaire
SPIRITISME : Science occulte
SPIROMETRE : Appareil de mesure de la capacit� respiratoire
SPLENDEUR : Magnificence
SPLENIQUE : Qui concerne la rate
SPOLIER : D�poss�der par la ruse
SPONGIAIRE : Animal aquatique cr�ant un courant d'eau � travers ses nombreux orifices
SPONGILLE : Eponge d'eau douce
SPONTANE : De son plein gr�
SPORADIQUE : Qui existe �a et l�
SPOROZOAIRE : Protozoaire capable de former des spores
SPORTIVEMENT : Loyalement
SPRAY : A�rosol
SPRINTER : Coureur de vitesse
SPUMEUX : Couvert d'�cume
SQUAMIFERE : Rev�tu d'�cailles
SQUATTER : Occuper
SR : St�radian
ST : Stokes
STABILISATEUR : M�canisme destin� � amortir les oscillations
STABULATION : S�jour des animaux dans l'�table
STAFF : Mat�riaux de construction
STAGNANTE : Qui ne fait aucun progr�s
STANDARDISER : Normaliser
STAPHYLIER : Faux pistachier
STARKING : Pomme rouge
STATION : Fa�on de se tenir
STATIONNEMENT : Arr�t en un lieu
STATIQUE : Qui n'�volue pas
STATOREACTEUR : Propulseur
STATUES : Ouvrages de sculpture
STATURE : Taille
STAYER : Coureur cycliste
STEARINE : Corps gras
STEGOSAURES : Reptiles du cr�tac� d'Am�rique
STELLERIDES : Etoile de mer
STENCIL : Matrice d'impression
STENOPE : Petit trou servant d'objectif
STEPPAGE : Anomalie de la marche
STERE : Unit� de mesure de volume
STEREOSCOPE : Instrument d'optique
STERNUTATION : Eternuement
STIBINE : Sulfure naturel d'antimoine
STILTON : Fromage
STIMULE : Incite
STIPENDIER : Avoir � sa solde
STIPULATION : Clause
STOCK : Marchandises disponibles
STOCKFISCH : Poisson s�ch�
STOP : Panneau de signalisation routi�re
STOPPER : Arr�ter
STORE : Rideau
STOUT : Bi�re anglaise
STRAMOINE : Plante v�n�neuse
STRAS : Ce qui brille d'un faux �clat
STRATE : Couche
STRATEGIE : Art de diriger un ensemble de dispositions pour atteindre un but
STRATIFIER : Disposer par couches
STRATOSPHERE : Entre troposph�re et m�sosph�re
STRESS : Perturbation biologique et psychique
STRICT : Qui ne laisse aucune libert�
STRIDULANTE : Qui fait entendre un bruit aigu
STRIGE : Vampire des l�gendes orientales
STROPHE : Groupe de vers
STUDETTE : Petit appartement
STUPEFACTION : Etonnement
STUPEFIE : Etonn�
STYLE : Mani�re de faire
STYLISER : Repr�senter d'une mani�re simplifi�e
STYLITE : Ermite qui passait sa vie sur une colonne
SUAGE : Petit ourlet sur le bord d'un plat d'�tain
SUAIRE : Linceul
SUBIR : Se soumettre de gr� ou de force
SUBJUGUER : S�duire
SUBLIME : Tr�s grand
SUBODORER : Pressentir
SUBORDINATION : D�pendance
SUBREPTICEMENT : Clandestinement
SUBSIDE : Subvention
SUBSISTER : Durer
SUBSTANCE : Mati�re dont quelque chose est form�
SUBSTANTIF : Nom
SUBSTITUTION : Remplacement
SUBTERFUGE : Ruse
SUBTILISER : D�rober
SUBVENTION : Aide
SUBVENTIONNER : Accorder une aide
SUBVERSIVE : Propre � d�truire l'ordre �tabli
SUC : Se qui existe de plus substantiel en fait de doctrine
SUCCEDER : Prendre la suite
SUCCESSIFS : Qui se suivent
SUCCIN : Ambre jaune
SUCCINCT : Bref
SUCCULENT : D�licieux
SUCCURSALE : Etablissement commercial d�pendant d'un autre
SUCETTE : Bonbon
SUCRE : Aliment de saveur douce
SUCRERIE : Friandise
SUCRIER : R�cipient
SUD : Point cardinal
SUDATION : Rejet d'eau
SUEDINE : Tissu de coton
SUER : Se donner beaucoup de peine
SUFFIRE : Etre capable de fournir le n�cessaire
SUFFIXE : El�ment ajout� � la fin
SUFFOQUER : Etouffer
SUGGESTIONNER : Influencer
SUIE : Mati�re d�pos�e par la fum�e
SUIF : Graisse animale
SUINTEMENT : Ecoulement
SUITE : Continuation
SUIVANTE : Qui est apr�s
SUIVI : Qui a lieu de mani�re continue
SUIVRE : Accompagner
SULFINISATION : C�mentation au souffre
SULTAN : D�tenteur de l'autorit� dans les pays musulmans
SUPER : Carburant
SUPERETTE : Libre-service
SUPERIEURE : Personne qui dirige une communaut� religieuse
SUPERMARCHE : Libre-service
SUPERPOSER : Ajouter
SUPERTANKER : Grand navire
SUPERVISER : Contr�ler
SUPPLANTER : Prendre la place
SUPPLEER : Ajouter ce qui manque
SUPPLICIER : Faire subir la torture
SUPPORT : Soutien
SUPPOSE : Admis comme hypoth�se
SUPPOT : Complice
SUPPUTER : Evaluer indirectement
SUPRACONDUCTION : Caract�ristique �lectrique aux tr�s basses temp�ratures
SUPREME : Au dessus de tout
SUR : En qui l'on peut avoir confiance
SURABONDANT : En exc�s
SURAH : Etoffe de soie crois�e
SURALE : Du mollet
SURANNEE : P�rim�e
SURBAU : Partie fixe d'une porte sur un bateau
SURCHARGER : Accabler
SURCHOIX : Premi�re qualit�
SURCOUPER : Couper avec un atout sup�rieur
SURDOUE : Tr�s malin
SURE : En qui l'on peut avoir confiance
SURES : En qui l'on peut avoir confiance
SURETE : Qualit� de quelqu'un sur qui on peut compter
SUREVALUER : Surestimer
SUREXCITE : Exalte
SUREXPOSE : Trop clair
SURF : Sport de glisse
SURFACER : Polir
SURFAITE : Estim�e au-dessus de sa valeur
SURFAIX : Bande servant � attacher une couverture sur le dos d'un cheval
SURFIL : Surjet l�che
SURFILER : Augmenter la torsion d'un fil
SURGELER : Congeler rapidement � tr�s basse temp�rature
SURHAUSSEE : Dont la fl�che est plus grande que la moiti� de la port�e
SURIN : Couteau
SURINER : Donner un coup de couteau
SURINTENSITE : Surcharge d'un circuit �lectrique
SURJALEE : Dont la cha�ne fait un tour sur le jas
SURJETER : Coudre
SURMENE : Impose un effort excessif
SURMONTER : Vaincre
SURMONTOIR : Publicit�
SUROIT : Vent
SURPASSER : Faire mieux
SURPLACE : Immobilit�
SURPLOMBER : Faire saillie
SURPRENDRE : Etonner
SURPRISE : Etonnement
SURRECTION : Soul�vement de l'�corce terrestre
SURSATURE : Contenant du quartz
SURSAUT : Mouvement brusque
SURSEOIR : Interrompre
SURSIS : Dispense d'ex�cution
SURTOUT : Principalement
SURVEILLANT : Personne charg�e de la discipline
SURVETEMENT : V�tement de sportif
SURVIVRE : R�chapper � une catastrophe
SURVOLER : Examiner rapidement
SURVOLTER : Mettre au paroxysme de l'excitation
SUS : En plus
SUSCITER : Etre la cause
SUSNOMME : Nomm� pr�c�demment
SUSPECTER : Soup�onner
SUSPENS : Non r�solu
SUSURRER : Murmurer
SVASTIKA : Symbole religieux de l'Inde
SWAHILI : Langue bantoue parl�e au Kenya et en Tanzanie
SYBARITE : Personne qui m�ne une vie facile et voluptueuse
SYCOPHANTE : D�lateur professionnel
SYLLABE : Morceau de mot
SYLLEPSE : Figure de style
SYLPHIDES : Femme gracieuse et l�g�re
SYLVE : For�t �quatoriale dense
SYLVINITE : Engrais
SYMBOLE : Signe figuratif
SYMPATHIE : Penchant qui porte deux personnes l'une vers l'autre
SYMPHONIE : Composition musicale
SYMPTOME : Indice
SYNANTHEREE : Compos�e
SYNAPSE : R�gion de contact entre deux neurones
SYNCHRONISATION : Calage
SYNCLINAL : Dont la convexit� est tourn�e vers le bas
SYNCOPE : Perte momentan�e de la sensibilit� et du mouvement
SYNDACTYLIE : Fusion de doigts
SYNECDOQUE : Figure de style
SYNERGIE : Association
SYNOPSIS : Bref expos� du sujet
SYNTAXE : Partie de la grammaire
SYNTONIE : Accord
SYRIAQUE : Langue s�mitique
SYRPHE : Mouche
SYSTOLE : Mouvement du coeur et des art�res
T : Pas de d�finition
TA : Adjectif possessif
TABAC : Plante de la famille de solanac�es
TABASSER : Battre violemment
TABES : Syphilis nerveuse
TABLEAU : Oeuvre picturale
TABLEE : Personnes partageant un repas
TABLETIER : Artisan qui fabrique des jeux
TABOU : Interdit
TABULAIRE : Plat
TAC : Onomatop�e
TACET : Indique le silence d'une partie
TACHEOMETRIE : Technique employ�e pour lever des plans
TACHINA : Mouche noire
TACHISME : Peinture abstraite
TACHOGRAPHE : Scanner
TACITURNE : Silencieux
TACT : D�licatesse
TACTIQUE : Art de conduire un combat
TAFIA : Eau-de-vie
TAIE : Enveloppe de tissu
TAILLAGE : Usinage sp�cial
TAILLE : Action de couper
TAIRE : Cacher
TALC : Silicate naturel de magn�sium
TALOCHE : Outil de pl�trier
TALON : Extr�mit� arri�re du ski
TAMARIN : Singe de l'Am�rique de Sud
TAMBOUR : Cylindre
TAMBOURINE : Frappe � coups r�p�t�s
TAMISER : Filtrer
TAMPONNER : Heurter
TAN : Poudre d'�corce de ch�ne
TANAGRA : Figurine
TANGAGE : Mouvement longitudinal
TANGENTE : Position limite d'une s�cante � une courbe
TANGIBLE : Que l'on peut percevoir par le toucher
TANGUER : Osciller
TANIN : Substance qui rend les peaux imputrescibles
TANK : Engin blind�
TANT : Adverbe de quantit�
TANTE : Soeur de parent
TAON : Mouche suceuse de sang
TAPAGEUSEMENT : Avec beaucoup de bruit
TAPE : Bouchon
TAPETTE : Pi�ge
TAPIR : Mammif�re de l'Asie tropicale et d'Am�rique
TAPISSER : Rev�tir
TAPOTER : Donner de petits coups
TAPURE : D�faut d'une pi�ce m�tallique
TAQUINER : Contrarier pour agacer
TARABISCOTEE : Orn�e � l'exc�s
TARAMA : Pr�paration � base d'oeufs de poisson fum�s
TARAUDAGE : Ex�cution d'un filetage
TARAUDE : Tourmente moralement
TARD : Apr�s le temps fix�
TARDILLON : Dernier-n�
TARE : Poids
TARENTELLE : Danse
TARGETTE : Petit verrou
TARIR : Mettre � sec
TARMACADAM : Mat�riau destin� au rev�tement des chauss�es
TARPON : Poisson des r�gions chaudes de l'Atlantique
TARSIER : Mammif�re nocturne de Malaisie
TARTE : G�teau
TARTUFE : Hypocrite
TAS : Accumulation
TASSEAU : Pi�ce de bois
TASSETTE : Pi�ce de l'armure
TATER : Sonder
TATOU : Mammif�re d'Am�rique tropicale
TATOUAGE : Dessin
TAU : Lettre de l'alphabet grec
TAUD : Tente
TAUDS : Tentes
TAUPE : Mammif�re qui creuse des galeries
TAUPIN : Insecte col�opt�re sauteur
TAUPINIERE : Petit monceau de terre
TAUTOLOGIE : R�p�tition
TAUX : Pourcentage
TAVELER : Moucheter
TAVILLON : Planche mince
TAXER : Accuser
TAXI : Automobile
TAXINOMIE : Th�orie de la classification
TB : Terbium
TC : Techn�tium
TCHADOR : Voile
TCHEREMISSE : Langue de la r�gion de la Volga
TE : Pronom personnel
TECHNICIENNE : Sp�cialiste
TECHNIQUE : M�thode
TEE : Cheville
TEGUMENT : Enveloppe
TEIGNEUSES : M�chantes
TEINTER : Colorer
TEK : Bois
TEL : Pareil
TELEGRAPHE : Dispositif de communication
TELEPHONE : Appareil de communication
TELESCOPE : Instrument d'observation
TELL : Colline form�e par des ruines
TELLE : Pareille
TELLURIQUE : Qui concerne la Terre
TEMOIGNAGE : Marque ext�rieure
TEMPE : Partie lat�rale de la t�te
TEMPERE : Ni trop chaud ni trop froid
TEMPETUEUX : Agit�
TEMPORAIREMENT : Provisoirement
TEMPOREL : Ensemble des biens appartenant � une �glise
TEMPORISE : Diff�re
TENACE : Qui adh�re fortement
TENAILLES : Pinces
TENANCIERE : Personne qui dirige une maison de jeu
TENDER : Navire annexe
TENEBRION : Ver de farine
TENICIDE : Vermifuge
TENNIS : Sport 
TENOR : Chanteur
TENSION : Diff�rence de potentiel
TENTACULE : Appendice mobile de certains animaux
TENURE : Terre conc�d�e
TEORBE : Grand luth
TER : Trois fois
TERCET : Groupe de vers
TEREBRANTE : Qui perce
TERGIVERSER : Prendre des d�tours
TERMINER : Finir
TERMINUS : Derni�re station
TERNE : Sans �clat
TERRARIUM : Emplacement r�serv� � l'�levage des reptiles
TERRASSER : Jeter � terre avec violence
TERRE : Plan�te du syst�me solaire
TERREUR : Grande peur
TERRIER : Trou creus� par certains animaux
TERRIL : Colline pr�s d'une mine
TERRORISER : Faire tr�s peur
TES : Adjectif possessif
TEST : Essai
TESTON : Monnaie d'argent � effigie de la t�te du roi
TETARD : Larve des amphibiens
TETE : Sommet
TETRADACTYLE : Qui a quatre doigts aux pieds
TETRAGONE : Plante originaire d'Australie
TETRARQUE : Souverain vassal � l'�poque gr�co-romaine
TETRODE : Tube �lectronique
TEUTON : De l'ancienne Germanie
TEX : Unit� de mesure de masse lin�ique
TEXAN : Am�ricain
TEXTUEL : Conforme au texte
TEXTURE : Mode d'entrecroisement des fils de tissage
TH : Thorium
THALIDOMIDE : Tranquillisant
THANATOLOGIE : Etude de la mort
THAUMATURGE : Personne qui fait des miracles
THEATRALEMENT : Avec beaucoup d'effets
THEATRE : Salle de spectacles
THEBAINE : Alcalo�de rencontr� dans l'opium
THEOCRATIE : R�gime politique dans lequel le pouvoir vient de Dieu
THEOLOGAL : Qui a Dieu pour objet
THEORIE : Ambassade solennelle envoy�e par une ville
THERIDION : Araign�e � couleurs vives
THERMISTANCE : Capteur de temp�rature
THERMOMETRE : Instrument de mesure
THESAURISATION : Action de faire des �conomies
THESE : Opinion
THIAMINE : Vitamine
THON : Poisson marin
THONINE : Poisson marin
THUYA : Arbre originaire d'Asie ou d'Am�rique
THYRISTOR : Composant �lectronique
TI : Titane
TIBIA : Os
TIC : Habitude
TICS : Habitudes
TIEDE : D'une chaleur tr�s att�nu�e
TIEN : Pronom possessif
TIERCE : Soixanti�me partie d'une seconde
TIGRE : Mammif�re carnassier
TILLAC : Pont sup�rieur
TIMBRE : Vignette adh�sive
TIMIDITE : Embarras
TIMORE : Craintif
TINTOUIN : Embarras
TIQUE : Parasite
TIRAILLE : Tr�s sollicit�
TIRELIRE : R�cipient muni d'une fente
TIREUSE : Machine photographique
TISANIERE : R�cipient
TISSAGE : Fabrication des tissus
TISSER : Construire
TISSU : Suite enchev�tr� de choses
TITANESQUE : Gigantesque
TITRE : Action
TITUBE : Chancelle
TL : Thallium
TM : Thulium
TOBOGGAN : Piste glissante
TOCCATA : Forme de musique
TOILETTE : Lavage
TOISON : Pelage
TOKAY : Vin de liqueur r�colt� en Hongrie
TOLERABLE : Supportable
TOLERENT : Supportent
TOLIERE : Logeuse
TOLU : Baume produit par un arbre de l'Am�rique du Sud
TOMBAC : Alliage de cuivre et de zinc
TOMBER : Perdre l'�quilibre
TOMBEREAU : Engin de transport de mat�riaux
TOMBOLO : Fl�che de sable unissant une �le � la c�te
TOMMETTE : Brique plate
TOMOGRAPHIE : Proc�d� de radiographie
TON : Inflexion de la voix
TONDRE : Raser
TONIFIER : Donner de la vigueur
TONITRUER : Crier
TONKA : F�ve
TONNEAUX : R�cipient
TONNER : Parler avec v�h�mence
TONOGRAPHIE : Enregistrement des variations de pression
TONSURE : Espace circulaire ras�
TOP : Signal de synchronisation
TOPOGRAPHIE : Relief d'un lieu
TOPOMETRIE : Mesures sur le terrain
TOQUADE : Caprice
TOQUER : Avoir un engouement pour (se)
TORCHER : B�cler
TORCHERE : Cand�labre
TORDANT : Tr�s dr�le
TORDRE : Plier
TOREUTIQUE : Art de ciseler
TORPEUR : Engourdissement
TORPILLE : Poisson marin
TORREFIER : Griller
TORRIDE : Tr�s chaud
TORSADE : Motif d'ornement
TORTICOLIS : Douleur au cou
TORTUEUSE : Sinueuse
TORTURE : Supplice
TORYSME : Opinion
TOTAL : Assemblage de plusieurs parties formant un tout
TOTALEMENT : Enti�rement
TOUBIB : M�decin
TOUCHE : Bouton
TOUFFEUR : Chaleur humide
TOUILLE : Roussette
TOUPILLON : Petite touffe de poils
TOUR : B�timent
TOURAILLON : Germe d'orge s�ch�
TOURBE : M�diocre combustible
TOURBILLONNANTE : Tournoyante
TOURDILLE : De couleur gris-jaune
TOURIERE : Charg�e des relations avec l'ext�rieur
TOURIN : Soupe � l'oignon li�e avec un jaune d'oeuf
TOURMENTEE : Angoiss�e
TOURMENTIN : Petit foc
TOURNAILLER : Roder
TOURNEVIS : Outil � main
TOURNIOLE : Panaris
TOURNIS : Vertige
TOURNURE : Mani�re dont les mots sont agenc�s dans une phrase
TOURTEAU : Crabe
TR : Tour
TRABOULE : Passage �troit qui fait communiquer deux rues
TRACAS : Souci
TRACASSER : Inqui�ter
TRACERET : Pointe � tracer
TRACTER : Tirer
TRACTIVE : Qui tire
TRADITIONNEL : Pass� dans les habitudes
TRADUCTRICE : Interpr�te
TRAFIC : Commerce ill�gal
TRAGIQUE : Terrible
TRAHIR : Abandonner
TRAINASSER : Perdre son temps
TRAINER : Tirer
TRAINING : Pull-over � cagoule
TRAITE : Ouvrage
TRAJECTOIRE : Direction
TRAMAIL : Filet de p�che
TRAMINOT : Conducteur de transport en commun
TRAMP : Navire de charge
TRANCHE : Morceau coup� mince
TRANCHER : Couper
TRANQUILLE : Paisible
TRANSBAHUTENT : Transportent
TRANSBORDER : Transf�rer des marchandises d'un v�hicule dans un autre
TRANSCENDE : D�passe
TRANSCODER : Changer de code
TRANSCRIRE : Copier
TRANSFERER : D�placer
TRANSFERT : D�placement
TRANSFILER : Lier une voile sur un espar
TRANSFORMATEUR : Appareil statique � induction �lectromagn�tique
TRANSFUSION : Injection de sang
TRANSGRESSER : Contrevenir
TRANSHUMANCE : Migration
TRANSIGER : Conclure un arrangement
TRANSISTOR : Composant �lectronique
TRANSITAIRE : Commissionnaire en marchandises
TRANSITE : Traverse
TRANSLATIF : Par lequel on transf�re une chose � une autre
TRANSLOCATION : Aberration chromosomique
TRANSMISSION : Communication
TRANSMUTATION : Transformation d'un noyau
TRANSPARAITRE : Se montrer
TRANSPARENT : Dont le sens se laisse deviner
TRANSPERCER : Passer au travers
TRANSPIRATION : Emission de vapeur d'eau
TRANSPLANTATION : Greffe
TRANSPORT : Sentiment vif
TRANSPOSER : Placer dans un autre d�cor
TRANSSUDER : Passer � travers la paroi d'un r�cipient
TRANSVASEMENT : Changement de r�cipient
TRANSVERSALE : Droite coupant un polygone ou une courbe
TRANSVIDER : Mettre dans un r�cipient plus petit
TRAPPILLON : Ouverture dans le plancher de la sc�ne
TRAPUS : Gros et court
TRAQUET : Oiseau passereau
TRAUMATIQUE : Qui concerne les plaies
TRAUMATOLOGIE : Partie de la chirurgie qui traite les blessures
TRAVAIL : Activit� d�ploy�e pour faire quelque chose
TRAVERSER : Aller d'un c�t� � l'autre
TRAVESTIR : D�guiser
TRAVIOLE : Tordu (de)
TRAYON : Extr�mit� du pis
TREBUCHET : Petite balance
TREFILER : Etirer
TREFLE : Plante herbac�e
TREILLAGE : Assemblage de lattes
TREMATAGE : D�passement
TREMBLE : Esp�ce de peuplier
TREMBLER : Etre agit� de petits mouvements
TREMBLOTER : Vaciller
TREMOUSSER : Gigoter (se)
TREMPER : plonger dans un liquide
TREMPETTE : Court bain
TREMULATION : Tremblement
TRENTE : Adjectif num�ral
TREPASSER : Mourir
TREPIDATION : Tremblement
TREPIGNER : Taper des pieds
TRESORERIE : Ensemble des actifs liquides
TRESSAUTER : Sursauter
TRESSER : Confectionner en entrela�ant les brins
TRETEAU : Th��tre ambulant
TRI : Classement
TRIADE : Groupe de trois unit�s
TRIAL : Sport motocycliste
TRIAS : Premi�re p�riode de l'�re secondaire
TRIBOLOGIE : Etude des frottements
TRIBORD : Droite
TRIBU : Groupement de familles
TRIBULATIONS : M�saventures
TRICENNAL : De trente ans
TRICHER : Ne pas respecter les r�gles
TRICHEUR : Qui ne respecte pas les r�gles
TRICHINE : Ver parasite
TRICHOLOME : Champignon
TRICOTER : Ex�cuter un tissu
TRICTRAC : Jeu
TRIDENT : Fourche � trois pointes
TRIEDRE : Figure g�om�trique
TRIENNALE : Tous les trois ans
TRIER : S�lectionner
TRIFORIUM : Galerie
TRIFOUILLER : Chercher sans m�thode
TRIGRAMME : Figure utilis�e dans la divination chinoise
TRILLE : Ornement musical
TRIMARDEUR : Vagabond
TRIMBALER : Tra�ner
TRIMBALLER : Tra�ner
TRIME : Travaille dur
TRIMER : Travailler dur
TRIMESTRE : Partie d'une ann�e
TRINGLE : Tige m�tallique
TRINITE : R�union de trois �l�ments formant un tout
TRINQUER : Subir un dommage
TRIODE : Tube �lectronique
TRIOMPHATEUR : Gagnant
TRIOMPHE : Grand succ�s
TRIPATOUILLANT : Modifiant avec maladresse
TRIPE : Partie int�rieure d'un cigare
TRIPLEX : Verre de s�curit�
TRIPLURE : Etoffe de coton
TRIPOT : Maison de jeu
TRIPOTER : Toucher sans cesse
TRIPTYQUE : Oeuvre peinte ou sculpt�e pliante
TRISMUS : Constriction des m�choires
TRISOC : Charrue
TRISSER : S'en aller rapidement
TRITIUM : Isotope radioactif de l'hydrog�ne
TRITURER : Manier sans soin
TRIVIAL : Vulgaire
TROCHEE : Pied form� d'une syllabe longue et d'une br�ve
TROGLOBIE : Qui vit dans les grottes
TROIKA : Groupe de trois chevaux attel�s de front
TROLLEY : Petit chariot roulant le long d'un c�ble
TROMBLON : Fusil court
TROMPE : Appareil avertisseur
TROMPETER : R�pandre � grand bruit
TROMPEUSEMENT : De fa�on � induire en erreur
TRONCHE : T�te
TRONCONNER : Couper
TRONER : S'�taler avec orgueil
TROPE : Figure de style
TROPICALISATION : Pr�paration d'un mat�riau pour le rendre insensible � la moisissure
TROPIQUE : Parall�le
TROQUE : Mollusque
TROT : Allure de quadrup�de
TROTTER : Marcher vite
TROTTEUSE : Aiguille
TROTTINE : Marche vite et � petit pas
TROUBADOUR : Po�te lyrique
TROUBLE : Agitation confuse
TROUEE : Ouverture
TROUPIALE : Oiseau passereau d'Am�rique
TROUSSE : Etui � compartiments
TROUVER : D�couvrir
TRUAND : Homme du milieu
TRUBLION : Individu qui s�me le trouble
TRUCIDE : Massacre
TRUELLE : Outil de ma�on
TRUITE : Poisson d'eau douce
TRUMEAU : Pan de mur entre deux embrasures de m�me niveau
TRUQUER : Falsifier
TRUSQUINER : Tracer des lignes parall�les
TRUSTER : Accaparer
TSAREVITCH : Fils du tsar
TU : Pronom personnel
TUB : Large cuvette
TUBA : Instrument de musique � vent
TUBE : R�cipient allong� de forme cylindrique
TUBERCULE : Excroissance
TUER : D�truire
TUF : Roche poreuse
TUFEAU : Roche calcaire renfermant des grains de quartz
TUILE : Ev�nement f�cheux
TULIPE : Fleur ornementale
TULLE : Tissu l�ger et tr�s transparent
TUMULUS : Eminence form�e par l'accumulation de terre au-dessus d'une s�pulture
TUNGSTENE : M�tal tr�s lourd
TUNIQUE : V�tement
TUQUE : Bonnet de laine orn� d'un pompon
TURBAN : Coiffure des Orientaux
TURBIN : Travail
TURBOT : Poisson plat
TURBULENT : Remuant
TURION : Jeune asperge
TURLUPINE : Tracasse
TURPITUDE : Action honteuse
TUTELAIRE : Qui tient sous sa protection
TUTEUR : Armature d'une jeune plante
TUTOYER : User de la deuxi�me personne du singulier
TUTU : Costume de sc�ne
TYMPAN : Membrane
TYNDALLISATION : Proc�d� de st�rilisation
TYPE : Individu quelconque
TYPHON : Cyclone en Extr�me-Orient
TYPOGRAPHIE : Proc�d� d'impression
TYRAN : Souverain despotique
U : Pas de d�finition
UFOLOGIE : Etude des ovnis
ULCERER : Blesser
ULEMA : Docteur de la loi musulmane
ULNAIRE : Qui a rapport � l'os cubital
ULTIME : Final
ULULEMENT : Cri des oiseaux rapaces nocturnes
UN : Adjectif num�ral
UNANIMISME : Ecole litt�raire du d�but du XX�me si�cle
UNCINE : Pourvu d'un crochet
UNE : Premi�re page
UNI : D'une seule couleur
UNICITE : Qualit� de ce qui est unique
UNIE : D'une seule couleur
UNIFORME : Costume
UNIFORMISER : Rendre de m�me genre
UNILATERAL : Qui n�glige un autre point de vue possible
UNIMENT : De fa�on �gale
UNIONISTE : Partisan du maintien de l'union dans un �tat conf�d�r�
UNIPOLAIRE : Se dit d'un neurone dont le corps cellulaire ne porte qu'un seul prolongement
UNIR : Joindre
UNISSON : En parfaite conformit�
UNITE : Grandeur de r�f�rence
UNIVALVE : Mollusque
UNIVERSALISER : R�pandre
UNIVERSELLE : Tr�s r�pandue
UNIVITELLIN : Provenant du m�me oeuf
UPERISER : St�riliser
URANE : Oxyde d'uranium
URANIE : Grand papillon
URBANISME : Science de l'am�nagement des villes
URDU : Langue du Pakistan
URGENTE : Qui ne peut �tre diff�r�e
URTICAIRE : Eruption cutan�e
URUBU : Esp�ce de vautour
US : Usage
USAGER : Utilisateur
USE : Vieux
USER : Utiliser
USES : Vieux
USINE : Etablissement industriel
USINER : Soumettre � l'action d'une machine-outil
USTENSILE : Objet de cuisine
USUFRUIT : Droit d'usage
USURIER : Pr�teur
USURPATRICE : Qui s'empare du pouvoir par des moyens injustes
UT : Note
UTILE : Qui rend service
UTILISER : Employer
UTOPIE : R�ve
UTRICULE : Cavit� de l'oreille
UV : Lumi�re noire
UVAL : Relatif au raisin
V : Pas de d�finition
VA : Puissance �lectrique efficace
VACANCE : Repos
VACATAIRE : Int�rimaire
VACCIN : Culture microbienne
VACCINER : Mettre � l'abri
VACHARD : M�chant
VACILLER : Tituber
VACUITE : Vide
VADROUILLE : Promenade
VAGABONDAGE : Errance
VAGUE : Ondulation
VAIGRE : Bordage int�rieur
VAILLANTE : En bonne sant�
VAINCRE : Triompher
VAISSEAU : Navire
VAISSELLE : R�cipient utilis� au service de la table
VAL : Vall�e
VALERIANE : Plante � fleurs
VALEUR : Qualit� physique
VALGA : D�viation
VALIDE : En bonne sant�
VALINE : Acide amin�
VALLEE : D�pression allong�e creus�e par un cours d'eau
VALLISNERIE : Plante des eaux stagnantes
VALORISATION : Mise en valeur
VALSE : Danse
VALVULE : Clapet
VAMPIRE : Suceur de sang
VAN : Panier
VANDA : Orchidac�e originaire de l'Inde et de l'Oc�anie
VANESSE : Papillon
VANILLE : Fruit utilis� comme parfum en p�tisserie
VANITEUSEMENT : En cherchant � produire de l'effet
VANNE : Plaisanterie d�sobligeante
VANTARD : Fanfaron
VANTER : Louer
VAPORISER : Projeter en gouttelettes fines
VAQUER : S'occuper de
VAR : D�partement fran�ais
VARAN : Reptile lacertilien
VARAPPE : Escalade
VARIA : Collection
VARIABLE : Sujet au changement
VARIATION : Changement
VARLOPE : Grand rabot
VASELINE : Graisse min�rale
VASISTAS : Vantail vitr�
VASTE : Spacieux
VATICINATION : Pr�diction
VAUDEVILLE : Com�die l�g�re
VAUTOUR : Oiseau rapace
VAUTRER : Se coucher (se)
VECTEUR : Segment de droite
VECU : R�el
VEGETAL : Plante
VEGETARISME : Syst�me d'alimentation
VEGETER : Se d�velopper difficilement
VEHICULANT : Transportant
VEILLER : Monter la garde
VEILLEUSE : Petite lampe �lectrique
VEINE : Vaisseau
VELAR : Sisymbre
VELITE : Soldat d'infanterie l�g�re chez les Romains
VELOCIPEDE : Appareil qui est � l'origine de la bicyclette
VELOUTE : Potage
VELOUTINE : Etoffe de soie du XVIII�me si�cle
VELTE : Instrument pour jauger les tonneaux
VENDANGE : R�colte
VENDANGETTE : Grive
VENDETTA : Vengeance
VENERABLE : Respectable
VENGEANCE : Vendetta
VENIMEUX : Mauvais pour la sant�
VENTE : Cession
VENTILER : A�rer
VENTIS : Arbres abattus
VENTRE : Partie renfl�e
VENTRILOQUE : Personne qui parle du ventre
VENUS : Praire
VERAISON : Etat de d�but de maturit�
VERBALEMENT : De vive voix
VERDEUR : D�faut de maturit�
VERDIER : Oiseau passereau vert
VERDUNISATION : Proc�d� de purification de l'eau
VERGE : Partie d'une ancre
VERGEOISE : Sucre
VERGNE : Aune
VERIDIQUE : Conforme � la v�rit�
VERIFICATION : Contr�le
VERJUS : Suc acide extrait du raisin vert
VERMEIL : Rouge vif
VERMICULURE : Trou de ver
VERMOULU : Mang� par les vers
VERNIE : Qui a de la chance
VERROTERIE : Bijou sans valeur
VERROUILLER : Fermer � clef
VERSANT : Pente
VERSEUSE : Cafeti�re
VERSIFICATION : Technique propre � un po�te
VERSUS : Par opposition �
VERTEX : Sommet du cr�ne
VERTICAL : Dans le sens de la hauteur
VERTIGINEUSE : Tr�s haute
VERTUEUX : Inspir� par le bien
VERVEUX : Filet de p�che
VESOU : Liquide qui sort de la cane � sucre quand on l'�crase
VESPERTILION : Chauve-souris
VESTE : Echec
VETILLE : Bagatelle
VETILLEUX : Qui s'attache � des choses sans importance
VETO : Opposition
VETUSTE : Vieux
VEULE : Mou
VEXATION : Blessure de l'amour-propre
VEXE : Bless� dans son amour-propre
VIA : En passant par
VIAGERE : Type de rente
VIBRAGE : Am�lioration de le solidit� du b�ton
VIBRER : Raisonner
VICAIRE : Pr�tre
VICIER : Corrompre
VICIEUX : Qui a des dispositions � faire le mal
VICOMTE : Titre de noblesse
VICTORIA : Ma�s d'eau
VICTUAILLES : Provisions alimentaires
VIDEO : Relatif � l'image
VIDICON : Tube analyseur d'images
VIE : Existence
VIEILLERIE : Objet ancien
VIELLE : Instrument de musique
VIF : Qui a de la vitalit�
VIFS : Qui ont de la vitalit�
VIGILANT : Attentif
VIGNEAU : Bigorneau
VIGNETTE : Timbre
VIGUEUR : Force
VIHARA : Monast�re bouddhique
VIL : M�prisable
VILAYET : Division administrative en Turquie
VILE : M�prisable
VILLE : Agglom�ration relativement importante
VILLEUX : Couvert de longs poils touffus
VILS : M�prisables
VIN : Boisson ferment�e
VINAGE : Condiment
VINAIGRETTE : Sauce
VINDICATIF : Qui aime � se venger
VINEUX : Riche en alcool
VINGT : Adjectif num�ral
VIOLACEE : Herbe � fleurs dialyp�tales
VIOLATION : Action d'enfreindre une obligation
VIOLENCE : Force brutale
VIOLONCELLE : Instrument de musique
VIPERE : Serpent
VIRAGE : Changement de direction
VIRANT : Changeant de direction
VIRER : Changer de direction
VIREVOLTE : Tour rapide sur soi-m�me
VIRGULE : Signe de ponctuation
VIROLE : Bague
VIROLER : Baguer un manche
VIRTUEL : Qui n'est pas r�alis�
VIRURE : File de bordages
VIS : Pi�ce d'assemblage
VISA : Sceau
VISAS : Sceaux
VISCERAL : Qui provient du plus profond de l'�tre 
VISCOREDUCTION : Proc�d� de raffinage
VISER : Pointer
VISIBLEMENT : Manifestement
VISIONNER : Voir un film avant sa distribution
VISITE : Tourn�e
VISON : Mammif�re carnassier recherch� pour sa fourrure
VISSE : Fixe
VITAL : Essentiel
VITALITE : Energie
VITAMINE : Substance indispensable � l'organisme
VITAUX : Essentiels
VITE : Rapidement
VITRE : Plaque de verre
VITRINE : Devanture de boutique
VITRIOL : Acide sulfurique concentr�
VITUPERE : Bl�me vivement
VIVACE : Tenace
VIVANDIER : Personne qui vendait des vivres aux soldats
VIVE : Poisson � �pines venimeuses
VIVIER : Pi�ce d'eau pour conserver le poisson
VIVIFIANTE : Tonifiante
VIVIPARITE : Mode de reproduction
VIVOTER : Aller au ralenti
VIVRES : Aliments
VO : Version originale
VOCABULAIRE : Ensemble des mots appartenant � une langue
VOCALISER : Faire des exercices de chants
VOCATION : Penchant pour une profession
VOCIFERATEUR : Personne qui � l'habitude de crier
VOCODEUR : Organe d'analyse des sons
VOGUER : Naviguer
VOILAGE : Grand rideau
VOILER : Cacher
VOILIER : Bateau
VOISEMENT : Vibration des cordes vocales
VOISINE : Situ�e � faible distance
VOITURE : V�hicule servant au transport des personnes et des marchandises
VOL : D�placement dans l'air
VOLAGE : Dont les sentiments changent souvent
VOLANT : Organe de manoeuvre d'un m�canisme
VOLATILISER : Faire dispara�tre
VOLCANIQUE : Imp�tueux
VOLE : Coup qui consiste � faire toutes les lev�es aux cartes
VOLEE : Suite de coups
VOLET : Panneau de bois pour clore une fen�tre
VOLETER : Parcourir de petites distances dans l'air
VOLIERE : Grande cage
VOLIGE : Planche mince utilis�e dans les couvertures et les cloisons
VOLIS : Cime d'un arbre cass�e
VOLONTARIAT : Service accompli par un engag�
VOLT : Unit� de mesure de diff�rence de potentiel
VOLTAGE : Tension
VOLTAMETRE : Appareil o� se produit une �lectrolyse
VOLTE : Mouvement en rond que l'on fait faire � un cheval
VOLTIGER : Flotter au gr� du vent
VOLUBILIS : Liseron
VOLUPTUEUSEMENT : Avec une satisfaction intense
VOLVE : Membrane qui entoure le chapeau et le pied de certains champignons
VOLVOX : Protozoaire d'eau douce
VOMER : Os du nez
VORACITE : Avidit� extr�me
VOS : Adjectif possessif
VOTE : Choix
VOTRE : Adjectif possessif
VOULOIR : D�sirer
VOUS : Pronom possessif
VOYAGE : D�placement
VOYANT : Appareil de signalisation
VRAI : Conforme � la r�alit�
VRAISEMBLANCE : Qualit� de ce qui a l'apparence de la v�rit�
VRILLE : Outil � percer le bois
VROMBIR : Produire un ronflement vibrant
VU : Aper�u
VUE : Aper�ue
VULCANISATION : Am�lioration du caoutchouc en le traitant par le soufre
VULGARISER : Rendre accessible � tous
VULGARITE : Grossi�ret�
VULPIN : Plante des prairies
W : Pas de d�finition
WAGAGE : Limon de rivi�re employ� comme engrais
WAGONNET : Petit v�hicule ferroviaire
WALLABY : Kangourou
WALLON : Dialecte roman de langue d'o�l
WARRANT : Titre � ordre
WASHINGTON : Ville am�ricaine
WATERGANG : Foss�
WATTHEURE : Unit� de mesure d'�nergie
WB : Weber
WEHNELT : Electrode cylindrique
WHARF : Appontement
WILLIAMS : Poire
WISHBONE : Vergue en forme d'arceau
WON : Unit� mon�taire de la Cor�e
X : Pas de d�finition
XE : X�non
XENOPHILIE : Sympathie pour les �trangers
XEROPHILE : Adapt� aux climats secs
XIANG : Dialecte chinois
XYLOGRAPHE : Graveur sur bois
Y : Pas de d�finition
YACHTMAN : Navigateur
YAK : Ruminant du Tibet
YATAGAN : Sabre
YB : Ytterbium
YEN : Unit� mon�taire du Japon
YIDDISH : Langue germanique des communaut�s juives d'Europe centrale et orientale
YOGA : Discipline spirituelle et corporelle
YPREAU : Peuplier blanc
YUCCA : Plante liliac�e am�ricaine
Z : Pas de d�finition
ZAIN : Se dit du cheval ou du chien qui n'a aucun poil blanc
ZAMBIE : Pays africain
ZANZIBAR : Jeu de hasard
ZEBRE : Mammif�re ongul� d'Afrique
ZEE : Saint-pierre
ZELE : Ardeur
ZEN : Secte bouddhique
ZENITH : Apog�e
ZESTE : Ecorce ext�rieure de l'orange ou du citron
ZEUZERE : Papillon nocturne
ZIEUTER : Regarder
ZIGOUILLER : Tuer
ZINGAGE : D�p�t �lectrolytique
ZINZIN : Un peu fou
ZLOTY : Unit� mon�taire de la Pologne
ZN : Zinc
ZOMBIE : Mort sorti du tombeau
ZONALE : Qui a des bandes transversales color�es
ZONE : Portion de territoire
ZOOLOGIE : Etude des animaux
ZOOMORPHISME : Action de donner la forme d'un animal
ZOOPHOBIE : Peur des animaux
ZYGENE : Papillon
ZYGOPETALE : Orchidac�e des r�gions chaudes de l'Am�rique
ZYMOTIQUE : Relatif aux ferments solubles
















"""

# Compilation de l'expression régulière pour de meilleures performances lors d'un usage intensif
pattern = re.compile(r':.*$', flags=re.MULTILINE)

# Application de la regex pour supprimer tout texte après ":" sur chaque ligne
resultat = pattern.sub('', texte)

# Enregistrement du résultat dans un fichier texte
with open('resultat.txt', 'w', encoding='utf-8') as fichier:
    fichier.write(resultat)

print("Le résultat a été sauvegardé dans 'resultat.txt'")
