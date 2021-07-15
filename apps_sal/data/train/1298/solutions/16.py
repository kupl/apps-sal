for _ in range(eval(input())):
 noc = eval(input())
 power = list(map(int, input().split()))
 spower = power[0]
 ppowers= power[1:]
 ans = sum([1 for x in ppowers if x > spower])
 print(ans)
