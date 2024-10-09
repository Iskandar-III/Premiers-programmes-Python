"""
The purpose of this calculator is to calculate a tip. 
From the amount of a bill, the customer can choose to tip.
If they don't want to, they can indicate 0.
If the user indicates something else, the calculator asks them to correct it.
Confirmation is requested from the user at the end of the process.
If the user indicates anything other than 0 or 1, the calculator asks them to correct it.
The calculator stops when the confirmation is correctly validated or refused.
"""


# Calculate tip percentage (amount * (tip /100))
def tip_percentage_calculation(amount, tip):
    return int(amount) * (int(tip) / 100)


# Check that the variable is an integer
def integer_check(number):
    while not number.isdigit():
        number = input("Veuillez entrer un nombre entier valide : ")
    return int(number)


# Ask customers if they want to leave a tip
def billing ():
    amount_bill = integer_check(input("\nMontant total de l'addition : "))
    tip_desired = integer_check(input("\nMontant du pourboire desire (en pourcentage) : "))
    tip_amount = tip_percentage_calculation(amount_bill, tip_desired)
    print(f"Montant du pourboire : {tip_amount:.2f} €")
    return amount_bill, tip_amount, tip_desired


# Use the “tip calculator” function and immediately store the result
bill_amount, tip_amount, tip_percentage = billing()


# Calculate the total amount to be paid
total_amount = bill_amount + tip_amount


# Asks customers for confirmation
print(f"\nVous vous appretez à valider une addition de {bill_amount} €, avec un pourboire de {tip_amount} €, soit un total de {total_amount} €.")
print("Confirmez-vous le pourboire ?")
print("0. Annuler")
print("1. Confirmer\n")


# Check that the choice is strictly 0 or 1
confirmation = input("Choix : ")
while confirmation not in ["0", "1"]:
    confirmation = input("Veuillez entrer un choix valide (0 ou 1) : ")
confirmation = int(confirmation)


# If choice OK, end program
match confirmation:
    case 0:
        print("\nRetour à l'Accueil.")
    case 1: 
        print("\nOpération confirmée.\n"
              f"Addition : {bill_amount:.2f} €\n"
              f"Pourboire : {tip_amount:.2f} €\n"
              f"Pourcentage pourboire : {tip_percentage:.2f} %\n"
              f"Total : {total_amount:.2f} €")