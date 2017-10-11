alphabets = list("abcdefghijklmnopqrstuvwxyz")  # learnt about the global variables referencing in fxns
# global vars can be referenced but not assigned values by fxns


def count_vowels(user_input):
    counts = 0
    for char in alphabets:  # learnt using zip() to loop
        count = user_input.count(char)  # learnt using .count() on strings
        counts += count
        print(char, ": ", count)
    print("There are", counts, "alphabets altogether.")


def read_file():
    file = open("textfile.txt")  # learnt how to open and read files
    line = file.read()
    file.close()
    count_vowels(line.lower())


read_file()
