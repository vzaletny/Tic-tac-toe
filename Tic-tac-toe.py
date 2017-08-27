import time
import random
import numpy as np
import matplotlib.pyplot as plt


def create_board():
    return np.zeros((3, 3), dtype=np.int)


def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board


def possibilities(board):
    return list(zip(*np.where(board == 0)))


def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selection = random.choice(selections)
        place(board, player, selection)
    return board


def row_win(board, player):
    return np.any(np.all(np.array(board) == player, axis=1))


def col_win(board, player):
    return np.any(np.all(np.array(board) == player, axis=0))


def diag_win(board, player):
    return np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player)


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(np.array(board) != 0) and winner == 0:
        winner = -1
    return winner


def play_game():
    board, winner = create_board(), 0
    while winner == 0:
        for player in (1, 2):
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


start = time.time()
games = [play_game() for i in range(10000)]
stop = time.time()
print(stop - start)
plt.hist(games)
plt.show()
