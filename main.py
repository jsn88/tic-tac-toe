import random

def main():
    global game_board
    game_board = ['-' for i in range(9)]

    play_game = True
    print('Welcome to Tic-Tac-Toe game')
    
    while play_game:
        answer = input("\nTo start the game type 'y' or 'n' to end: ")
        match answer:
            case 'y':
                player_choice()
            case 'n':
                play_game = False
                exit()
            case default:
                print('Invalid input, please try again!')
        
        game_board = ['-' for i in range(9)]

def player_choice():
    choice = True
    
    while choice:
        player = input("Would you like to start as 'x' or 'o': ")
        match player:
            case 'x':
                choice = False
                print("You start as 'x', you play first.")
                return play_game(player=1)
            case 'o':
                choice = False
                print("You play as 'o', you play second.")
                return play_game(player=2)
            case 'exit':
                exit()
            case default:
                print('Invalid input, please try again!')

def play_game(player):
    continue_game = True
    x = 'x'
    o = 'o'
    while continue_game:
        if player == 1:
            show_board()
            human_move(x)
            if check_for_win(choice=x,player=1) > 0:
                continue_game = False
            else:
                computer_move(o)
                if check_for_win(choice=o,player=2) >= 2:
                    continue_game = False
        else:
            computer_move(x)
            show_board()
            if check_for_win(choice=x,player=2) >= 2:
                continue_game = False
            else:
                human_move(o)
                if check_for_win(choice=o,player=1) > 0:
                    continue_game = False

def human_move(choice):
    print('Choose between 1-9 to make your move.\n')
    move = int(input('Your move: '))
    match move:
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 :
            if check_move(move=(move-1)):
                game_board[move-1] = choice
            else:
                print('Invalid move')
                return human_move(choice)
        case default:
            print('Invalid input, please use numbers from 1-9!')
            return human_move(choice)

def computer_move(choice):
    comp_move = random.randint(0,8)
    if check_move(comp_move):
        game_board[comp_move] = choice
    else:
        return computer_move(choice)
    
def check_move(move):
    if game_board[move] == '-':
        return True
    else:
        return False

def show_board():
    count = 0
    print('\n- - - - - - - -')
    for row in game_board: 
        print(f' | {row}', end = '')
        if count == 2 or count == 5 or count == 8:
            print(' | \n- - - - - - - -')
        count += 1

def check_for_win(choice,player):
    if game_board.count(choice) >= 3:
        if game_board[0:3].count(choice) == 3 or game_board[3:6].count(choice) == 3 or game_board[6:].count(choice) == 3 or game_board[0::3].count(choice) == 3 or game_board[1::3].count(choice) == 3 or game_board[2::3].count(choice) == 3 or game_board[0::4].count(choice) == 3 or game_board[2:7:2].count(choice) == 3:
            if player == 1:
                show_board()
                print('Congratulations, you won!')
                return 1
            elif player == 2:
                show_board()
                print('Computer wins, good luck next time!')
                return 2
    if game_board.count('-') == 0:
        show_board()
        print('Draw')
        return 3
    else:
        return 0
main()