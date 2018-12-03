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

board2 = [ [_, _, _, _, R],
            [_, _, _, R, _],
            [R, _, _, _, _],
            [_, M, _, R, M],
            [M, R, _, R, R] ]


board3 = [ [_, R, R, _, _],
            [R, M, R, _, R],
            [_, _, R, _, R],
            [_, _, _, M, R],
            [M, _, _, R, R] ]

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
    assert at((0,1)) == R
    assert at((0,2)) == R
    assert at((0,3)) == R
    assert at((1,0)) == R
    assert at((1,1)) == R
    assert at((1,2)) == R
    assert at((1,3)) == R
    assert at((1,4)) == R
    assert at((2,0)) == R
    assert at((2,1)) == R
    assert at((2,2)) == M
    assert at((2,3)) == R
    assert at((2,4)) == R
    assert at((3,0)) == R
    assert at((3,1)) == R
    assert at((3,2)) == R
    assert at((3,3)) == R
    assert at((3,4)) == R
    assert at((4,0)) == M
    assert at((4,1)) == R
    assert at((4,2)) == R
    assert at((4,3)) == R
    assert at((4,4)) == R
    assert get_board() == board
def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    assert at((4,0)) == _
    assert at((4,3)) == R
    #eventually add some board2 and at least 3 tests with it
    set_board(board)
    assert at((0,0)) == R
    assert at((2,2)) == M
    assert at((1,3)) == R
    assert at((4,0)) == M
    assert at((4,3)) == R


    
def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board
    set_board(board)
    assert board == get_board()

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
        string_to_location('A7')
        string_to_location('E31')
        string_to_location('XE3')
    assert string_to_location('A1') == (0,0)
    assert string_to_location('A2') == (0,1)
    assert string_to_location('A3') == (0,2)
    assert string_to_location('A4') == (0,3)
    assert string_to_location('A5') == (0,4)
    assert string_to_location('B1') == (1,0)
    assert string_to_location('B2') == (1,1)
    assert string_to_location('B3') == (1,2)
    assert string_to_location('B4') == (1,3)
    assert string_to_location('B5') == (1,4)
    assert string_to_location('C1') == (2,0)
    assert string_to_location('C2') == (2,1)
    assert string_to_location('C3') == (2,2)
    assert string_to_location('C4') == (2,3)
    assert string_to_location('C5') == (2,4)
    assert string_to_location('D1') == (3,0)
    assert string_to_location('D2') == (3,1)
    assert string_to_location('D3') == (3,2)
    assert string_to_location('D4') == (3,3)
    assert string_to_location('D5') == (3,4)
    assert string_to_location('E1') == (4,0)
    assert string_to_location('E2') == (4,1)
    assert string_to_location('E3') == (4,2)
    assert string_to_location('E4') == (4,3)
    assert string_to_location('E5') == (4,4)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string('X3')
        location_to_string([X3])
    assert location_to_string((0,0)) == 'A1'
    assert location_to_string((0,1)) == 'A2'
    assert location_to_string((0,2)) == 'A3'
    assert location_to_string((0,3)) == 'A4'
    assert location_to_string((0,4)) == 'A5'
    assert location_to_string((1,0)) == 'B1'
    assert location_to_string((1,1)) == 'B2'
    assert location_to_string((1,2)) == 'B3'
    assert location_to_string((1,3)) == 'B4'
    assert location_to_string((1,4)) == 'B5'
    assert location_to_string((2,0)) == 'C1'
    assert location_to_string((2,1)) == 'C2'
    assert location_to_string((2,2)) == 'C3'
    assert location_to_string((2,3)) == 'C4'
    assert location_to_string((2,4)) == 'C5'
    assert location_to_string((3,0)) == 'D1'
    assert location_to_string((3,1)) == 'D2'
    assert location_to_string((3,2)) == 'D3'
    assert location_to_string((3,3)) == 'D4'
    assert location_to_string((3,4)) == 'D5'
    assert location_to_string((4,0)) == 'E1'
    assert location_to_string((4,1)) == 'E2'
    assert location_to_string((4,2)) == 'E3'
    assert location_to_string((4,3)) == 'E4'
    assert location_to_string((4,4)) == 'E5'
    
def test_at():
    set_board(board)
    assert at((0,0)) == r
    assert at((1,0)) == r
    assert at((2,2)) == m
    assert at((3,1)) == r
    assert at((4,0)) == m

    set_board(board1)
    assert at((0,0)) == _
    assert at((1,3)) == M
    assert at((2,3)) == R
    assert at((3,1)) == R
    assert at((4,0)) == _

def test_all_locations():
    set_board(board)
    #creating a list of tuples of all locations
    al=[]
    for i in range(5):
        for j in range(5):
            al.append((i,j))
        
    assert all_locations() == al
    set_board(board1)
    #writing out tuples of all locations one by one
    assert all_locations() == [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),
                               (2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4),
                               (4,0),(4,1),(4,2),(4,3),(4,4)]

def test_adjacent_location():
    set_board(board)
    assert adjacent_location((0,0),right)== (0,1)
    assert adjacent_location((0,0),down)== (1,0)
    assert adjacent_location((4,4),left)== (4,3)
    assert adjacent_location((4,4),up)== (3,4)
    assert adjacent_location((2,2),right)== (2,3)
    assert adjacent_location((2,2),down)== (3,2)
    assert adjacent_location((2,2),left)== (2,1)
    assert adjacent_location((2,2),up)== (1,2)
    assert adjacent_location((3,1),right)== (3,2)
    assert adjacent_location((1,0),up)== (0,0)
    
