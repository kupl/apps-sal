from itertools import groupby

for case in range(int(input())):
    string=''.join(input().split())
    N=int(input())
    char_string=input()
    
    dicti={i:len(list(i)) for i,j in groupby(string,key=None)}
    
    old=0

    for i in dicti:
        if i not in char_string:
            old+=1
    
    if old==0:
        print(1)
    
    else:
        print(0)
