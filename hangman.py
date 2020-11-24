import random

# DEFINITIONS
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = ["aardvark", "baboon", "camel","mouse","dog","cat"]

# functions
def split(word): 
    return [char for char in word]  
  
def drawAnswer(answerArray):
  answer = ""
  for char in answerArray:
    answer += char + " "
  print(answer)    

  
#START GAME  
print('''_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''
                   )

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = random.choice(word_list)
wordToGuess = split(random_word)

answerArray = []
for char in wordToGuess:
  answerArray.append("_")


gameover = False
counter = 0;
print(HANGMANPICS[counter] + "\n")

while(not(gameover)):

  drawAnswer(answerArray)
  
  # get users guess
  guess = input("Guess a letter: ").lower()
  
  # check whether guess is in word or not
  if(guess in wordToGuess):
    for n in range(0, len(random_word)):
      if(guess == wordToGuess[n]):
          answerArray[n] = guess
  else:
    counter += 1

  # check for end conditions  
  if counter >= 6:
      gameover = True  
  elif not("_" in  answerArray):
      gameover = True 

  #draw hangman
  print(HANGMANPICS[counter] + "\n")

if(not("_" in  answerArray)):
  print("you win")
else:
  print("you loose")      

