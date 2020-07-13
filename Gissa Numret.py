
'''Deklarera  variabler(hårkodat)'''
secret_num=
guesses=1
guess_limit=3


'''bygg en while loop med en kondition'''
while(guesses<=guess_limit):
    your_guess = input('What is the number?')
    converted_guess=int(your_guess)
    if converted_guess==secret_num and guesses<=guess_limit:
        print('You win!')
        break;
    elif converted_guess<secret_num and guesses<guess_limit:
        print('to low try again')
    elif converted_guess>secret_num and guesses<guess_limit:
        print('to high try again')
    elif guesses==guess_limit:
        print('you lose')

    guesses+=1
