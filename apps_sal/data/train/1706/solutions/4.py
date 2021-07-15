def rectangle_rotation(a, b):
  x=a//2**0.5
  y=b//2**0.5
  return x*2*y+x+y+1-((x-y)%2)
