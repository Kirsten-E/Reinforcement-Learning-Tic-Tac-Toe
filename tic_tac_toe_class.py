from __future__ import annotations



class TicTacToe():

    # Grid code - 0 for no element, 1 for player 1, 2 for player 2
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]


    def print_grid(self):
        for row in self.grid:
            row_string = ""
            for entry in row:
                if entry == 0:
                    row_string = row_string + "   |"
                elif entry == 1:
                    row_string = row_string + " O |"
                else:
                    row_string = row_string + " X |"
            print(row_string)
    
    def check_winner(self, player) -> bool:
        # Check rows
        for row in self.grid:
            if all([
                row[0] == row[1],
                row[1] == row[2],
                row[2] == player
                ]):
                return True
        # Check columns
        for column in range(0, 3):
            if all([
                self.grid[0][column] == self.grid[1][column],
                self.grid[1][column] == self.grid[2][column],
                self.grid[2][column] == player
                ]):
                return True
        # Check diagonals
        if all([
                self.grid[0][0] == self.grid[1][1],
                self.grid[1][1] == self.grid[2][2],
                self.grid[2][2] == player
                ]):
                return True  
        if all([
                self.grid[0][2] == self.grid[1][1],
                self.grid[1][1] == self.grid[2][0],
                self.grid[2][0] == player
                ]):
                return True
        return False
    
    def play_turn(self, player, row, column) -> bool | None:
        if self.grid[row][column] != 0:
            return None
        else:
            self.grid[row][column] = player
            return self.check_winner(player)
    
