import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


def main():
    root = tk.Tk()
    root.title("Vote for your favorite food")
    root.geometry("900x520")
    root.minsize(820, 480)
    root.configure(bg="#03163D")

    #header
    header = tk.Frame(root, bg="#111827", padx=18, pady=14)
    header.pack(fill="x")

    root.mainloop()



if __name__ == "__main__":
    main()