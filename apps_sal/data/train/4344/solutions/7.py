def rectangles(n, m):
  OneOnOneRects = (n-1) * (m-1)
  sumOfM = sum(range(1, m-1))
  sumOfN = sum(range(1, n-1))
  OneAndSome = (n-1) * sumOfM
  SomeAndOne = (m-1) * sumOfN

  SomeAndSome = 0
  for i in range(2, n):
      for j in range(2, m):
          SomeAndSome = SomeAndSome + (n-i)*(m-j)

  return OneOnOneRects + OneAndSome + SomeAndOne + SomeAndSome
