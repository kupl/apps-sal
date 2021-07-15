# Post Prefixes
for t in range(int(input())):

 n, k = list(map(int, input().split())) # Two inputs
 flips = n - k
 A = []
 # Logic: Flip n-k numbers from i to (-i). First start with even numbers
 #        beginning from 2. If n-k > n/2 ie no of flips is greater than even
 #        numbers available, then flip remaining odd numbers starting from         the
 #        back, ie bigger numbers till total (n-k) numbers are flipped.

 for i in range(n):
  a = i
  if (i + 1) % 2 == 0 and flips > 0:  # If even and flips > 0, i = -i
   A.append(-(a+1))
   flips -= 1
  else:
   A.append(a+1)

 if flips > 0:  # If no. of flips still exist
  if n % 2:
   last_odd = n-1 # List is 0 based
  else:
   last_odd = n-2

  while (flips > 0):
   A[last_odd] *= -1
   flips -= 1
   last_odd -= 2

 print(*A)


