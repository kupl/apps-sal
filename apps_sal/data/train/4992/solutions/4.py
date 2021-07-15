def matches(set,digits):
    count = 0   
    if 'FREE SPACE' in set:
        count += 1
    for digit in digits:
        if int(digit[1:]) in set:
            count += 1           
    return count

def bingo(card, numbers):

    for set in card:
        count_row = matches(set,numbers)
        if count_row == 5:
            break
            
    for column in range(5):
        cols = []
        for row in range(1,6):
            cols.append(card[row][column])
        count_col = matches(cols, numbers)
        if count_col == 5:
            break

    diag_r = []
    diag_l = [] 
    for i in range(5):
        diag_r.append(card[i+1][i])
        diag_l.append(card[5-i][i])
    
    return count_row == 5 or count_col == 5 or matches(diag_r, numbers) == 5 or matches(diag_l, numbers) == 5
