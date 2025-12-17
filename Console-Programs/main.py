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
#print("Welcome to the Number Guessing Game!")
#import random

#number_to_guess = random.randint(1, 100)
#attempts = 0


#while attempts == 0:
#    print("Choose the diffuculty level: \n 1. Easy (10 attempts) \n 2. Medium (7 attempts) \n 3. Hard (5 attempts)")
#    difficulty = input("Your choice: ")
#    if difficulty == '1':
#        attempts = 10
#    elif difficulty == '2':
#        attempts = 7
#    elif difficulty == '3':
#        attempts = 5
#    else:
#        print("Invalid choice. Please select 1, 2, or 3.")


#guessed_correctly = False
#while attempts > 0:
#    print(f"\nYou have {attempts} attempts left.")
#    try:
#        user_guess = int(input("Make a guess between 1 and 100: "))
#    except ValueError:
#        print("That's not a valithe number!")
#        guessed_correctly = True
#       break
    
#    attempts -= 1

#if not guessed_correctly:
#   print(f"\nSorry, you ran out of attempts. The number was {number_to_guess}.")


# Mini Finance Tracker

users = {}
is_working = True
print("Welcome to Mini Finance Tracker")


user_register = input("Enter your name: ").strip()

if user_register:
    if user_register not in users:
        users[user_register] = 0
    print(f"Hello, {user_register}!")
else:
    print("Error: Name cannot be empty")
    exit()
while is_working:
    print("\nChoose the function:")
    print("1. See balance")
    print("2. Remove from balance")
    print("3. Add to balance")
    print("4. Exit")

    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Please enter a valid number (1-4).")
        continue

    if choice == 1:
        print(f"Your Balance is: {users[user_register]}")
    elif choice == 2:
        try:
            remove_money = int(input("Enter money to remove from balance: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if remove_money > users[user_register]:
            print("Not enough balance!")
        else:
            users[user_register] -= remove_money
            print(f"{remove_money} removed. New Balance: {users[user_register]}")
    elif choice == 3:
        try:
            add_money = int(input("Enter money to add to balance: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        users[user_register] += add_money
        print(f"{add_money} added. New Balance: {users[user_register]}")
    elif choice == 4:
        print("Exiting Mini Finance Tracker...")
        is_working = False
    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
