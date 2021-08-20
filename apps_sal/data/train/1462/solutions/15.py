for i in range(int(input())):
    val = list(map(str, input().split(' ')))
    for j in range(len(val)):
        val[j] = val[j].lower()
    if 'berhampore' in val and 'serampore' in val:
        print('Both')
    elif 'serampore' in val:
        print('GCETTS')
    elif 'berhampore' in val:
        print('GCETTB')
    else:
        print('Others')
