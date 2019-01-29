print(
  '-----------------------------------------\n'\
  'Practical python education || Python Operators:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Explore and analyze all available types of operators on the Python.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

#Default function for handling execution loop:
def execution_loop():
  data = input("Do you want to try again ? Enter [y] - for continue / [n] - for quit : ")
  if data == "y":
    return True
  elif data == "n":
    return False
  else:
    print("Error: your entered incorrect command. Please, try again...")
    execution_loop()

#Function for testing all available arithmetic operators on the Python:
def arithmetic_func(x, y):
    print('x + y =', x+y)
    print('x - y =', x-y)
    print('x * y =', x*y)
    print('x / y =', x/y)
    print('x // y =', x//y)
    print('x ** y =', x**y)

#Default parameter for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  print("Please, enter your operands for starting all necessary operations:")
  x = int(input('x = '))
  y = int(input('y = '))
  arithmetic_func(x, y)
  execution_loop()

  #The end of execution:
  if again_exec == False:
    print("Program was executed: ",counter_exec, ' times.')
    break


print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )