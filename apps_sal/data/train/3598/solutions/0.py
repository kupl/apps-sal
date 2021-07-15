def plane_seat(a):
    front, middle, back = (list(range(1,21)), list(range(21,41)), list(range(41,61)))
    left, center, right = ('ABC', 'DEF', "GHK")
    x, y = ('', '')
        
    if int(a[:-1]) in front:    x = 'Front-'
    if int(a[:-1]) in middle:   x = 'Middle-'
    if int(a[:-1]) in back:     x = 'Back-'

    if a[-1] in left:    y = 'Left'
    if a[-1] in center:  y = 'Middle'
    if a[-1] in right:   y = 'Right'
    
    return x+y if all((x,y)) else 'No Seat!!'

