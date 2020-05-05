def main():
    input_string = input("Enter a string: \n")
    characters = character_count(input_string)
    if characters == False:
        print("Empty string!")
    else:
        characters_format = ""
        loop_count = 0
        for char, count in characters.items():
            loop_count += 1
            characters_format += str(str(count) + " x " + char)
            if loop_count < len(characters):
                characters_format += ", "
        print(f"\n\"{input_string}\" has {characters_format}.")

def character_count(inp):
    if len(inp) == 0:
        return False
    characters = {}
    for char in inp:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

if __name__ == "__main__":
    main()
