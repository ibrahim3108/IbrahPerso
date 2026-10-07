import tkinter as tk


def ouvrir_calculatrice(fenetre_principale):
    calc = tk.Toplevel(fenetre_principale)
    calc.title("Calculatrice - IbrahPerso 1")
    calc.geometry("320x430")
    calc.resizable(False, False)

    ecran = tk.Entry(
        calc,
        font=("Arial", 22),
        justify="right"
    )
    ecran.pack(fill="x", padx=10, pady=10, ipady=10)

    def ajouter(valeur):
        ecran.insert("end", valeur)

    def effacer():
        ecran.delete(0, "end")

    def calculer():
        try:
            expression = ecran.get()

            autorises = "0123456789+-*/(). "

            if all(caractere in autorises for caractere in expression):
                resultat = eval(expression, {"__builtins__": None}, {})
                ecran.delete(0, "end")
                ecran.insert(0, str(resultat))
            else:
                ecran.delete(0, "end")
                ecran.insert(0, "Erreur")

        except:
            ecran.delete(0, "end")
            ecran.insert(0, "Erreur")

    cadre = tk.Frame(calc)
    cadre.pack()

    boutons = [
        ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
        ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
        ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
        ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3)
    ]

    for texte, ligne, colonne in boutons:
        if texte == "=":
            commande = calculer
        else:
            commande = lambda valeur=texte: ajouter(valeur)

        bouton = tk.Button(
            cadre,
            text=texte,
            font=("Arial", 18),
            width=5,
            height=2,
            command=commande
        )
        bouton.grid(row=ligne, column=colonne, padx=3, pady=3)

    bouton_effacer = tk.Button(
        calc,
        text="Effacer",
        font=("Arial", 16),
        command=effacer
    )
    bouton_effacer.pack(fill="x", padx=10, pady=10)