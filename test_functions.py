"""Test for my functions.

"""

from my_module.projmodule import character_create_race, phoenix_route_warrior_1
##

def test_character_create_race():

    assert callable(character_create_race)
    assert character_create_race() == 'phoenix'


def test_phoenix_route_warrior_1():

	assert callable(phoenix_route_warrior_1)




                 
    
