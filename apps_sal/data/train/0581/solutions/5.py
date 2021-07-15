for __ in range(eval(input())):
 n, l, e = list(map(int, input().split()))
 a = list(map(int, input().split()))
 if l%(sum(a) + e)==0: print('YES')
 else: print('NO')

