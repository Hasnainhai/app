# Functions
def say_hi(name,age):
    print("Hello your name is: " + name + " and your age is: " + age)
say_hi('hasnain','23')
#
# # Return Function
def cube(num):
   return num*num*num
result = cube(5)
print("Return result of the return fun is: " +str(result) )
#
# # max number fun
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return print('The max number is num1: ' + str(num1) )
    elif num2 >= num1 and num2 >= num3:
        return print('The max number is num2: ' + str(num2) )
    else:
        return print('The max number is num3: ' + str(num3) )
print(str( max_num(100,180,4)))

# calculator
num1 = float(input("Enter first number: "))
operator = input("Enter the operator: ")
num2 = float(input("Enter second number: "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
     print(num1 / num2)
else:
    print("Invalid operator")

# dictionary
monthConversions = {
    'Jan': 'january',
    'Feb': 'february',
    'Mar': 'march',
    'Apr': 'april',
    'May': 'may',
    'Jun': 'june',
    'Jul': 'july',
    'Aug': 'august',
    'Sep': 'september',
    'Oct': 'october',
    'Nov': 'november',
    'Dec': 'december',
}
print(monthConversions.get('Oct','invalid key'))

# guess game
secret_word = 'password'
guess = ''
guess_count = 0
guess_limit =3
out_of_guesses = False
while secret_word != guess and not(out_of_guesses):
    if guess_count < guess_limit:
      guess = input('Enter your guess: ')
      guess_count += 1
    else:
      out_of_guesses = True

if out_of_guesses:
    print('Sorry, You loss the match ')
else:
  print('you win')