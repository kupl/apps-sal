def is_zigzag(h):
 if (len(h) <= 1):
  return True
 sign = h[1] - h[0]
 if (len(h) == 2 and sign == 0):
  return False
 for i in range(2, len(h)):
  diff = h[i] - h[i - 1]
  if (diff * sign >= 0):
   return False
  sign = diff 
 return True

def is_possible(h, r):
 for i in range(1, len(h)):
  diff = h[i] - h[i - 1]
  if (diff < 0 and r[i] > r[i - 1]):
   return True
  elif (diff > 0 and r[i] < r[i - 1]):
   return True
  elif (diff == 0 and r[i] != r[i - 1]):
   return True
 return False

def add_day(h, r):
 for i in range(len(h)):
  h[i] += r[i]

INF = float('inf')
def find_intervals(heights, rates):
 intervals = []
 f = is_zigzag(heights)
 if (f):
  interval = [0, 'Inf']
  intervals.append(interval)
 day = 0
 while (is_possible(heights, rates)):
  day += 1
  add_day(heights, rates)
  if (is_zigzag(heights)):
   if (f == 1):
    continue
   else:
    intervals.append([day, 'Inf'])
    f = 1
  else:
   if (f == 1):
    intervals[-1][-1] = day - 1
    f = 0

 return intervals


t = int(input())
for i in range(t):
 n = int(input())
 heights = []
 rates = []
 for k in range(n):
  h, m = list(map(int, input().split()))
  heights.append(h)
  rates.append(m)
 intervals = find_intervals(heights, rates)
 print(len(intervals))
 for interval in intervals:
  print('{} {}'.format(interval[0], interval[1]))

