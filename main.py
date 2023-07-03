import random
import text
word = ""
guess = ""
board = ["__ ","__ ","__ ","__ ","__ "]
tries_left = 7
guessed_letters = []
word_guessed = False

def start_game():
  global word
  userinput = input(text.intro_text + text.indent)
  if userinput.isalpha() == True:
    if userinput.lower() == "animals" or userinput.lower() == "a":
      word = choose_word(text.animal_list)
      print(text.topic_a)
    elif userinput.lower() == "food" or userinput.lower() == "f":
      word = choose_word(text.food_list)
      print(text.topic_f)
    elif userinput.lower() == "colours" or userinput.lower() == "c":
      word = choose_word(text.colour_list)
      print(text.topic_c)
    else:
      text.error_reloop(print(text.topic_invalid), start_game())
  else:
    text.error_reloop(print(text.topic_invalid), start_game())
    
  return word

def choose_word(list):
  global word
  rand = random.randint(0,len(list)-1)
  word = list[rand]
  return word

def play():
  global word
  global tries_left
  print(*board)

  while tries_left > 0 and word_guessed == False:
    print("\nEnter a letter to guess: \n")
    user_guess = input("\n"+text.indent).lower()
    player_guess(user_guess)
    check_win(board[0]+board[1]+board[2]+board[3]+board[4])
  if tries_left == 0 and word_guessed == False:
    last_guess_check()
  elif word_guessed == True:
    print(text.player_won)

def last_guess_check():
  last_guess = input("\nOut of tries! You have one chance to guess the full word:\n\n"+text.indent)
  if last_guess.isalpha() and len(last_guess) == 5:
    if last_guess.lower() == word:
      print(text.player_won)
    else:
      print("\nOut of tries! The word was " + word + "!")
  else:
    text.error_reloop(print(text.guess_invalid), last_guess_check())

def player_guess(guess):
  global tries_left
  if guess.isalpha() and len(guess) == 1:
    if guess not in guessed_letters:
      if guess in word:
        for letter in word:
          if guess == letter:
            board[word.index(letter)] = guess
            tries_left -= 1
      else:
        print("\n//"+guess+" is not in the word!//")
        tries_left -= 1
    else:
      print(text.letter_invalid)
    guessed_letters.append(guess)
  else:
    print(text.guess_invalid)
  print("\n")
  print(*board)
  if tries_left > 0:
    print("\n\tTries left:",tries_left)

def check_win(list):
  global word
  global word_guessed
  if list == word:
    word_guessed = True
    return word_guessed

start_game()
play()