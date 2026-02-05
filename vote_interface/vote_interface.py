import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("650x1155")
        self.title("Vote for your favorite dish")
        # Background
        
        img = Image.open('background.jpg')
        self.bg_img = ImageTk.PhotoImage(img)

        bg_label = tk.Label(self, image=self.bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img = Image.open("background.jpg")
        self.bg_img = ImageTk.PhotoImage(img)

        bg_label = tk.Label(self, image=self.bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # label of frame Layout 2
        title_label = tk.Label(self, text="Vote for your favorite food",
                       font=("Arial", 24, ),
                       fg="white", bg="#111827")

        # putting the grid in its place by using
        title_label.place(relx=0.5, y=40, anchor="center")

        button_vote = ttk.Button(
            self, text="Vote", command=lambda: controller.show_frame(VotePage)
        )
        
        # putting the button in its place by
        button_vote.place(relx=0.5, y=200, anchor="center")

        button_result = ttk.Button(
            self, text="Result", command=lambda: controller.show_frame(ResultPage)
        )
        
        # putting the button in its place by
        button_result.place(relx=0.5, y=450, anchor="center")

        button_winner = ttk.Button(
            self, text="Winner", command=lambda: controller.show_frame(WinnerPage)
        )
        
        # putting the button in its place by
        button_winner.place(relx=0.5, y=700, anchor="center")

        button_reset = ttk.Button(
            self, text="Reset"
        )
        
        # putting the button in its place by
        button_reset.place(relx=0.5, y=950, anchor="center")



# second window frame page1
class Page1(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(
            self, text="StartPage", command=lambda: controller.show_frame(StartPage)
        )

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
