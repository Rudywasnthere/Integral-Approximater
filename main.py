##Rudy Garcia

import math as math

MENU = "\n\t\t--MENU--\t\t\n n - new function \n c - change step \n m - mess with limits \n r - reset all \n t - type of approximation (best of all by default) \n g - go! \n ? - how does this work?\n q - quit"

menu_options = "ncmrtg?q"
aprox_types = "rlmtpab"

def correct_choice():
  play = False
  while play == False:
    choice = input("your choice: ").lower()
    if choice in menu_options:
      play = True
    else:
      play = False
  return choice

def correct_approx():
  play = False
  while play == False:
    aprox = input("   approx type: ").lower()
    if aprox in aprox_types:
      play = True
    else:
      play = False
  return aprox

def new_function():
  tries = 0
  play = False
  while play == False:
    user_function = input("Function: ")
    user_function = replacer(user_function)
    f = lambda x: eval(user_function)
    try:
      useless_garbage = f(0)
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
      if low_lim == "pi":
        low_lim = math.pi
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
      if upper_lim == "pi":
        upper_lim = math.pi
        play = True
      else:
        print("I need a number please")
        play = False
  return low_lim, upper_lim

def replacer(user_function):
  if ".cos(" not in user_function:
    user_function = user_function.replace("cos(", "math.cos(")
  if ".sin(" not in user_function:
    user_function = user_function.replace("sin(", "math.sin(")
  if ".tan(" not in user_function:
    user_function = user_function.replace("tan(", "math.tan(")
  if ".acos(" not in user_function:
    user_function = user_function.replace("arccos(", "math.acos(")
    user_function = user_function.replace("cos^-1(", "math.acos(")
  if ".asin(" not in user_function:
    user_function = user_function.replace("arcsin(", "math.asin(")
    user_function = user_function.replace("sin^-1(", "math.asin(")
  if ".atan(" not in user_function:
    user_function = user_function.replace("arctan(", "math.atan(")
    user_function = user_function.replace("tan^-1(", "math.atan(")
  return user_function

def approximater(user_function, step, low_limit, upper_limit, aprox_type):
  best_type = ""
  string = f"\nYour "
  if aprox_type == "r":
    total = right_pnt(step, user_function, low_limit, upper_limit)
    string += "right endpoint approxiamtion"
  if aprox_type == "l":
    total = left_pnt(step, user_function, low_limit, upper_limit)
    string += "left endpoint approximation"
  if aprox_type == "m":
    total = midpoint(step, user_function, low_limit, upper_limit)
    string += "midpoint approximation"
  if aprox_type == "t":
    total = trapezoid(step, user_function, low_limit, upper_limit)
    string += "trapezoidal approximation"
  if aprox_type == "p":
    total = parabolic(step, user_function, low_limit, upper_limit)
    string += "parabolic approximation"
  if aprox_type == "a":
    total = right_pnt(step, user_function, low_limit, upper_limit) + left_pnt(step, user_function, low_limit, upper_limit) + midpoint(step, user_function, low_limit, upper_limit) + trapezoid(step, user_function, low_limit, upper_limit) + parabolic(step, user_function, low_limit, upper_limit)
    total /= 5
    string += "average approximation"
  if aprox_type == "b":
    total_vals = []
    total_vals.append(trapezoid(step, user_function, low_limit, upper_limit))
    total_vals.append(parabolic(step, user_function, low_limit, upper_limit))
    total, best_type = best(total_vals, step, user_function, low_limit, upper_limit)
    string += f" best approximation for {step} steps"
  total = total.__round__(11)
  return total, string, best_type

def right_pnt(step, user_function, low_limit, upper_limit):
  total = 0
  count = 1
  f = lambda x: eval(user_function)
  rise = (upper_limit - low_limit)/ step
  while (count <= step):
    total += f(low_limit + count*rise)
    count += 1
  total *= rise
  return total

def left_pnt(step, user_function, low_limit, upper_limit):
  total = 0
  count = 0
  f = lambda x: eval(user_function)
  rise = (upper_limit - low_limit)/ step
  while ( count < step):
    total += f(low_limit + count*rise)
    count += 1
  total *= rise
  return total

def midpoint(step, user_function, low_limit, upper_limit):
  total = 0
  count = 0
  f = lambda x: eval(user_function)
  rise = (upper_limit - low_limit)/ step
  rise_2 = rise/2
  low_limit += rise_2
  while ( count < step):
    step_val = low_limit + count*rise
    total += f(step_val)
    count += 1
  total *= rise
  return total

def trapezoid(step, user_function, low_limit, upper_limit):
    total = 0
    count = 0
    others = 2
    f = lambda x: eval(user_function)
    rise = (upper_limit - low_limit)/ step
    while ( count <= step):
      step_val = low_limit + count*rise
      if count != 0 and count != step:
       total += 2* f(step_val)
      else:
        total += f(step_val)
      count += 1
    total *= rise
    total /= 2
    return total

def parabolic(step, user_function, low_limit, upper_limit):
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
  return total

def best(total_vals, step, user_function, low_limit, upper_limit):
  position_bests = ["trapezoidal", "parabolic"]
  step = step
  test_1 = parabolic(100, user_function, low_limit, upper_limit)
  test_2 = parabolic(1000, user_function, low_limit, upper_limit)
  test = test_1 - test_2
  if test > 0:
    best = min(total_vals)
  if test < 0:
    best = max(total_vals)
  position = total_vals.index(best)
  best_type = position_bests[position]
  return best, best_type

def main():
  print("Hello, I approximate integrals for you")
  user_function = new_function()
  step = change_step()
  lower_limit, upper_limit = change_limits()
  user_input = ""
  aprox_type = "b"
  print(MENU)
  while user_input != "q":
    if user_input == "g":
      useless_2 = input()
      print(MENU)
    user_input = correct_choice()
    if user_input == "n":
      user_function = new_function()
      user_function = replacer(user_function)

    if user_input == "c":
      step = change_step()
    
    if user_input == "m":
      lower_limit, upper_limit = change_limits()

    if user_input == "r":
      user_function = new_function()
      step = change_step()
      lower_limit, upper_limit = change_limits()

    if user_input == "t":
      print("\n--- r - right endpoint\n    l - left endpoint\n    m - midpoint\n    t - trapezoidal\n    p - parabolic\n    a - average of all types\n    b - best of all types")
      aprox_type = correct_approx()

    if user_input == "g":
      best_type = ""
      approximation, string, best_type = approximater(user_function, step , lower_limit, upper_limit, aprox_type)
      print(f"{string}: {approximation}")
      if best_type != "":
        print(f"The best approximation type was: {best_type}")

    if user_input == "?":
      print("This uses a type of area approximation called Simpson's Rule,\nwhich is a sum of parabolas formed between the points we're approximating from...")

  print("Thank you for using me :), I hope I helped from tedious calculation")

main()
