def plane_seat(a):
    row = int(a[:-1])
    seat = a[-1]
    
    if row > 60 or seat not in 'ABCDEFGHK':
        return 'No Seat!!'
        
    if row <= 20:
        end = 'Front'
    elif row <= 40:
        end = 'Middle'
    else:
        end = 'Back'
        
    if seat in 'ABC':
        side = 'Left'
    elif seat in 'DEF':
        side = 'Middle'
    else:
        side = 'Right'
        
    return f'{end}-{side}'



