from sys import stdin
lines = stdin.readlines()[1:]

for line in lines:
 str_2n = str(2 ** int(line))
 sum = 0
 for i in str_2n:
  sum += int(i)
 print(sum)

