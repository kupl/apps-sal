try:
    for i in range(int(input())):
        st = input()
        balance = 0
        max_balance = 0
        for i in st:
            if i == '(':
                balance += 1
            else:
                balance -= 1
            max_balance = max(max_balance, balance)
        print('(' * max_balance, ')' * max_balance, sep="")
except Exception as e:
    print(e)
