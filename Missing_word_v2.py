# Missing Word Guessing Game

import random
import os
import sys

class sentences_file:
    @classmethod
    def total_add(cls, lines):
        cls.total = lines
    @classmethod
    def total(cls):
        return cls.total
    @classmethod
    def add(cls, sentences_split):
        cls.sentences = sentences_split
    @classmethod
    def list(cls):
        return cls.sentences
    @classmethod
    def lines(cls):
        return len(cls.sentences)

class guessed:
    guessed_lines = []
    @classmethod
    def add(cls, line_num):
        cls.guessed_lines.append(line_num)
        cls.guessed_lines.sort()
    @classmethod
    def list(cls):
        return cls.guessed_lines
    @classmethod
    def lines(cls):
        return len(cls.guessed_lines)

def main():
    print("Welcome to the word guessing game. Guess the empty word, type \"end\" to end the game.")
    round = 0
    score = 0
    read_file()
    while True:
        question, answer, full, line = get()
        print(f"Round {round + 1}!")
        print()
        print(question)
        print()
        guess = input("Please enter your guess: \n>>> ")
        print()
        #print(round + 1, sentences_file.lines())
        if guess.lower() == answer.lower():
            score += 1
            guessed.add(line)
            print(f"\"{answer}\" is correct! +1 point")
        elif guess.lower() == "end":
            break
        else:
            guessed.add(line)
            print(f"Sorry, \"{guess.lower()}\" is not correct, the correct answer was \"{answer}\".")
            print(f"\"{full}\"")
        if (round + 1) == sentences_file.lines():
            print("You have guessed every single question!\n")
            break
        round += 1
        print()
        print(f"score: {score}")
        input("Press \"Enter\" to continue...")
        print()

    if guessed.lines() != 0:
        print(f"Final score: {score}, out of a total of {guessed.lines()} rounds. ({int(score / guessed.lines() * 100)}%)")
        input("Press \"Enter\" to continue...")

    play_again()

def play_again():
    print()
    while True:
        choice = input("Do you want to play again? (y/n)\n>>> ").lower()
        if choice == "y":
            print()
            print()
            os.execl(sys.executable, sys.executable, * sys.argv)
            break
        if choice == "n":
            break

def read_file():
    file = open("Missing_word.ini", "r")
    sentences = file.read()
    file.close()
    if sentences[-1] == "\n":
        sentences = sentences[:-1]
    sentences_file.add(sentences.split("\n"))
    sentences_file.total_add(sentences.count("\n"))

def get():
    while True:
        random_line = random.randint(0, sentences_file.lines() - 1)
        if random_line not in guessed.list():
            break
    sentence = sentences_file.list()[random_line]

    # Debugging
    #print(sentences_file.lines())
    #print(random_line)
    #print(guessed.list())
    #print(guessed.lines())

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
    return question.replace("<", "").replace(">", ""), answer, sentence.replace("<", "").replace(">", ""), random_line

if __name__ == "__main__":
    main()
