import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 Board
        self.current_player = "X"  # X starts the game

        self.buttons = [[None for _ in range(3)] for _ in range(3)]  # Buttons list
        self.create_board()
        
        self.window.mainloop()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.window, text="", font=("Arial", 20), height=2, width=5,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

        # Reset Button
        reset_button = tk.Button(self.window, text="Restart Game", font=("Arial", 14), command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} Wins! 🎉")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a Draw! 🤝")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check Rows, Columns, and Diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True  # Row match
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True  # Column match

        # Check Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True

        return False

    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False  
        return True

    def reset_game(self):
       
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

if __name__ == "__main__":
    TicTacToe()
