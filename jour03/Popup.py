import tkinter as tk
from tkinter import ttk
from Shop import Shop

class ModifierProduitPopup(tk.Toplevel):
    def __init__(self, parent, product_info):
        super().__init__(parent)
        self.parent = parent
        self.product_info = product_info

        self.title("Modifier Produit")
        self.modified_values = None


        self.label_nom = tk.Label(self, text="Nom du produit:")
        self.entry_nom = tk.Entry(self)
        self.label_prix = tk.Label(self, text="Prix du produit:")
        self.entry_prix = tk.Entry(self)
        self.label_quantite = tk.Label(self, text="Quantité du produit:")
        self.quantite_entry = tk.Entry(self)

        self.btn_valider = tk.Button(self, text="Valider", command=self.valider_modification)


        self.label_nom.grid(row=0, column=0, sticky=tk.W)
        self.entry_nom.grid(row=0, column=1)
        self.label_prix.grid(row=1, column=0, sticky=tk.W)
        self.entry_prix.grid(row=1, column=1)
        self.label_quantite.grid(row=2, column=0, sticky=tk.W)
        self.quantite_entry.grid(row=2, column=1)

        self.btn_valider.grid(row=3, column=0, columnspan=2, pady=10)


    def valider_modification(self):

        new_name = self.entry_nom.get()
        new_price = self.entry_prix.get()
        new_quantity = self.quantite_entry.get()

        if hasattr(self.parent, 'shop'):
            self.modified_values = (new_name, new_price, new_quantity)
            self.shop.update_Product(self.product_info[0], new_name, new_price, new_quantity)
            self.afficher_produits()
            self.destroy()
        else:
            print("Parent does not have 'shop' attribute.")

