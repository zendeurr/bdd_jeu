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
#       si le choix est bon
        if verifier_choix_joueurs(choix, options):
#           retourner choix valide
            return int(choix)
#       sinon afficher un message d'erreur
        print("tu te baves dessus écrit mieux stp")


# Action joueur
# lancer l'action qui correspond au choix du menu
def action_joueur(choix):
#   si le choix est jouer
    if choix == CHOIX_JOUER:
#       lancer une partie
        lancer_partie()
#   ou si le choix est leaderboard
    elif choix == CHOIX_LEADERBOARD:
#       voir le leaderboard
        contenu_leaderboard()
#   ou si le choix est quitter
    elif choix == CHOIX_QUITTER:
#       afficher un message de fermeture et quitter
        print("bisousx 😘")
#   faire une pause
    time.sleep(PAUSE)


# Répéter Menu
# afficher le menu, lancer l'action choisie par le joueur, puis recommencer jusqu'à ce qu'il choisisse Quitter
def repeter_menu()
#   créer le choix de départ (0)
    choix = 0
#   tant que le choix n'est pas Quitter
    while choix != CHOIX_QUITTER:
#       afficher le titre du jeu
        afficher_titre(NOM_DU_JEU)
#       récup un choix valide parmi les options du menu
        choix = recuperer_choix_valide(OPTIONS_MENU)
#       exécuter l'action de ce choix
        action_joueur(choix)


# Partie Combat


# Demander pseudo joueur
def demander_pseudo_joueur():
#   tant que true
    while True:
#       demander pseudo au joueur
        pseudo = input("Ton pseudo ma biche : ").strip()
#       si pseudo contient caractères spéciaux et plus de 15 caractères
        if len(pseudo) <= PSEUDO_MAX and pseudo.isalnum():
#           retourner le pseudo
            return pseudo
#       afficher erreur
        print("jsp c'est quoi ton pseudo bien nul mais ça marche pas, tu peux pas jouer mdr")


# Lancer partie
def lancer_partie(): 
#   demander son pseudo au joueur
    pseudo = demander_pseudo_joueur()
#   recup les personnages dans la bdd
    personnages = lire_personnages()
#   recup les monstres dans la bdd
    monstres = lire_monstres()
#   faire choisir 3 personnages au joueur pour former son équipe
    equipe = choisir_equipe(personnages)
#   faire combattre l'équipe vague après vague
    vagues = lancer_les_vagues(equipe, monstres)
#   enregistrer le record du joueur (s'il la battu)
    enregistrer_score(pseudo, vagues)
#   afficher le score de la partie 
    afficher_resultat_de_la_partie(pseudo, vagues)


# Equipe au complet
def equipe_au_complet(equipe):
#   si l'équipe est au complet
    if len(equipe) == TAILLE_EQUIPE:
#       retourner Vrai
        return True
#   sinon retourner faux
    return False


# Est-ce que personnages disponibles
def personnages_disponibles(personnages_en_base, equipe):
#   créer la liste vide des personnages disponible
    disponibles = []
#   pour chaque personnage choisissable dans la bdd
    for perso in personnages_en_base:
#       si l'équipe ne contient pas ce personnage
        if perso not in equipe:
#           ajouter dans la liste
            disponibles.append(perso)
#   retourner personnages disponibles
    return disponibles

# Construire options affichables
def construire_options_affichables(personnages):
#   créer une liste vide 
    options = []
#   pour chaque personnage
    for perso in personnages:
#       écrire les détails de la liste de texte d'un personnage par ex: "Paladin - 67 ATK - 10 DEF - 50HP"
        texte = afficher_description(perso)
#       ajouter ce texte à la liste des options
        options.append(texte)
#    retourner la liste des options
    return options


# Choisir un personnage
def choisir_un_personnage(personnages_en_base, equipe):
#   déterminer les personnages disponibles
    disponibles = personnages_disponibles(personnages_en_base, equipe)
#   construire les textes à afficher pour ces personnages
    options = construire_options_affichables(disponibles)
#   afficher "personnages disponibles:" récupérer un choix valide
    print("Pays disponibles 🌈🏳️: ")
#   récupérer un choix valide
    choix = recuperer_choix_valide(options)
#   retourner le personnage choisi par le joueur
    return disponibles[choix - 1]


# Choisir équipe 
#   Faire choisir 3 personnages au joueur
def choisir_equipe(personnages_en_base):
#   afficher le titre du choix des personnages
    afficher_titre("Choisis les pays que tu souhaites 😘😊 :")
