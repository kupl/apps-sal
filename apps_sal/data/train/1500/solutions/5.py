for i in range(int(input())):
    j = input()
    balance = 0
    max_balance = 0
    for i in range(len(j)):
        if j[i] == '(':
            balance += 1
        if j[i] == ')':
            balance -= 1
        max_balance = max(max_balance, balance)
    for i in range(max_balance):
        print('(', end='')
    for i in range(max_balance):
        print(')', end='')
    print()
