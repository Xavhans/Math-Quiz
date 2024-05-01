# Imports
import random

# Global Variables
score = 0


def check_int(question):
    while True:
        try:
            user_input = int(input(question))
            if user_input < -10:
                print("ERROR: PLEASE ENTER A VALID NUMBER!\n")
            else:
                return user_input
        except:
            print("ERROR: PLEASE ENTER NUMBER!\n")


def menu():
    menu = ["1. Addition","2. Subtraction","3. Exit" ]
    print(menu[0])
    print(menu[1])
    print(menu[2])


def menu_checker():
    menu_input = int(input("\nEnter Your choice!\n"))
    while menu_input > 3 or menu_input <= 0:
        print("ERROR: PLEASE ENTER A VALID NUMBER\n")
        menu_input = int(input("TRY AGAIN!\n"))
    else:
        if menu_input == 3:
            print("Thank you for playing my quiz!")
            quit()
        return menu_input



def one_quiz():
    global score, round_amount, round_counter
    round_counter = 0

    for x in range(round_amount):
        round_counter += 1

        # Generating random numbers
        num1 = random.randint(1, 10)
        num2 = random.randint(2, 9)

        # Telling the user what question they are on
        print(f"Question: {round_counter}")

        # Asking the user the question
        if choice == 1:
            print(f"What is {num1} + {num2} = ")

        # Checking the users answer to see if it is an integer
            user_answer = check_int("")

        # The correct answer
            answer = num1 + num2

        # Prints if the user got the correct answer
            if user_answer == answer:
                print("Correct!\n")

            # Adds one to the user's score
                score += 1
        # Prints if the user inputted the incorrect answer. Displays correct answer
            else:
                print(f"Wrong!\nThe correct answer is {answer}\n")


        if choice == 2:
            print(f"What is {num1} - {num2} = ")

        # Checking the users answer to see if it is an integer
            user_answer = check_int("")

        # The correct answer
            answer = num1 - num2

        # Prints if the user got the correct answer
            if user_answer == answer:
                print("Correct!\n")

            # Adds one to the user's score
                score += 1
        # Prints if the user inputted the incorrect answer. Displays correct answer
            else:
                print(f"Wrong!\nThe correct answer is {answer}\n")





# main



# Title


print(" ,---.  ,--.                 ,--.           ,--.   ,--.          ,--.  ,--.                 ,-----.           ,--.        \n"
      "'   .-' `--',--,--,--. ,---. |  | ,---.     |   `.'   | ,--,--.,-'  '-.|  ,---.  ,---.     '  .-.  '  ,--.,--.`--',-----. \n"
      "`.  `-. ,--.|        || .-. ||  || .-. :    |  |'.'|  |' ,-.  |'-.  .-'|  .-.  |(  .-'     |  | |  |  |  ||  |,--.`-.  /  \n"
      ".-'    ||  ||  |  |  || '-' '|  |\   --.    |  |   |  |\ '-'  |  |  |  |  | |  |.-'  `)    '  '-'  '-.'  ''  '|  | /  `-. \n"
      "`-----' `--'`--`--`--'|  |-' `--' `----'    `--'   `--' `--`--'  `--'  `--' `--'`----'      `-----'--' `----' `--'`-----' \n"
      "                      `--'")

# Welcoming the user
print("Welcome to the Simple Maths Quiz. In this quiz you will answer simple addition and subtraction questions\n")

# Asking the user how many questions they want to be asked

menu()
choice = menu_checker()


round_amount = check_int("How many questions would you like to be asked?\n")
one_quiz()
# Getting the users percentage score
percent_score = (score / round_amount)
perc = percent_score * 100

# Displaying the user's final score
print(f"Your final score is {score} out of {round_amount}")
if perc == 100:
    print("WELL DONE!")
print(f"{round(perc, 2)}%")

