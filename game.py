"""
Global variables to set player one, player two values, winning count, and the depth of the game.
"""
P_ONE = 1
P_TWO = 2
WIN_COUNT = 4
DEPTH = 1

"""
Game class which initialises the variables needed to play the game, and checks for wins within the grid. 
Also, used to create the grid matrix layout. 
"""

class Game:

    """Constructor to initialize the grid, moves, and to set the column, blocks and height of the grid."""
    def __init__(self, cols, blocks, grid=None, height=None, moveCount = 0):
        self.moveCount = moveCount
        self.cols = cols
        self.blocks = blocks
        self.grid = grid if grid is not None else [
            [0 for i in range(cols)] for j in range(blocks)]
        self.height = height if height is not None else [
            0 for i in range(cols)]

    """ 
    Function to drop a connect-4 disc onto the grid. 
     """
    def move_disc(self, player, column):
        if self.height[column] == self.blocks:
            return None

        self.grid[self.blocks -
                   self.height[column] - 1][column] = player
        self.height[column] += 1

        self.moveCount += 1

        return True

    """ 
    This method is typically used when making a move in the game and then checking if it is a valid move. 
    If the move is not valid, the game state can be restored to its previous state.
    """
    def revert_move(self, column):
        self.grid[self.blocks -
                   self.height[column]][column] = 0
        self.height[column] -= 1
        self.moveCount -= 1

    """ 
    Helper function to check if the subsequence of WIN_COUNT values starting at that index all have the same non-zero value. 
    """
    def helper_array(arr):
        for x in range(len(arr) - WIN_COUNT + 1):
            if (arr[x] == P_ONE or arr[x] == P_TWO):
                lst = arr[x:x+WIN_COUNT]
                if lst.count(lst[0]) == len(lst):
                    return arr[x]
        return None

    """ 
    The horizontal_win function is used to check if there is a horizontal win in the game. 
    """
    def horizontal_win(self):
        for line in self.grid:
            val = Game.helper_array(line)
            if val:
                return val
        return None

    """ 
    The vertical_win function is used to check if there is a horizontal win in the game. 
    """
    def vertical_win(self):
        for c in range(self.cols):
            column = [row[c] for row in self.grid]
            val = Game.helper_array(column)
            if val:
                return val
        return None

    """ 
    The diagonal_win function is used to check if there is a horizontal win in the game. 
    """
    def diagonal_win(self, diag):
        temp_val1 = 0 if diag else WIN_COUNT - 1
        temp_val2 = self.cols - WIN_COUNT + 1 if diag else self.cols
        temp_val3 = 1 if diag else -1
        for line in range(WIN_COUNT - 1, self.blocks):
            for column in range(temp_val1, temp_val2):
                arr = [self.grid[line-i]
                       [column+(i*temp_val3)] for i in range(0, WIN_COUNT)]
                val = Game.helper_array(arr)
                if val:
                    return val
        return None

    """ 
    Function to check for any kind of win i.e; vertical, diagonal, horizontal. 
    """
    def check_win(self):
        if self.moveCount == self.blocks * self.cols:
            return 3
        return self.horizontal_win() or self.vertical_win() or self.diagonal_win(True) or self.diagonal_win(False)

    """ 
    The function is used to create a string representation of the game grid that can be printed to the screen. 
    """
    def __str__(self):
        grid_layout = ''.join(['{:4}'.format(str(i))
                     for i in range(len(self.grid) + 1)]) + '\n'
        grid_layout += ''.join(['{:4}'.format('|')
                      for i in range(len(self.grid) + 1)]) + '\n'

        grid_layout += '\n'.join([''.join(['{:4}'.format(str(value) if value > 0 else '-')
                                 for value in row]) for row in self.grid])
        grid_layout += '\n'
        return grid_layout
