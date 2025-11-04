#Task 1:
# print("Welcome to the Simple Calculator!\n This calculator can perform addition, subtraction, multiplication, and division.")
# num1 = int(input("Enter the first number: "))
# operation = input("Enter the operation (+, -, *, /): ")
# num2 = int(input("Enter the second number: "))
# caclulator_mode = True

# while caclulator_mode == True:
#     if operation == '+':
#         result = num1 + num2
#         print(f"The result of {num1} + {num2} is {result}")
#         caclulator_mode = False
#     elif operation == '-':
#         result = num1 - num2
#         print(f"The result of: {num1} - {num2} is {result}")
#         caclulator_mode = False
#     elif operation == '*':
#         result = num1 * num2
#         print(f"The result of: {num1} * {num2} is {result}")
#         caclulator_mode = False
#     elif operation == '/':
#         result = num1 / num2
#         print(f"The result of: {num1} / {num2} is {result}")
#         caclulator_mode = False
#     else:
#         print("Invalid operation. Please enter one of +, -, *, /.")

# Task 2:
# print("Welcome to the To-DO List")

# todos = []

# users = {
#     "Aza": {
#         "password": 23,
#         "todos": ["Clean the room", "Do the homework"]
#     },
#     "Jovo": {
#         "password": 290,
#         "todos": ["Learn Math", "Training Gym"]
#     }
# }

# username = input("Enter your username: ")
# password = int(input("Enter your password: "))

# if username in users and users[username]["password"] == password:
#     print("Choose an option(Write number of option): \n 1. View To-Do List \n 2. Remove To-Do Item")
#     option = int(input("Your option: "))
#     if option == 1:
#         print("Your To-Do List:")
#         for idx, todo in enumerate(users[username]["todos"], start=1):
#             print(f"{idx}. {todo}")
#     elif option == 2:
#         print("Your To-Do List:")
#         for idx, todo in enumerate(users[username]["todos"], start=1):
#             print(f"{idx}. {todo}")
#         item_number = int(input("Enter the number of the item you want to remove: "))
#         if 1 <= item_number <= len(users[username]["todos"]):
#             removed_item = users[username]["todos"].pop(item_number - 1)
#             print(f"Removed: {removed_item}")
#         else:
#             print("Invalid item number.")
#     else:
#         print("Invalid option selected.")



# Task 3:
print("Welcome to the Number Guessing Game!")
import random

number_to_guess = random.randint(1, 100)
attempts = 0


while attempts == 0:
    print("Choose the diffuculty level: \n 1. Easy (10 attempts) \n 2. Medium (7 attempts) \n 3. Hard (5 attempts)")
    difficulty = input("Your choice: ")
    if difficulty == '1':
        attempts = 10
    elif difficulty == '2':
        attempts = 7
    elif difficulty == '3':
        attempts = 5
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


guessed_correctly = False
while attempts > 0:
    print(f"\nYou have {attempts} attempts left.")
    try:
        user_guess = int(input("Make a guess between 1 and 100: "))
    except ValueError:
        print("That's not a valid number. Try again.")
        continue

    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number!")
        guessed_correctly = True
        break
    
    attempts -= 1

if not guessed_correctly:
    print(f"\nSorry, you ran out of attempts. The number was {number_to_guess}.")