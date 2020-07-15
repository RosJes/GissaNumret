import random
'''make a play field '''
'''what is the game structure?'''
'''figure out user input, what happens?'''
'''What classes do you need? player etc.'''
'''Learn classes,methods etc.'''

'''display field nad choosing coordinates'''
''''''
rows, cols = (3, 3)
win=False
def play_game():
    i = 0
    play_rows = 1
    arr = [[0 for i in range(cols)]
           for j in range(rows)]

    print('1   2   3')
    print('------------')
    for row in arr:
        i += 1
        print(i, row)
        if (i >= 3):
            i = 0
    while(True):
      x_guess = input('Select destination x')
      y_guess = input('Select destination y')
      comp_movex=random.randint(0, 2)
      comp_movey=random.randint(0, 2)
      play_rows+=1
      arr[int(x_guess)][int(y_guess)] = 1
      arr[int(comp_movex)][int(comp_movey)] = 5
      wincheck1 = arr[0][0] + arr[0][1] + arr[0][2]
      wincheck4=arr[1][0] + arr[1][1] + arr[1][2]
      wincheck5 = arr[2][0] + arr[2][1] + arr[2][2]
      wincheck2=arr[0][0] + arr[1][0] + arr[2][0]
      wincheck6 = arr[0][1] + arr[1][1] + arr[2][1]
      wincheck7 = arr[0][2] + arr[1][2] + arr[2][2]
      wincheck3=arr[0][0] + arr[1][1] + arr[2][2]
      wincheck8 = arr[0][2] + arr[1][2] + arr[2][0]
      '''make a search loop or better solution'''

      print('1   2   3')
      print('------------')
      for row in arr:
          i+=1
          print(i,row)
          if(i>=3):
              i=0
      if wincheck1==3 or wincheck2==3 or wincheck3==3or wincheck4==3or wincheck5==3or wincheck6==3or wincheck7==3or wincheck8==3:
        print('you win')
        break
      elif wincheck1==15 or wincheck2==15 or wincheck3==15or wincheck4==15or wincheck5==15or wincheck6==15or wincheck7==15or wincheck8==15:
          print('computer win')
          break

play_game()
'''display field'''
'''create method'''
'''user input'''
'''computer input'''
'''clear terminal'''
'''make logic with koordinations ex 1,2'''
'''the user changes the zero to X with specification
the user input can ba f example this:
write destination X= 1
write destination Y=2
the position of X is now [1,2]
    '''



