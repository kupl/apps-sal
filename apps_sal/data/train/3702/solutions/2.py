def olympic_ring(string):
  h = {'a':1, 'b':1, 'd':1, 'e': 1, 'g':1, 'o':1, 'p':1, 'q':1, 'A':1, 'B':2, 'D':1, 'O':1, 'P':1, 'R':1, 'Q':1}
  result = lambda i: {i <= 1: 'Not even a medal!', i == 2: 'Bronze!', i == 3: 'Silver!', i >= 4: 'Gold!'}[True]
  return result(sum([h[i] if i in h.keys() else 0 for i in string])//2)
