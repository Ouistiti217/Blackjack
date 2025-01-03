# Blackjack

This project was created in the frame of being the final project for the CS50p course.

## About:
There are three ways of using this program:
1. This program enables you to play a simple game of Blackjack, when executed without any command-line arguments.
    - 6 Decks in the shoe
    - 1000 jetons starting budget
    - Blackjack plays 2:3
    - Dealer must stay on 17

2. Multiple command line argumets (use of flags) can be specified, to modify the parameters of the game
    - Specify number of players: Control 1-7 players at the same table
    - Specify the number of decks in the shoe
    - Specify the index at which the shoe should be cut after shuffeling (essentially taking this many cards out of the game)
    - Specify the starting budget for all players

3. Card counting and perfect strategy
    -  Get the running count of of a specified card counting system
    -  Get the true count in correlation to the cards still in the game
      -  Recommended bet amounts for a statistical maximization of profits
