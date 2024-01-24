class TicTacToe:
    def __init__(self):
        # Represents the Tic Tac Toe board with empty spaces
        self.board = [" " for _ in range(9)]
        # Starting with player X
        self.current_player = "X"

    def make_move(self, position):
        # Check if the chosen position is empty
        if self.board[position] == " ":
            # Place the current player's symbol in the chosen position
            self.board[position] = self.current_player
            # Toggle to the next player
            self.toggle_player()
            return True
        else:
            # If the chosen position is not empty, the move is invalid
            return False

    def toggle_player(self):
        # Switch between X and O players
        self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if (
                self.board[i] == self.board[i + 3] == self.board[i + 6] != " "
                or self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != " "
            ):
                return self.board[i]

        if (
            self.board[0] == self.board[4] == self.board[8] != " "
            or self.board[2] == self.board[4] == self.board[6] != " "
        ):
            return self.board[4]

        return None

    def is_board_full(self):
        # Check if the board is full (no empty spaces)
        return " " not in self.board

    def print_board(self):
        # Print the current state of the Tic Tac Toe board
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("---------")


if __name__ == "__main__":
    # Create a Tic Tac Toe game instance and play until there's a winner or a tie
    game = TicTacToe()
    while True:
        game.print_board()
        position = int(input(f"Player {game.current_player}, enter your move (1-9): ")) - 1
        if 0 <= position <= 8:
            if game.make_move(position):
                winner = game.check_winner()
                if winner:
                    print(f"Player {winner} wins!")
                    break
                elif game.is_board_full():
                    print("It's a tie!")
                    break
        else:
            print("Invalid move. Please enter a number between 1 and 9.")
