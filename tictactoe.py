

def print_board(board):
    print(f'  1  2  3\nA {board[0][0]}  {board[0][1]}  {board[0][2]}\nB {board[1][0]}  {board[1][1]}  {board[1][2]}\nC {board[2][0]}  {board[2][1]}  {board[2][2]}')
    
def check_victory(board, player, player_token):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player_token:
            print(f'Player {player} Wins!')
            return 1
        if board[0][i] == board[1][i] == board[2][i] == player_token:
            print(f'Player {player} Wins!')
            return 1
    if board[0][0] == board[1][1] == board[2][2] == player_token:
        print(f'Player {player} Wins!')
        return 1
    if board[2][0] == board[1][1] == board[0][2] == player_token:
        print(f'Player {player} Wins!')
        return 1
    else:
        return 0
        

        
def tic_tac_toe():
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    status = 0
    player = 1
    player_token = 'x'
    while status == 0:     
        print_board(board)
        entry = input(f"Player {player}\nWhich space would you like to adjust? (example: 'A1') ")
        while 1==1:
            entry = entry.strip()
            entry = entry.upper()
            if entry[0] in ('A','B','C') and entry[1] in ('1','2','3') and board[ord(entry[0])-65][int(entry[1])-1] == '-':
                board[ord(entry[0])-65][int(entry[1])-1] = player_token
                break
            else:
                entry = input(f"Player {player}\nError. Try again: ")
        status = check_victory(board, player, player_token)
        if player == 1:
            player = 2
            player_token = 'o'
        elif player == 2:
            player = 1
            player_token = 'x'
    print_board(board)
