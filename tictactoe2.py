def tic_tac_toe():
    board = [1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 1.4, 1.5, 1.6, 2.4, 2.5, 2.6, 3.4, 3.5, 3.6, 1.7, 1.8, 1.9, 2.7, 2.8, 2.9, 3.7, 3.8, 3.9,
             4.1, 4.2, 4.3, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 4.4, 4.5, 4.6, 5.4, 5.5, 5.6, 6.4, 6.5, 6.6, 4.7, 4.8, 4.9, 5.7,
             5.8, 5.9, 6.7, 6.8, 6.9, 7.1, 7.2, 7.3, 8.1, 8.2, 8.3, 9.1, 9.2, 9.3, 7.4, 7.5, 7.6, 8.4, 8.5, 8.6, 9.4, 9.5,
             9.6, 7.7, 7.8, 7.9, 8.7, 8.8, 8.9, 9.7, 9.8, 9.9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    
    def draw():
        print(board[0], "|",  board[1],"|", board[2],   "|",board[3], "|",board[4],"|", board[5],"|",board[6], "|", board[7] ,"|", board[8])
        print ("________________|_________________|_________________")
        print(board[9], "|", board[10], "|", board[11], "|", board[12], "|", board[13], "|", board[14], "|", board[15], "|", board[16], "|", board[17])
        print ("________________|_________________|_________________")
        print(board[18],"|", board[19],"|", board[20],  "|", board[21],"|", board[22],"|", board[23], "|", board[24],"|", board[25],"|", board[26])
        print ("________________|_________________|_________________")
        print(board[27], "|",  board[28],"|", board[29],"|", board[30], "|",  board[31],"|", board[32], "|", board[33], "|",  board[34],"|", board[35])
        print ("________________|_________________|_________________")
        print(board[36],"|", board[37],"|", board[38],  "|", board[39], "|",  board[40],"|", board[41], "|", board[42], "|",  board[43],"|", board[44])
        print ("________________|_________________|_________________")
        print(board[45],"|", board[46],"|", board[47],  "|", board[48], "|",  board[49],"|", board[50], "|", board[51], "|",  board[52],"|", board[53])
        print ("________________|_________________|_________________")
        print(board[54], "|",  board[55],"|", board[56],"|",board[57], "|",board[58],"|", board[59],"|",board[60], "|", board[61] ,"|", board[62])
        print ("________________|_________________|_________________")
        print(board[63], "|", board[64], "|", board[65],"|", board[66], "|", board[67], "|", board[68], "|", board[69], "|", board[70], "|", board[71])
        print ("________________|_________________|_________________")
        print(board[72],"|", board[73],"|", board[74],  "|", board[75],"|", board[76],"|", board[77], "|", board[78],"|", board[79],"|", board[80])
        print()
    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = "X"

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 81):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                   print("\nThat's not a number. Try again")
                   continue

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose where to place a cross")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 2 choose where to place a nought")
        p2()
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()
