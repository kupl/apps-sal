T = int(input())
for t in range(T):
    s = input()
    s = s.lower()
    b_check = 'berhampore' in s
    s_check = 'serampore' in s
    if (b_check) and (s_check):
        print('Both')
    elif (b_check) and (not s_check):
        print('GCETTB')
    elif (not b_check) and (s_check):
        print('GCETTS')
    else:
        print('Others')
