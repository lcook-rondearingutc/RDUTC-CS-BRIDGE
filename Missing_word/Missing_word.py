# Missing Word Guessing Game

import random

def main():
    print("Welcome to the word guessing game. Guess the empty word, type \"end\" to end the game.")
    round = 0
    score = 0
    while True:
        question, answer, full = get()
        print(f"Round {round + 1}!")
        print()
        print(question)
        print()
        guess = input("Please enter your guess: \n>>> ")
        print()
        if guess.lower() == answer.lower():
            score += 1
            print(f"\"{answer}\" is correct! +1 point")
        elif guess.lower() == "end":
            break
        else:
            print(f"Sorry, \"{guess.lower()}\" is not correct, the correct answer was \"{answer}\".")
            print(f"\"{full}\"")
        round += 1
        print()
        print(f"score: {score}")
        input("Press \"Enter\" to continue...")
        print()
    print(f"Final score: {score}, out of a total of {round} rounds. ({int(score / round * 100)}%)")

def get():
    file = open("Missing_word.ini", "r")
    sentences = file.read()
    file.close()
    if sentences[-1] == "\n":
        sentences = sentences[:-1]
    sentences_split = sentences.split("\n")
    lines = sentences.count("\n")
    print(lines)
    random_line = random.randint(0, lines)
    sentence = sentences_split[random_line]

    question = ""
    answer = ""
    hide = [sentence.find("<"), sentence.find(">")]
    for char_count, char in enumerate(sentence):
        #print(char_count, hide[0], hide[1])
        if char_count > hide[0] and char_count < hide[1]:
            question += "_"
            answer += char
        else:
            if char_count == hide[1] + 1:
                question += str(f"({len(answer)})")
            question += char
    return question.replace("<", "").replace(">", ""), answer, sentence.replace("<", "").replace(">", "")

if __name__ == "__main__":
    main()
