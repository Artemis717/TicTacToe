#simple game of TicTacToe created for JetBrains project
#EL
#plays are made by entering coordinates on a 3x3 grid


cells = "         "
matrix = [[cells[0],cells[1],cells[2]],
         [cells[3],cells[4],cells[5]],
         [cells[6],cells[7],cells[8]]]

def print_board():
    print(f"---------\n| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |" \
        f"\n| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |" \
        f"\n| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |\n---------")

print_board()

def get_move():
# gets user input and tests to make sure they entered integers and that
# those integers are between 1-3

    tryagain = True
    while tryagain:
        move = input("Enter the coordinates: ")
        move = move.replace(" ","")
        try:
            test = int(move)
            tryagain = False
            trynext = True
        except:
            print("You should enter numbers!")
            trynext = False

        while trynext:
            move = list(move)

            if move[0] not in "123" or move[1] not in "123":
                print("Coordinates should be from 1 to 3!")
                tryagain = True
                break
            else:
                tryagain = False
                break

#converts user coordinates to matrix indeces
    move[0] = (int(move[0])-1)
    move[1] = (3-(int(move[1])))

    return move

def make_move(t,player):
#applies player move to matrix, unless cell is occupied

    while matrix[t[1]][t[0]] not in "_ ":
        print ("This cell is occupied! Choose another one!")
        t = get_move()

    matrix[t[1]][t[0]] = player
    print_board()
    return

def check_win():
# defines winning combinations, columns and diagonals.
# checks areas for winning combinations

    xs = ['X', 'X', 'X']
    os = ['O', 'O', 'O']
    cols = [[matrix[0][0], matrix[1][0], matrix[2][0]],
            [matrix[0][1], matrix[1][1], matrix[2][1]],
            [matrix[0][2], matrix[1][2], matrix[2][2]]]

    diags = [[matrix[0][0], matrix[1][1], matrix[2][2]],
             [matrix[2][0], matrix[1][1], matrix[0][2]]]

    winner = "Draw"
#if no winner is determined, the game is a Draw
    for r in matrix:
        if r == xs:
            winner = "X wins"
        elif r == os:
            winner = "O wins"
    for c in cols:
        if c == xs:
            winner = "X wins"
        elif c == os:
            winner = "O wins"
    for d in diags:
        if d == xs:
            winner = "X wins"
        elif d == os:
            winner = "O wins"

    return winner

player = 1
plays = 0
game_state = "Draw"

while plays < 9 and game_state == "Draw":
    if player == 1:
        turn = get_move()
        make_move(turn,"X")
        game_state = check_win()
        player = 2
        plays +=1
    else:
        turn = get_move()
        make_move(turn,"O")
        game_state = check_win()
        player = 1
        plays +=1

print(game_state)