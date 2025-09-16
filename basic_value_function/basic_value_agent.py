from __future__ import annotations
from copy import deepcopy

def flatten(board):
    return str(tuple(cell for row in board for cell in row))


class TicTacToe():

    def __init__(self):
        self.grid = [[0, 0, 0],
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
    

from random import random, randint

import json

class Agent2():


    def __init__(self):
        self.exploratory_param = 0.1
        self.step_size = 0.5
        self.last_state = "(0, 0, 0, 0, 0, 0, 0, 0, 0)"
        self.last_state_value = 0
        with open("basic_value_function/value_function_2.json", 'r') as file:
            self.value_function = json.load(file)

    def play_turn(self, game: TicTacToe):
        if random() <= self.exploratory_param:
            # print("EXPLORATORY MOVE")
            result = None
            while result is None:
                move = randint(0, 8)
                match move:
                    case 0:
                        result = game.play_turn(2, 0, 0)
                    case 1:
                        result = game.play_turn(2, 0, 1)
                    case 2:
                        result = game.play_turn(2, 0, 2)
                    case 3:
                        result = game.play_turn(2, 1, 0)
                    case 4:
                        result = game.play_turn(2, 1, 1)
                    case 5:
                        result = game.play_turn(2, 1, 2)
                    case 6:
                        result = game.play_turn(2, 2, 0)
                    case 7:
                        result = game.play_turn(2, 2, 1)
                    case 8:
                        result = game.play_turn(2, 2, 2)
            return result
        else:
            # print("OPTIMAL MOVE")
            board_copy = deepcopy(game.grid)
            current_win_prob = -1
            current_win_coordinates = (4, 4)
            for i in range(0, 3):
                for j in range(0, 3):
                    board_copy = deepcopy(game.grid)
                    if board_copy[i][j] == 0:
                        board_copy[i][j] = 2
                        prob = self.value_function[flatten(board_copy)]
                        if prob > current_win_prob:
                            current_win_prob = prob
                            current_win_coordinates = (i, j)
            result = game.play_turn(2, current_win_coordinates[0], current_win_coordinates[1])
            self.value_function[self.last_state] = self.last_state_value + self.step_size * (current_win_prob - self.last_state_value)
            self.last_state = flatten(game.grid)
            self.last_state_value = current_win_prob
            return result

    def save_value_function(self):
        with open("basic_value_function/value_function_2.json", "w") as file:
            json.dump({str(k): v for k, v in self.value_function.items()}, file, indent=2)


class Agent1():

    def __init__(self):
        self.exploratory_param = 0.1
        self.step_size = 0.5
        self.last_state = "(0, 0, 0, 0, 0, 0, 0, 0, 0)"
        self.last_state_value = 0
        with open("basic_value_function/value_function_1.json", 'r') as file:
            self.value_function = json.load(file)

    def play_turn(self, game: TicTacToe):
        if random() <= self.exploratory_param:
            # print("EXPLORATORY MOVE")
            result = None
            while result is None:
                move = randint(0, 8)
                match move:
                    case 0:
                        result = game.play_turn(1, 0, 0)
                    case 1:
                        result = game.play_turn(1, 0, 1)
                    case 2:
                        result = game.play_turn(1, 0, 2)
                    case 3:
                        result = game.play_turn(1, 1, 0)
                    case 4:
                        result = game.play_turn(1, 1, 1)
                    case 5:
                        result = game.play_turn(1, 1, 2)
                    case 6:
                        result = game.play_turn(1, 2, 0)
                    case 7:
                        result = game.play_turn(1, 2, 1)
                    case 8:
                        result = game.play_turn(1, 2, 2)
            return result
        else:
            # print("OPTIMAL MOVE")
            board_copy = deepcopy(game.grid)
            current_win_prob = -1
            current_win_coordinates = (4, 4)
            for i in range(0, 3):
                for j in range(0, 3):
                    board_copy = deepcopy(game.grid)
                    if board_copy[i][j] == 0:
                        board_copy[i][j] = 1
                        prob = self.value_function[flatten(board_copy)]
                        if prob > current_win_prob:
                            current_win_prob = prob
                            current_win_coordinates = (i, j)
            result = game.play_turn(1, current_win_coordinates[0], current_win_coordinates[1])
            self.value_function[self.last_state] = self.last_state_value + self.step_size * (current_win_prob - self.last_state_value)
            self.last_state = flatten(game.grid)
            self.last_state_value = current_win_prob
            return result

    def save_value_function(self):
        with open("basic_value_function/value_function_1.json", "w") as file:
            json.dump({str(k): v for k, v in self.value_function.items()}, file, indent=2)





for i in range(0, 1):
    agent_1 = Agent1()
    agent_2 = Agent2()
    game = TicTacToe()
    end = False
    player = 1
    while not end:
        game.print_grid()
        move = None
        while move is None:
            if player == 1:
                row = int(input("Row: "))
                column = int(input("Column: "))
                move = game.play_turn(1, row, column)
                # move = agent_1.play_turn(game)
            else:
                move = agent_2.play_turn(game)
        if move:
            print(f"Player {player} wins")
            end = True
        else:
            end = True
            for row in game.grid:
                for entry in row:
                    if entry == 0:
                        end = False
        if player == 1:
            player = 2
        else:
            player = 1
    game.print_grid()
    agent_1.save_value_function()
    agent_2.save_value_function()
