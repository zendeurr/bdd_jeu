#   PLANIFICATION DU PROJET
# Le jeu se lance 
#   Menu apparaît 
#        Joueur doit choisir une option *valable*
#           Si joueur choisit option parmis celles valables, lancer option
#           Sinon afficher_erreur et boucler
#
# 1. Jouer  
# Demander son pseudo au joueur
# Affichage d'un nombre x de personnages via un print (pour l'instant), demande à utilisateur d'en choisir 3
#   Ne peut pas choisir le même perso
# Le jeu se lance lorsqu'il a selectionné = 5 personnages
#       Tant que l'équipe du joueur est en vie, une nouvelle vahue d'ennemie arrive(Trois fenêtres sont affichées)
#           Trois "blocs" dans la console, réafichées actualisés(
#               Celle de gauche = Équipe du joueur(ATK,DEF,PV actuels) 
#               Celle du centre = État de la partie(Qui fait quoi, quand)
#               Celle de droite = Équipe de l'adversaire(ATK, DEV, PV actuels)
#           )
#           Lorsque partie est finie 
#               Si joueur a gagné ajouter +1 poin au leaderboard
#               Sinon ne rien faire
#           
# 2. Leaderboard
#   Afficher menu leaderboard(plus haute vague gagnée selon pseudo)
#
# 3. Quitter
# Afficher message de fermeture du programme
# sleep()
# Fermer le programme

# Autre ? Afficher erreur, fonction en elle même ?


# --> Affichage(menu en lui même, erreur) 
# --> Menu(Demander choix utilisateur, vérif choix valide, boucle menu,) 
# --> Partie(Lancer la partie, choisir équipe, lancer combat, combat terminé) 
# --> autre(bdd) 