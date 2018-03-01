def tic_tac_toe():
    board = [1, 2, 3, 11, 12, 13, 21, 22, 23, 4, 5, 6, 14, 15, 16, 24, 25, 26, 7, 8, 9, 17, 18, 19, 27, 28, 29,
             31, 32, 33, 41, 42, 43, 51, 52, 53, 34, 35, 36, 44, 45, 46, 54, 55, 56, 37, 38, 39, 47,
             48, 49, 57, 58, 59, 61, 62, 63, 71, 72, 73, 81, 82, 83, 64, 65, 66, 74, 75, 76, 84, 85,
             86, 67, 68, 69, 77, 78, 79, 87, 88, 89]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    
    def draw():
        print(board[0], "|",  board[1],"|", board[2],   "|", board[3], "|",board[11],"|", board[12],"|",board[21], "|", board[22] ,"|", board[23], board[10])
        print ("__________|______________|______________")
        print(board[9], "|", board[10], "|", board[11], "|", board[12], "|", board[13], "|", board[14], "|", board[15], "|", board[16], "|", board[17])
        print ("__________|______________|______________")
        print(board[18],"|", board[19],"|", board[20],  "|", board[21],"|", board[22],"|", board[23], "|", board[24],"|", board[25],"|", board[26])
        print ("__________|______________|______________")
        print(board[27], "|",  board[28],"|", board[29],"|", board[30], "|",  board[31],"|", board[32], "|", board[33], "|",  board[34],"|", board[35])
        print ("__________|______________|______________")
        print(board[36],"|", board[37],"|", board[38],  "|", board[39], "|",  board[40],"|", board[41], "|", board[42], "|",  board[43],"|", board[44])
        print ("__________|______________|______________")
        print(board[45],"|", board[46],"|", board[47],  "|", board[48], "|",  board[49],"|", board[50], "|", board[51], "|",  board[52],"|", board[53])
        print ("__________|______________|______________")
        print(board[54], "|",  board[55],"|", board[56],"|",board[57], "|",board[58],"|", board[59],"|",board[60], "|", board[61] ,"|", board[62])
        print ("__________|______________|______________")
        print(board[63], "|", board[64], "|", board[65],"|", board[66], "|", board[67], "|", board[68], "|", board[69], "|", board[70], "|", board[71])
        print ("__________|______________|______________")
        print(board[72],"|", board[73],"|", board[74],  "|", board[75],"|", board[76],"|", board[77], "|", board[78],"|", board[79],"|", board[80])
        print()
    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = " X "

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p2()
        else:
            board[n] = " O "

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
