from itertools import product
import json


# Check if a player has won
def check_win(board, player):
# rows, cols, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): # row
            return True
        if all(board[j][i] == player for j in range(3)): # col
            return True
    if all(board[i][i] == player for i in range(3)): # main diag
        return True
    if all(board[i][2 - i] == player for i in range(3)): # anti diag
        return True
    return False


# Flatten nested list to tuple for dict keys
def flatten(board):
    return tuple(cell for row in board for cell in row)


# Generate all valid states after Player 2 moves (assuming Player 1 goes first)
def generate_states():
    states = {}
    for cells in product([0, 1, 2], repeat=9):
        board = [list(cells[i:i+3]) for i in range(0, 9, 3)]
            # Count moves
        count1 = sum(cell == 1 for cell in cells)
        count2 = sum(cell == 2 for cell in cells)


        # Player 1 goes first, so valid states require count1 == count2
        if count1 == count2 + 1:
            if check_win(board, 2):
                states[flatten(board)] = 1
            else:
                # Check if Player 1 can win on next move
                player2_can_win = False
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            board[i][j] = 2
                            if check_win(board, 2):
                                player2_can_win = True
                            board[i][j] = 0
                states[flatten(board)] = 0 if player2_can_win else 0.5
    return states


states_dict = generate_states()


print(f"Generated {len(states_dict)} valid states.")


# Save to JSON for inspection
with open("tic_tac_toe_states.json", "w") as f:
    json.dump({str(k): v for k, v in states_dict.items()}, f, indent=2)


print("States saved to tic_tac_toe_states.json")


# Print preview
preview = dict(list(states_dict.items())[:5])
print("Preview of first 5 states:")
for k, v in preview.items():
    print(k, ":", v)

