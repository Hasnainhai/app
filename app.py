# from student import student
from Questions import Questions
# # Functions
# def say_hi(name,age):
#     print("Hello your name is: " + name + " and your age is: " + age)
# say_hi('hasnain','23')
# #
# # # Return Function
# def cube(num):
#    return num*num*num
# result = cube(5)
# print("Return result of the return fun is: " +str(result) )
# #
# # # max number fun
# def max_num(num1,num2,num3):
#     if num1 >= num2 and num1 >= num3:
#         return print('The max number is num1: ' + str(num1) )
#     elif num2 >= num1 and num2 >= num3:
#         return print('The max number is num2: ' + str(num2) )
#     else:
#         return print('The max number is num3: ' + str(num3) )
# print(str( max_num(100,180,4)))
#
# # calculator
# num1 = float(input("Enter first number: "))
# operator = input("Enter the operator: ")
# num2 = float(input("Enter second number: "))
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#      print(num1 / num2)
# else:
#     print("Invalid operator")
#
# # dictionary
# monthConversions = {
#     'Jan': 'january',
#     'Feb': 'february',
#     'Mar': 'march',
#     'Apr': 'april',
#     'May': 'may',
#     'Jun': 'june',
#     'Jul': 'july',
#     'Aug': 'august',
#     'Sep': 'september',
#     'Oct': 'october',
#     'Nov': 'november',
#     'Dec': 'december',
# }
# print(monthConversions.get('Oct','invalid key'))
#
# # guess game
# secret_word = 'password'
# guess = ''
# guess_count = 0
# guess_limit =3
# out_of_guesses = False
# while secret_word != guess and not(out_of_guesses):
#     if guess_count < guess_limit:
#       guess = input('Enter your guess: ')
#       guess_count += 1
#     else:
#       out_of_guesses = True
#
# if out_of_guesses:
#     print('Sorry, You loss the match ')
# else:
#   print('you win')
#
# # Exponent Function
# def raise_to_power(bas_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#          result = result * bas_num
#     return result
# print(raise_to_power(3, 3))
#
# # List & Nested Loops
# number_grid = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
# ]
# # print(number_grid[2][3])
# for row in number_grid:
#     for col in row:
#      print(col)
#
# # Building a Translator
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.islower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#               translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
# print(translate("Enter a phrase: "))
# from Questions import Questions
from student import Student

# try except errors
# try:
#    value = 10/0
#    number = int(input("Enter a number: "))
#    print(number)
#    print(value)
# except ValueError:
#     print('invalid input')
# except ZeroDivisionError as err:
#     print(err)
#
# employee_file = open("employees.txt","r")
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.read())
# employee_file.close()
# employee_file = open("index.html","w")
# employee_file.write("<p>This is Html</p>")
# employee_file.write('\nNew one')
# employee_file.close()

ali  = Student('ali','23','CS','3.0','yes')
hasnain  = Student('hasnain','24','SE','3.2','No')
basit  = Student('Basit','25','SE','3.4','yes')
print('........ Student Ali Result............')
print('Name: '+ali.name,'\nAge: '+ ali.age,'\nMajor: '+ ali.major,'\nGPA: '+ ali.gpa, '\nis_on_probition: '+ ali.is_on_probition)
print('........\n Student Hasnain Result............')
print('Name: '+hasnain.name,'\nAge: '+ hasnain.age,'Major: '+ hasnain.major,'\nGPA: '+ hasnain.gpa, '\nis_on_probition: '+ hasnain.is_on_probition)
print('........\n Student Basit Result............')
print('Name: '+basit.name,'\nAge: '+ basit.age,'Major: '+ basit.major,'\nGPA: '+ basit.gpa, '\nis_on_probition: '+ basit.is_on_probition)


# Questions quiz
question_prompts = [
    "What color are apples?\n (a) Red/Green\n (b) Purple\n (c) Orange \n\n",
    "What color are bananas?\n (a) Teal \n (b) Magenta \n (c) Yellow \n\n",
    "What color are strawberries?\n (a) Yellow \n (b) Red \n (c) Blue \n\n",
    "What color are papetas?\n (a) Red/Green\n (b) Purple\n (c) Orange \n\n",
    "What color are Mangoes?\n (a) Yellow \n (b) Red \n (c) Blue \n\n",
]

questions = [
    Questions(question_prompts[0], 'a'),
    Questions(question_prompts[1], 'c'),
    Questions(question_prompts[2], 'b'),
    Questions(question_prompts[3], 'a'),
    Questions(question_prompts[4], 'b'),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print(f"You got {score}/{len(questions)} Correct")

run_test(questions)