def test_is_legal_move_by_musketeer():
    set_board(board)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0,0), down)
        is_legal_move_by_musketeer((2,3), left)
        is_legal_move_by_musketeer((4,4), up)
        is_legal_move_by_musketeer((0,3), right)
        is_legal_move_by_musketeer((1,1), down)
    assert is_legal_move_by_musketeer((0,4),down)== True
    assert is_legal_move_by_musketeer((0,4),left)== True
    assert is_legal_move_by_musketeer((2,2),down)== True
    assert is_legal_move_by_musketeer((2,2),right)== True
    assert is_legal_move_by_musketeer((4,0),up)== True
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0,0), down)
        is_legal_move_by_musketeer((2,2), left)
        is_legal_move_by_musketeer((4,4), up)
        is_legal_move_by_musketeer((3,3), right)
        is_legal_move_by_musketeer((1,1), down)
    assert is_legal_move_by_musketeer((0,3),down)== False
    assert is_legal_move_by_musketeer((1,3),left)== True
    assert is_legal_move_by_musketeer((1,3),down)== True
    assert is_legal_move_by_musketeer((1,3),right)== False
    assert is_legal_move_by_musketeer((2,2),down)== False
    
def test_is_legal_move_by_enemy():
    set_board(board)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0,4),left)
        is_legal_move_by_enemy((0,4),down)
        is_legal_move_by_enemy((2,2),up)
        is_legal_move_by_enemy((2,2),right)
        is_legal_move_by_enemy((4,0),left)
    assert is_legal_move_by_enemy((0,0),down)== False
    assert is_legal_move_by_enemy((2,3),up)== False
    assert is_legal_move_by_enemy((4,3),right)== False
    assert is_legal_move_by_enemy((4,1),left)== False
    assert is_legal_move_by_enemy((1,1),down)== False
    set_board(board1)
    assert is_legal_move_by_enemy((4,3),up)== True
    assert is_legal_move_by_enemy((3,1),up)== False
    assert is_legal_move_by_enemy((3,1),right)== True
    assert is_legal_move_by_enemy((2,1),left)== True
    assert is_legal_move_by_enemy((1,2),up)== True
    
def test_is_legal_move():
    set_board(board)
    assert is_legal_move((0,1),down) == False
    assert is_legal_move((0,4),left) == True
    assert is_legal_move((2,2),right) == True
    assert is_legal_move((3,1),down) == False
    assert is_legal_move((4,2),up) == False
    set_board(board1)
    assert is_legal_move((1,2),left) == True
    assert is_legal_move((1,3),left) == True
    assert is_legal_move((2,3),up) == False
    assert is_legal_move((3,1),right) == True
    assert is_legal_move((0,1),down) == False
    
def test_can_move_piece_at():
    set_board(board)
    assert can_move_piece_at((0,0)) == False
    assert can_move_piece_at((0,4)) == True
    assert can_move_piece_at((1,3)) == False
    assert can_move_piece_at((2,2)) == True
    assert can_move_piece_at((4,0)) == True
    set_board(board1)
    assert can_move_piece_at((4,3)) == True
    assert can_move_piece_at((2,2)) == True
    assert can_move_piece_at((1,1)) == False
    assert can_move_piece_at((0,3)) == False
    assert can_move_piece_at((1,3)) == True
    
def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board
    set_board(board)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == False
    
def test_possible_moves_from():
    set_board(board)
    assert possible_moves_from((0,0)) == []
    assert possible_moves_from((0,4)) == [down,left]
    assert possible_moves_from((1,2)) == []
    assert possible_moves_from((2,2)) == [up,down,left,right]
    assert possible_moves_from((4,0)) == [up,right]
    set_board(board1)
    assert possible_moves_from((2,2)) == [up,left,right]
    assert possible_moves_from((0,3)) == []
    assert possible_moves_from((1,3)) == [down,left]
    assert possible_moves_from((2,1)) == [up,left]
    assert possible_moves_from((0,0)) == []
    
def test_is_legal_location():
    set_board(board)
    assert is_legal_location((0,0)) == True
    assert is_legal_location((5,0)) == False
    assert is_legal_location((4,3)) == True
    assert is_legal_location((2,7)) == False
    assert is_legal_location((2,4)) == True
    assert is_legal_location((4,4)) == True
    assert is_legal_location((5,5)) == False
    assert is_legal_location((7,0)) == False
    assert is_legal_location((1,2)) == True
    assert is_legal_location((3,3)) == True
    
    
def test_is_within_board():
    set_board(board)
    assert is_within_board((0,0),down) == True
    assert is_within_board((0,0),left) == False
    assert is_within_board((4,2),up) == True
    assert is_within_board((4,2),down) == False
    assert is_within_board((2,2),down) == True
    assert is_within_board((1,4),right) == False
    assert is_within_board((2,1),left) == True
    assert is_within_board((0,3),up) == False
    assert is_within_board((4,3),right) == True
    assert is_within_board((1,0),left) == False
    
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
    set_board(board1)
    make_move((2,2), up)
    assert get_board()[2][2]=='-'
    assert get_board()[1][2]=='M'
    make_move((2,3),right)
    assert get_board()[2][3]=='-'
    assert get_board()[2][4]=='R'
    
def test_choose_computer_move():
    set_board(board)
    assert choose_computer_move(m) == ((0,4),down)
    make_move((0,4),down)
    assert choose_computer_move(r) == ((0,3),right)
    set_board(board1)
    assert choose_computer_move(m) == ((1,3),down)
    make_move((1,3),down)
    assert choose_computer_move(r) == ((1,2),up)

def test_is_enemy_win():
    set_board(board)
    assert is_enemy_win() == False
    set_board(board1)
    assert is_enemy_win() == False
    make_move((2,2),right)
    assert is_enemy_win() == True

