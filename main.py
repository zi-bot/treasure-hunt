from random import randint

board = [
    ['#','#','#','#','#','#','#','#'],
    ['#','.','.','.','.','.','.','#'],
    ['#','.','#','#','#','.','.','#'],
    ['#','.','.','.','#','.','#','#'],
    ['#','X','#','.','.','.','.','#'],
    ['#','#','#','#','#','#','#','#'],

]
def print_board(board):
    for row in board:
        print( " ".join(row))
print('\nWelcome to the treasure hunt!')
print('''
You can move in the following directions:
N - north (up)
S - south (down)
E - east (right)
W - west (left)


# - wall
. - clear path
X - player
''')
print_board(board)

def get_treasure_location(board):
    rand =  [randint(0,len(board)-1),randint(0,len(board[0])-1)]
    if board[rand[0]][rand[1]] != '.':
        return get_treasure_location(board)
    return rand

def get_player_location(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X':
                return [i,j]

def get_clear_path_coordinates(board):
    clear_path = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                clear_path.append([i,j])
    return clear_path

def show_probable_treasure_location(board, trtreasure_location):
    print('\nMaybe you can find the treasure in this ($) location:')
    probable = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.' and i >= trtreasure_location[0] and j <= trtreasure_location[1] and probable < 3:
                print('$', end=' ')
                probable += 1
            else:
                print(board[i][j], end=' ')
        print()

def set_new_board(player_location, player_location_old):
    if board[player_location[0]][player_location[1]] == '#':
        return False

    board[player_location[0]][player_location[1]] = 'X'
    board[player_location_old[0]][player_location_old[1]] = '.'
    return board

def init_game():
    global player_location
    global treasure_location
    player_location = get_player_location(board)
    treasure_location = get_treasure_location(board)
    show_probable_treasure_location(board,treasure_location)
    active = True
    while active:
        print("\nEnter your move (N,S,E,W) or Q to quit")
        move = str(input())
        move = move.upper()
        active = move_player(move)

def move_player(move):
    if move == 'Q':
        print("\nQuitting game")
        return False
    if move not in ('N','S','E','W'):
        print("\nInvalid move")
        return True
    if move == 'N':
        player_location_old = player_location.copy()
        player_location[0] -= 1
        new_board = set_new_board(player_location, player_location_old)
        if not new_board:
            print("\nYou can't move there")
            player_location[0] += 1
    elif move == 'E':
        player_location_old = player_location.copy()
        player_location[1] += 1
        new_board = set_new_board(player_location, player_location_old)
        if not new_board:
            print("\nYou can't move there")
            player_location[1] -= 1
    elif move == 'S':
        player_location_old = player_location.copy()
        player_location[0] += 1
        new_board = set_new_board(player_location, player_location_old)
        if not new_board:
            print("\nYou can't move there")
            player_location[0] -= 1
    elif move == 'W':
        player_location_old = player_location.copy()
        player_location[1] -= 1
        new_board = set_new_board(player_location, player_location_old)
        if not new_board:
            print("\nYou can't move there")
            player_location[1] += 1
    
    print_board(board)
    if player_location == treasure_location:
        print('\nYou found the treasure!')
        return False 
    return True

init_game()
print("\nThanks for playing!")
