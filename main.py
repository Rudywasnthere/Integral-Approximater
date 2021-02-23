##Rudy Garcia

import math as math
import random as rd
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import os

MENU = "\n\t\t--MENU--\t\t\n n - new function \n c - change step \n m - mess with limits \n r - reset all \n t - type of approximation (best of all by default) \n a - compare exact answer \n g - go! \n ? - how does this work?\n q - quit"

menu_options = "ncmrtag?q"
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
    random_1 = rd.randint(0,100)
    random_2 = rd.randint(0,100)
    random_3 = rd.randint(0,100)
    try:
      useless_garbage = f(random_1)
      play = True
    except ZeroDivisionError:
      print(f"break at: {random_1}")
      try:
        useless_again = f(random_2)
        play = True
      except ZeroDivisionError:
        play = True
        print(f"break two at: {random_2}")
        try:
          useless_finally = f(random_3)
        except ZeroDivisionError:
          print(f"break three at: {random_3}")
    except SyntaxError:
      if tries//2 == 0:
        print("I need correct syntax")
      play = False
    except NameError:
      print("NameError")
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
    low_lim = low_lim.replace("pi", "math.pi")
    low_lim = low_lim.replace("e", "math.e")
    low_lim = eval(low_lim)
    try: 
      low_lim = float(low_lim)
      play = True
    except ValueError:
      print("I need a number please")
      play = False
  play = False
  while play == False:
    upper_lim = input("upper limit: ")
    upper_lim = upper_lim.replace("pi", "math.pi")
    upper_lim = upper_lim.replace("e", "math.e")
    upper_lim = eval(upper_lim)
    try: 
      upper_lim = float(upper_lim)
      play = True
    except ValueError:
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
  if ".log(" not in user_function:
    user_function = user_function.replace("log(", "math.log10(")
  if ".ln(" not in user_function:
    user_function = user_function.replace("ln(", "math.log(")
  if ".sqrt(" not in user_function:
    user_function = user_function.replace("sqrt(", "math.sqrt(")
  if ".exp(" not in user_function:
    user_function = user_function.replace("e**x" , "math.exp(x)")
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
    try:
      total += f(low_limit + count*rise)
    except ZeroDivisionError:
      useless = 1
    count += 1
  total *= rise
  return total

def left_pnt(step, user_function, low_limit, upper_limit):
  total = 0
  count = 0
  f = lambda x: eval(user_function)
  rise = (upper_limit - low_limit)/ step
  while ( count < step):
    try:
      total += f(low_limit + count*rise)
    except ZeroDivisionError:
      useless = 1
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
    try:
      total += f(step_val)
    except ZeroDivisionError:
      useless = 1
    count += 1
  total *= rise
  return total

def trapezoid(step, user_function, low_limit, upper_limit):
    total = 0
    count = 0
    f = lambda x: eval(user_function)
    rise = (upper_limit - low_limit)/ step
    try:
      while ( count <= step):
        step_val = low_limit + count*rise
        try:
          if count != 0 and count != step:
            total += 2* f(step_val)
          else:
            total += f(step_val)
        except ZeroDivisionError:
          print("divide by zero error")
          useless = 1
        count += 1
      total *= rise
      total /= 2
    except TypeError:
      print("Trapezoidal method not working...")
    return total

def parabolic(step, user_function, low_limit, upper_limit):
  odd, even, rest = 4,2,1
  total = 0
  count = 0
  step_values = ""
  try:
    f = lambda x: eval(user_function)
    rise = (upper_limit - low_limit)/step
    while ( count <= step):
      step_value = low_limit + count *rise
      step_values += f"{step_value}  "
      try:
        if ( count == 0 or count == step):
          total += rest * f(step_value)
        elif ( count%2 == 1):
          total += odd * f(step_value)
        elif ( count%2 == 0):
          total += even * f(step_value)
      except ZeroDivisionError:
        useless = 1
      count += 1
    total *= rise
    total /= 3
  except TypeError:
    print("Parabolic method not working...")
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
  elif test == 0:
    best = test_1
  position = total_vals.index(best)
  best_type = position_bests[position]
  return best, best_type

def main():
  approximation = 0
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

    if user_input == "a":
      exact = input("exact answer: ")
      exact = exact.replace("pi", "math.pi")
      exact = exact.replace("e", "math.e")
      compare_answer = eval(exact)
      compare = abs(compare_answer - approximation)
      if compare < 0.0001:
        print(f"This is probably the exact answer (difference of : {compare} )")
      else: 
        print("Either you didn't use enough steps ( I recommend over 5000 on best)\nor your exact answer isn't it")
    if user_input == "g":
      best_type = ""
      approximation, string, best_type = approximater(user_function, step , lower_limit, upper_limit, aprox_type)
      print(f"{string}: {approximation}")
      if best_type != "":
        print(f"The best approximation type was: {best_type}")

    if user_input == "?":
      filename = ""
      if aprox_type == "r":
        print("Right endpoint approximation simply finds\nthe sum of areas of rectangles who heights\nare the right edge of the rectangle")
        filename = "all-points-approximation.png"
      if aprox_type == "l":
        print("Left endpoint approximation simply finds\nthe sum of areas of rectangles who heights\nare the left edge of the rectangle")
        filename = "all-points-approximation.png"
      if aprox_type == "m":
        print("Midpoint approximation simply finds\nthe sum of areas of rectangles who heights are is\n a vertical line splitting the rectangle in half")
        filename = "all-points-approximation.png"
      if aprox_type == "t":
        print("This basically connects the points together into a series\nof trapezoids, and adds those trapezoids together")
        filename = "trapezoid-sum.png"
      if aprox_type == "p":
        print("This uses a type of area approximation called\nSimpson's Rule,which is a sum of parabolas formed between\nthe points we're approximating from...")
        filename = "simpson-sum.jpg"
      if aprox_type == "a":
        print("This finds the a\verage for all of these 5 types of approximations demonstrated here ")
      if aprox_type == "b":
        print("This finds the approximation closest to the real value\nof the integral.It finds the direction of the approximation\nby comparinga lower approximation with a more accurate one\nto find if the approximation is goingupwards or downwards.\nFrom there it either finds the max or min\nof the trapezoidal and parabolic rule,\nbecause these two are the most satistically accurate")
      try:
        file_path = str(__file__)
        f_n_length = len(file_path) - 7
        file_name = file_path[0:f_n_length] + f"{filename}"
        print("close image to continue")
      except:
        pass
      try:
        img = mpimg.imread(f'{file_name}')
        imgplot = plt.imshow(img)
        plt.show()
      except AttributeError:
        pass
      except IOError:
        print("IOError...")
        pass
  print("Thank you for using me :), I hope I helped from tedious calculation")

main()