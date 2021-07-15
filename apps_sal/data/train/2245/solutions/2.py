read_input = lambda: list(map(int, input().split()))

n, m, k = read_input()
init_array = read_input()
operations = [read_input() for _ in range(m)]
additionals = [0]*(m+1)
sums = [0]*(n+1)

# Calculates the number of operations needed by using increments and decrements
for _ in range(k):
  x, y = read_input()
  additionals[x-1] += 1
  additionals[y  ] -= 1

# Calculates the operations times the number of times the operation is executed
sum_so_far = 0
for i in range(m):
  l, r, val_to_add = operations[i]
  sum_so_far += additionals[i]
  sums[l-1] += sum_so_far*val_to_add
  sums[r  ] -= sum_so_far*val_to_add

# Calculates the final number. Positives add while negatives remove
sum_so_far = 0
for i in range(n):
  sum_so_far += sums[i]
  init_array[i] += sum_so_far
print(' '.join(map(str, init_array)))
