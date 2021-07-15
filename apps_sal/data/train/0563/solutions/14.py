t = int(input())
for x in range(t):
    n = int(input())
    arr = input().split()
    for i in range(len(arr)):
      arr[i] = int(arr[i])
    q = int(input())
    for y in range(q):
      s = input().split()
      q1 = int(s[0])-1
      q2 = int(s[1])-1
      print(sum(arr[q1:q2+1]))
