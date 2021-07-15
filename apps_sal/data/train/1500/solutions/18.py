for i in range(int(input())):
    x=input()
    maxlen=0
    balance=0
    for i in x:
        if i=='(':
            balance+=1
        else:
            balance-=1
        maxlen=max(maxlen,balance)
    print('('*maxlen +')'*maxlen)
