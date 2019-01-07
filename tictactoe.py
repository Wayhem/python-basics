game = [[0,0,0],[0,0,0],[0,0,0]]


def game_screen(player=0, row=0, column=0):
    if player != 0:
        game[row][column] = player
    print('   0  1  2')
    for count, line in enumerate(game):
        print(count, line)

game_screen()

game[0][1] = 1

game_screen()

