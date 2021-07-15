for _ in range(int(input())):
    l=list(map(str,input().split()))
    k=[]
    for i in l:
        k.append(i.lower())
    if 'berhampore' in k and "serampore" in k:
        print('Both')
    elif "serampore" in k and 'berhampore' not in k:
        print('GCETTS')
    elif "serampore" not in k and 'berhampore'  in k:
        print('GCETTB')
    else:
        print('Others')



