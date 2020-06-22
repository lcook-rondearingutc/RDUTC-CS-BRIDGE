# Switch out vowels for random other vowels (English vowels only)

# SETTINGS − set your file name here
input_file = "text_file(vowels).txt"
output_file = "text_file(vowels)-output.txt"
vowels = ["a", "e", "i", "o", "u"]

import random
import os

def main():
    if os.path.isfile(input_file) == False:
        # Create file if not existant
        create_file = open(input_file, "a")
        create_file.close()
        print("File created!")
    else:
        open_file = open(input_file, "r") # read file
        file_data = open_file.readlines()
        open_file.close()

        new_data = random_vowels(''.join(file_data)) # randomize vowels
        write_file = open(output_file, "a") # write new data to file
        write_file.write(new_data)
        write_file.close()


def random_vowels(text):
    print("Randomising vowels...")
    str = ""
    #lines = countlines(text)
    #print(lines)
    for char in text:
        if char.lower() in vowels:
            new_vowel = random.choice(vowels)
            if char.isupper() == True:
                new_vowel = new_vowel.upper()
            str += new_vowel
        else:
            str += char
    return str

def countlines(text):
    if text[-1] == "\n":
        text = text[:-1]
    return text.count("\n") + 1

if __name__ == "__main__":
    main()
