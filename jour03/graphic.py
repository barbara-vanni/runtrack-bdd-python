import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog
from Shop import Shop
from Popup import ModifierProduitPopup



class GUI:
    def __init__(self, root, shop):
        self.root = root
        self.root.title("Store")
        self.shop = Shop()

        # Création d'un cadre principal
        main_frame = tk.Frame(root)
        main_frame.pack(padx=10, pady=10)

        # Création des sous-cadres
        input_frame = tk.Frame(main_frame)
        input_frame.pack(side=tk.TOP, padx=10, pady=10)

        buttons_frame = tk.Frame(main_frame)
        buttons_frame.pack(pady=10)

        tree_frame = tk.Frame(main_frame)
        tree_frame.pack(pady=10)


        self.nom_produit_label = tk.Label(input_frame, text="Nom du Produit:")
        self.nom_produit_entry = tk.Entry(input_frame)

        self.description_produit_label = tk.Label(input_frame, text="Description du Produit:")
        self.description_produit_entry = tk.Entry(input_frame)

        self.quantite_produit_label = tk.Label(input_frame, text="Quantité du Produit:")
        self.quantite_produit_entry = tk.Entry(input_frame)

        self.prix_produit_label = tk.Label(input_frame, text="Prix du Produit:")
        self.prix_produit_entry = tk.Entry(input_frame)

        self.category_label = tk.Label(input_frame, text="Category:")
        self.category_entry = tk.Entry(input_frame)


        self.nom_produit_label.grid(row=0, column=0, padx=10, pady=10)
        self.nom_produit_entry.grid(row=0, column=1, padx=10, pady=10)

        self.description_produit_label.grid(row=1, column=0, padx=10, pady=10)
        self.description_produit_entry.grid(row=1, column=1, padx=10, pady=10)

        self.quantite_produit_label.grid(row=2, column=0, padx=10, pady=10)
        self.quantite_produit_entry.grid(row=2, column=1, padx=10, pady=10)

        self.prix_produit_label.grid(row=3, column=0, padx=10, pady=10)
        self.prix_produit_entry.grid(row=3, column=1, padx=10, pady=10)

        self.category_label.grid(row=4, column=0, padx=10, pady=10)
        self.category_entry.grid(row=4, column=1, padx=10, pady=10)


        self.ajouter_button = tk.Button(buttons_frame, text="Ajouter Produit", command=self.ajouter_produit)
        self.supprimer_button = tk.Button(buttons_frame, text="Supprimer Produit", command=self.supprimer_produit)
        self.modifier_button = tk.Button(buttons_frame, text="Modifier Produit", command=self.modifier_produit)

        self.ajouter_button.grid(row=0, column=0, padx=10, pady=10)
        self.supprimer_button.grid(row=0, column=1, padx=10, pady=10)
        self.modifier_button.grid(row=0, column=2, padx=10, pady=10)


        self.tree = ttk.Treeview(tree_frame, columns=('ID', 'Nom', 'Description', 'Prix', 'Quantite', 'Categorie'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nom', text='Nom')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Prix', text='Prix')
        self.tree.heading('Quantite', text='Quantite')
        self.tree.heading('Categorie', text='Categorie')


        self.tree.grid(row=0, column=0, padx=10, pady=10)


        self.label_category_filter = tk.Label(root, text="Filtrer par catégorie:")
        self.category_filter_var = tk.StringVar()
        self.category_filter_var.set("Toutes les catégories")
        self.category_filter = ttk.Combobox(root, textvariable=self.category_filter_var, values=["Toutes les catégories"] + shop.read_Category())
        self.category_filter.bind("<<ComboboxSelected>>", self.afficher_produits_par_categorie)


        self.label_category_filter.pack(side='top', padx=10, pady=10)
        self.category_filter.pack(side='top', padx=10, pady=10)


        self.afficher_produits()

    def ajouter_produit(self):
        nom_produit = self.nom_produit_entry.get()
        description_produit = self.description_produit_entry.get()
        prix_produit = self.prix_produit_entry.get()
        quantite_produit = self.quantite_produit_entry.get()
        category = self.category_entry.get()


        self.shop.create_Product(nom_produit, description_produit, prix_produit, quantite_produit, category)


        self.afficher_produits()

    def supprimer_produit(self):

        selected_item = self.tree.selection()
        if selected_item:

            id = self.tree.item(selected_item, 'values')[0]

            self.shop.delete_Product(id)

            self.afficher_produits()

    def modifier_produit(self):

        selected_item = self.tree.selection()

        if selected_item:

            product_id = self.tree.item(selected_item, 'values')[0]

            selected_product = self.shop.find_Product(product_id)

            modifier_popup = ModifierProduitPopup(self.root, selected_product)
            self.root.wait_window(modifier_popup)

            modified_values = modifier_popup.modified_values
            if modified_values:
                new_name, new_price, new_quantity = modified_values
                self.shop.update_Product(product_id, new_name, new_price, new_quantity)
                self.afficher_produits()

    def show_modify_popup(self, product_data):
        popup = tk.Toplevel(self.root)
        popup.title("Modifier Produit")


        modify_button = tk.Button(popup, text="Modifier", command=lambda: self.on_modify_button_click(popup))
        modify_button.pack(padx=10, pady=10)

        popup.wait_window()

        return self.modified_values

    def on_modify_button_click(self, popup):
        self.modified_values = (
            self.modified_nom_produit_entry.get(),
            self.modified_description_produit_entry.get(),
            self.modified_prix_produit_entry.get(),
            self.modified_quantite_produit_entry.get()
        )
        popup.destroy()


    def afficher_produits(self):
        self.tree.delete(*self.tree.get_children())
        if self.tree:
            for row in self.tree.get_children():
                if row:  
                    self.tree.delete(row)

        produits = self.shop.read_Product()


        for produit in produits:
            self.tree.insert('', 'end', values=produit)


        categories = ["Toutes les catégories"] + self.shop.read_Category()
        self.category_filter['values'] = categories
        self.category_filter_var.set("Toutes les catégories")


    def afficher_produits_par_categorie(self, event):
        selected_category = self.category_filter_var.get()
        if selected_category == "Toutes les catégories":
            self.afficher_produits()
        else:

            self.category_filter_var.set(selected_category)

            categories = ["Toutes les catégories"] + self.shop.read_Category()
            self.category_filter['values'] = categories


            self.afficher_produits_par_categorie_impl()

    def afficher_produits_par_categorie_impl(self):
        selected_category = self.category_filter_var.get()

        produits = self.shop.read_Product(category=selected_category)
        
        for row in self.tree.get_children():
            self.tree.delete(row)

        for produit in produits:
            self.tree.insert('', 'end', values=produit)


root = tk.Tk()
shop = Shop()

gui_instance = GUI(root, shop)