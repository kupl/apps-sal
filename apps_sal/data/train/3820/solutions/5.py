def checkered_board(n):
  return '\n'.join(' '.join(['□■', '■□'][n%2][j%2-i%2] for i in range(n)) for j in range(n)) if type(n) is int and n > 1 else False
