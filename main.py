TAILLE_EQUIPE = 3
PAUSE = 2
PSEUDO_MAX = 15
CHOIX_JOUER = 1
CHOIX_LEADERBOARD = 2
CHOIX_QUITTER = 3

NOM_DU_JEU = "World Simulator 😎🌍"
OPTIONS_DU_JEU = ["Jouer", "Leaderboard", "Quitter 😔😪😭🥺"]


# Partie Affichage


# Afficher titre
def afficher_titre(texte):
# afficher une ligne de "-"
print("-----------------------------------------")
# afficher le titre
print(texte)
# afficher une ligne de "-"
print("-----------------------------------------")


# Afficher groupe
def afficher_groupe(groupe):
#   affiche une ligne par membre d'un groupe
    for membre in groupe:
#       pour chaque membre du groupe
        print(afficher_description(membre))
#       afficher sa description

# Afficher description
# Ecrit le texte d'un personnage ou d'un monstre
def afficher_description(perso):
#   écrit nom du personnage, ATK, DEF et PV sur une ligne
    texte = f'{perso["nom"]} - {perso["atk"]} ATK - {perso["defense"]} DEF - {perso["pv"]} PV'
#   retourner
    return texte

# Afficher état du combat
def afficer_etat_du_combat(equipe, ennemis):
#   afficher le titre de l'équipe
    print("Le mauvais côté de l'Histoire : ")
#   afficher l'équipe
    afficher_groupe(equipe)
#   afficher le titre des ennemis
    print("Le bon côté de l'Histoire : ")
#   afficher les ennemis
    afficher_groupe(ennemis)

# Afficher etat puis pause
def afficher_etat_puis_pause(equipe, ennemis):
    # afficher état du combat
    afficer_etat_du_combat(equipe, ennemis)
    # sleep() pour laisser au joueur le temps de lire ce qu'il se passe
    time.sleep(PAUSE)

# Partie Menu


# Vérifier choix joueur
def verifier_choix_joueurs(choix, options):
#   Si le choix n'est pas un nombre
    if choix.isdecimal():
#       retourner False
        return False
#   transformer le choix en chiffre
    nombre = int(choix)
#   si le nombre est entre 1 et le nombre d'options
    if nombre >= 1 and nombre <= len(options):
#       retourner True
        return True
#   retourner False
    return False


# Récupérer choix valide
# récup choix valide parmis les options 
def recuperer_choix_valide(options):
#   tant que true
    while True:
#       afficher les options numérotées
        afficher_options(options)
#       demander un choix à l'utilisateur
        choix = input("Choisis ton pays : ")
#           si le choix est bon
#               retourner choix valide
#           sinon afficher un message d'erreur 


# Action joueur
# lancer l'action qui correspond au choix du menu
#   si le choix est jouer
#       lancer une partie
#   ou si le choix est leaderboard
#       voir le leaderboard
#   ou si le choix est quitter
#       afficher un message de fermeture et quitter
#   faire une pause


# Répéter Menu
# afficher le menu, lancer l'action choisie par le joueur, puis recommencer jusqu'à ce qu'il choisisse Quitter
#   créer le choix de départ (0)
#   tant que le choix n'est pas Quitter
#       afficher le titre du jeu
#       récup un choix valide parmi les options du menu
#       exécuter l'action de ce choix


# Partie Combat


# Demander pseudo joueur
# tant que true
#   demander pseudo au joueur
#       si pseudo contient caractères spéciaux et plus de 15 caractères
#           afficher erreur
#       sinon afficher pseudo du joueur et message de succès


# Lancer partie 
#   demander son pseudo au joueur
#   recup les personnages dans la bdd
#   recup les monstres dans la bdd
#   faire choisir 3 personnages au joueur pour former son équipe
#   faire combattre l'équipe vague après vague
#   enregistrer le record du joueur (s'il la battu)
#   afficher le score de la partie  


# Equipe au complet
#   si l'équipe est au complet
#       retourner Vrai
#   sinon retourner faux


# Est-ce que personnages disponibles
#   créer la liste vide des personnages disponible
#   pour chaque personnage choisissable dans la bdd
#       si l'équipe ne contient pas ce personnage
#           ajouter dans la liste
#   retourner personnages disponibles

# Construire options affichables
# créer une liste vide 
#   écrire les détails de la liste de texte d'un personnage par ex: "Paladin - 67 ATK - 10 DEF - 50HP"
#   ajouter ce texte à la liste des options 
# retourner la liste des options


