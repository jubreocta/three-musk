# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    if ord(s[0])-ord('A')>4 or int(s[1])>5 or 1>int(s[1]) or 0>ord(s[0])-ord('A') or len(s)>2:
        raise ValueError
    else:    
        return (ord(s[0])-ord('A'),int(s[1])-1)

def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    if type(location)!=tuple or len(location)>2:
        raise ValueError
    if location[0]<0 or location[1]<0 or location[0]>4 or location[0]>4:
        raise ValueError
    else:
        return chr(location[0]+ord('A'))+ str(location[1]+1)

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    al=[]
    for i in range(5):
        for j in range(5):
            al.append((i,j))
    return al

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, column) = location
    if direction=='up':
        row-=1
    if direction=='down':
        row+=1
    if direction=='left':
        column-=1
    if direction=='right':
        column+=1
    return (row,column)

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    if at(location)!='M':
        raise ValueError
    else:
        if is_within_board(location, direction):
            if at(adjacent_location(location, direction))== 'R':
                return True
            else:
                return False
        else:
            return False
def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    if at(location)!='R':
        raise ValueError
    else:
        if is_within_board(location, direction):
            if at(adjacent_location(location, direction))== '-':
                return True
            else:
                return False
        else:
            return False

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    if at(location)=='M' and is_legal_move_by_musketeer(location, direction) is True:
        return True
    elif at(location)=='R' and is_legal_move_by_enemy(location, direction) is True:
        return True
    else:
        return False

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range.
    You can assume that input will always be in correct range."""
    if at(location)=='R':
        if is_legal_move_by_enemy(location, 'up') is True or\
           is_legal_move_by_enemy(location, 'down') is True or\
           is_legal_move_by_enemy(location, 'left') is True or\
           is_legal_move_by_enemy(location, 'right') is True:
            return True
        else:
            return False
    elif at(location)=='M':
        if is_legal_move_by_musketeer(location, 'up') is True or\
           is_legal_move_by_musketeer(location, 'down') is True or\
           is_legal_move_by_musketeer(location, 'left') is True or\
           is_legal_move_by_musketeer(location, 'right') is True:
            return True
        else:
            return False
    else:
        return False
def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    a=[]
    if who=='M':
        for i in all_locations():
            if at(i)=='M':
                a.append(can_move_piece_at(i))
        if True in a:
            return True
        else:
            return False
        a=[]
    if who=='R':
        for i in all_locations():
            if at(i)=='R':
                a.append(can_move_piece_at(i))
        if True in a:
            return True
        else:
            return False
        a=[]
def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    a=[]
    #directions will always be given in the order up, down, left, right
    direction=['up','down','left','right']
    for i in direction:
        if is_legal_move(location,i):
            a.append(i)
    return a

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be a pair of integers."""
    if location[0]< 0 or location[1]<0 or location[0]>4 or location[1]>4:
        return False
    else:
        return True
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    if is_legal_location(adjacent_location(location, direction)) is True:
        return True
    else:
        return False
    
def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    a=[]
    direction=['up','down','left','right']
    if player=='M':
        for i in all_locations():
            if at(i)=='M':
                for j in direction:
                    if is_within_board(i,j) and is_legal_move(i,j):
                        a.append((i,j))
    elif player=='R':
        for i in all_locations():
            if at(i)=='R':
                for j in direction:
                    if is_within_board(i,j) and is_legal_move(i,j):
                        a.append((i,j))
    return a

def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    #need to copy board so changes dont permanently change original board
    import copy
    a=copy.deepcopy(board)
    if at(location)=='M':
        a[location[0]][location[1]]='-'
        a[adjacent_location(location, direction)[0]]\
        [adjacent_location(location, direction)[1]]='M'
    if at(location)=='R':
        a[location[0]][location[1]]='-'
        a[adjacent_location(location, direction)[0]]\
        [adjacent_location(location, direction)[1]]='R'
    set_board(a)
    
def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    #computer awlays plays the first move available
    #which is the piece with the lowest row number,lowest column number
    #followed by up,down, left,right. whichever is available first.
    return all_possible_moves_for(who)[0]

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    a=[]
    for i in all_locations():
        if at(i)=='M':
            a.append(i)
    if a[0][0]==a[1][0]==a[2][0] or a[0][1]==a[1][1]==a[2][1]:
        return True
    else:
        return False

#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    global user
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

#
#
##
###
####
#####
#first question is to know if user wants to load a game or start a new game

def choose_load_or_new():
    a = ''
    while a != 'L' and a!= 'N':
        choice = input("Would you like to load a game (L) or start a new game (N)? ")
        choice = choice.strip()
        if choice != '':
            a = choice[0].upper()
    return a
#next we need to edit the start function to act based on choose_load_or _new
def start():
    """Plays the Three Musketeers Game."""
    load_or_new = choose_load_or_new()
    if load_or_new == 'N':
        users_side = choose_users_side()
        board = create_board()
    else:
        board = load_board()
        users_side = choose_users_side()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")


            break


#now we need to create a way to first save and then load board
#save boards
#we edit get_users_move to take inputs save,new game, load game
def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    print('Enter (S) to save this game, (N) to load a new game or make your move')
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
        else:      
            print("Illegal move--'" + move + "'")
            return get_users_move()
    elif move[0] == 'N':
        sure = input("Are you sure you want to load a new game?You current game will be lost!!!Yes(Y)/No(N)??").upper()
        if sure == 'Y':
            return start()
        else:
            return get_users_move()
    elif move[0] == 'S':
        sure = input("Are you sure you want to save this game and continue? Yes(Y)/No(N)??").upper()
        if sure == 'Y':
            save_board()
            return get_users_move()
        else:
            return get_users_move()
    else:      
        print("Illegal move--'" + move + "'")
        return get_users_move()


#now we need to define save board

#we need to define how to load a game

#edit load board and save board to take more files and be named
def save_board():
    try:
        outfile = open('boards.txt','r+')
        outfile.read()
    except:
        outfile = open('boards.txt','w')
    a= get_board()
    b=''
    for i in a:
        for j in i:
            b+=j
    name=input('Input the name you want to save this game as. ')
    outfile.write(name)
    outfile.write('\n')
    outfile.write(user)
    outfile.write('\n')
    outfile.write(b)
    outfile.write('\n')
    outfile.close()

def load_board():
    try:
        infile = open('boards.txt','r')
        a = infile.readlines()
        infile.close()
        print('Which of your saved games do you want to load??')
        for i in range(0,len(a),3):
            print('%15s' % a[i])
        b=None
        while b not in a:
            choice = input('???')
            if choice != '':
                b = choice + '\n'
        board_index = a.index(b)+2
        board_letters = a[board_index].strip()
        needed_board = []
        for i in range(5):
            c=[board_letters[i] for i in range(5)]
            board_letters=board_letters[5:]
            needed_board.append(c)
        set_board(needed_board)
        print('You saved this game playing as %s' % a[a.index(b)+1])
    except:
        print('There is no saved game!')
        create_board()
start()
