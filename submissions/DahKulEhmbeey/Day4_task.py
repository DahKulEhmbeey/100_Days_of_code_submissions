def get_input():
    user_input = input("Please enter a value: ")
    check_palindrome(user_input)


def check_palindrome(user_input):
    first_check = user_input[:]
    second_check = user_input[::-1]
    if first_check == second_check:
        print("{} is a palindrome".format(user_input))
    else:
        print("Oops!!! {} is not a palindrome".format(user_input))

print("Palindrome checker!!!\n")
get_input()
