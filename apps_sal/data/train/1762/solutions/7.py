def mouse_path(path):
  moves = parse_path(path)
  points = convert_moves_to_points(moves)
  if (is_valid(points)):
    return calculate_using_polygon_formula(points)
    if (result == 0):
      return None
    else:
      return result
  else:
    return None

def parse_path(path):
  charIndexList = []
  for i, c in enumerate(list(path)):
    if (c == 'L' or c == 'R'):
      charIndexList.append(i)
  resultList = [('R', int(path[0:charIndexList[0]]))]
  i = 0
  while i < (len(charIndexList) - 1):
    str = path[(charIndexList[i] + 1):(charIndexList[i + 1])]
    resultList.append((path[charIndexList[i]], int(str)))
    i = i + 1
  resultList.append((path[charIndexList[-1]], int(path[(charIndexList[-1] + 1):])))
  return resultList
  
def convert_moves_to_points(moves):
  points = [(0, 0)]
  x = 0
  y = 0
  dir = 0
  for i in range(len(moves)):
    if (dir == 0):
      if (moves[i][0] == 'L'):
        x = x - moves[i][1]
      else:
        x = x + moves[i][1]
    elif (dir == 1):
      if (moves[i][0] == 'L'):
        y = y + moves[i][1]
      else:
        y = y - moves[i][1]
    elif (dir == 2):
      if (moves[i][0] == 'L'):
        x = x + moves[i][1]
      else:
        x = x - moves[i][1]
    elif (dir == 3):
      if (moves[i][0] == 'L'):
        y = y - moves[i][1]
      else:
        y = y + moves[i][1]
    if (moves[i][0] == 'L'):
      if (dir == 0):
        dir = 3
      else:
        dir = (dir - 1) % 4
    else:
      dir = (dir + 1) % 4
    points.append((x, y))
  return points

def is_valid(points):
  if (points[0] != points[-1]):
    return False
  if (points[-2][0] != 0):
    return False
  if (len(points) - 1 != len(set(points[1:]))):
    return False
  lines = list(zip(points, points[1:]))
  i = 2
  while (i < len(lines)):
    j = i - 2
    while (j >= 0):
      if (intersect(lines[i][0], lines[i][1], lines[j][0], lines[j][1])):
        if (not(i == len(lines) - 1 and j == 0)):
          return False  
      j = j - 1
    i = i + 1
  return True
  
  
def intersect(p1, p2, p3, p4):
  linesParallel = (p1[0] == p2[0] and p3[0] == p4[0]) or (p1[1] == p2[1] and p3[1] == p4[1])
  if (linesParallel):
    if (p1[0] == p2[0] and p1[0] == p3[0]):
      secondAbove = max(p2[1], p1[1]) >= min(p3[1], p4[1]) and min(p1[1], p2[1]) <= min(p3[1], p4[1])
      firstAbove = min(p1[1], p2[1]) <= max(p3[1], p4[1]) and  min(p1[1], p2[1]) >= min(p3[1], p4[1])
      return secondAbove or firstAbove
    elif (p1[1] == p2[1] and p1[1] == p3[1]):
      secondAbove = max(p3[0], p4[0]) >= min(p1[0], p2[0]) and max(p3[0], p4[0]) <= max(p1[0], p2[0])
      firstAbove = min(p3[0], p4[0]) >= min(p1[0], p2[0]) and min(p3[0], p4[0]) <= max(p1[0], p2[0])
      return secondAbove or firstAbove
    return False
  isSecondLineVertical = p4[0] == p3[0]
  if (isSecondLineVertical):
    return min(p1[0], p2[0]) <= p4[0] and p4[0] <= max(p1[0], p2[0]) and min(p3[1], p4[1]) <= p1[1] and max(p3[1], p4[1]) >= p1[1]
  else:
    return p3[1] >= min(p1[1], p2[1]) and p3[1] <= max(p1[1], p2[1]) and min(p3[0], p4[0]) <= p1[0] and max(p3[0], p4[0]) >= p1[0]
  
def calculate_using_polygon_formula(points):
  result = 0
  for i in range(len(points) - 1):
    p1 = points[i]
    p2 = points[i + 1]
    result = result + (p1[0] * p2[1] - p1[1] * p2[0])
  return int(abs(result) / 2)
