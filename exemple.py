# Afficher Menu 
# Recuperer un choix valide parmi les options
#   tant que infini
#       afficher les options numerotees
#           pour chaque option dans enumerate(options, start=1)
#               afficher{i}, {option}
#       demander un choix à l'utilisateur
#       si le choix est valide
#           retourner le choix valide
#       afficher un message d'erreur 

# Besoin la liste des personnages de la DB
def creer_equipe(liste_personnage_db):
    # creer la variable equipe vide
    equipe = []
    # tant que l'équipe n'est pas complete
    while not est_mon_equipe(equipe):
    #   determiner la liste des personnages disponibles
    personnages_disponibles = determiner_personnages_disponibles(
       liste_personnage_db, equipe)
    #   contruire la liste des options a afficher disponibles
    options_affichables = construire_options_affichables(personnages_disponibles)
    #   ["Guerre - ATK : 10 - DEF : 12  - PV : 15"]
    #   recuperer un choix valide
    choix = recuperer_choix_utilisateur(options_affichables)
    #   ajouter le personnage choisi a l'équipe index = choix - 1
    equipe.append(personnages_disponibles[choix - 1])
    # retourner l'équipe
    return equipe

def determiner_personnages_disponibles(liste_personnage_db, equipe):
    # creer la liste des personnages disponibles
    # pour chaque personnage dnas la liste des personnages de la DB
    #   si le personnage n'est pas dans l'équipe
    #       l'ajouter a la liste des personnages disponibles
    # renvoyer la liste des personnages disponible

 def construire_options_affichables(personnages_disponibles):
    # creer la liste options
    # pour chaque personnage dans personnages_disponibles
    #   ajouter à la liste : f""{personnage["nom"]} - ATK : {personnage["atk"]}"
    # retourner la liste des options

# ^^^^ Modèle à appliquer aux commentaires ^^^^^