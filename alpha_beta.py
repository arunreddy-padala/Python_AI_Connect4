import sys

"""
Global variables to set positive, and negative infinity values, grid values,  winning count, and the depth of the game.
"""

POSITIVE_INFINITY = sys.maxsize
WIN_COUNT = 4
NEGATIVE_INFINITY = -POSITIVE_INFINITY - 1
DEPTH = 1

grid_values = [
    [0, 0, 0, -50, -512],
    [1, 0, 0, -10, -512],
    [10, 0, 0, -1, -512],
    [50, 0, 0, 0, -512],
    [512, 512, 512, 512, 512]
]


"""
Function to update game Depth
"""
def set_depth(depth):
    global DEPTH
    DEPTH = depth

"""
The get_result function is a helper function that takes a list and a 
player number and returns a value from the grid_values list.
"""
def get_result(l, player):
    global grid_values
    player_one_result = l.count(player)
    player_two_result = l.count(3-player)

    return grid_values[player_one_result][player_two_result]

"""
The column_result function is used to calculate the score for a player in a given game based on the values in the columns of the game grid.
"""
def column_result(game, player):
    value = 0
    for col in range(game.cols):
        column = [row[col] for row in game.grid]
        for k in range(game.blocks - WIN_COUNT + 1):
            value = value + get_result(column[k:k + WIN_COUNT], player)
    return value


"""
The diagonal_result function is used to calculate the score for a player in a given game based on the values in the diagonals of the game grid.
"""
def diagonal_result(game, diag, player):
    value = 0
    for row in range(WIN_COUNT - 1, game.blocks):
        for column in range(0 if diag else WIN_COUNT - 1, game.cols - WIN_COUNT + 1 if diag else game.cols):
            arr = [game.grid[row-i][column+(i if diag else -i)] for i in range(0, WIN_COUNT)]
            value = value+ get_result(arr, player)
    return value

"""
The line_result function is used to calculate the score for a player in a given game based on the values in the straight line of the game grid.
"""
def line_result(game, player):
    value = 0
    for row in game.grid:
        for k in range(game.cols - WIN_COUNT + 1):
            value = value + get_result(row[k:k + WIN_COUNT], player)
    return value

"""
The helper_value function is a helper function used to evaluate the game state and determine the score for a given player.
"""
def helper_value(game, player):
    win = game.check_win()
    if win == player:
        return 512
    elif win != None:
        return -512
    elif win == 3:
        return 0

    return line_result(game, player) + column_result(game, player) + diagonal_result(game, False, player) + diagonal_result(game, True, player)


"""
Function to implement the Alpha Beta search algorithm. 
"""
def alpha_beta(game, maximizing_player, player, last_move, depth, alpha=NEGATIVE_INFINITY, beta=POSITIVE_INFINITY):

    if depth == 0 or (game.moveCount >= 8 and game.check_win()):
        value = (1 if maximizing_player else -1) * \
            helper_value(game, player)

    else:
        if maximizing_player:
            value = NEGATIVE_INFINITY

            for i in range(game.cols):
                if game.move_disc(player, i):
                    value = max(value, alpha_beta(
                        game, False, 3-player, i, depth - 1, alpha, beta))
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break

        else:
            value = POSITIVE_INFINITY

            for i in range(game.cols):
                if game.move_disc(player, i):
                    value = min(value, alpha_beta(game, True, 3-player, i, depth - 1, alpha, beta))
                    beta = min(beta, value)
                    if alpha >= beta:
                        break

    if last_move != -1:
        game.revert_move(last_move)
    return value

"""
The bot_move function is used to make a move in the game on behalf of an AI player i.e; Alpha Beta
"""
def bot_move(game, player):
    dict = {}
    for i in range(game.cols):
        if game.move_disc(player, i):
            dict[i] = alpha_beta(game, False, 3-player, i, depth=DEPTH)
    value = max(dict, key=dict.get)
    game.move_disc(player, value)
