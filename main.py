
# Partie Menu


# Afficher menu 
# récup choix valide parmis les options 
#   tant que true
#       afficher les options numérotées
#           pour chaque option dans enumerate(options, start=1)
#           afficher {i}. {option}
#       demander un choix à l'utilisateur
#           si le choix est bon
#               retourner choix valide
#           sinon afficher un message d'erreur 


# Action joueur
# lancer l'action qui correspond au choix du menu
#   si le choix est jouer
#       lancer une partie
#   ou si le choix est eaderboard
#       voir le leaderboard
#   ou si le choix est quitter
#       afficher un msssage de fermeture
#   faire une pause


# Répéter Menu
# afficher le menu jusqu'à ce que l'utilisateur choisisse Quitter
#   tant que le choix n'est pas Quitter
#       afficher le titre du jeu
#       récup un choix valide parmi les options du menu
#       exécuter l'action de ce choix


# Vérifier choix joueur 
#   Vérifier qu'un choix x est valide 
#       Si le choix n'est pas un nombre:
#           retourner Faux
#       transformer le choix en nombre entier
#   Si le nombre est entre 1 et le nombre d'options
#       retourner Vrai
#   Sinon retourner Faux

# Afficher erreur (inutile finalement je vais enlever, autant mettre juste une erreur dans une fonction pas la peine d'utiliser une sous fonction)


# Partie Combat


# Demander pseudo joueur
# tant que true
#   demander pseudo au joueur
#       si pseudo ne contient pas caractères spéciaux et plus de 15 caractères
#           afficher pseudo du joueur et message de succès
#       sinon afficher erreur


# Lancer partie 
#   demander son pseudo au joueur
#       recup les personnages dans la bdd
#       afficher menu du choix des personnages
#           faire choisir 3 personnages au joueur pour former son équipe
#               faire combattre l'équipe vague après vague
#            enregistrer le record du joueur (s'il la battu)
#               afficher le score de la partie  


# Choisir équipe 
#   Faire choisir 3 personnages au joueur
#       tant que l'équipe n'a pas 3 personnages selectionnés
#           montrer les personnages disponibles
#           recup choix valide
#           lorsque joueur selectionne personnage celui-ci est retiré de la liste disponible et annoncé comme choisit 
#           ajouter personnage a l'équipe
#       retourner l'équipe


# Lancer combat
#   tant que l'équipe du joueur n'est pas battue
#       l'équipe attaque les monstres
#       tant que les monstres ne sont pas battus
#           les monstres attaquent l'équipe
#   retourner true si l'


# Lancer la vague
#   tant que l'équipe a des personnages en vie
#       creer les ennemis de la vague 
#   si l'équipe gagne le combat 
#       ajouter 1 point au leaderboard du joueur 
#   retourner nombre de vagues survécues


# Créer la vague
#   prendre monstre de la base de données
#       ajouter 1 monstre de plus toutes les 2 vagues
#       calculer atk def pv (augmente en fonction de la vague)
#       importer ennemi de mongodb  


# Faire attaquer
#   creer liste des actions du joueur et des monstres de la vague
#       pour chaque unité qui attaque
#      si l'unité est vivante et qu'il reste supérieur ou égal a une cible
#       calculer les dégâts de l'attaque
#       soustraire les dégats au pv de la cible
#       ajouter aux actions qui a frappé qui 
#   retourner liste des actions

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

# Est-ce que groupe en vie
#   pour chaque membre du groupe
#       si le membre à plus de 0PV
#       retourner True
#   sinon retourner Faux


# Afficher résultat partie

# Partie "Autre"



# Connecter a la base de données
#   se connecter au serveur mongodb
#   sélectionner base de données 
#   retourner

# Lire leaderboard
#   se connter a la base
#   lire "leaderboard"
#   afficher plus grand nombre de vagues au plus petit
#   garder le top 3 des score
#  retourner 

# Contenu Leaderboard
#   lire le leaderboard dans la base de données
#       afficher le leaderboard

# Afficher le leaderboard
#   afficher le titre "leaderboard"
#       si personne n'a joué 
#           dire qu'aucune partie n'a été jouée
#       sinon pour chaque joueur 
#           afficher pseudo et score 