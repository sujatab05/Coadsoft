import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")

        self.user_choice = ""
        self.computer_choice = ""
        self.outcome = ""

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(master, text="Choose rock, paper, or scissors:")
        self.label.pack()

        self.choice_var = tk.StringVar()
        self.choice_var.set("rock")

        self.choices = ["rock", "paper", "scissors"]
        self.choice_menu = tk.OptionMenu(master, self.choice_var, *self.choices)
        self.choice_menu.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play_game)
        self.play_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.score_label = tk.Label(master, text="")
        self.score_label.pack()

    def play_game(self):
        self.user_choice = self.choice_var.get()
        self.computer_choice = random.choice(self.choices)

        if self.user_choice == self.computer_choice:
            self.outcome = "It's a tie!"
        elif (self.user_choice == "rock" and self.computer_choice == "scissors") or \
                (self.user_choice == "paper" and self.computer_choice == "rock") or \
                (self.user_choice == "scissors" and self.computer_choice == "paper"):
            self.outcome = "You win!"
            self.user_score += 1
        else:
            self.outcome = "You lose!"
            self.computer_score += 1

        self.update_result()

    def update_result(self):
        result_text = f"You chose {self.user_choice}. Computer chose {self.computer_choice}. {self.outcome}"
        self.result_label.config(text=result_text)

        score_text = f"Score: You {self.user_score} - {self.computer_score} Computer"
        self.score_label.config(text=score_text)

        messagebox.showinfo("Result", result_text)


def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
