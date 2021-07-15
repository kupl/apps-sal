def direction_in_grid(n,m):
  return "LRUD"[2*(n>m)+(m if n>m else n)%2]
