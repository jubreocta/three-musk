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

m = 'M'
r = 'R'
board = [ [r, r, r, r, m],
          [r, r, r, r, r],
          [r, r, m, r, r],
          [r, r, r, r, r],
          [m, r, r, r, r] ]



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
    set_board(board)
    assert at((0,0)) == r

def test_all_locations():
    set_board(board)
    #creating a list of tuples of all locations
    al=[]
    for i in range(5):
        for j in range(5):
            al.append((i,j))
        
    assert all_locations() == al

def test_adjacent_location():
    set_board(board)
    assert adjacent_location((0,0),right)== (0,1)
    
    
def test_is_legal_move_by_musketeer():
    set_board(board)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0,0), down)
    assert is_legal_move_by_musketeer((0,4),down)== True
    
def test_is_legal_move_by_enemy():
    set_board(board)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0,4),left)
    assert is_legal_move_by_enemy((0,0),down)== False
    set_board(board1)
    assert is_legal_move_by_enemy((4,3),up)== True
    
def test_is_legal_move():
    set_board(board)
    assert is_legal_move((0,1),down) == False
    set_board(board1)
    assert is_legal_move((1,2),left) == True

def test_can_move_piece_at():
    set_board(board)
    assert can_move_piece_at((0,0)) == False
    set_board(board1)
    assert can_move_piece_at((4,3)) == True
def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    set_board(board)
    assert possible_moves_from((0,0)) == []
    set_board(board1)
    assert possible_moves_from((2,2)) == [up,left,right]
def test_is_legal_location():
    set_board(board)
    assert is_legal_location((0,0)) == True
    assert is_legal_location((5,0)) == False
    assert is_legal_location((4,3)) == True
    assert is_legal_location((2,7)) == False
def test_is_within_board():
    set_board(board)
    assert is_within_board((0,0),down) == True
    assert is_within_board((0,0),left) == False
    assert is_within_board((4,2),up) == True
    assert is_within_board((4,2),down) == False
def test_all_possible_moves_for():
    set_board(board)
    assert all_possible_moves_for(m) == [((0,4),down),((0,4),left),
                                         ((2,2),up),((2,2),down),((2,2),left),((2,2),right),
                                         ((4,0),up),((4,0),right)]
    assert all_possible_moves_for(r) == []
    set_board(board1)
    assert all_possible_moves_for(M) == [((1,3),down),((1,3),left),
                                         ((2,2),up),((2,2),left),
                                         ((2,2),right)]
    assert all_possible_moves_for(R) == [((1,2),up),((1,2),left),
                                         ((2,1),up),((2,1),left),
                                         ((2,3),down),((2,3),right),
                                         ((3,1),down),((3,1),left),
                                         ((3,1),right),((4,3),up),
                                         ((4,3),left),((4,3),right)]
def test_make_move():
    set_board(board)
    make_move((0,4), down)
    assert get_board()[0][4]=='-'
    assert get_board()[1][4]=='M'
    make_move((0,3),right)
    assert get_board()[0][3]=='-'
    assert get_board()[0][4]=='R'
    
def test_choose_computer_move():
    set_board(board)
    assert choose_computer_move(m) == ((0,4),down)

def test_is_enemy_win():
    set_board(board)
    assert is_enemy_win() == False
    set_board(board1)
    assert is_enemy_win() == False
    make_move((2,2),right)
    assert is_enemy_win() == True

