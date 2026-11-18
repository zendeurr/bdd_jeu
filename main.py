
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


# Boucle combat

# Afficher résultat partie

# Partie "Autre"



# Lancer base de données

# Lancer Leaderboard

# Contenu Leaderboard