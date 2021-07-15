def seven(m, step = 0):
  if m < 100: return (m, step)
  x, y, step = m // 10, m % 10, step + 1
  res = x - 2 * y
  return seven(res, step)
