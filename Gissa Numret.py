import random
secret_num=random.randint(0,100)
guesses=1
guess_limit=3

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
