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

#Default variables:
comparison_counter = 0

#Default function for handling execution loop:
def execution_loop():
  data = input("Do you want to try again ? Enter [1] - for continue / [0] - for quit : ")
  if data == 1:
    return True
  elif data == 0:
    return False
  else:
    print("Error: your entered incorrect command. Please, try again...")
    execution_loop()

#Function for testing all available arithmetic operators on the Python:
def arithmetic_func(x, y):
    print('\nArithmetic operations')
    print('{0} + {1} = {2}'.format(x, y, x+y))
    #print(f'{x} - {y} = {x-y}')
    print('{0} - {1} = {2}'.format(x, y, x-y))
    if (y == 0):
      #print(f'You cannot divide {x} by zero.')
      print('You cannot divide {0} by zerp.'.format(x))
    else:
      #print(f'{x} / {y} = {x/y}')
      #print(f'{x} // {y} = {x//y}')
      print('{0} / {1} = {2}'.format(x, y, x/y))
      print('{0} // {1} = {2}'.format(x, y, x//y))
    #print(f'{x} * {y} = {x*y}')
    #print(f'{x} ^ {y} = {x**y}')
    print('{0} * {1} = {2}'.format(x, y, x*y))
    print('{0} ** {1} = {2}'.format(x, y, x**y))

#Function for testing all available comparison operators on the Python:
def comparison_func(x, y):
  print('\nComparison operations for operands:\n')
  comparator = x > y
  command = 'greater_than'
  print(comparison_string_func(command, comparator, x, y, 1))
  comparator = x < y
  command = 'less_than'
  print(comparison_string_func(command, comparator, x, y, 2))
  comparator = x == y
  command = 'equal_to'
  print(comparison_string_func(command, comparator, x, y, 3))
  comparator = x != y
  command = 'not_equal_to'
  print(comparison_string_func(command, comparator, x, y, 4))
  comparator = x >= y
  command = 'greater_equal'
  print(comparison_string_func(command, comparator, x, y, 5))
  comparator = x <= y
  command = 'less_equal'
  print(comparison_string_func(command, comparator, x, y, 6))
  print('\n')

def comparison_string_func(operation, comparator, x, y, index):
  message = {
    'greater_than': 'is greater than' if comparator else 'is not greater than',
    'less_than': 'is less than' if comparator else 'is not less than',
    'equal_to': 'is equal to' if comparator else 'is not equal to',
    'not_equal_to': 'is not equal to' if comparator else 'is equal to',
    'greater_equal': 'is greater or equal to' if comparator else 'is not greater or equal to',
    'less_equal': 'is less or equal to' if comparator else 'is not less or equal to'
  }[operation]
  #output = f'{index}. Operand {x} {message} {y}.'
  output = '{0}. Operand {1} {2} {3}'.format(index, x, message, y)
  return output

#Default parameter for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  print("Please, enter your operands for starting all necessary operations:")
  x = float(input('x = '))
  y = float(input('y = '))
  arithmetic_func(x, y)
  comparison_func(x, y)
  counter_exec = counter_exec + 1
  again_exec = execution_loop()

  #The end of execution:
  if again_exec == False:
    print("Program was executed: ",counter_exec, ' times.')
    break


print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )