import sys
import random

ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


def main(num_decks = None, num_players = None):
    # initialization of the number of decks at the table + shuffling
    if num_decks is None:
        num_decks = int(input("How many decks are in play? "))
        num_cards = num_decks * 52
        discards = []
        shoe = []
        for deck in range(num_decks):
            for suit in suits:
                for rank in ranks:
                    shoe.append({"rank": rank, "suit": suit, "deck": deck})
                    random.shuffle(shoe)
    # initialization of the number of players at the table
    if num_players is None:
        num_players = int(input("How many players are at the table? "))
        players = []
        for i in range(num_players):
            player = Player(id = i)
            players.append(player)

    for player in players:
        print (player)

    
        
    print(shoe)
    print(discards)
    turn = 0
    cut(4)
    print(discards)
    draw()
    draw()
    print (discards)
    print(len(shoe))

    print()
    player = Player("0", 1000)
    player.hit()
    player.hit()
    print(player.get_hand)
    print(player.get_hand_values)
    print(player.get_best_hand_value())

    # while len(shoe) > 20:
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
    def __init__(self, id :int, balance = 1000):
        self._id = id
        self._hand = []
        if balance <= 0:
            raise ValueError(f"Player {self._id} is bankrot.")
        else:
            self._balance = balance

    def __str__(self):
        return f"Player {self._id} has a balance of {self._balance} with the hand: {self._hand}"

    def bet(self, amount :int):
        if amount <= self._balance:
            return amount
        else:
            raise ValueError(f"Player {self._id} has insufficient funds for this bet.")

    # draw another card
    def hit(self):
        self._hand.append(draw())
        #turn += 1

    # pass on drawing (should exempt you from drawing again for the round)
    def stay(self):
        ...
        #turn += 1
    
    # return a list of the cards in the players hand
    @property
    def get_hand(self):
        return self._hand

    # calculate and return the total value of the players hand as a list. 
    # The normal value is at index 0. If there are aces, all unique possible values will be returned as a set.
    @property
    def get_hand_values(self):
        values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}
        hand = self.get_hand
        possible_values = [0]
        for card in hand:
            if card["rank"] == "Ace":
                new_values = []
                for value in possible_values:
                    new_values.append(value + 1)
                    new_values.append(value + 11)
                possible_values = new_values
            else:
                possible_values = [value + values[card["rank"]] for value in possible_values]
        return sorted(set(possible_values))
    
    # return the highest value which isn't over 21. If there is none, the player is most likely bust.
    def get_best_hand_value(self):
        best_value = None
        for value in self.get_hand_values:
            if value <= 21:
                if best_value is None or value > best_value:
                    best_value = value
        return best_value

    # return the number of aces the player has in their hand
    @property
    def num_aces(self):
        num_aces = 0
        for card in self.get_hand():
            if card[rank] == "Ace":
                num_aces += 1
        return num_aces

    # return the amount of chips the player has on the bank
    @property
    def get_balance(self):
        return self._balance


if __name__ == "__main__":
    main()