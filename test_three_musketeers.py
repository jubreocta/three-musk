import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string('X3')
    assert location_to_string((0,0)) == 'A1'
    
def test_at():
    set_board(new_board)
    assert at((0,0)) == r

def test_all_locations():
    set_board(new_board)
    #creating a list of tuples of all locations
    al=[]
    for i in range(5):
        for j in range(5):
            al.append((i,j))
        
    assert all_locations() == al

def test_adjacent_location():
    set_board(new_board)
    assert adjacent_location((0,0),right)== (0,1)
    
    
def test_is_legal_move_by_musketeer():
    set_board(new_board)
    with pytest.raises(ValueError):
        at((0,0))
    assert is_legal_move_by_musketeer((0,4),down)== True
    
def test_is_legal_move_by_enemy():
    set_board(new_board)
    with pytest.raises(ValueError):
        at((0,4))
    assert is_legal_move_by_enemy((0,0),down)== True
    
def test_is_legal_move():
    set_board(new_board)
    assert is_legal_move((0,1),down) == True

def test_can_move_piece_at():
    set_board(new_board)
    assert can_move_piece_at((0,0)) == True

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    # Replace with tests

def test_is_legal_location():
    # Replace with tests

def test_is_within_board():
    # Replace with tests

def test_all_possible_moves_for():
    # Replace with tests
    
def test_make_move():
    # Replace with tests
    
def test_choose_computer_move():
    # Replace with tests; should work for both 'M' and 'R'

def test_is_enemy_win():
    # Replace with tests


