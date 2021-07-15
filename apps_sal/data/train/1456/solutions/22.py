def solve(a):
 b = 1
 for i in range(31):
  if a < b:
   length = i
   b >>= 1
   break
  b <<= 1
 res = a * (a + 1) // 2
 cumusum = 0
 for _ in range(length):
  n = a // b - cumusum
  res -= n * b + 1
  cumusum += n
  b >>= 1
 return res

def main():
 T = int(input())
 for _ in range(T):
  l, r = list(map(int, input().split()))
  print(solve(r) - solve(l - 1))

def __starting_point():
 main()

__starting_point()
