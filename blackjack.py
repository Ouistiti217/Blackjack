import sys
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
suits = ["hearts", "diamonds", "clubs", "spades"]

discards = []
shoe = []
players = []
dealer_hand = []


def main(num_decks = None, num_players = None):
    # setting game parameters through cmd-line arguments
    if len(sys.argv) == 1:  # default settings
        num_jetons = 1000
        num_players = 1
        num_decks = 6
        blackjack_payout = "2:3"
        cut_index = 0
    elif len(sys.argv) > 6:
        sys.exit("Too many command-line arguments")
    else:
        try:
            num_players = int(sys.argv[1])
            try:
                num_jetons = int(sys.argv[2])
            except IndexError:
                num_jetons = 1000
            try:
                num_decks = int(sys.argv[3])
            except IndexError:
                num_decks = 6
            try:
                blackjack_payout = sys.argv[4]
            except IndexError:
                blackjack_payout = "2:3"
            try:
                cut_index = int(sys.argv[5])
            except IndexError:
                cut_index = 0
        except ValueError:
            sys.exit("Command-line arguments need to be enered in this order: int(num_players) int(num_jetons) int(num_decks) str(blackjack_payout e.g. \"2:3\") int(cut_index)")
    
    if int(num_players) < 1:
        sys.exit("Too few players for a nice game of Blackjack")
    elif int(num_players) > 7:
        sys.exit("The table does not accommodate more than seven players")

    # initialization of the number of decks at the table + shuffling
    for deck in range(num_decks):
        for suit in suits:
            for rank in ranks:
                shoe.append({"rank": rank, "suit": suit, "deck": deck})
                random.shuffle(shoe)
    # initialization of the number of players at the table
    for i in range(num_players):
        player = Player(id = i)
        players.append(player)
    # initialize the dealer
    dealer = Dealer()
    
    num_cards = int(num_decks) * 52


    print("\n---------------Game Details---------------")
    if num_players == 1:
        print (f"Player starts with {num_jetons} jetons")
    else:
        print (f"{num_players} players at the table\nEvery player starts with {num_jetons} jetons")
    print(f"{num_decks} decks in the shoe ({num_cards} cards) \nBlackjack pays {blackjack_payout} \nDealer must stay on 17")
    if (cut_index != 0):
        print(f"The shoe will be cut at index {cut_index} after shuffling")
    print("------------------------------------------")


    # Create a window wiht tkinter
    root = create_window()

    # Change the background colour to a random value
    def change_bg():
        root.configure(bg = str("#{:06x}".format(random.randint(0, 0xFFFFFF))))

    label = ttk.Label(root, text="Moinsen", font=("Arial", 16, "bold"))
    label.pack(pady=100)

    image = Image.open(f"PNG-cards-1.3\\ace_of_clubs.png")
    resized_img = image.resize((250, 381))
    tk_image = ImageTk.PhotoImage(resized_img)
    image_label = tk.Label(root, image = tk_image)
    image_label.place(x=1000, y=50)



    button = tk.Button(
        root, 
        text = "Drück mich",
        bg = "darkred",
        fg = "blue",
        relief = "raised",
        command = change_bg
    )
    button.pack()

    root.mainloop()







    # Gameloop
    #while (True):
    #    for i in range(num_players):
    #        if (players[i].is_bust() == True):
    #            print (f"Hui{i}")
    #        else: 
    #            print (f"Sad{i}")





    # for player in players:
        # print (player)
    # 
    # print (shoe)
    # dealer = Dealer()
    # print (dealer)
    # dealer.deal()
    # for player in players:
        # print (player)
    # print (dealer)
           
    
    # print (discards)
    # print(len(shoe))
    # players[3].hit()
    
    # # while len(shoe) > 20:
    # #     print(len(shoe), " Cards in play")
    # #     print(draw())




# cutting the shoe at a specified index, essentially discarding this amount of cards
def cut(index):
    global shoe
    global discards
    for card in shoe[:index]:
        discards.append(card)
    shoe = shoe[index:]

# return a random card from the shoe
def draw():
    choice = random.choice(shoe)
    shoe.remove(choice)
    discards.append(choice)
    return choice


class Entity:
    def __init__(self):
        pass

    # return a list of the cards in hand
    @property
    def get_hand(self):
        return self._hand
    
    def set_hand(self, new_hand):
        if not isinstance(new_hand, list):
            raise ValueError("The new hand must be a list of cards.")
        for card in new_hand:
            if not isinstance(card, dict) or not {"rank", "suit", "deck"}.issubset(card.keys()):
                raise ValueError ("Each card in the new hand must be a dict with 'rank', 'suit', 'deck'.")
        self._hand = new_hand


    # calculate and return the total value of the hand as a list. 
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
    
    # return the highest value which isn't over 21. return None if no valid value exists.
    def get_best_hand_value(self):
        best_value = None
        for value in self.get_hand_values:
            if value <= 21:
                if best_value is None or value > best_value:
                    best_value = value
        return best_value
    
    # return true if the hand value exceeds 21 and false if the entity is not bust.
    def is_bust(self):
        best_hand_value = self.get_best_hand_value()
        if best_hand_value is None or best_hand_value > 21:
            return True
        else:
            return False


class Player(Entity):
    def __init__(self, id :int, balance = 1000):
        self._id = id
        self._hand = []
        if balance <= 0:
            raise ValueError(f"Player {self._id} is bankrot.")
        else:
            self._balance = balance

    def __str__(self):
        return f"Player {self._id} has a balance of {self._balance} with the hand: {self._hand} for a total of {self.get_best_hand_value()} is_bust = {self.is_bust()}"

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
        

    # return the amount of chips the player has on the bank
    @property
    def get_balance(self):
        return self._balance
    
    def set_balance(self, value):
        if value < 0:
            raise ValueError(f"Balance of player {self._id} must not be negative.")
        else:
            self._balance = value


class Dealer(Entity):
    def __init__(self):
        self._hand = []

    def __str__(self):
        return f"The dealer has: {self._hand} for a total of {self.get_best_hand_value()}"
    
    # Deal out two cards for every player and the dealer
    def deal(self):
        for i in range(2):
            for player in players:
                player._hand.append(draw())
            self._hand.append(draw())


# tkinter methods
def create_window():
    root = tk.Tk()
    root.title("Blackjack")
    root.geometry("1080x720")
    root.configure(bg ="darkgreen")
    return root




if __name__ == "__main__":
    main()