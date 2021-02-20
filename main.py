##Rudy Garcia
import math, m

MENU = "\n\t\t--MENU--\t\t\n n - new function \n c - change step \n m - mess with limits \n r - reset all \n g - go! \n q - quit"

menu_options = "ncmrgq"

def correct_choice():
  play = False
  while play == False:
    choice = input("your choice: ").lower()
    if choice in menu_options:
      play = True
    else:
      play = False
  return choice

def new_function():
  tries = 0
  play = False
  while play == False:
    user_function = input("Function: ")
    try:
      f = lambda x: eval(input())
      play = True
    except:
      if tries//2 == 0:
        print("I need correct syntax")
      play = False
  return user_function

def change_step():
  play = False
  while play == False:
    step = input("What is your step (n): ")
    try:
      step = int(step)
      if step%2 == 1:
        print("step needs to be an even number")
        play = False
      else:
        play = True
    except ValueError:
      play = False
  return step

def change_limits():
  play = False
  while play == False:
    low_lim = input("lower limit: ")
    try: 
      low_lim = float(low_lim)
      play = True
    except ValueError:
      if low_lim == "e":
        low_lim = math.e
        play = True
      else:
        print("I need a number please")
        play = False
  play = False
  while play == False:
    upper_lim = input("upper limit: ") 
    try: 
      upper_lim = float(upper_lim)
      play = True
    except ValueError:
      if upper_lim == "e":
        upper_lim = math.e
        play = True
      else:
        print("I need a number please")
        play = False
  return low_lim, upper_lim

def approximater(user_function, step, low_limit, upper_limit):
  f = lambda x: eval(user_function)
  odd, even, rest = 4,2,1
  total = 0
  count = 0
  step_values = ""
  rise = (upper_limit - low_limit)/step
  while ( count <= step):
    step_value = low_limit + count *rise
    step_values += f"{step_value}  "
    if ( count == 0 or count == step):
      total += rest * f(step_value)
    elif ( count%2 == 1):
      total += odd * f(step_value)
    elif ( count%2 == 0):
      total += even * f(step_value)
    count += 1
  total *= rise
  total /= 3
  total = total.__round__(10)
  return total



def main():
  print("Hello, I approximate integrals for you")
  user_function = new_function()
  step = change_step()
  lower_limit, upper_limit = change_limits()
  user_input = ""
  while user_input != "q":
    print(MENU)
    user_input = correct_choice()
    if user_input == "n":
      user_function = new_function()
    
    if user_input == "c":
      step = change_step()
    
    if user_input == "m":
      lower_limit, upper_limit = change_limits()

    if user_input == "r":
      user_function = new_function()
      step = change_step()
      lower_limit, upper_limit = change_limits()

    if user_input == "g":
      approximation = approximater(user_function, step , lower_limit, upper_limit)
      print(f"Your approximation: {approximation}")
  print("Thank you for using me :), I hope I helped from tedious calculation")


main()
