import sys
import random

ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

num_decks = int(input("How many decks are in play? "))
num_cards = num_decks * 52
num_players = int(input("How many players are at the table? "))

# Create the shoe (all cards still in the game) and shuffle it
discards = []
shoe = []
for deck in range(num_decks):
    for suit in suits:
        for rank in ranks:
            shoe.append({"rank": rank, "suit": suit, "deck": deck})
random.shuffle(shoe)
    

def main():
    print(shoe)
    print(discards)
    turn = 0
    cut(4)
    print(discards)
    draw()
    draw()
    print (discards)
    print(len(shoe))

    # while len(shoe) > 0:
    #     print(len(shoe), " Cards in play")
    #     print(draw())


# return a random card from the shoe
def draw():
    choice = random.choice(shoe)
    shoe.remove(choice)
    discards.append(choice)
    return choice


# cutting the shoe at a specified index, essentially discarding this amount of cards
def cut(index):
    global shoe
    global discards
    for card in shoe[:index]:
        discards.append(card)
    shoe = shoe[index:]



class Player:
    def __init__(self, id :int, hand :list, balance = 5000):
        self._id = id
        self._hand = hand
        if balance <= 0:
            raise ValueError(f"Player {self._id} is bankrot.")
        else:
            self._balance = balance

    def bet(self, amount :int):
        if amount <= self._balance:
            return amount
        else:
            raise ValueError(f"Player {self._id} has insufficient funds for this bet.")

    def hit(self):
        self._hand.append(draw())
        turn += 1

    def stay(self):
        turn += 1
    
    @property
    def get_hand(self):
        return self._hand
    
    @property
    def get_balance(self):
        return self._balance


if __name__ == "__main__":
    main()
