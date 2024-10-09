import string
from random import choice, randint
from tkinter import *

def genrate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max))) 
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# creer la fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.minsize(700,400)
window.config(background="#8F1D14")

# creer la frame principale
frame = Frame(window, bg="#8F1D14")

# creer une sous boite
right_frame = Frame(frame, bg="#8F1D14")

# creer un titre
label_title = Label (right_frame, text="Générer un mot de passe", font=("Helvetica", 18), bg="#8F1D14", fg="white")
label_title.pack()

# creer un champ/entree/input
password_entry = Entry (right_frame, font=("Helvetica", 20), bg="white", fg="#1B120F")
password_entry.pack()

# creer un bouton
generate_password_button = Button (right_frame, text="Générer", font=("Helvetica", 20), bg="#1B120F", fg="white", command=genrate_password)
generate_password_button.pack(fill=X,)

# on place la sous_boite a droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

# afficher la frame
frame.pack(expand=YES)

# afficher la fenetres
window.mainloop()