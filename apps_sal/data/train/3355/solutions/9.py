import re
def solve(n):
    print(n)
    min_moves=[]
    n=str(n)
    l=len(n)-1
    extra=0
    
    if '2' in n and '5' in n:
        print('25')
        temp=list(n)
        if n.rindex('2') > n.rindex('5'):
            extra=1
        temp[n.rindex('2')]=''
        temp[n.rindex('5')]=''
        #temp=re.sub(' ','',temp)
        temp=''.join(temp)
        if temp and temp[0]=='0':
                x = re.search("[1-9]", temp)
                if x:
                    extra+=x.start()
        min_moves.append(l-1-n.rindex('2')+l-n.rindex('5')+extra)
        extra=0
         
    if '7' in n and '5' in n:
        print('75')
        temp=list(n)
        if n.rindex('7') > n.rindex('5'):
            extra=1
        temp[n.rindex('7')]=''
        temp[n.rindex('5')]=''
        #temp=re.sub(' ','',temp)
        temp=''.join(temp)
        print('temp',temp)
        if temp and temp[0]=='0':
                x = re.search("[1-9]", temp)
                if x:
                    extra+=x.start()
                    print('extra',extra)
        min_moves.append(l-1-n.rindex('7')+l-n.rindex('5')+extra)
        extra=0
    if '5' in n and '0' in n:
        print('50')
        if n.rindex('5') > n.rindex('0'):
            extra=1
        
        min_moves.append(l-1-n.rindex('5')+l-n.rindex('0')+extra)
        extra=0
    if n.count('0')>1:
        print('00')
        min_moves.append(l-1-n.rindex('0')+l-n.rindex('0',0,n.rindex('0')))
    print(min_moves)
    if not min_moves:
        return -1
    return min(min_moves)
