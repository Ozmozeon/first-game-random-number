import random
import tkinter as tk
from tkinter import messagebox


class GuessingGameGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Guess the Number")

        # Game state
        self.secret = random.randint(1, 100)
        self.tries = 0

        # UI
        self.title_label = tk.Label(root, text="Guess a number between 1 and 100")
        self.title_label.pack(padx=12, pady=(12, 6))

        self.info_label = tk.Label(root, text="Enter your guess:")
        self.info_label.pack(padx=12, pady=(0, 6))

        self.guess_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.guess_var)
        self.entry.pack(padx=12, pady=(0, 10))
        self.entry.focus()

        self.result_label = tk.Label(root, text="", font=("Segoe UI", 10))
        self.result_label.pack(padx=12, pady=(0, 10))

        btn_frame = tk.Frame(root)
        btn_frame.pack(padx=12, pady=(0, 12))

        self.guess_btn = tk.Button(btn_frame, text="Guess", command=self.make_guess)
        self.guess_btn.pack(side=tk.LEFT, padx=(0, 8))

        self.new_btn = tk.Button(btn_frame, text="New Game", command=self.new_game)
        self.new_btn.pack(side=tk.LEFT)

        # Enter key triggers guess
        self.root.bind("<Return>", lambda event: self.make_guess())

    def make_guess(self):
        raw = self.guess_var.get().strip()

        if not raw.isdigit():
            self.result_label.config(text="Enter a whole number (1–100).")
            return

        guess = int(raw)
        if guess < 1 or guess > 100:
            self.result_label.config(text="Out of range. Pick 1–100.")
            return

        self.tries += 1

        if guess < self.secret:
            self.result_label.config(text="Too low.")
        elif guess > self.secret:
            self.result_label.config(text="Too high.")
        else:
            messagebox.showinfo("Correct!", f"You got it in {self.tries} tries!")
            self.new_game()
            return

        # Clear entry for next guess
        self.guess_var.set("")
        self.entry.focus()

    def new_game(self):
        self.secret = random.randint(1, 100)
        self.tries = 0
        self.guess_var.set("")
        self.result_label.config(text="New game started. Make a guess!")
        self.entry.focus()


def main():
    root = tk.Tk()
    root.resizable(False, False)
    GuessingGameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
