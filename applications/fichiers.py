# =========================================================
# FICHIERS
# =========================================================

def ouvrir_fichiers():

    fichiers = tk.Toplevel(root)
    fichiers.title("Fichiers - IbrahPerso 1")
    fichiers.geometry("650x500")
    fichiers.configure(bg="white")

    # Dossier de départ
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

        liste.delete(0, tk.END)

        label_chemin.config(
            text=dossier_actuel[0]
        )

        try:

            elements = os.listdir(
                dossier_actuel[0]
            )

            # Dossiers d'abord, fichiers ensuite
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

    # -----------------------------------------------------
    # OUVRIR UN DOSSIER
    # -----------------------------------------------------

    def ouvrir_element(event=None):

        selection = liste.curselection()

        if not selection:
            return

        texte = liste.get(
            selection[0]
        )

        # On enlève "📁 " ou "📄 "
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

        # Empêche de remonter indéfiniment
        if parent != dossier_actuel[0]:

            dossier_actuel[0] = parent

            afficher_contenu()

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

    # Double clic
    liste.bind(
        "<Double-Button-1>",
        ouvrir_element
    )

    # Premier affichage
    afficher_contenu()