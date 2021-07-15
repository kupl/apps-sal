def who_is_winner(pieces_position_list):
  C, counts, rows = {'R':'Red', 'Y':'Yellow'}, [0,0,0,0,0,0,0], 6
  grid, slots, I = list(), 7, {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6}
  # grid index is 0-6 for A-G. Contains list up to 6 "R"=-1 or "Y"=1 (or None = 0)
  for i in range(7): grid.append([0,0,0,0,0,0])
  for piece in pieces_position_list:
    slot, color = I[piece[0]], C[piece[2]]
    grid[slot][counts[slot]] = color
    # Test win condition
    # VERTICAL
    n = 0
    for y in range(counts[slot], rows):
      if grid[slot][y] == color: n += 1
      else: break
    for y in range(counts[slot]-1, -1, -1):
      if grid[slot][y] == color: n += 1
      else: break
    if n >= 4: return color
    # HORIZONTAL
    n = 0
    for x in range(slot, slots):
      if grid[x][counts[slot]] == color: n += 1
      else: break
    for x in range(slot-1, -1, -1):
      if grid[x][counts[slot]] == color: n += 1
      else: break
    if n >= 4: return color
    # NORTHEAST
    x, y, n = slot, counts[slot], 0 
    while x < slots and y < rows:
      if grid[x][y] == color: x, y, n = x+1, y+1, n+1
      else: break
    x, y = slot-1, counts[slot]-1
    while x >= 0 and y >= 0:
      if grid[x][y] == color: x, y, n = x-1, y-1, n+1
      else: break
    if n >= 4: return color
    # NORTHWEST
    x, y, n = slot, counts[slot], 0 
    while x >= 0 and y < rows:
      if grid[x][y] == color: x, y, n = x-1, y+1, n+1
      else: break
    x, y = slot+1, counts[slot]-1
    while x < slots and y >= 0:
      if grid[x][y] == color: x, y, n = x+1, y-1, n+1
      else: break
    if n >= 4: return color
    counts[slot] += 1
  return "Draw"

