import tkinter as tk
from tkinter import colorchooser, messagebox
from datetime import datetime
import os


# =========================================================
# FENÊTRE PRINCIPALE
# =========================================================

root = tk.Tk()
root.title("IbrahPerso 1")
root.geometry("1000x650")
root.minsize(800, 500)

couleur_bureau = "#2f78c4"

root.configure(bg=couleur_bureau)


# =========================================================
# VARIABLES
# =========================================================

menu_ouvert = False
horloge_visible = True


# =========================================================
# ÉCRAN DE DÉMARRAGE
# =========================================================

root.withdraw()

demarrage = tk.Toplevel(root)
demarrage.overrideredirect(True)
demarrage.configure(bg="#111111")

largeur = 520
hauteur = 320

largeur_ecran = demarrage.winfo_screenwidth()
hauteur_ecran = demarrage.winfo_screenheight()

x = int((largeur_ecran / 2) - (largeur / 2))
y = int((hauteur_ecran / 2) - (hauteur / 2))

demarrage.geometry(
    f"{largeur}x{hauteur}+{x}+{y}"
)

logo = tk.Label(
    demarrage,
    text="IbrahPerso",
    font=("Arial", 34, "bold"),
    bg="#111111",
    fg="white"
)

logo.pack(pady=(80, 15))

version = tk.Label(
    demarrage,
    text="Version 1",
    font=("Arial", 13),
    bg="#111111",
    fg="#cccccc"
)

version.pack()

texte_demarrage = tk.Label(
    demarrage,
    text="Démarrage...",
    font=("Arial", 14),
    bg="#111111",
    fg="white"
)

texte_demarrage.pack(pady=35)


def terminer_demarrage():
    demarrage.destroy()
    root.deiconify()


root.after(2500, terminer_demarrage)


# =========================================================
# HORLOGE
# =========================================================

label_horloge = tk.Label(
    root,
    font=("Arial", 12),
    bg="black",
    fg="white"
)


def mettre_a_jour_horloge():

    heure = datetime.now().strftime("%H:%M:%S")

    label_horloge.config(
        text=heure
    )

    root.after(
        1000,
        mettre_a_jour_horloge
    )


mettre_a_jour_horloge()


# =========================================================
# APPLICATION FICHIERS
# =========================================================

