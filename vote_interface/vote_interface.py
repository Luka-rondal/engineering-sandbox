import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

list_dishes = ["Pizza", "Burger", "Nuggets", "Noodles", "Salad", "Sandwich"]


# Class to access vote list
class vote:
    def __init__(self):
        self.reset_list()

    def reset_list(self):
        self.vote_list = [0, 0, 0, 0, 0, 0]

    def increment_vote_by_index(self, i):
        self.vote_list[i] += 1

    def get_winner(self):
        win = []
        for i in range(len(self.vote_list)):
            if self.vote_list[i] == max(self.vote_list):
                win.append(list_dishes[i])
        return win

    def is_reset(self):
        if self.vote_list == [0, 0, 0, 0, 0, 0]:
            return True
        else:
            return False


res_vote = vote()


class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("650x500")
        self.title("Vote for your favorite dish")

        # Background
        img = Image.open("background.jpg")
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
        for F in (StartPage, VotePage, ResultPage, WinnerPage):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, frame):
        frame = self.frames[frame]
        # refresh when resultPage is load to get the number of votes
        if frame is ResultPage:
            for i in range(6):
                frame.labels_list[i].config(
                    text=f"{list_dishes[i]}: {res_vote.vote_list[i]} votes"
                )
        # refresh when winnerPage is load to get the winner(s)
        if frame == WinnerPage:
            frame.create_labels()
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img = Image.open("background.jpg")
        self.bg_img = ImageTk.PhotoImage(img)

        bg_label = tk.Label(self, image=self.bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # label of frame Layout 2
        title_label = tk.Label(
            self,
            text="Vote for your favorite food",
            font=(
                "Arial",
                24,
            ),
            fg="white",
            bg="#111827",
        )

        # putting the grid in its place by using .place
        title_label.place(relx=0.5, y=40, anchor="center")

        button_vote = ttk.Button(
            self, text="Vote", command=lambda: controller.show_frame(VotePage)
        )

        button_vote.place(relx=0.5, y=100, anchor="center")

        button_result = ttk.Button(
            self, text="Result", command=lambda: controller.show_frame(ResultPage)
        )

        button_result.place(relx=0.5, y=200, anchor="center")

        button_winner = ttk.Button(
            self, text="Winner", command=lambda: controller.show_frame(WinnerPage)
        )

        button_winner.place(relx=0.5, y=300, anchor="center")

        button_reset = ttk.Button(self, text="Reset", command=res_vote.reset_list)

        button_reset.place(relx=0.5, y=400, anchor="center")


# second window frame (votePage)
class VotePage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        img = Image.open("background.jpg")
        self.bg_img = ImageTk.PhotoImage(img)

        bg_label = tk.Label(self, image=self.bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        buttons_list = [None] * 6
        cols_relx = [0.166, 0.5, 0.833]
        rows_rely = [0.25, 0.65]

        # Show button to vote for dishes
        for i in range(6):
            row = i // 3
            col = i % 3
            buttons_list[i] = ttk.Button(
                self,
                text=list_dishes[i],
                command=lambda i=i: res_vote.increment_vote_by_index(i),
            )
            buttons_list[i].place(
                relx=cols_relx[col], rely=rows_rely[row], anchor="center"
            )

        button_StartPage = ttk.Button(
            self, text="Menu", command=lambda: controller.show_frame(StartPage)
        )
        button_StartPage.grid()


class ResultPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img = Image.open("background.jpg")
        self.bg_img = ImageTk.PhotoImage(img)

        bg_label = tk.Label(self, image=self.bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        button_StartPage = ttk.Button(
            self, text="Menu", command=lambda: controller.show_frame(StartPage)
        )
        button_StartPage.grid()

        self.labels_list = [None] * 6
        cols_relx = [0.166, 0.5, 0.833]
        rows_rely = [0.25, 0.65]

        # Show labels with votes results
        for i in range(6):
            row = i // 3
            col = i % 3
            self.labels_list[i] = tk.Label(
                self,
                text=f"{list_dishes[i]}: {res_vote.vote_list[i]} votes",
                font=("Arial", 12),
                fg="white",
                bg="#111827",
            )
            self.labels_list[i].place(
                relx=cols_relx[col], rely=rows_rely[row], anchor="center"
            )


class WinnerPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        img = Image.open("background.jpg")
        self.bg_img = ImageTk.PhotoImage(img)

        bg_label = tk.Label(self, image=self.bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        button_StartPage = ttk.Button(
            self, text="Menu", command=lambda: controller.show_frame(StartPage)
        )
        button_StartPage.grid()
        self.label_list = []

    def create_labels(self):
        # Remove actual label
        for label in self.label_list:
            label.destroy()
        self.label_list = []
        if res_vote.is_reset():
            return
        n = len(res_vote.get_winner())
        if n == 0:
            return

        font_size = 20
        i = 0
        # Show the list of winners
        for winner in res_vote.get_winner():
            label = tk.Label(
                self,
                text=winner,
                font=("arial", font_size, "bold"),
                fg="white",
                bg="#111827",
            )
            label.place(relx=0.5, y=100 + 50 * i, anchor="center")
            i += 1
            self.label_list.append(label)


# Driver Code
app = tkinterApp()
app.mainloop()
