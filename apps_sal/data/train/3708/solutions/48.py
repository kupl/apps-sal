def hex_to_dec(s):
    dec = 0
    rev_s = s[::-1]
    count = 0
    for i in rev_s:
        if i == '0':
            dec += 0 * 16 ** count
            count += 1
        elif i == '1':
            dec += 1 * 16 ** count
            count += 1
        elif i == '2':
            dec+= 2 * 16 ** count
            count += 1
        elif i == '3':
            dec += 3 * 16 ** count
            count += 1
        elif i == '4':
            dec += 4 * 16 ** count
            count += 1
        elif i == '5':
            dec+= 5 * 16 ** count
            count += 1
        elif i == '6':
            dec += 6 * 16 ** count
            count += 1
        elif i == '7':
            dec+= 7 * 16 ** count
            count += 1    
        elif i == '8':
            dec+= 8 * 16 ** count
            count += 1
        elif i == '9':
            dec += 9 * 16 ** count
            count += 1
        elif i.lower() == 'a':
            dec += 10 * 16 ** count
            count += 1
        elif i.lower() == 'b':
            dec += 11 * 16 ** count
            count += 1
        elif i.lower() == 'c':
            dec += 12 * 16 ** count
            count += 1
        elif i.lower() == 'd':
            dec += 13 * 16 ** count
            count += 1
        elif i.lower() == 'e':
            dec += 14 * 16 ** count
            count += 1
        elif i.lower() == 'f':
            dec += 15 * 16 ** count
            count += 1
    return dec
