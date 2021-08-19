t = int(input())
for i in range(t):
    try:
        s = str(input())
        s1 = s.lower()
        if 'berhampore' in s1 and 'serampore' not in s1:
            print('GCETTB')
        elif 'serampore' in s1 and 'berhampore' not in s1:
            print('GCETTS')
        elif 'berhampore' in s1 and 'serampore' in s1:
            print('Both')
        else:
            print('Others')
    except EOFError:
        print('Others')
