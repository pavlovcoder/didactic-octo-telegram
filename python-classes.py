print(
  '-----------------------------------------\n'\
  'Python Education || Documentation - Classes\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to test all available functionalities and code samples from the official documentation.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

#Default function for handling execution loop:
def execution_loop():
  data = int(input("Do you want to try again ? Enter [1] - for continue / [0] - for quit :"))
  if data == 1:
    return True
  elif data == 0:
    return False
  else:
    print("Error: your entered incorrect command. Please, try again...")
    execution_loop()

#Function for testing definition of function outside of the class:
def fl(self, x, y):
    return min(x, x+y)

class C:
    f = fl
    def g(self):
        return 'I\'m a function "g".'
    h = g

#Initializing a new Reverse class:
class Reverse:
  def __init__(self, data):
    self.data = data
    self.index = len(data)

  def __iter__(self):
    return self

  def __next__(self): 
    if self.index == 0:
      raise StopIteration
    self.index = self.index - 1
    return self.data[self.index]

#Function for testing iterators:
def iterators_func():
  print('Iterators fucntion was called:')
  print('Testing for loop statement with iterators:')
  for element in [1, 2, 3]:
    print(element)
  for element in (4, 5, 6):
    print(element)
  for key in {'one': 1, 'two': 2, 'three': 3}:
    print(key)
  for char in "789":
    print(char)
  for line in open("./python-classes.txt"):
    print(line, end='')

  print('\nLooping over a backward sequence:\n')

  test_string = 'vr player'
  it = iter(test_string)
  print(it)
  print(next(it))
  print(next(it))
  print(next(it))

  print('\nDisplaying a backward sequence:\n')
  rev = Reverse('spam')
  iter(rev)
  for char in rev:
    print(char)


#Default parameter for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  iterators_func()
  again_exec = execution_loop()
  counter_exec = counter_exec + 1

  #The end of execution:
  if again_exec == False:
    print("Program was executed: ",counter_exec, ' times.')
    break


print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )