#word lists
animal_list = ["camel", "finch", "horse", "hyena", "mouse", "rhino", "sloth", "tiger", "whale", "zebra"]
food_list = ["bagel", "bread", "grape", "lemon", "mango", "peach", "sugar"]
colour_list = ["amber", "black", "brown", "coral", "hazel", "olive", "white"]

#input prompts
intro_text = "Choose a topic, and guess a 5 letter word related to it!:\n\nAnimals\t\tFood\t\tColours\n\t\n"
topic_a = "\nYour word relates to animals! You have 7 tries.\n"
topic_f = "\nYour word relates to food! You have 7 tries.\n"
topic_c = "\nYour word relates to colours! You have 7 tries.\n"

#error messages
topic_invalid = "\n//Please choose a topic.//\n"
guess_invalid = "\n//Not a valid guess.//\n"
letter_invalid = "\n//Already guessed this letter!//\n"

def error_reloop(output, action):
  output
  action

#format
indent = "\t> "
player_won = "\nYou guessed the word! Congratulations!"