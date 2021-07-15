def connect_four_place(columns):
    ls = [['-']*7,['-']*7,['-']*7,['-']*7,['-']*7,['-']*7] # create the board
    for i,j in enumerate(columns):
        if i%2 == 0: #assign the tokens
            token = 'Y'
        else:
            token = 'R'
        z = 5
        while z >= 0:   #deal with already filled-in positions
            if ls[z][j] == '-':
                ls[z][j] = token
                break
            elif ls[z][j] != '-':
                z -= 1      
    return ls
