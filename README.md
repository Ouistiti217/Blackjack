# Blackjack

This repository was created in the scope of being the final project for the CS50p course.
I tried putting my aquired skills to use, to create a game of Blackjack wh

## About:
There are three ways of using this program:
1. This program enables you to play a simple game of Blackjack, when executed without any command-line arguments.
    - Singleplayer against the dealer
    - 6 Decks in the shoe
    - 1000 jetons starting budget
    - Blackjack pays 2:3
    - Dealer must stay on 17

    `python blackjack.py`

2. Multiple command line argumets (use of flags) can be specified, to modify the parameters of the game
    - Specify number of players: Control 1-7 players at the same table
    - Specify the starting budget for all players
    - Specify the number of decks in the shoe
    - Specify the payout ratio of Blackjack
    - Specify the index at which the shoe should be cut after shuffeling (essentially taking this many cards out of the game)

        By entering `python blackjack.py 2 5000 1 "2:3" 12` into the command-line, you would be starting a game with two players, each begining with 5000 jetons. The game would be played with one deck and blackjack pays out 2:3. In this example the deck would also be cut at index 12.

        By entering `python blackjack.py 4 3000 8` into the command-line, you would be starting a game with four players, each starting with 3000 jetons and a shoe containing eight decks. The unspecified settings will revert to their default as mentioned in the first way, without cutting the deck. This is possible for any amount of argumnets between 1 and 5, while maintaining said order.

3. Card counting and perfect strategy
    -  Get the running count of of a specified card counting system
    -  Get the true count in correlation to the cards still in the game
      -  Recommended bet amounts for a statistical maximization of profits


## Ressources / Dependencies
The GUI uses playing card graphics, which were released into the public domain. Project link: https://code.google.com/archive/p/vector-playing-cards/


## Development process
At first I started by writing out the markdown-file to get an overview of what I wanted to do for my final project. I was intrigued by the possibility of not only creating a simple game against the computer, but also making it as close as possible to a real game of Blackjack. Thus, my version of Blackjack should be realistic enough, to be able to actually practice card counting strategies and fully keep track of a customizable digital deck of cards. From here on out the leap to implementing a full on card counting mechanic to play perfect strategy after the *Revere RAPC* to achieve a high betting correlation and playing efficiency. 
In the beginning I implemented a basic game of Blackjack, constantly jumping across all parts of the program. The first version relied on dialogue in the terminal window to set up the game parameters, which eventually changed to a sys prompt using command-line arguments on startup.
Early on I implemented an object-oriented aproach with a player-class, which I eventually split into a Player- and Dealer-class, inheriting from a shared Entity-class. This had the advantage of me being able to already implement a large chunk of the game logic in methods for easier use in the future. 
In parallel to developing this project, I inquired about *tkinter* and the possibileties of creating my own dedicated UI for the game, to make it as aesthetically pleasing as possible. In the same breath I found a set of playing card graphics, from where on I clearly could not go back to my original idea of creating an ASCII-art-display in the terminal window.
Faced with the challange of creating an adaptive layout, which includes haneling images, I also had to trace back to the pillow-library we already started using in the scope of the CS50p-course.