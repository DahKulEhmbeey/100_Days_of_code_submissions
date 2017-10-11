vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def get_input():
    user_input = input("Please enter a value: ").split()  # revised splitting texts into lists
    if len(user_input) != 1:
        arg_passer(user_input)
    else:
        print(count_vowels(user_input))


def count_vowels(user_input):
    count = 0
    for char in vowels:
        count += "".join(user_input).count(char)  # revised using __delimiter__.join(strings) method
    return count


def arg_passer(input_list):
    count = 0
    for word in input_list:
        vowel_count = count_vowels(word)
        print("There is/are {} vowel(s) in {}".format(vowel_count, word))
        count += vowel_count
    print("\nAnd there are {} vowels in all".format(count))

get_input()
