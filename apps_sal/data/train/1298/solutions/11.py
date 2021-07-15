for i in range(eval(input())):
 n = eval(input())
 l = list(map(int, input().split()))
 b = l[0]
 c = [x for x in l[1:] if x>b]
 print(len(c))
