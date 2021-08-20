for _ in range(int(input())):
    s = input()
    check1 = 'berhampore'
    check2 = 'serampore'
    if check1 in s.casefold() and check2 in s.casefold():
        print('Both')
    elif check1 in s.casefold():
        print('GCETTB')
    elif check2 in s.casefold():
        print('GCETTS')
    else:
        print('Others')
