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