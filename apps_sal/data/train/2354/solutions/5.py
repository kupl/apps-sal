p = input().strip()
a = [input().strip() for i in range(int(input()))]
b = [(ai[1]+aj[0]) for ai in a for aj in a]
print('YES' if p in a+b else 'NO')
