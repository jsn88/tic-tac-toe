
def player_choice():
    choice = True
    player = ''
    
    while choice:
        player = input("Would you like to start as 'x' or 'o': ")
        match player:
            case 'x':
                choice = False
                return player_move()
            case 'o':
                choice = False
                return computer_move()
            case default:
                print('Invalid input, please try again!')

def player_move():
    pass

def computer_move():
    pass

def check_for_win():
    pass

def show_grid():
    for row in game:
        print('\n- - - - - - - - -\n')        
        for pos in row:
            print(f' | {pos}')
        print(' | ')
        print('\n- - - - - - - - -\n')  
        
game = [[],[],[]]

play_game = True

print('Welcome to Tic-Tac-Toe game\n')

while play_game:
    answer = input("To start the game type 'y' or 'n' to end: ")
    if answer == 'y':
        # player_choice()
        show_grid()
        # check_for_win()
    elif answer == 'n':
        play_game = False
    else:
        print('Unrecognized character, please try again.')
