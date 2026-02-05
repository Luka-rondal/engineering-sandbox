# 🍽️ Food Voting App (Tkinter)

Une application graphique en **Python / Tkinter** permettant aux utilisateurs de voter pour leur plat préféré et d’afficher les résultats ainsi que le(s) gagnant(s).

---

## 📌 Fonctionnalités

- 🗳️ Vote pour un plat parmi une liste prédéfinie
- 📊 Affichage des résultats en temps réel
- 🏆 Affichage du ou des plats gagnants (gestion des égalités)
- 🔄 Réinitialisation des votes
- 🖼️ Interface graphique

---

## 🛠️ Technologies utilisées

- **Python 3**
- **Tkinter**
- **ttk**
- **Pillow (PIL)** pour la gestion des images

---

## 📂 Structure de l’application

L’application est construite autour d’une classe principale `tkinterApp` qui gère plusieurs pages :

- `StartPage` → Menu principal
- `VotePage` → Page de vote
- `ResultPage` → Résultats des votes
- `WinnerPage` → Affichage du ou des gagnants

Chaque page est un `tk.Frame` affiché dynamiquement.

---

## 🍕 Plats disponibles

```python
list_dishes = ["Pizza", "Burger", "Nuggets", "Noodles", "Salad", "Sandwich"]
```
## Remarks
This README has been generate by AI. AI Has been use to know how to refresh a frame before showing it. The basics of frames on tinker come from [Guide Tkinter : changer de pages avec des Frames](https://www.geeksforgeeks.org/python/tkinter-application-to-switch-between-different-page-frames/)

The exemple of this website has been use as start template.