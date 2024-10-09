import tkinter as tk
from tkinter import messagebox

# Calculate tip percentage (amount * (tip / 100))
def tip_percentage_calculation(amount, tip):
    return amount * (tip / 100)

# Validate integer input
def integer_check(entry):
    try:
        value = int(entry)
        return value
    except ValueError:
        return None

# Function to calculate and display the tip
def calculate_tip():
    amount_bill = integer_check(bill_entry.get())
    tip_desired = integer_check(tip_entry.get())
    
    if amount_bill is None or amount_bill < 0:
        messagebox.showerror("Erreur", "Veuillez entrer un montant valide pour l'addition.")
        return
    if tip_desired is None or tip_desired < 0:
        messagebox.showerror("Erreur", "Veuillez entrer un pourcentage de pourboire valide.")
        return
    
    tip_amount = tip_percentage_calculation(amount_bill, tip_desired)
    total_amount = amount_bill + tip_amount
    
    confirmation = messagebox.askquestion("Confirmation", 
        f"Vous vous apprêtez à valider une addition de {amount_bill:.2f} €, "
        f"avec un pourboire de {tip_amount:.2f} €, soit un total de {total_amount:.2f} €.\n\n"
        "Confirmez-vous le pourboire ?")
    
    if confirmation == 'yes':
        messagebox.showinfo("Confirmation", 
            f"Opération confirmée.\n"
            f"Addition : {amount_bill:.2f} €\n"
            f"Pourboire : {tip_amount:.2f} €\n"
            f"Pourcentage pourboire : {tip_desired:.2f} %\n"
            f"Total : {total_amount:.2f} €")
    else:
        messagebox.showinfo("Annulé", "Retour à l'accueil.")

# Set up the main application window
app = tk.Tk()
app.title("Calculateur de Pourboire")

# Create and place the labels and entry fields
tk.Label(app, text="Montant total de l'addition :").grid(row=0, column=0, padx=10, pady=10)
bill_entry = tk.Entry(app)
bill_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Montant du pourboire désiré (en %) :").grid(row=1, column=0, padx=10, pady=10)
tip_entry = tk.Entry(app)
tip_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the Calculate button
calculate_button = tk.Button(app, text="Calculer", command=calculate_tip)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Run the application
app.mainloop()