def ouvrir_fichiers():

    fichiers = tk.Toplevel(root)
    fichiers.title("Fichiers")
    fichiers.geometry("700x520")
    fichiers.configure(bg="white")

    dossier_actuel = [os.getcwd()]

    # -----------------------------------------------------
    # TITRE
    # -----------------------------------------------------

    titre = tk.Label(
        fichiers,
        text="📁 Fichiers",
        font=("Arial", 22, "bold"),
        bg="white"
    )

    titre.pack(pady=(15, 5))

    # -----------------------------------------------------
    # CHEMIN ACTUEL
    # -----------------------------------------------------

    label_chemin = tk.Label(
        fichiers,
        text=dossier_actuel[0],
        font=("Arial", 10),
        bg="white",
        fg="#555555"
    )

    label_chemin.pack(pady=(0, 10))

    # -----------------------------------------------------
    # BARRE DE BOUTONS
    # -----------------------------------------------------

    barre_boutons = tk.Frame(
        fichiers,
        bg="white"
    )

    barre_boutons.pack(
        fill="x",
        padx=15,
        pady=5
    )

    # -----------------------------------------------------
    # LISTE DES FICHIERS
    # -----------------------------------------------------

    liste = tk.Listbox(
        fichiers,
        font=("Arial", 13),
        bg="#f4f4f4",
        selectbackground="#2f78c4",
        selectforeground="white"
    )

    liste.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=10
    )

    # -----------------------------------------------------
    # AFFICHER LE CONTENU
    # -----------------------------------------------------

    def afficher_contenu():

        liste.delete(
            0,
            tk.END
        )

        label_chemin.config(
            text=dossier_actuel[0]
        )

        try:

            elements = os.listdir(
                dossier_actuel[0]
            )

            elements.sort(
                key=lambda nom: (
                    not os.path.isdir(
                        os.path.join(
                            dossier_actuel[0],
                            nom
                        )
                    ),
                    nom.lower()
                )
            )

            for element in elements:

                chemin = os.path.join(
                    dossier_actuel[0],
                    element
                )

                if os.path.isdir(chemin):

                    liste.insert(
                        tk.END,
                        "📁 " + element
                    )

                else:

                    liste.insert(
                        tk.END,
                        "📄 " + element
                    )

        except PermissionError:

            messagebox.showerror(
                "Accès refusé",
                "IbrahPerso n'a pas l'autorisation "
                "d'ouvrir ce dossier."
            )

        except Exception as erreur:

            messagebox.showerror(
                "Erreur",
                str(erreur)
            )

    # -----------------------------------------------------
    # OUVRIR UN ÉLÉMENT
    # -----------------------------------------------------

    def ouvrir_element(event=None):

        selection = liste.curselection()

        if not selection:
            return

        texte = liste.get(
            selection[0]
        )

        nom = texte[2:]

        chemin = os.path.join(
            dossier_actuel[0],
            nom
        )

        if os.path.isdir(chemin):

            dossier_actuel[0] = chemin

            afficher_contenu()

        else:

            messagebox.showinfo(
                "Fichier",
                f"Fichier sélectionné :\n\n{nom}"
            )

    # -----------------------------------------------------
    # RETOUR
    # -----------------------------------------------------

    def retour():

        parent = os.path.dirname(
            dossier_actuel[0]
        )

        if parent != dossier_actuel[0]:

            dossier_actuel[0] = parent

            afficher_contenu()

    # -----------------------------------------------------
    # BOUTONS
    # -----------------------------------------------------

    bouton_retour = tk.Button(
        barre_boutons,
        text="← Retour",
        font=("Arial", 11),
        command=retour
    )

    bouton_retour.pack(
        side="left"
    )

    bouton_actualiser = tk.Button(
        barre_boutons,
        text="⟳ Actualiser",
        font=("Arial", 11),
        command=afficher_contenu
    )

    bouton_actualiser.pack(
        side="left",
        padx=8
    )

    liste.bind(
        "<Double-Button-1>",
        ouvrir_element
    )

    afficher_contenu()


# =========================================================
# CALCULATRICE
# =========================================================

def ouvrir_calculatrice():

    calculatrice = tk.Toplevel(root)
    calculatrice.title("Calculatrice")
    calculatrice.geometry("340x450")
    calculatrice.configure(bg="#252525")

    affichage = tk.Entry(
        calculatrice,
        font=("Arial", 22),
        justify="right"
    )

    affichage.pack(
        fill="x",
        padx=10,
        pady=10
    )

    def ajouter(valeur):

        affichage.insert(
            tk.END,
            valeur
        )

    def effacer():

        affichage.delete(
            0,
            tk.END
        )

    def calculer():

        try:

            expression = affichage.get()

            caracteres_autorises = (
                "0123456789+-*/(). "
            )

            for caractere in expression:

                if caractere not in caracteres_autorises:
                    raise ValueError

            resultat = eval(
                expression,
                {"__builtins__": {}},
                {}
            )

            affichage.delete(
                0,
                tk.END
            )

            affichage.insert(
                0,
                resultat
            )

        except:

            affichage.delete(
                0,
                tk.END
            )

            affichage.insert(
                0,
                "Erreur"
            )

    boutons = [
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("0", ".", "=", "+")
    ]

    for ligne in boutons:

        cadre = tk.Frame(
            calculatrice,
            bg="#252525"
        )

        cadre.pack()

        for texte in ligne:

            if texte == "=":
                commande = calculer

            else:
                commande = lambda x=texte: ajouter(x)

            bouton = tk.Button(
                cadre,
                text=texte,
                width=6,
                height=2,
                font=("Arial", 15),
                command=commande
            )

            bouton.pack(
                side="left",
                padx=3,
                pady=3
            )

    bouton_effacer = tk.Button(
        calculatrice,
        text="Effacer",
        font=("Arial", 13),
        command=effacer
    )

    bouton_effacer.pack(
        fill="x",
        padx=10,
        pady=10
    )


