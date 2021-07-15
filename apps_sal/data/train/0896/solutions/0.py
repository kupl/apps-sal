for tc in range(int(input())):
 N = int(input())
 a, b = list(map(int, input().split()))
 pr = []

 # 'L' is lexicographically lower than 'R'.
 # so, we should first try to apply L+ or L-
 # if we can't then only we'll try to apply R+ or R-

 for i in range(N - 1):
  l, r = list(map(int, input().split()))

  #continue the following process until a == l and b == r
  while a != l or b != r:
   # trying to apply L-
   if a > l:
    a -= 1
    pr.append('L-')

   # now, trying to apply L+ (if a < b)
   elif a + 1 < b and a < l:
    a += 1
    pr.append('L+')

   # ok, so far, so good... now, let's try to apply R+
   elif b < r:
    b += 1
    pr.append('R+')

   # finally, lastly, trying to apply R- (if a < b)
   elif b - 1 > a and b > r:
    b -= 1
    pr.append('R-')

 print(len(pr))
 print(''.join(pr))