#   créer une équipe vide
    equipe = []
#   tant que l'équipe n'a pas 3 personnages selectionnés
    while not equipe_au_complet(equipe):
#       afficher les personnages du joueurs
        afficher_equipe_du_joueur(equipe)
#       faire choisir un personnage parmis ceux disponibles
        perso = choisir_un_personnage(personnages_en_base, equipe)
#       ajouter ce personnage à l'équipe du joueur
        equipe.append(perso)
#       afficher qu'il rejoint l'équipe
        print(perso["nom"], "rejoint ta team de gros bg enfaite 🏳️‍⚧️👌")
#   retourner l'équipe
    return equipe


# Afficher équipe du joueur
def afficher_equipe_du_joueur(equipe):
#   afficher nombre de personnages choisit par le joueur sur le maximum choisissable
    print(f"T'a actuellementt ({len(equipe)}/{TAILLE_EQUIPE}) pays a envoyer au front :")
#   pour chaque personnage de l'équipe avec son propre numéro
    for i, perso in enumerate(equipe, start=1):
#       afficher numéro et description du personnage
        print(f"Pays {i} : {afficher_description(perso)}")    


# Lancer combat
def lancer_combat(equipe, ennemis):
#   tant que l'équipe du joueur et les monstres ont encore des survivants
    while groupe_en_vie(equipe) and groupe_en_vie(ennemis):
#       l'équipe attaque les monstres
        faire_attaquer(equipe, ennemis)
#       afficher l'état puis pause
        afficher_etat_puis_pause(equipe, ennemis)
#       si des ennemise sont encore en vie
        if groupe_en_vie(ennemis):
#           les ennemises attaquent l'équipe
            faire_attaquer(ennemis, equipe)
#           afficher l'état puis pause
            afficher_etat_puis_pause(equipe, ennemis)
#   retourner true si l'équipe est toujours en vie
    return groupe_en_vie(equipe)


# Lancer la vague
def lancer_la_vague(equipe, monstres, numero_vague):
#   afficher la vague
    afficher_titre("VAGUE " + str(numero_vague))
#   prendre un monstre au hasard
    monstre = prendre_un_monstre_au_hasard(monstres)
#   afficher les caractéristiques du monstre
    print("La télé a dit qu'un pays était méchant, donc il l'est 😱😮 ! C'est : ", afficher_description(monstre))
#   faire combattre l'équipe contre le monstre
    return lancer_combat(equipe, [monstre])


# Lancer les vagues
def lancer_les_vagues(equipe, monstres):
#   commencer avec 0 vague survécue
    vagues_survecues = 0
#   tant que l'équipe a des personnages en vie
    while groupe_en_vie(equipe):
#       Calculer le numéro de la vague en cours 
        numero_vague = vagues_survecues + 1
#       si l'équipe gagne le combat 
        if lancer_la_vague(equipe, monstres, numero_vague):
#           ajouter 1 point au vagues survecues du joueur 
            vagues_survecues = vagues_survecues + 1
#   retourner nombre de vagues survécues
    return vagues_survecues

# Prendre un monstre au hasard
def prendre_un_monstre_au_hasard(monstres):
#   choisit un monstre aléatoirement dans la db
    modele = random.choice(monstres)
#   en faire une copie 
    monstre = dict(modele)
#   retourner la copie 
    return monstre


# Faire attaquer
def faire_attaquer(attaquants, cibles):
#   pour chaque unité qui attaque
    for attaquant in attaquants:
#       si l'unité est vivante et qu'il reste supérieur ou égal a une cible
        if attaquants["pv"] > 0 and groupe_en_vie(cibles):
#           choisir au hasard une cible parmi celle en vie
            cible = choisir_cible_a_attaquer_au_hasard(cibles)
#           calculer les dégâts de l'attaque
            degats = calculer_les_degats(attaquant, cible)
#           soustraire les dégats au pv de la cible
            cible["pv"] = cible["pv"] - degats
#           afficher qui frappe qui
            print(f'{attaquant["nom"]} envoie un missile balistique sur {cible["nom"]} : -{degats}')


# Lister unités en vie
def lister_unites_en_vie(groupe):
#   créer liste des unités en vie
    en_vie = []
#   pour chaque unité du groupe
    for unite in groupe:
#       si celle-ci a plus de 0 pv
        if unite["pv"] > 0:
#           ajouter à la liste des unités en vie
            en_vie.append(unites)
