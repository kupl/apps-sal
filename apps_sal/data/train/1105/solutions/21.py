t = int(input())
output = []

for _ in range(t):
 n = int(input())

 c = list(map(int, input().split()))
 c.sort(reverse=True)

 burner1 = 0
 burner2 = 0

 for x in range(n):
  if burner1 < burner2:
   burner1 += c[x]
  else:
   burner2 += c[x]

 output.append(str(max(burner1,burner2)))

print('\n'.join(output))
