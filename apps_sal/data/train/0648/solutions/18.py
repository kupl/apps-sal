n, queries = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))

for i in range(queries):
 inp = list(map(int, input().strip().split()))
 if inp[0] == 1:
  curr, maxJumps, out = inp[1] - 1, inp[2], inp[1] - 1
  while maxJumps > 0:
   #print 'starting : ', maxJumps, ' at : ', curr
   i, nextTo = curr + 1, curr
   while i < n and i < curr + 101:
    if arr[i] > arr[curr]:
     nextTo = i
     break
    i+=1
   if nextTo == curr:
    out = nextTo
    break
   out = nextTo
   curr = nextTo
   maxJumps -= 1
   #print 'Left : ', maxJumps, ' at : ', out + 1
  print(out + 1)
 else:
  for i in range(inp[1] - 1, inp[2]):
   arr[i] += inp[3]