# =========================================================
# PARAMÈTRES
# =========================================================

def ouvrir_parametres():

    parametres = tk.Toplevel(root)
    parametres.title("Paramètres - IbrahPerso")
    parametres.geometry("700x520")
    parametres.configure(bg="#202020")

    titre = tk.Label(
        parametres,
        text="⚙ Paramètres",
        font=("Arial", 25, "bold"),
        bg="#202020",
        fg="white"
    )

    titre.pack(pady=20)

    # -----------------------------------------------------
    # CHANGER COULEUR DU BUREAU
    # -----------------------------------------------------

    def changer_couleur():

        global couleur_bureau

        couleur = colorchooser.askcolor()[1]

        if couleur:

            couleur_bureau = couleur

            root.configure(
                bg=couleur_bureau
            )

            titre_bureau.configure(
                bg=couleur_bureau
            )

            texte_bienvenue.configure(
                bg=couleur_bureau
            )

    bouton_couleur = tk.Button(
        parametres,
        text="🎨 Changer la couleur du bureau",
        font=("Arial", 13),
        width=34,
        command=changer_couleur
    )

    bouton_couleur.pack(
        pady=8
    )

    # -----------------------------------------------------
    # HORLOGE
    # -----------------------------------------------------

    def afficher_cacher_horloge():

        global horloge_visible

        horloge_visible = not horloge_visible

        if horloge_visible:

            label_horloge.pack(
                side="right",
                padx=15
            )

            bouton_horloge.config(
                text="🕐 Cacher l'horloge"
            )

        else:

            label_horloge.pack_forget()

            bouton_horloge.config(
                text="🕐 Afficher l'horloge"
            )

    bouton_horloge = tk.Button(
        parametres,
        text="🕐 Cacher l'horloge",
        font=("Arial", 13),
        width=34,
        command=afficher_cacher_horloge
    )

    bouton_horloge.pack(
        pady=8
    )

    # -----------------------------------------------------
    # À PROPOS
    # -----------------------------------------------------

    def a_propos():

        messagebox.showinfo(
            "À propos",
            "IbrahPerso 1\n\n"
            "Interface personnelle créée en Python.\n"
            "Interface graphique : Tkinter."
        )

    bouton_apropos = tk.Button(
        parametres,
        text="ℹ À propos de IbrahPerso",
        font=("Arial", 13),
        width=34,
        command=a_propos
    )

    bouton_apropos.pack(
        pady=8
    )

    # -----------------------------------------------------
    # REDÉMARRAGE
    # -----------------------------------------------------

    def redemarrer_interface():

        reponse = messagebox.askyesno(
            "Redémarrer",
            "Voulez-vous redémarrer IbrahPerso ?"
        )

        if reponse:

            parametres.destroy()
            root.withdraw()

            nouveau_demarrage = tk.Toplevel(root)

            nouveau_demarrage.overrideredirect(
                True
            )

            nouveau_demarrage.configure(
                bg="#111111"
            )

            largeur = 520
            hauteur = 320

            x = int(
                (root.winfo_screenwidth() / 2)
                -
                (largeur / 2)
            )

            y = int(
                (root.winfo_screenheight() / 2)
                -
                (hauteur / 2)
            )

            nouveau_demarrage.geometry(
                f"{largeur}x{hauteur}+{x}+{y}"
            )

            label = tk.Label(
                nouveau_demarrage,
                text="IbrahPerso",
                font=("Arial", 34, "bold"),
                bg="#111111",
                fg="white"
            )

            label.pack(
                pady=(90, 20)
            )

            texte = tk.Label(
                nouveau_demarrage,
                text="Redémarrage...",
                font=("Arial", 14),
                bg="#111111",
                fg="white"
            )

            texte.pack()

            def retour_bureau():

                nouveau_demarrage.destroy()
                root.deiconify()

            root.after(
                2000,
                retour_bureau
            )

    bouton_redemarrer = tk.Button(
        parametres,
        text="🔄 Redémarrer IbrahPerso",
        font=("Arial", 13),
        width=34,
        command=redemarrer_interface
    )

    bouton_redemarrer.pack(
        pady=8
    )

    # -----------------------------------------------------
    # FERMER
    # -----------------------------------------------------

    bouton_fermer = tk.Button(
        parametres,
        text="Fermer",
        font=("Arial", 13),
        width=20,
        command=parametres.destroy
    )

    bouton_fermer.pack(
        pady=30
    )


