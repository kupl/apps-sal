T = int(input())

def solve(nums, K):
 if K <= 0 or len(nums) == 0:
  return 0
 c = [x for x in nums if x > 0]
 c.sort()
 #print c
 #print K
 if c[0] >= K:
  return (K-1)*len(c)+1
 else:
  a = c[0]
  return len(c)*a + solve([x-a for x in c], K-a)

for _ in range(T):
 [R, G, B] = [int(x) for x in input().rstrip().split(" ")]
 K = int(input())
 print(solve([R, G, B], K))
