def points(games):
    pts = 0
    for i in games:
      if i[0] > i[2]:
        pts += 3
      elif i[0] == i[2]:
        pts += 1
    return pts