# Choisir un personnage
#   déterminer les personnages disponibles
#   construire les textes à afficher pour ces personnages
#   afficher "personnages disponibles:" récupérer un choix valide
#   retourner le personnage choisi par le joueur


# Choisir équipe 
#   Faire choisir 3 personnages au joueur
#   afficher le titre du choix des personnages
#   créer une équipe vide
#   tant que l'équipe n'a pas 3 personnages selectionnés
#       afficher les personnages du joueurs
#       faire choisir un personnage parmis ceux disponibles
#       ajouter ce personnage à l'équipe du joueur
#       afficher qu'il rejoint l'équipe
#   retourner l'équipe


# Afficher équipe du joueur
#   afficher nombre de personnages choisit par le joueur sur le maximum choisissable
#   pour chaque personnage de l'équipe avec son propre numéro
#       afficher numéro et description du personnage    


# Lancer combat
#   tant que l'équipe du joueur et les monstres ont encore des survivants
#       l'équipe attaque les monstres
#           afficher l'état puis pause
#       si des ennemise sont encore en vie
#           les ennemises attaquent l'équipe
#           afficher l'état puis pause
#   retourner true si l'équipe est toujours en vie


# Lancer la vague
#   afficher la vague
#   prendre un monstre au hasard
#   afficher les caractéristiques du monstre
#   faire combattre l'équipe contre le monstre


# Lancer les vagues
#   commencer avec 0 vague survécue
#   tant que l'équipe a des personnages en vie
#       Calculer le numéro de la vague en cours 
#       si l'équipe gagne le combat 
#           ajouter 1 point au leaderboard du joueur 
#   retourner nombre de vagues survécues


# Prendre un monstre au hasard
#   choisit un monstre aléatoirement dans la db 
#   en faire une copie 
#   retourner la copie 


# Faire attaquer
#   pour chaque unité qui attaque
#       si l'unité est vivante et qu'il reste supérieur ou égal a une cible
#           choisir au hasard une cible parmi celle en vie
#           calculer les dégâts de l'attaque
#           soustraire les dégats au pv de la cible
#           afficher qui frappe qui


# Lister unités en vie
#   créer liste des unités en vie
#   pour chaque unité du groupe
#       si celle-ci a plus de 0 pv
#           ajouter à la liste des unités en vie
#   retourner liste des unités en vie


# Choisir cible a attaquer au hasard
#   lister les cibles encore en vie 
#   choisir une cible au hasard
# retourner la cible


# Calculer les dégâts
#   dégats = ATK de de l'attaquant - DEF de l'ennemi
#   si les dégats sont inférieurs à 1
#       définir les dégats a 1 (évite que les attaquent fassent 0 dégats parce que ATK = DEF) 
#   retourner les dégats


# Est-ce que groupe en vie
#   pour chaque membre du groupe
#       si le membre à plus de 0 PV
#           retourner True
#   sinon retourner Faux


# Afficher résultat de la partie
#   retour à la ligne, afficher "game over :("
#   retour à la l, afficher pseudo du joueur
#   retour à la l, afficher score 


# Afficher options
#   pour chaque option possédant un numéro
#       afficher son numéro et son texte



# Partie "Autre"



# Connecter a la base de données
#   se connecter au serveur mongodb
#   sélectionner base de données 
#   retourner

# Lire personnages 
#   se connecter à la db
#   lire "personnages"
#   retourner la liste de personnages

# Lire monstres 
#   se connecter à la db
#   lire "monstres"
#   retourner la liste de monstres   

# Enregistrer score
#   se connecter à la base de données
#   voir si joueur existe 
#   si le joueur n'existe pas encore
#       l'ajouter avec son score respectif
#   sinon son score est plus élevé que son ancien record
#       mettre à jour le score     


# Lire leaderboard
#   se connecter a la base
#   lire "leaderboard"
#   afficher plus grand nombre de vagues au plus petit
#   garder le top 3 des scores
#   retourner 

# Contenu Leaderboard
#   lire le leaderboard dans la base de données
#   afficher le leaderboard

# Afficher le leaderboard
#   afficher le titre "leaderboard"
#   si personne n'a joué 
#       dire qu'aucune partie n'a été jouée
#   sinon pour chaque joueur 
#       afficher pseudo et score 

# Lancer programme
#   boucler le menu