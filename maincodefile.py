from mathmodule import *
import sys

print("Welcome to my basic \'Calculator\'")

print("Please choose your best option (+, -, *, /) ")

# user input part 
while True:
  try:
    A = int(input("Now Enter your first Value="))
    break
  except:
    print("Oops!", sys.exc_info()[0], "occurred.")
while True:
  mathoparetor = input("Enter your Math oparetor=")
  try:
    if mathoparetor in ['+','-','*','/']:
      break
    else:
      raise Exception
  except:
    print("Opp, Enter Math again")

while True:
  try:
    B = int(input("Now Enter your second Value="))
    break
  except:
    print("Oops!", sys.exc_info()[0], "occurred.")



# programing for perform
if mathoparetor == '+':
  print('The addition number is', add(A,B))

elif mathoparetor == '-':
  print('The subtraction number is', sub(A,B))

elif mathoparetor == '*':
  print('The multiaplication number is', mull(A,B))

elif mathoparetor == '/':
  print('The division number is', divi(A,B))