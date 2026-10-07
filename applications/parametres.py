import tkinter as tk
from tkinter import colorchooser, messagebox


def ouvrir_parametres(fenetre_principale):

    parametres = tk.Toplevel(fenetre_principale)
    parametres.title("Paramètres - IbrahPerso")
    parametres.geometry("650x450")
    parametres.configure(bg="#202020")

    # Empêche d'ouvrir la fenêtre derrière la principale
    parametres.transient(fenetre_principale)

    # -------------------------
    # TITRE
    # -------------------------

    titre = tk.Label(
        parametres,
        text="⚙ Paramètres",
        font=("Arial", 24, "bold"),
        bg="#202020",
        fg="white"
    )

    titre.pack(pady=20)

    # -------------------------
    # FOND DU BUREAU
    # -------------------------

    def changer_couleur():

        couleur = colorchooser.askcolor()[1]

        if couleur:
            fenetre_principale.configure(bg=couleur)

    bouton_couleur = tk.Button(
        parametres,
        text="🎨 Changer la couleur du bureau",
        font=("Arial", 13),
        width=30,
        command=changer_couleur
    )

    bouton_couleur.pack(pady=10)

    # -------------------------
    # À PROPOS
    # -------------------------

    def a_propos():

        messagebox.showinfo(
            "À propos",
            "IbrahPerso 1\n\n"
            "Système personnel créé en Python.\n"
            "Interface graphique : Tkinter"
        )

    bouton_apropos = tk.Button(
        parametres,
        text="ℹ À propos de IbrahPerso",
        font=("Arial", 13),
        width=30,
        command=a_propos
    )

    bouton_apropos.pack(pady=10)

    # -------------------------
    # REDÉMARRAGE INTERFACE
    # -------------------------

    def message_redemarrage():

        messagebox.showinfo(
            "Redémarrage",
            "La fonction de redémarrage sera ajoutée plus tard."
        )

    bouton_redemarrer = tk.Button(
        parametres,
        text="🔄 Redémarrer IbrahPerso",
        font=("Arial", 13),
        width=30,
        command=message_redemarrage
    )

    bouton_redemarrer.pack(pady=10)

    # -------------------------
    # FERMER
    # -------------------------

    bouton_fermer = tk.Button(
        parametres,
        text="Fermer",
        font=("Arial", 13),
        width=20,
        command=parametres.destroy
    )

    bouton_fermer.pack(pady=30)
    