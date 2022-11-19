# Hangman Game

![Hangman Game Images](assets/test-file/hangman-responsive.PNG)

[View the live project here](https://hangman-3a34.onrender.com/)

## Contents
1. [Introduction](#Introduction)

2. [User Experience](#User-Experience)

3. [Target](#Target)

4. [Design](#Design)

5. [Features](#Features)

6.  [Flowchart](#Flowchart)

7. [Bugs](#Bugs)

8. [Other Features](#Other-Features)

9. [Features Left to Implement](#Feature-Left-to-Implement)

10. [Technologies Used](#Technologies-Used)

11. [Frameworks Libraries and Programs Used](#Frameworks-Libraries-and-Programs-Used)

12. [Testing](#Testing)

    - [Testings.md](assets/test-file/testings.md)

13. [Deployment](#Deployment)

14. [Make a clone](#Make-a-clone)

15. [Credit](#Credit)

16. [Acknowledgements](#Acknowledgements)
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

#### Skeleton
* I used [Figma](https://www.figma.com/file/7ut2bGOE3cAV0KdPhhgvKx/hangman?node-id=0%3A1) Wireframe to attach the following pages:

#### Desktop Tablet Mobile Page
![](assets/readme-files/hangman-wireframe.PNG)

[Go Top](#Hangman-Game)

## Design

 ### Colour Schema
* I used four colours in this game. The colour blue was used for the big Hangman title, Hangman images, and for tee instructions, Yellow was used for all the inputs, red was used for input of an invalid name, incorrect guess, and if the word/letter is not in the list and green was used if the user guesses the correct word/letter as well as If they win the game.
* Colorama was used to import the colours into the python terminal.


#### Typography
* I used a font from [Colorama](https://pypi.org/project/colorama/), I imported colorama into the python terminal.
* I used the font Bright for all the text.

#### Imagery
* I used one background image on the page. This image is of a hangman gallows.
* I used this image to easily inform users that this website is about hangman. This image does not distract the user in game because I overlayed light colour on it.

[Go Top](#Hangman-Game)

## Features

1. Starting page.
2. Guess the word page.
3. End game.
4. Play again.

#### Starting page :
* On the starting page, users will get an input for entering their name, if the user enters fewer than 2 letters or digits, they will get an error message. If the user enters a valid name, then they will see menu below the hangman title text. In this menu users will get 3 options either to see the instructions, quit or to start playing the game. If the user selects the instructions option, they will see instructions about how to play this game and at the bottom of the instructions text, they will see 2 more options. The 2 options the user can choose from are “Are you ready to play?” if the user selects Y they will enter in the main game where they guess the word but if they select N then they will go in the main menu again.
  ***All the images are found*** [here](assets/game-screenshot/screenshot.md)

#### Guess the word page :
* On the guess the word page, users will get an image of a hangman with a row of dashes, with 6 lives. On this page users have to guess letters of a word which is in the games word list, if the users guess is incorrect, they will see the next part of the hangman image and the user will lose 1 life, but if the user guesses the correct letter, then that letter is added in the row of dashes and hangman image and lives will stay same. When the user enters the correct letter, they will also get a message to say you are doing well. If users select a letter they have used before they will receive a message saying “you have already tried this word and if users tried a number or other special character, then they will see the message that this letter is not in the word list. But the hangman image and lives will stay the same.

  ***All the images are found*** [here](assets/game-screenshot/screenshot.md)

#### End game :
* At the end of the game, if the user guesses all the letters correctly, then the user will get a message saying “congratulations” or if the user guesses the letters incorrectly, and all their lives are lost then the users will get a full hangman image with the message “sorry your lives have run out” with the correct word which they were trying to guess at the end of the game.

  ***All the images are found*** [here](assets/game-screenshot/screenshot.md)

#### Play again :
* Users will get the play again option whether they win or lose. If they select Y they the game will restart with a new word. If they select N then they will get a message say "thanks for playing, see you again.

  ***All the images are found*** [here](assets/game-screenshot/screenshot.md)

## Flowchart
This game is following this flow diagram:
![](assets/readme-files/diagram.png)

## Bugs
* The first bug I was having issues with was getting a random word every time. The reason I had this bug was because my code was not using loop to cycle through the word list cells in google spread sheet.I solved this problem with the help of stack overflow.




## Issue Left
* The game is working smoothly. I didn’t leave any bugs in the game but there is 1 error. The error is (Global variable ‘Name’ undefined at the module level).

* I have included screenshots of the error below:
#### Error
![](assets/readme-files/hangman-error.PNG)

[Go Top](#Hangman-Game)

## Other Features
* I used google spread sheet for the word list, because if you import your word list file to the terminal, then the user can see the word list. I developed the game in this way to make the game interesting and challenging.
* I imported OS into the python terminal to clear the terminal of the previous text according to the next option.
* I imported Time into the terminal to add a delay during the game in between the user selecting an option and the next option being displayed. For example, I added time for the phrases (wait…) and (game loading…) as it gives a nice effect in a terminal game.
* The entered username is saved in the terminal, because when the user replays the game after either winning or losing in the same session his name will not need to be re-entered unless they exit the game.

### Feature Left to Implement
* The username is saved in the terminal where if the user exits the game and re-enters their name will already be there.

## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JS](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks Libraries and Programs Used

* [Os](https://docs.python.org/3/library/os.html "Link to os homepage")
* Os library was used to clear the previous print statement in the terminal.

* [Colorama](https://pypi.org/project/colorama/ "Link to colorama homepage")
* Colorama library was used to change the colours of texts.

* [Time](https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/ "Link to time homepage")
* Time library was used to add delays in the functions.

* [Random](https://www.programiz.com/python-programming/modules/random "Link to random homepage")
* Random library was used to get random words from word list.

* [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
* I used Font awesome to get the play icon for the terminal button. I needed for my website.

* [Git](https://git-scm.com/ "Link to Git homepage")
* Gitpod was used for writing the code in the terminal; it was also used to commit and push the code in GitHub.

* [GitHub](https://github.com/ "Link to GitHub")
* GitHub was used to store the data which was pushed by Gitpod.

* [Figma](https://www.figma.com/ "Link to Figma homepage")
* Figma was used to create the wireframe of the project before starting code on the terminal.

* [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
* Am I Responsive? was used to see if the site is responsive on different types of devices.

[Go Top](#Hangman-Game)

## Testing
All the testing information is found [here](assets/test-file/testings.md)

## Deployment

### Heroku Pages
This site was deploy via Heroku.

This project was developed using a template provide by code institute however the template was upgraded to improve its functionality, which you can see in the commit.

To deploy this project on Heroku I used followed these steps:

1. [Login](https://dashboard.heroku.com/apps) into Heroku.

2. In the main Heroku dashboard select ‘New’in the top right corner.

3. In the drop down, menu select ‘Create New App’.

4. Give a name related your project. I gave hangman-games to my project.

5. When you see green text with your project name then press ‘create app’button.

6. From the dashboard select ‘setting’option.

7. After select setting option scroll down in the config setting. Select the config vars section This will display the current config vars for the app, there should be nothing already there.

8. After config var select Buildpacks option which is located under the config vars option.

9. In the buildpacks select python pack first save it then repeat select nodejs pack and save it.

10. After this scroll up and select ‘Deploy’ option.

11. In the ‘deploy’ option select ‘GitHub’ option to select your project which one you want to deploy on Heroku, choose your project and connect to the Heroku.

12. After connecting your project to Heroku scroll down on Automatic Deploys button.

13. This will ensure whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app. If you select this manually you can manually deploy options further down. For this project, I did Automatic Deployment to enable me to check changes I made to the app as I developed it.

14. Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.


### Make a Clone

1. [Login](https://github.com/)

2.	Click on Your Repository option and select your project

3.	Click on the code dropdown menu.

4.	To clone the repository using HTTPS, click "Clone with HTTPS", and copy the link.

5.	In your local IDE open the Git Bash terminal.

6.	Change the current working directory to the location where you want the cloned directory to be made.

7.	Type git clone, and then paste the URL you copied in Step 3.

           git clone https://github.com/USERNAME/REPOSITORY

8.	Press Enter. Your local clone will be created.

### Forking a Repository
1.	[Login](https://github.com/) into GitHub.

2.	On the top right, click the fork button.

3.	You will get a copy of the repository in your GitHub account.

## Credit

### Media
* It was very hard to find a background image for the hangman game. I searched on many websites but found it difficult to find an appropriate HD. The image that I selected was a downloaded background image from [pixabay](https://pixabay.com/illustrations/halloween-creepy-spooky-gallows-6749878/) and I converted it to an svg file.
### Code
To get a better understanding of the code and different features to add to the game I used the following sites to improve my knowledge:
* [W3school](https://www.w3schools.com/)
* [Stack Overflow](https://stackoverflow.com/)
* [Google](https://www.google.co.uk/)

* This [Youtube tutorial](https://www.youtube.com/watch?v=m4nEnsavl6w) helped me achieve the results I needed for my project.

## Acknowledgements
* I would especially like to thank my wife, who helped me by giving me some ideas regarding my website. She motivated me to finish this project to the best of my ability.
* Secondly I would like to thank my mentor Seun, she helped during the whole process of the project.
* Lastly I would like to acknowledge the W3School website as I gained many ideas from there.

[Go Top](#Hangman-Game)


