from game import Game
from alpha_beta import bot_move as ab_bot, set_depth as minmax_set_depth
from mcts import bot_move as mcts_bot, rollout_time as mcts_set_roullout_times, expansion_time as mcts_set_expand_time
from player import move_player as player_move
import argparse

"""
Code for reading and parsing the command line arguments. 
"""
bot_one = None
bot_two = None
players = {"mcts": mcts_bot, "monte_carlo_tree_search": mcts_bot, "alpha_beta": ab_bot,
           "minimax": ab_bot, "alphabeta": ab_bot, "human": player_move, "player": player_move}

parser = argparse.ArgumentParser(description='Connect4 AI using AlphaBeta / MCTS')

parser.add_argument('First_Player', type=str,
                    help='First player (human, alphabeta or mcts)')
parser.add_argument('Second_Player', type=str,
                    help='Second player (human, alphabeta or mcts)')
parser.add_argument('-d', '--depth', type=int, default=4,
                    help='Depth of the tree')
parser.add_argument('-t', '--time', type=float, default=8,
                    help='Time of expanding tree in mcts')
parser.add_argument('-r', '--rollout', type=int, default=1,
                    help='Rollout count in mcts algorithm')
parser.add_argument('-s', '--statistics', action='store_true',
                    default=False, help='Statistics of game')

args = parser.parse_args()
minmax_set_depth(args.depth)
mcts_set_roullout_times(args.rollout)
mcts_set_expand_time(args.time)

"""
Code used to select the AI players that will play the game based on their names.
"""
for name, bot in players.items():
    if name.lower().startswith(args.First_Player.lower()):
        bot_one = bot
    if name.lower().startswith(args.Second_Player.lower()):
        bot_two = bot

"""
The play function is used to play a game of Connect Four between two players.
"""
def play(p=True):
    game = Game(7, 6)

    while not game.check_win():
        bot_one(game, 1)
        if p:
            print(game)
        if game.check_win():
            break
        bot_two(game, 2)
        if p:
            print(game)

    win = game.check_win()
    if win == 3:
        return 0
    else:
        return win

"""
Code to print the statistics of the game. 
"""
if args.statistics:
    results = {0: 0, 1: 0, 2: 0}
    for i in range(0, 1):
        results[play(False)] += 1

    print("DRAW: ", results[0])
    print(args.first, results[1])
    print(args.second, results[2])

else:
    play()
