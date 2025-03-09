import pytest
from blackjack import Player

def test_player_init():
    player = Player("0", 1000)
    assert player.get_balance == 1000
    assert len(player.get_hand) == 0


