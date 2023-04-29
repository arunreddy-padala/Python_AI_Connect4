import sys
import copy
import math
import time

from game import Game
from random import randint

"""
Global variables to set positive, and negative infinity values, rollout, and expansion time of the game.
"""

temp = {}
POSITIVE_INFINITY = sys.maxsize
NEGATIVE_INFINITY = -POSITIVE_INFINITY - 1
ROLLOUT_COUNT = 1
EXPANSION_TIME = 1

"""
Function to update expansion time of MCTS. 
"""
def expansion_time(new):
    global EXPANSION_TIME
    EXPANSION_TIME = new

"""
Function to update rollout time of MCTS. 
"""
def rollout_time(new):
    global ROLLOUT_COUNT
    ROLLOUT_COUNT = new

"""
Function to copy the current game. 
"""
def copy_game(game):
    return Game(game.cols, game.blocks, copy.deepcopy(
        game.grid), copy.deepcopy(game.height), game.moveCount)


"""
Function to implement the Monte Carlo Tree search algorithm. 
"""
def monte_carlo_tree_search(game, player):
    temp[tuple(map(tuple, game.grid))] = (0, 1)
    start_time = time.time()
    while True:
        for i in range(10):
            node, next_player, path = selection(game, player)
            wins, loses, draws, times = expansion(node, next_player, player)
            backpropagation(path, wins, loses,times, player, next_player)
        if time.time() - start_time > EXPANSION_TIME:
            break

"""
The helper_optimal_move function is a helper function that is used to determine the optimal move f
or an AI player to make in a given game state. It uses the upper confidence bound, it is a measure of the uncertainty in the previous scores, 
and it is used to determine how promising the game state is.
"""
def helper_optimal_move(game, current_player):
    MAX_VAL = NEGATIVE_INFINITY
    MAX_COL = -1
    for i in range(game.cols):
        w = temp[tuple(map(tuple, game.grid))][1]
        visited_count = 2 * math.log(w)
        if game.move_disc(current_player, i):
            t = tuple(map(tuple, game.grid))

            if t in temp:
                avg = temp[t][0] / temp[t][1]
                upper_confidence_bound_val = avg + 2 * math.sqrt(visited_count/temp[t][1])
                if upper_confidence_bound_val > MAX_VAL:
                    MAX_VAL = upper_confidence_bound_val
                    MAX_COL = i

            game.revert_move(i)

    return MAX_COL


"""
Function to implement the Monte Carlo Tree Selection phase. 
"""
def selection(original_game, player):
    game_copy = copy_game(original_game)
    current_player = player
    path = []

    while True:
        path.append(tuple(map(tuple, game_copy.grid)))
        best_val = helper_optimal_move(game_copy, current_player)

        if best_val == -1:
            return game_copy, current_player, path

        if best_val != -1:
            game_copy.move_disc(current_player, best_val)
            current_player = 3 - current_player


"""
Function to implement the Monte Carlo Tree Expansion phase. 
"""
def expansion(game, player, first_player):
    wins = 0
    loses = 0
    draws = 0
    times = 0

    win_check = game.check_win()
    if win_check == first_player:
        return ROLLOUT_COUNT*7, 0, 0, ROLLOUT_COUNT*7
    elif win_check == 3 - first_player:
        return 0, ROLLOUT_COUNT*7, 0, ROLLOUT_COUNT*7

    for i in range(game.cols):
        if game.move_disc(player, i):
            sum_wins, sum_loses, sum_draws, sum_times = simulation(
                game, 3 - player, first_player, ROLLOUT_COUNT)
            temp[tuple(map(tuple, game.grid))] = (sum_wins, sum_times)
            wins = wins + sum_wins
            loses = loses + sum_loses
            draws = draws + sum_draws
            times = times + sum_times
            game.revert_move(i)
    return wins, loses, draws, times


"""
Function to implement the Monte Carlo Tree Simulation phase. 
"""
def simulation(original_game, player, first_player, times):
    wins_count = 0
    draws_count = 0
    loses_count = 0

    win_check = original_game.check_win()
    if win_check:
        if win_check == first_player:
            return times, 0, 0, times
        elif win_check == 3 - first_player:
            return 0, times, 0, times
        else:
            return 0, 0, times, times

    for i in range(times):
        current_player = player

        game = copy_game(original_game)

        while True:
            while True:
                random = randint(0, game.cols - 1)
                if game.move_disc(current_player, random):
                    break
            current_player = 3-current_player
            win_check = game.check_win()
            if win_check:
                if win_check == first_player:
                    wins_count = wins_count + 1
                elif win_check == 3 - first_player:
                    loses_count = loses_count + 1
                else:
                    draws_count = draws_count + 1
                break

    return wins_count, loses_count, draws_count, times

"""
Function to implement the Monte Carlo Tree Backpropagation phase. 
"""
def backpropagation(path, wins, loses, times, first_player, last_player):
    for i in range(len(path)):
        if i % 2:
            k = wins
        else:
            k = loses
        temp[path[i]] = (temp[path[i]][0] + k, temp[path[i]][1] + times)

"""
The bot_move function is used to make a move in the game on behalf of an AI player i.e; MCTS
"""
def bot_move(game, player):
    temp.clear()
    monte_carlo_tree_search(game, player)

    MAX_VAL = -1
    MAX_COL = -1
    for i in range(game.cols):
        if game.move_disc(player, i):
            t = tuple(map(tuple, game.grid))
            if t in temp and temp[t][1] > MAX_VAL:
                MAX_VAL = temp[t][1]
                MAX_COL = i
            game.revert_move(i)

    game.move_disc(player, MAX_COL)