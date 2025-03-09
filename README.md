# Blackjack

This project was created in the frame of being the final project for the CS50p course.

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

        By entering `python blackjack.py 2 5000 1 "2:3" 12` into the command-line, you would be starting a game with two players, each starting with 5000 jetons. The game would be played with one deck and blackjack pays out 2:3. In this example the deck would also be cut at index 12.

        By entering `python blackjack.py 4 3000 8` into the command-line, you would be starting a game with four players, each starting with 3000 jetons and a shoe containing eight decks. The unspecified settings will revert to their default as mentioned in the first way, without cutting the deck. This is possible for any amount of argumnets between 1 and 5, while maintaining said order.

3. Card counting and perfect strategy
    -  Get the running count of of a specified card counting system
    -  Get the true count in correlation to the cards still in the game
      -  Recommended bet amounts for a statistical maximization of profits
