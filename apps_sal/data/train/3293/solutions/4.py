def cell30(l, c, r):
  if l == 1: return 1 if c == 0 and r == 0 else 0
  return 0 if c == 0 and r == 0 else 1
def rule30(row, n):
  return pure30([c if c == 1 else 0 for c in row], n)
def pure30(row, n):
  for i in range(n):
    row.append(0)
    row.insert(0, 0)
    ref = row[:]
    row = [cell30(0 if i == 0 else ref[i - 1], v, ref[i + 1] if i + 1 < len(ref) else 0) for i, v in enumerate(row)]
  return row
