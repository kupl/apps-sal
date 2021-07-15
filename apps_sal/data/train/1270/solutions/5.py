def min_boxes(k, boxes):
 sum_ = sum(boxes)
 if sum_ < 2 * k: return -1
 boxes = sorted(boxes, reverse=True)

 n = len(boxes)

 table = [[-1 for _ in range(sum_ + 1)] for _ in range(n + 1)]

 table[0][:] = [False for _ in range(sum_ + 1)]

 for i in range(n + 1):
  table[i][0] = True
 
 for i in range(1, n + 1):
  for j in range(1, sum_ + 1):
   if boxes[i - 1] > j:
    table[i][j] = table[i - 1][j]
   else:
    table[i][j] = table[i - 1][j] or table[i - 1][j - boxes[i - 1]]


 i = 0
 x = boxes[0]
 while x < 2 * k:
  i += 1
  x += boxes[i]
 
 if i == 1:
  i += 1

 while i < n + 1:
  sum_till_here = sum(boxes[ : i])
  for j in range(k, sum_ + 1):
   if table[i][j]:
    if sum_till_here - j >= k:
     return i
  i += 1

 return -1


def __starting_point():
 test_cases = int(input())
 while test_cases:


  n, k = map(int, input().split())
  boxes = list(map(int, input().split()))

  print(min_boxes(k, boxes))

  test_cases -= 1
__starting_point()
