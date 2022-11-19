# Hangman Game - Testing

[README.md file](/README.md)

[View live project](https://hangman-3a34.onrender.com/)

[View website in GitHub Pages](https://github.com/preetbhullar90/project-3-with-python)

## Table of contents
1. [Testing User Stories](#Testing-User-Stories)
2. [Manual File Test](#Manual-File-Test)
3. [Automated Testing](#Automated-Testing)
     - [Code Validation](#Code-Validation)
     - [Browser Validation](#Browser-Validation)


***
## Testing User Stories
#### New players Goals:
1. As a new player, I want this game to start easily.
* For new players, I have provided the options in a clear and concise manner to ensure new players understand and able to easily start and play this game.

2. As a new player, I want to see the full instructions about how to play and what I need to do to continue.
* For new players, I have provided 2 options at the beginning of the game. If players know how to play the game, then they have the option to continue straight to the game without reading the instructions.
The second option provided is for new players who are not familiar with the game, they can proceed to the instructions page to understand the rules of the game before playing.

3. As a new player, I want to see the correct or incorrect selected letters in the terminal while playing.
* For new players, I have created a function that shows the incorrectly selected answers at the top of the game in the colour red.
* Another function I have added to the game to make it more user-friendly is to see all the previously guessed letters. This ensures that the player has a smooth gaming experience and does not select the same letters as before although if they do this I have added a function where a message appears in red informing them that they have already used this letter before.

4. As a new player, I want this game to be challenging therefore I do not want access to the word list.
* For new players, I added all the words in google spread sheet and linked it with creds.
* I have added this function to make the game more challenging and to prevent the player from cheating by opening the word list page because this is not possible when the words are linked using gspread sheet as I have done in the development of my game.

#### Current players Goals:
1. As a current player, I want random words every time.
* For current players, I ensured that the word changes every time they play the game. A random word is selected from the gspead sheet every time they replay the game. I have added this feature to make the game as interesting as possible by reducing repetition.

2. As a current player, I should have fun with the game by ensuring it runs smoothly with interesting words.
* For current players, I have ensured that the word list is a secret, and that the player gets feedback when they select the correct or incorrect letters. The player will also see a positive message when they select the correct letter. These features ensure engagement throughout the game which provides a positive user experience
* If the player guesses all the letters correctly in turn guessing the word correctly, they will get a congratulations message with their name.


[Go Top](#Table-of-contents)

## Manual File Test


### Staring-Page
![](/assets/test-file/test-image-1.gif)


### Name-Validation
![](/assets/test-file/test-image-2.gif)


### Game-Menu
![](/assets/test-file/test-image-3.gif)


### Game-Instruction
![](/assets/test-file/test-image-4.gif)

[Go Top](#Table-of-contents)


### Not-Guessed-word
![](/assets/test-file/test-image-5.gif)

### Guessed-word
![](/assets/test-file/test-image-6.gif)

### On-Tablet
![](/assets/test-file/test-image-7.gif)

### On-mobile
![](/assets/test-file/test-image-8.gif)

[Go Top](#Table-of-contents)

## Automated Testing

### Code Validation
The [PEP8 Online](http://pep8online.com/) service was used to validate the `Python` code used.

**Results:**

### **Run.py Page**
![](/assets/test-file/run-py-image.PNG)

### **Hangman-Images Page**
![](/assets/test-file/display-hangman-image.PNG)

### **Clear-terminal Page**
![](/assets/test-file/clear-terminal-image.PNG)

### **Ascii-text-image Page**
![](/assets/test-file/ascii-image.PNG)

### Browser Validation
- Chrome - [test image](/assets/test-file/browser-testing/chrome.PNG)
- Edge - [test image](/assets/test-file/browser-testing/edge.PNG)
- Opera - [test image](/assets/test-file/browser-testing/opera.PNG)
- Firefox - [test image](/assets/test-file/browser-testing/firefox.PNG)

[Go Top](#Table-of-contents)