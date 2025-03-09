import pytest
from blackjack import Player

def test_player_init():
    # initialize a valid player
    player = Player("0", 5000)
    assert player.get_balance == 5000
    assert len(player.get_hand) == 0

    # initialize an invalid player
    with pytest.raises(TypeError):
            player = Player()

    # test default money value
    player = Player ("1")
    assert player.get_balance == 1000
    assert len(player.get_hand) == 0