# =========================================================
# MENU
# =========================================================

def ouvrir_menu():

    global menu_ouvert

    if menu_ouvert:

        menu_frame.place_forget()

        menu_ouvert = False

    else:

        root.update_idletasks()

        menu_frame.place(
            x=5,
            y=root.winfo_height() - 275
        )

        menu_frame.lift()

        menu_ouvert = True


menu_frame = tk.Frame(
    root,
    bg="#303030",
    width=260,
    height=220
)

menu_frame.pack_propagate(
    False
)

bouton_fichiers = tk.Button(
    menu_frame,
    text="📁 Fichiers",
    font=("Arial", 13),
    anchor="w",
    command=ouvrir_fichiers
)

bouton_fichiers.pack(
    fill="x",
    padx=10,
    pady=(15, 5)
)

bouton_calculatrice = tk.Button(
    menu_frame,
    text="🧮 Calculatrice",
    font=("Arial", 13),
    anchor="w",
    command=ouvrir_calculatrice
)

bouton_calculatrice.pack(
    fill="x",
    padx=10,
    pady=5
)

bouton_parametres = tk.Button(
    menu_frame,
    text="⚙ Paramètres",
    font=("Arial", 13),
    anchor="w",
    command=ouvrir_parametres
)

bouton_parametres.pack(
    fill="x",
    padx=10,
    pady=5
)

bouton_quitter = tk.Button(
    menu_frame,
    text="⏻ Éteindre",
    font=("Arial", 13),
    anchor="w",
    command=root.destroy
)

bouton_quitter.pack(
    fill="x",
    padx=10,
    pady=5
)


# =========================================================
# BARRE DES TÂCHES
# =========================================================

barre = tk.Frame(
    root,
    bg="black",
    height=48
)

barre.pack(
    side="bottom",
    fill="x"
)

barre.pack_propagate(
    False
)

bouton_menu = tk.Button(
    barre,
    text="☰ Menu",
    font=("Arial", 12, "bold"),
    command=ouvrir_menu
)

bouton_menu.pack(
    side="left",
    padx=6,
    pady=6
)

label_horloge.pack(
    side="right",
    padx=15
)


# =========================================================
# BUREAU
# =========================================================

titre_bureau = tk.Label(
    root,
    text="IbrahPerso 1",
    font=("Arial", 21, "bold"),
    bg=couleur_bureau,
    fg="white"
)

titre_bureau.place(
    x=20,
    y=20
)

texte_bienvenue = tk.Label(
    root,
    text="Bienvenue",
    font=("Arial", 13),
    bg=couleur_bureau,
    fg="white"
)

texte_bienvenue.place(
    x=22,
    y=60
)


# =========================================================
# RACCOURCIS DU BUREAU
# =========================================================

raccourci_fichiers = tk.Button(
    root,
    text="📁\nFichiers",
    font=("Arial", 12),
    width=10,
    height=4,
    command=ouvrir_fichiers
)

raccourci_fichiers.place(
    x=30,
    y=120
)

raccourci_calculatrice = tk.Button(
    root,
    text="🧮\nCalculatrice",
    font=("Arial", 12),
    width=10,
    height=4,
    command=ouvrir_calculatrice
)

raccourci_calculatrice.place(
    x=30,
    y=220
)

raccourci_parametres = tk.Button(
    root,
    text="⚙\nParamètres",
    font=("Arial", 12),
    width=10,
    height=4,
    command=ouvrir_parametres
)

raccourci_parametres.place(
    x=30,
    y=320
)


# =========================================================
# LANCEMENT
# =========================================================

root.mainloop()