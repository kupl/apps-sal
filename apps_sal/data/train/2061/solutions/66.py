for _ in range(int(input())):
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))

    x = min(ax, bx, cx)
    y = min(ay, by, cy)

    if [x, y] not in [[ax, ay], [bx, by], [cx, cy]]:
      x = 2*x + 1
      y = 2*y + 1
    elif [x+1, y] not in [[ax, ay], [bx, by], [cx, cy]]:
        x *= 2
        y = 2*y + 1
    elif [x, y+1] not in [[ax, ay], [bx, by], [cx, cy]]:
        x = 2*x + 1
        y *= 2
    else:
        x *= 2
        y *= 2
    
        
    if x != y:
      print((max(abs(x), abs(y))))
    elif x == 0 or x == 1:
      print(x)
    else:
      print((abs(x)+1))


