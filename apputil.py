import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt


def update_board(current_board):
    # create a reference to the current board
    updated_board = current_board.copy()
    rows, cols = current_board.shape
    
    # iterate through each cell in the board
    for i in range(rows):
        for j in range(cols):
            # count live neighbors
            def check_cell(r, c):
                if 0 <= r < rows and 0 <= c < cols:
                    return current_board[r, c]
                return 0

            for i in range(rows):
                for j in range(cols):
                    total = (
                        check_cell(i-1, j-1) + check_cell(i-1, j) + check_cell(i-1, j+1) +
                        check_cell(i,   j-1)                + check_cell(i,   j+1) +
                        check_cell(i+1, j-1) + check_cell(i+1, j) + check_cell(i+1, j+1)
                    )
            
            # apply rules
            # if cell is alive
            if current_board[i, j] == 1: 
                updated_board[i, j] = 1 if total in [2, 3] else 0
            # if cell is dead
            else:  
                updated_board[i, j] = 1 if total == 3 else 0
                    
    return updated_board


def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. In this array, ` represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='plasma', cbar=False, square=True)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)