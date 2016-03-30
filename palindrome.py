import re
import string

user_string = ""


def scrub_string(string_to_scrb):
    pattern = "[^A-Za-z]"
    return re.sub(pattern, "", string_to_scrb.lower())

def reverse_str(string_to_rev):
    if len(string_to_rev) == 0:
         return ''
    return reverse_str(string_to_rev[1:]) + string_to_rev[0]



def is_palindrome(string):
    # string = 'To Ot!!!'
    string = scrub_string(string)
    # string = 'toot'
    string_rev = reverse_str(string)
    # string_rev = 'toot'

    return string == string_rev


def main():
    user_string = input('Enter your palindrome phrase: ')

    if is_palindrome(user_string):
        print('It is a palindrome...!')

    else:
        print('It is not palindrome...!')


if __name__ == "__main__":
    main()
