"""
This program allows users to create a shopping list.
There are no item limits.
Users write "stop" to stop adding items.
At the end of the program, users can validate the list, modify it or cancel it.
Users can edit the list as many times as they want.
The program stops when users validate or cancel.
"""


# Starts the shopping list.
def list_typing():
    print("\nMA LISTE DE COURSES\n"
      "Vous pouvez ajouter autant d'articles que vous le souhaitez.\n"
      "Ecrivez 'stop' (sans majuscules) pour arreter d'ajouter des articles a la liste.\n")
    shopping_list = []
    item = 0
    counter = 0


    # Stops the shopping list if the user writes "stop"
    while item != "stop":
        item = input("Ajouter un article : ")
        if item == "stop":
            break
        elif item.strip() == "":
           print("Attention: Vous ne pouvez pas laisser un espace ou laisser vide cette donnée.")
           continue    
        shopping_list.append (item)


    # Summarizes the shopping list into an ordered list
    print("\nVotre liste de courses :")
    for articles in shopping_list:
        counter += 1
        print(f"{counter}. {articles}")


# Validates, modifies or cancels the list.
def get_user_choice():
    print("\nValidez-vous la liste de courses?\n"
        "2. Valider : enregistre la liste et quitte le programme\n"
        "1. Modifier : efface la liste pour en faire une nouvelle\n"
        "0. Quitter : efface la liste et quitte le programme\n")
    choice = input("Indiquez avec 0, 1 ou 2 votre choix : ")


    # Forces the user to enter 0,1 or 2
    while choice not in ["0", "1", "2"]:
        choice = input("Veuillez entrer un chiffre parmi 0, 1 ou 2 : ")


    # Execute user choice if valid
    choice = int(choice)
    match choice:
        case 2:
            print("\nListe de courses validée.\n")
        case 1:
            print("\nListe de courses effacée.\n")
            main()
        case 0:
            print("\nListe de courses annulée. Sortie du programme.\n")


def main():
    list_typing()
    get_user_choice()


# Start the program
main()