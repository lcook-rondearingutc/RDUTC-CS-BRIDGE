# Convert Numbers to Words
def main():
    while True:
        num = input("Please enter a whole number: ")
        try:
            num = int(num.replace(",", ""))
            if num >= -999999999 and num <= 999999999:
                break
            else:
                print("Out of range! (-999,999,999 ~ 999,999,999)")
        except:
            pass

    if num < 0:
        eng = "minus "
        num = abs(num)
    else:
        eng = ""

    length = len(str(num))
    if length == 1:
        eng += convert_1(num, True)
    if length == 2:
        eng += convert_2(num, True)
    if length == 3:
        eng += convert_3(num, True)
    if length == 4:
        eng += convert_4(num, True)
    if length == 5:
        eng += convert_5(num, True)
    if length == 6:
        eng += convert_6(num, True)
    if length == 7:
        eng += convert_7(num, True)
    if length == 8:
        eng += convert_8(num, True)
    if length == 9:
        eng += convert_9(num, True)

    print()
    print(eng)
    again()

def again():
    print()
    while True:
        choice = input("Again? (y/n)\n>>> ").lower()
        if choice == "y":
            print()
            main()
            break
        if choice == "n":
            break

def convert_1(num, main):
    if num == 0:
        word = "zero"
    elif num == 1:
        word = "one"
    elif num == 2:
        word = "two"
    elif num == 3:
        word = "three"
    elif num == 4:
        word = "four"
    elif num == 5:
        word = "five"
    elif num == 6:
        word = "six"
    elif num == 7:
        word = "seven"
    elif num == 8:
        word = "eight"
    elif num == 9:
        word = "nine"

    if main == True:
        return word
    elif main == False:
        if num == 0:
            return ""
        return "-" + word

def convert_1x(num):
    if num == 10:
        return "ten"
    if num == 11:
        return "eleven"
    if num == 12:
        return "twelve"
    if num == 13:
        return "thirteen"
    if num == 14:
        return "fourteen"
    if num == 15:
        return "fifteen"
    if num == 16:
        return "sixteen"
    if num == 17:
        return "seventeen"
    if num == 18:
        return "eightteen"
    if num == 19:
        return "nineteen"

def convert_2(num, main):
    comp = int(str(num)[0])
    if comp == 1:
        word = convert_1x(num)
    if comp == 2:
        word = "twenty" + convert_1(int(str(num)[-1]), False)
    if comp == 3:
        word = "thirty" + convert_1(int(str(num)[-1]), False)
    if comp == 4:
        word = "fourty" + convert_1(int(str(num)[-1]), False)
    if comp == 5:
        word = "fifty" + convert_1(int(str(num)[-1]), False)
    if comp == 6:
        word = "sixty" + convert_1(int(str(num)[-1]), False)
    if comp == 7:
        word = "seventy" + convert_1(int(str(num)[-1]), False)
    if comp == 8:
        word = "eighty" + convert_1(int(str(num)[-1]), False)
    if comp == 9:
        word = "ninety" + convert_1(int(str(num)[-1]), False)

    if main == True:
        return word
    elif main == False:
        if num == 0:
            return ""
        elif len(str(num)) == 1:
            word = convert_1(num, True)
        return " and " + word

def convert_3(num, main):
    if main == True:
        space = ""
    elif main == False:
        space = " "

    comp = int(str(num)[0])
    if len(str(num)) < 3:
        return convert_2(num, False)
    return space + convert_1(int(str(num)[0]), True) + " hundred" + convert_2(int(str(num)[-2:]), False)

def convert_4(num, main):
    if main == True:
        space = ""
    elif main == False:
        space = " "

    comp = int(str(num)[0])
    if main == False:
        if len(str(num)) < 4:
            return convert_3(num, False)
    return space + convert_1(int(str(num)[0]), True) + " thousand" + convert_3(int(str(num)[-3:]), False)

def convert_5(num, main):
    if main == True:
        space = ""
    elif main == False:
        space = " "

    comp = int(str(num)[0])
    if main == False:
        if len(str(num)) < 5:
            return convert_4(num, False)
    return space + convert_2(int(str(num)[:2]), True) + " thousand" + convert_3(int(str(num)[-3:]), False)

def convert_6(num, main):
    if main == True:
        space = ""
    elif main == False:
        space = " "

    comp = int(str(num)[0])
    if main == False:
        if len(str(num)) < 6:
            return convert_5(num, False)
    return space + convert_3(int(str(num)[:3]), True) + " thousand" + convert_3(int(str(num)[-3:]), False)

def convert_7(num, main):
    if main == True:
        space = ""
    elif main == False:
        space = " "

    comp = int(str(num)[0])
    if main == False:
        if len(str(num)) < 7:
            return convert_6(num, False)
    return space + convert_1(int(str(num)[:1]), True) + " million" + convert_6(int(str(num)[-6:]), False)

def convert_8(num, main):
    if main == True:
        space = ""
    elif main == False:
        space = " "

    comp = int(str(num)[0])
    if main == False:
        if len(str(num)) < 8:
            return convert_7(num, False)
    return space + convert_2(int(str(num)[:2]), True) + " million" + convert_6(int(str(num)[-6:]), False)

def convert_9(num, main):
    if main == True:
        space = ""
    elif main == False:
        space = " "

    comp = int(str(num)[0])
    if main == False:
        if len(str(num)) < 9:
            return convert_8(num, False)
    return space + convert_3(int(str(num)[:3]), True) + " million" + convert_6(int(str(num)[-6:]), False)

if __name__ == "__main__":
    main()