#   retourner liste des unités en vie
    return en_vie


# Choisir cible a attaquer au hasard
def choisir_cible_a_attaquer_au_hasard(cibles):
#   lister les cibles encore en vie 
    en_vie = lister_unites_en_vie(cibles)
#   choisir une cible au hasard
    cible = random.choice(en_vie)
#   retourner la cible
    return cible


# Calculer les dégâts
def calculer_les_degats(attaquant, cible):
#   dégats = ATK de de l'attaquant - DEF de l'ennemi
    degats = attaquant["atk"] - cible["defense"]
#   si les dégats sont inférieurs à 1
    if degats < 1:
#       définir les dégats a 1 (évite que les attaquent fassent 0 dégats parce que ATK = DEF) 
        degats = 1
#   retourner les dégats
    return degats


# Est-ce que groupe en vie
def groupe_en_vie(groupe):
#   pour chaque membre du groupe
    for membre in groupe:
#       si le membre à plus de 0 PV
        if membre["pv"] > 0:
#           retourner True
            return True
#   sinon retourner Faux
    return False


# Afficher résultat de la partie
def afficher_resultat_de_la_partie(pseudo, vagues):
#   retour à la ligne, afficher "game over :("
    print("\ngame over nullos")
#   retour à la l, afficher pseudo du joueur
    print("\nJoueur :", pseudo)
#   retour à la l, afficher score
    print("\nVagues survécues :", vagues)


# Afficher options
def afficher_options(options):
#   pour chaque option possédant un numéro
    for i, option in enumerate(options, start=1):
#       afficher son numéro et son texte
        print(f"{i}. {option}")



# Partie "Autre"



# Connecter a la base de données
def connecter_a_la_base_de_donnes():
#   se connecter au serveur mongodb
    client = MongoClient(ADRESSE_MONGO)
#   sélectionner base de données 
    base = client[NOM_BASE]
#   retourner
    return base

# Lire personnages
def lire_personnage(): 
#   se connecter à la db
    base = connecter_a_la_base_de_donnes()
#   lire "personnages"
    personnages = list(base["personnages"].find())
#   retourner la liste de personnages
    return monstres

# Lire monstres 
def lire_monstres():
#   se connecter à la db
    base = connecter_a_la_base_de_donnes()
#   lire "monstres"
    monstres = list(base["monstres"].find())
#   retourner la liste de monstres   
    return monstres

# Enregistrer score
def enregistrer_score(pseudo, vagues):
#   se connecter à la base de données
    base = connecter_a_la_base_de_donnes()
#   voir si joueur existe 
    ancien = base["leaderboard"].find_one({"pseudo": pseudo})
#   si le joueur n'existe pas encore
    if ancien is None:
#       l'ajouter avec son score respectif
        base["leaderboard"].insert_one({"pseudo": pseudo, "vagues": vagues})
#   sinon son score est plus élevé que son ancien record
    elif vagues > ancien["vagues"]:
#       mettre à jour le score     
        base["leaderboard"].update_one({"pseudo": pseudo}, {"$set": {"vagues": vagues}})


# Lire leaderboard
def lire_leaderboard():
#   se connecter a la base
    base = connecter_a_la_base_de_donnes()
#   lire "leaderboard"
    resultats = base["leaderboard"].find()
#   afficher plus grand nombre de vagues au plus petit
    resultats = resultats.sort("vagues", -10)
#   garder le top 3 des scores
    resultats = resultats.limit(TAILLE_LEADERBOARD)
#   retourner 
    return list(resultats)

# Contenu Leaderboard
def contenu_leaderboard():
#   lire le leaderboard dans la base de données
    leaderboard = lire_leaderboard()
#   afficher le leaderboard
    afficher_le_leaderboard(leaderboard)

# Afficher le leaderboard
def afficher_le_leaderboard(leaderboard):
#   afficher le titre "leaderboard"
    afficher_titre("Leaderboard")
#   si personne n'a joué 
    if len(leaderboard) == 0:
#       dire qu'aucune partie n'a été jouée
        print("Mon jeu a flop : 0 ventes sur Steam 😭 allo carrefour ? c pour un cdi")
#   sinon
    else:
#       pour chaque joueur
        for joueur in leaderboard:
#           afficher pseudo et score 
            print(joueur["pseudo"], ":", joueur["vagues"], "vagues")

# Lancer programme
def lancer_programme():
#   boucler le menu
    repeter_menu