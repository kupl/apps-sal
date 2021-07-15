def land_perimeter(arr):
  perimetr=0
  height=len(arr)
  for y in range(height):
    width=len(arr[y])
    for x in range(width):
      if arr[y][x]=='X':
        if x==0 or arr[y][x-1]=='O':perimetr+=1
        if x==width-1 or arr[y][x+1]=='O':perimetr+=1
        if y==0 or arr[y-1][x]=='O':perimetr+=1
        if y==height-1 or arr[y+1][x]=='O':perimetr+=1
  return 'Total land perimeter: '+str(perimetr)
