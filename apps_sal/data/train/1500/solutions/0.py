try:
    for i in range(int(input())):
        s=input()
        balance=0
        max_balance=0
        for i in s:
            if i=='(':balance+=1
            else:
                balance-=1
            max_balance=max(max_balance,balance)
        print('('*max_balance,')'*max_balance,sep="")
except Exception as e:
    print(e)
        
