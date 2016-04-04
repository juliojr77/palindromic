import random
import os
import sys




#
# def generate_words(val_1,val_2):
#     words = []
#     with open ('words.txt', 'r') as sample:
#         for word_line in sample:
#             if val_2 == 0:
#                 if len(word_line) >= val_1:
#
#                     words += word_line.lower().split()
#             elif len(word_line) == val_1 or len(word_line) == val_2:
#                 words += word_line.lower().split()
#     return words
#_-------------------------------------------

def make_raw_list():
    raw_words = []
    with open ('words.txt', 'r') as sample:
        for word_line in sample:

            raw_words += word_line.lower().split()

    return raw_words


#-------------------------------------------

def easy_words(raw_list):
        words_easy = []

        for word in raw_list:
            if len(word) in range(4,7):
                #print(len(word))
                #input()
                words_easy += word.lower().split()
        return words_easy



#----------------------------------------------

def medium_words(raw_list):
        words_med = []

        for word in raw_list:
            if len(word) in range(6,9):
                #print(len(word))
                #input()
                words_med += word.lower().split()
        return words_med

#----------------------------------------------

def hard_words(raw_list):
        words_hard = []

        for word in raw_list:
            if len(word) >= 8:
                #print(len(word))
                #input()
                words_hard += word.lower().split()
        return words_hard



#----------------------------------------------

def random_word(list_of_words):

    secret_word = random.choice(list_of_words)
    return secret_word




#----------------------------------------------
def draw(bad_guesses, good_guesses, secret_word):
    os.system('clear')
    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')
    for letter in bad_guesses:
        print(letter, end = "")
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end = "")
        else:
            print('_', end = '')

    print('')


#----------------------------------------------
def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1:
            print('You can only guess a single letter')

        elif guess in bad_guesses or guess in good_guesses:
            print('You already guessed that letter..!!')

        elif not guess.isalpha():
            print('You can only guess letters')

        else:
            return guess


#---------------------------------------------


def play_game(done,secret_word):
    os.system('clear')
    bad_guesses = []
    good_guesses = []

    while True:

        draw(bad_guesses,good_guesses,secret_word)

        guess = get_guess(bad_guesses,good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False

            if found:
                print("You win..!!")
                print("The secret word was {}".format(secret_word))
                done = True

        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses,good_guesses,secret_word)
                print('You lost')
                print("The secret_word was: {}".format(secret_word))
                done = True

        if done:
            play_again = input("Play again? Y/N..:").lower()
            if play_again == 'y':
                return 0
            else:
                return 4


#-----------------------------------------------


def choose_game_level(level):

    done = False
    if not level.isdigit() or int(level) > 4:
        input("Invalid input. Press enter to continue!... " )
        return 0


    # easy Level
    elif int(level) == 1:


        easy_secret_word = random_word(easy_words(make_raw_list()))
        return play_game(done, easy_secret_word)


    # medium Level
    elif int(level) == 2:

        medium_secret_word = random_word(medium_words(make_raw_list()))
        return play_game(done, medium_secret_word)


    # Hard level
    elif int(level) == 3:

        hard_secret_word = random_word(hard_words(make_raw_list()))
        return play_game(done, hard_secret_word)


    else:
        return 4
#-----------------------------------------------------------



def main():

    while True:

        os.system('clear')
        print('WELCOME TO THE MISTERY WORD GAME')
        print('\n\n')
        print('Difficulty level:\n')
        print('1.) Easy\n')
        print('2.) Medium\n')
        print('3.) Hard\n')
        print('4.) Quit game\n\n\n')

        diff_level = input("Choose the number of your difficulty level and press enter: ")

        if choose_game_level(diff_level) == 0:
            continue
        else:
            print('\n\n')
            print("Bye... Have a Nice Day!")
            print('\n\n')
            sys.exit()




if __name__ == '__main__':
    main()
