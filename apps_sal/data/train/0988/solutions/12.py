# cook your dish here
for _ in range(int(input())):
 n = int(input())
 arr = list(map(int, input().split()))
 x, max_bit = 0, 0 #max bit is the highest value bit (0-indexed)
 bitset = {}
 for ele in arr:
  for i, bit in enumerate(reversed(bin(ele)[2:])):
   if bit == '1':
    bitset[i] = bitset.get(i,0)+1
   max_bit = max(max_bit, i)
 for b in range(max_bit+1):
  if b in bitset:
   if bitset[b] > n-bitset[b]: x |= (1 << b)
 total = 0
 for ele in arr: total += ele^x
 print(total)

