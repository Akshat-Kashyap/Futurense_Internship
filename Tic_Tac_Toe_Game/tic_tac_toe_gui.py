# tic_tac_toe_gui.py
import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import TicTacToe

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        # Create an instance of the Tic Tac Toe game
        self.game = TicTacToe()

        # Create buttons for each cell in the Tic Tac Toe grid
        self.buttons = [
            tk.Button(master, text=" ", font=("Helvetica", 24), width=6, height=3, command=lambda i=i: self.make_move(i))
            for i in range(9)
        ]

        # Place buttons in a 3x3 grid
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

    def make_move(self, position):
        # Handle a player's move in the GUI
        if self.game.make_move(position):
            self.update_board()
            winner = self.game.check_winner()
            if winner:
                self.show_winner(winner)
            elif self.game.is_board_full():
                self.show_tie()

    def update_board(self):
        # Update the buttons to reflect the current state of the Tic Tac Toe board
        for i, button in enumerate(self.buttons):
            button["text"] = self.game.board[i]
            button["state"] = "disabled" if self.game.board[i] != " " else "normal"

    def show_winner(self, winner):
        # Show a message box declaring the winner
        tk.messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.disable_buttons()

    def show_tie(self):
        # Show a message box declaring a tie
        tk.messagebox.showinfo("Game Over", "It's a tie!")
        self.disable_buttons()

    def disable_buttons(self):
        # Disable all buttons to prevent further moves after the game ends
        for button in self.buttons:
            button["state"] = "disabled"


if __name__ == "__main__":
    # Create the main Tkinter window and start the GUI
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()