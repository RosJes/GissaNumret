import random
import os

'''Solution to one loop:
is here switches to true and error message to false
if errormessage is false the loop will jump to the beginning, well in the beginning 
there is an if condition: is here true and errormessage komp is now true since the switch is back to normal
test the while loop, why doesn't it break when one of the statements switch to false?
'''
rows, cols = (3, 3)
errormessageyou = False;
errormessagecomp = False
is_here = False;
play_again = True


def play_game():
    i = 0
    play_rows = 1
    arr = [[0 for i in range(cols)]
           for j in range(rows)]
    print(' 1   2   3 ')
    for row in arr:
        i += 1
        print(i, row)
        if (i >= 3):
            i = 0
    while (not errormessagecomp or not errormessageyou or play_again):
        if (errormessagecomp is True and is_here is True):
            comp_movex = random.randint(0, 2)
            comp_movey = random.randint(0, 2)
            arr[int(comp_movex)][int(comp_movey)] = 5

        os.system('cls')
        x_guess = input('Select destination x')
        y_guess = input('Select destination y')
        if arr[int(x_guess)][int(y_guess)] != 0:
            print("The destination is occupied")
            errormessageyou is True

        else:
            arr[int(x_guess)][int(y_guess)] = 1
        comp_movex = random.randint(0, 2)
        comp_movey = random.randint(0, 2)
        print(comp_movey, comp_movex)
        if arr[int(comp_movex)][int(comp_movey)] != 0:
            print('computer fucked up')
            errormessagecomp is True
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
        print('1   2   3')
        print('------------')
        for row in arr:
            i += 1
            print(i, row)
            if (i >= 3):
                i = 0
        if wincheck1 == 3 or wincheck2 == 3 or wincheck3 == 3 or wincheck4 == 3 or wincheck5 == 3 or wincheck6 == 3 or wincheck7 == 3 or wincheck8 == 3:
            print('you win')
            user_input = input('play again?y/n')
            if user_input == 'y':
                play_again is True
                arr = [[0 for i in range(cols)]
                       for j in range(rows)]
            else:
                break;

        elif wincheck1 == 15 or wincheck2 == 15 or wincheck3 == 15 or wincheck4 == 15 or wincheck5 == 15 or wincheck6 == 15 or wincheck7 == 15 or wincheck8 == 15:
            print('computer win')
            user_input = input('play again?y/n')
            if user_input == 'y':
                play_again is True
                arr = [[0 for i in range(cols)]
                       for j in range(rows)]
            else:
                break;


play_game()




