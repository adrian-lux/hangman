import random
#Step 1 

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

def split(word): 
    return [char for char in word]  

print('''_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''
                   )

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = random.choice(word_list)

#print(random_word)
wordToGuess = split(random_word)

answerArray = []
for char in wordToGuess:
  answerArray.append("_")

def drawAnswer(answerArray):
  answer = ""
  for char in answerArray:
    answer += char + " "
  print(answer)  

gameover = False
counter = 0;
print(HANGMANPICS[counter] + "\n")
while(not(gameover)):
  
  

  drawAnswer(answerArray)
  #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  guess = input("Guess a letter: ").lower()

  if(guess in wordToGuess):
    for n in range(0, len(random_word)):
      if(guess == wordToGuess[n]):
          answerArray[n] = guess
  else:
    counter += 1

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

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
