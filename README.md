# Hangman Game

![Hangman Game Images](assets/test-file/hangman-responsive.PNG)

[View the live project here](https://hangman-games.herokuapp.com/)

## Contents
1. [Introduction](#Introduction)

2. [User Experience](#User-Experience)

3. [Target](#Target)

4. [Design](#Design)

5. [Features](#Features)

6. [Bugs](#Bugs)

7. [Other Features](#Other-Features)

8. [Features Left to Implement](#Feature-Left-to-Implement)

9. [Technologies Used](#Technologies-Used)

10. [Frameworks Libraries and Programs Used](#Frameworks-Libraries-and-Programs-Used)

11. [Testing](#Testing)

    - [Testings.md](assets/test-file/testings.md)

12. [Deployment](#Deployment)

13. [Make a clone](#Make-a-clone)

14. [Credit](#Credit)

15. [Acknowledgements](#Acknowledgements)
***

## Introduction

This is my 3rd project at code institute. I developed hangman the word game, which runs in the python terminal and is deployed on Heroku, usually, this game is a 2-player game however, the version I have created is played between the user and computer. In this game, users guess the words by choosing letters. The user has 6 chances for selecting the wrong letter before the game is over. In the starting user sees a hangman image and 1 row of dashes. If the user guesses the correct letter of the word, then that letter will appear in the row of dashes, otherwise, users will lose 1 of their 6 chances and they will get the next hangman image. If users guess incorrectly 6 times, then they will lose all their chances and the game will be over. Users can play this game an unlimited amount of times.

[Go Top](#Hangman-Game)

## User Experience

### Ideal User Demographic
* New users.
* Current users.

### User Stories

#### New users :
* As a new player, I want this game to start easily.
* As a new player, I want to see the full instructions about how to play and what I need to do to continue.
* As a new player, I want to see the correct or incorrect selected letters in the terminal while playing.
* As a new player, I want this game to be challenging therefore I do not want access to the word list.

#### Current users :
* As a current player, I want random words every time.
* As a current player, I should have fun with the game by ensuring it runs smoothly with interesting words.

[Go Top](#Hangman-Game)

## Target
* In this game, I have added a background image of gallows as this directly relates to hangman.This sets the seen for the game.
* At the starting of the game when the user enters their name if it’s a name made up of letters then the user will see a big title saying “Hangman”. I did this so the user can easily understand that they have entered the game correctly.
* In the game, I have made the user chances visible. This has been done to make it easy for the user to know how they are progressing in the game and so they can see how many tries they have used and how they have left so they can play carefully.

[Go Top](#Hangman-Game)

## Design

 ### Colour Schema
* I used four colours in this game. The colour blue was used for the big Hangman title, Hangman images, and for tee instructions, Yellow was used for all the inputs, red was used for input of an invalid name, incorrect guess, and if the word/letter is not in the list and green was used if the user guesses the correct word/letter as well as If they win the game.
* Colorama was used to import the colours into the python terminal.


#### Typography
* I used a font from [Colorama](https://pypi.org/project/colorama/), I imported colorama into the python terminal.
* I used the font Bright for all the text.



