def did_I_win_2D(player, board):
    did_win = True
    # for x in range(3):
        # print(did_win, x,"above")
        # did_win &=  player==board[x][0] or \
        #           player == board[x][1] or \
        #           player == board[x][2]
        # print(did_win, x,"below")

        # print(board[x][0],"first slot")
        # print(board[x][1],"second slot")
        # print(board[x][2],"third slot")


    did_win = player == board[0][0] and player == board[1][0] and player == board[2][0] or\
    player == board[0][1] and player == board[1][1] and player == board[2][1] or\
    player == board[0][2] and player == board[1][2] and player == board[2][2] or \
    player == board[0][0] and player == board[1][1] and player == board[2][2] or\
    player == board[0][2] and player == board[1][1] and player == board[2][0]


    return did_win

def print_2D_board(b):
    for i in range(len(b)):
        print(b[i])


def main():
        boards =  [

                     [["X","O","O"]] *3,\
                     [["O","O","X"],["O","X","O"], ["X","O","O"]]
        ]

        for b in boards:
            print_2D_board(b)
            print("X won?", did_I_win_2D
("X", b))
            print("O won?", did_I_win_2D
("O", b))

if __name__ == "__main__":
    main()
