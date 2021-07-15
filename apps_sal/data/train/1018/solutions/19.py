for _ in range(int(input())):
 size = int(input())
 a = [int(x) for x in input().split(" ")]
 b = []
 for i in range(len(a)-1):
  b.append(a[i]-a[i+1])
 print(min(b))
