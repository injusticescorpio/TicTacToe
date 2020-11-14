print("########################")
print('Welcome to TicTacToe game')
print("########################")
board=[' ']*9
player1=''
player2=''
gameon=True
flag=0

len=len(board)
# def winner_is(condition):
#     if co
def show_board(board):
    print(board[6] + '|'+board[7]+'|'+board[8])
    print(''+'-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('' + '-----')
    print(board[0] + '|' + board[1] + '|' + board[2])


def player_symbol():
    mark=''
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
        return 0
    else:
        board[position]=mark
        return 1
def game_starts(board):

    player1,player2 =player_symbol()
    gameon=True
    while(gameon and ' 'in board):
        playing_x_stop = 0
        playing_y_stop = 0
        while(playing_x_stop==0):
            position1=int(input(f'Enter position for {player1}'))
            playing_x_stop=addboard(board,player1,position1)
            show_board(board)
            flag=iswinner(board)
            if(playing_x_stop==1):
                break
        if (flag == 1):
            break
        while(playing_y_stop==0):
            position2 = int(input(f'Enter position for {player2}'))
            playing_y_stop=addboard(board, player2, position2)
            show_board(board)
            flag=iswinner(board)
            if(playing_y_stop==1):
                break
        if (flag == 1):
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
        print('Tie')

    return 0

game_starts(board)