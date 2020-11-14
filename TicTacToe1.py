import os
print("########################")
print('Welcome to TicTacToe game')
print("########################")
board=[' ']*9
player1=''
player2=''
flag=0

def winner_is(condition):
    if condition.upper() =='X':
        print('Wow! X won the game')
        exit(1)
    elif condition.upper() =='O':
        print('Wow! O won the game')
        exit(1)
    else:
        print('Tie case')
        exit(1)

def show_board(board):
    print(board[6] + '|'+board[7]+'|'+board[8])
    print(''+'-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('' + '-----')
    print(board[0] + '|' + board[1] + '|' + board[2])


def player_symbol():
    mark=input('Which symbol do u want X or O\n')
    player1=mark
    if(player1.upper() =='X' or player1.upper()=='O'):

        if(player1.upper()=='X'):
            return('X','O')
        else:
            return ('O','X')
    else:
        print('error')

def addboard(board,mark,position):
    if(board[position]=='X'or board[position]=='O'):
        print("there is already a value")
        return False
    else:
        board[position]=mark
        return  True

def game_starts(board):
    player1,player2 =player_symbol()
    while(' 'in board):
        x_or_y_no_repeat_1 = False
        x_or_y_no_repeat = False
        while(not(x_or_y_no_repeat_1)):
            position1=int(input(f'Enter position for {player1}'))
            x_or_y_no_repeat_1=addboard(board,player1,position1)
        show_board(board)
        flag=iswinner(board)
        if (flag == 1):
            winner_is('x')
        while(not(x_or_y_no_repeat)):
            position2 = int(input(f'Enter position for {player2}'))
            x_or_y_no_repeat=addboard(board, player2, position2)
        show_board(board)
        flag=iswinner(board)
        if (flag == 1):
            winner_is('o')
            break

def iswinner(board):
    #change to 0 as index starts from zeo

    winposition=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    if (' ' in board):
        for a,b,c in winposition:
            if(board[a]+board[b]+board[c])=='X'*3 or (board[a]+board[b]+board[c])=='O'*3 :
                flag=1
                return(flag)
                break
            else:
                continue
    else:
        winner_is('tie')

    return 0

game_starts(board)