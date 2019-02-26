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
  #data = input("Do you want to try again ? Enter [y] - for continue / [n] - for quit : ")
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
    return min(x, x+Y)

class C:
    f = fl
    def g(self):
        return 'I\'m a function "g".'
    h = g

#Default parameter for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  first_instance = new C()
  print(first_instance.f())
  print(first_instance.g())
  print(first_instance.h())
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