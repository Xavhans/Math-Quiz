# Imports
import random

# Global Variables
score = 0


def check_int(question):
    while True:
        try:
            user_input = int(input(question))
            if user_input < 1:
                print("ERROR: PLEASE ENTER A VALID NUMBER!\n")
            else:
                return user_input
        except:
            print("ERROR: PLEASE ENTER NUMBER!\n")


def one_quiz():
    global score, round_amount, round_counter
    round_counter = 0
    for x in range(round_amount):
        round_counter += 1
        num1 = random.randint(1, 10)
        num2 = random.randint(2, 9)
        print(f"Question: {round_counter}")
        print(f"What is {num1} x {num2} = ")

        user_answer = check_int("")
        answer = num1 * num2
        if user_answer == answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong!\nThe correct answer is {answer}\n")
# main


print(" ,---.  ,--.                 ,--.           ,--.   ,--.          ,--.  ,--.                 ,-----.           ,--.        \n"
      "'   .-' `--',--,--,--. ,---. |  | ,---.     |   `.'   | ,--,--.,-'  '-.|  ,---.  ,---.     '  .-.  '  ,--.,--.`--',-----. \n"
      "`.  `-. ,--.|        || .-. ||  || .-. :    |  |'.'|  |' ,-.  |'-.  .-'|  .-.  |(  .-'     |  | |  |  |  ||  |,--.`-.  /  \n"
      ".-'    ||  ||  |  |  || '-' '|  |\   --.    |  |   |  |\ '-'  |  |  |  |  | |  |.-'  `)    '  '-'  '-.'  ''  '|  | /  `-. \n"
      "`-----' `--'`--`--`--'|  |-' `--' `----'    `--'   `--' `--`--'  `--'  `--' `--'`----'      `-----'--' `----' `--'`-----' \n"
      "                      `--'")
print("Welcome to the Simple Maths Quiz. In this quiz you will answer simple multiplication questions\n")
round_amount = check_int("How many questions would you like to be asked?\n")


one_quiz()
percent_score = (score / round_amount)
perc = percent_score * 100

print(f"Your final score is {score} out of {round_amount}")
if perc == 100:
    print("WELL DONE!")
print(f"{round(perc, 2)}%")

