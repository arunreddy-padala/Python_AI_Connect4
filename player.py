"""
The move_player function is used to make a move in the game on behalf of a human player based on the column input.
"""
def move_player(game, player):
    while(True):
        print("Enter column value to place the disc:")
        column = int(input())
        t = game.move_disc(player, column)
        if t:
            return
