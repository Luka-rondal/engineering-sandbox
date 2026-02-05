import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk



interface = 0
def change_interface(n):
    global interface
    interface = n


def main():
    root = tk.Tk()
    root.title("Vote for your favorite food")
    root.geometry("650x1155")
    
    
    img = Image.open(r"C:\Users\15691\epf-programming\python projet\engineering-sandbox\vote_interface\background.jpg")
    bg_img = ImageTk.PhotoImage(img)

    root.bg_img = bg_img  
    bg_label = tk.Label(root, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)


    # header
    header = tk.Frame(root, bg="#111827", padx=18, pady=14)
    header.pack(fill="x")

    if interface == 0:
        vote_button = ttk.Button(root, text="Vote", command=change_interface(1))
        result_button = ttk.Button(root, text="Results", command=change_interface(2))
        winner_button = ttk.Button(root, text="Winner", command=change_interface(3))

        vote_button.pack(ipadx=5, ipady=5, expand=True)
        result_button.pack(ipadx=5, ipady=5, expand=True)
        winner_button.pack(ipadx=5, ipady=5, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
