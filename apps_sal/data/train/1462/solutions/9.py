n = int(input())
for l in range(n):
    s = list(map(str, input().strip().split()))
    a = []
    for x in s:
        a.append(x.lower())
    if 'berhampore' in a and 'serampore' in a:
        print('Both')
    elif 'serampore' in a:
        print('GCETTS')
    elif 'berhampore' in a:
        print('GCETTB')
    else:
        print('Others')
