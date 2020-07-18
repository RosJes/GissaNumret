import random
import os

'''What is not working: Clear screen
when computer choose a destination or you do it you dont get a second chance'''
rows, cols = (3, 3)
errormessageyou = False;
errormessagecomp = False
is_here = False;
play_again = True


def play_game():
    i = -1
    arr = [[0 for i in range(cols)]
           for j in range(rows)]
    print(' x.0   x.1  x.2 ')
    for row in arr:
        i += 1
        print('y.',i, row)
        if (i >= 2):
            i = -1
    while (play_again):
        os.system('cls')
        x_guess = input('Select destination y')
        y_guess = input('Select destination x')
        if arr[int(x_guess)][int(y_guess)] != 0:
            print("The destination is occupied your round doesn't count sorry...")

        else:
            arr[int(x_guess)][int(y_guess)] = 1
        comp_movex = random.randint(0, 2)
        comp_movey = random.randint(0, 2)
        if arr[int(comp_movex)][int(comp_movey)] != 0:
            print("computer chose the same coordinates as you"
                  "(continue playing it's my fault really sigh...)")
        else:
            arr[int(comp_movex)][int(comp_movey)] = 5

        wincheck1 = arr[0][0] + arr[0][1] + arr[0][2]
        wincheck4 = arr[1][0] + arr[1][1] + arr[1][2]
        wincheck5 = arr[2][0] + arr[2][1] + arr[2][2]
        wincheck2 = arr[0][0] + arr[1][0] + arr[2][0]
        wincheck6 = arr[0][1] + arr[1][1] + arr[2][1]
        wincheck7 = arr[0][2] + arr[1][2] + arr[2][2]
        wincheck3 = arr[0][0] + arr[1][1] + arr[2][2]
        wincheck8 = arr[0][2] + arr[1][2] + arr[2][0]
        wincheck9=arr[0][2] + arr[1][1] + arr[2][0]

        print('x.0   x.1   x.2')
        print('------------')
        for row in arr:
            i += 1
            print('y.',i, row)
            if (i >= 2):
                i = -1
        if wincheck1 == 3 or wincheck2 == 3 or wincheck3 == 3 or wincheck4 == 3 or wincheck5 == 3 or wincheck6 == 3 or wincheck7 == 3 or wincheck8 == 3 or wincheck9==3:
            print('you win')
            user_input = input('play again?y/n')
            if user_input == 'y':
                play_again is True
                arr = [[0 for i in range(cols)]
                       for j in range(rows)]
            else:
                break;

        elif wincheck1 == 15 or wincheck2 == 15 or wincheck3 == 15 or wincheck4 == 15 or wincheck5 == 15 or wincheck6 == 15 or wincheck7 == 15 or wincheck8 == 15 or wincheck9==15:
            print('computer win')
            user_input = input('play again?y/n')
            if user_input == 'y':
                arr = [[0 for i in range(cols)]
                       for j in range(rows)]
            else:
                break;


play_game()


