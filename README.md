### DESCRIPTION ###
This program shows a difficulty level menu to play a mystery word game. Easy chooses a 4 to 6 character long word, Medium chooses a 
6 to 8 character long word and the hard level chooses a 8+ character long word to be guessed by the user.

## Proccess ##
	1.) Main() funtion takes a numeric character and pass it to choose_level_game() funtion
	2.) choose_level_game() pick the computer word through random_word(easy_words(make_raw_list())) funtion
        3.) Once the word is picked the game starts by calling the funtion play_game()
	4.) the Play_game_funtion uses the draw() and guess() funtion to show the user the good and bad gueses.  
	5.) Finally play_game() funtion will show the user if he gussed the word or not.
