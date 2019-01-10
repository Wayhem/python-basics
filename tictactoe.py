game = [[0,0,0],[0,0,0],[0,0,0]]


def game_screen(player=0, row=0, column=0, just_display=False):
    if not just_display:
        game[row][column] = player
    print('   0  1  2')
    for count, line in enumerate(game):
        print(count, line)

game_screen(just_display=True)
game_screen(1, 2, 1)

