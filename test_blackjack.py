import pytest
from blackjack import Player

# test Player init.
def test_valid_player_init():   # initialize a valid player
    player = Player("0", 5000)
    assert player.get_balance == 5000
    assert len(player.get_hand) == 0

def test_invalid_player_init():    # initialize an invalid player
    with pytest.raises(TypeError):
            player = Player()

def test_default_balance():    # default balance should be 1000
    player = Player ("1")
    assert player.get_balance == 1000
    assert len(player.get_hand) == 0


# test setters
def test_set_valid_balance():    # set a valid balance
    player = Player(0, 3000)
    player.set_balance(7000)
    assert player.get_balance == 7000
 
def test_set_zero_balance():    # 0 should be a valid balance
    player = Player(0, 3000)
    player.set_balance(0)
    assert player.get_balance == 0
    
def test_set_invalid_balance():    # setting an invalid balance should raise a ValueError
    player = Player(0)
    with pytest.raises(ValueError):
        player.set_balance(-1000)


def test_set_hand():
    player = []
    for i in range(4):
        player.append(Player(i))

def test_set_valid_hand():
    player = Player(0)
    assert player.get_hand == []
    player.set_hand([{"rank": "Ace", "suit": "Spades", "deck": 0}, {"rank": "Jack", "suit": "Clubs", "deck": 0}])
    assert player.get_hand == [{"rank": "Ace", "suit": "Spades", "deck": 0}, {"rank": "Jack", "suit": "Clubs", "deck": 0}]
    
def test_set_invalid_hand_no_list():    # the new hand must be a list of cards
    player = Player(0)
    assert player.get_hand == []
    with pytest.raises(ValueError):
       player.set_hand({"rank": "Ace", "suit": "Spades", "deck": 0})
    
def test_set_invalid_hand_missing_keys():    # the new hand list must be a dict of cards with valid keys
    player = Player(0)    
    assert player.get_hand == []
    with pytest.raises(ValueError):
        player.set_hand([{"rank": "King", "suit": "Hearts"}, {"rank": "Jack", "deck": 1}])


# test Player-methods
def test_is_bust_true():    # 25 should be invalid
    player = Player(0)
    player.set_hand([{"rank": "10", "suit": "Spades", "deck": 0}, {"rank": "Jack", "suit": "Clubs", "deck": 0}, {"rank": "5", "suit": "Clubs", "deck": 0}])
    assert player.is_bust() is True

def test_is_bust_false():   # 21 should be valid
    player = Player(0)
    player.set_hand([{"rank": "Ace", "suit": "Spades", "deck": 0}, {"rank": "Jack", "suit": "Clubs", "deck": 0}])
    assert player.is_bust() is False


def test_is_bust_Aces(): # Both aces should be counted as 1 to avoid being over 21 with a 12.
    player = Player(0)
    player.set_hand([{"rank": "Ace", "suit": "Spades", "deck": 0}, {"rank": "Jack", "suit": "Clubs", "deck": 0}, {"rank": "Ace", "suit": "Clubs", "deck": 0}])
    assert player.is_bust() is False
