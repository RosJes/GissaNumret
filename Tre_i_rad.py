import random
'''make a play field '''
'''what is the game structure?'''
'''figure out user input, what happens?'''
'''What classes do you need? player etc.'''
'''Learn classes,methods etc.'''

'''display field nad choosing coordinates'''
''''''
rows, cols = (3, 3)

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
    while(play_rows<=6):
      x_guess = input('Select destination x')
      y_guess = input('Select destination y')
      comp_movex=random.randint(0, 2)
      comp_movey=random.randint(0, 2)
      play_rows+=1
      arr[int(x_guess)][int(y_guess)] = 1
      arr[int(comp_movex)][int(comp_movey)] = 2
      print('1   2   3')
      print('------------')
      for row in arr:
          i+=1
          print(i,row)
          if(i>=3):
              i=0

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



