# Math Quiz

import random

def main():
    print("Hello, welcome to the python math quiz!")
    difficulty = choose()
    # SETTINGS
    if difficulty == 1:
        max = 2
        highest = 10
        rounds = 3
        operands = ["+", "-"]
    if difficulty == 2:
        max = 3
        highest = 12
        rounds = 5
        operands = ["+", "-", "*"]
    if difficulty == 3:
        max = 5
        highest = 15
        rounds = 10
        operands = ["+", "-", "*", "/"]

    points = 0
    for round in range(rounds):
        print()
        print("Round", round + 1)
        equation, answer = generate(difficulty, max, highest, operands)
        while True:
            print()
            print(equation)
            user_answer = input("Please work out the missing gap: \n>>> ")
            if user_answer.isdigit() == True:
                break
        if str(user_answer) == str(answer):
            points += 1
            print("That’s correct!")
        else:
            print("Sorry, that’s not correct, the correct answer was", answer)
        print("Score:", points, "out of", rounds)
    print()
    percentage = str(int(points / rounds * 100))
    print("The end! You got " + percentage + "% of the questions correct!")

    play_again()

def generate(difficulty, max, highest, operands):
    #i = -1
    while True:
        #i += 1
        #print("try", i)
        cover, question, question_mc, q_answer, answer = form_equation(max, highest, operands)
        #print(question)
        #print(q_answer)
        if difficulty == 3:
            if str(q_answer).isdigit() == False:
                #j = -1
                while True:
                    #j += 1
                    #print("tryj", j)
                    #print(question)
                    #print(q_answer)
                    cover, question, question_mc, q_answer, answer = form_equation(max, highest, operands)
                    if str(q_answer)[-2:] == ".0":
                        q_answer = int(q_answer)
                    if "/" in question and str(q_answer).isdigit()  == True and '-' not in str(q_answer):
                        break
                break
            else:
                break
        elif '-' not in str(q_answer):
            break
        #print("EQU_TRY", question, "ANS_TRY", answer)

    if cover == -1:
        equation = question + str(" __")
        answer = q_answer
        #print("COV-1", equation, answer)
    else:
        equation = question_mc + str(q_answer)
        #print("COV0", equation, answer)

    read_equation = readable(equation)
    return read_equation, answer

def form_equation(max, highest, operands):
    amount_of_numbers = random.randint(2, max)
    q_number = []
    q_operand = []
    answer = ""
    for number in range(amount_of_numbers):
        #print("NUM", number)
        #print("AON", amount_of_numbers)
        q_number.append(random.randint(1, highest))
        if number != (amount_of_numbers - 1):
            q_operand.append(random.choice(operands))
    q_operand.append("=")
    cover = random.randint(-1, amount_of_numbers - 1)
    question = ""
    question_mc = ""
    for number in range(amount_of_numbers):
        question += str(q_number[number])
        question += q_operand[number]
        if number == cover:
            question_mc += "__"
            answer = q_number[cover]
        else:
            question_mc += str(q_number[number])
        question_mc += q_operand[number]
    q_answer = eval(question[:-1])
    return cover, question, question_mc, q_answer, answer

def readable(equ):
    output = ""
    for char in equ:
        if char == "+":
            output += " + "
        elif char == "-":
            output += " − "
        elif char == "*":
            output += " × "
        elif char == "/":
            output += " ÷ "
        elif char == "=":
            output += " = "
        else:
            output += char
    return output

def choose():
    while True:
        choice = input("Please select difficulty.\n1 – Easy: 3 rounds, adding and subtracting small positive full numbers \n2 – Medium: 5 rounds, adding, subtracting and multiplying medium positive full numbers\n3 – Hard: 10 rounds, adding, subtracting, multiplying, and deviding harder positive full numbers\nPlease enter number:\n>>> ")
        if choice.isdigit() == True and eval(choice) >= 1 and eval(choice) <= 3:
            return int(choice)
        print()

def play_again():
    print()
    while True:
        choice = input("Do you want to play again? (y/n)\n>>> ").lower()
        if choice == "y":
            print()
            main()
            break
        if choice == "n":
            break

if __name__ == "__main__":
    main()
