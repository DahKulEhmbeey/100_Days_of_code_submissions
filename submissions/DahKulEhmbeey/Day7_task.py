def get_input():
    user_input = input("Please enter a string for sorting: ")
    pass_arg(user_input)


def sort_text(word):
    word_list = list(word)
    word_list.sort()
    return "".join(word_list)


def pass_arg(user_input):
    each_word = user_input.split(" ")
    sorted_list = []
    for word in each_word:
        sort_word = sort_text(word)
        sorted_list.append(sort_word)
    print(" ".join(sorted_list))


get_input()
