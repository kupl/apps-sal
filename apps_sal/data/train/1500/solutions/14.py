T = int(input())
for j in range(0, T):
    s = input()
    maxbalance = 0
    balance = 0
    for i in range(len(s)):
        a = s[i]
        if a == '(':
            balance += 1
        else:
            balance -= 1
        if balance > maxbalance:
            maxbalance = balance
    print('(' * maxbalance, ')' * maxbalance, sep='')
