from math import atan2, degrees

def get_score(x, y):
    scores = [8, 16, 7, 19, 3, 17, 2, 15, 10, 6,
              13, 4, 18, 1, 20, 5, 12, 9, 14, 11]
    
    distance = (x*x + y*y) ** 0.5
    angle = degrees(atan2(y, x))
    mod = ''
    
    if distance > 340 / 2:
        return 'X'         # outside
    elif distance < 12.7 / 2:
        return 'DB'        # bull's eye
    elif distance < 31.8 / 2:
        return 'SB'        # bull
    elif 198 / 2 < distance < 214 / 2:
        mod = 'T'          # triple
    elif 324 / 2 < distance < 340 / 2:
        mod = 'D'          # double
    
    number = str( scores[int((angle + 180 + 9) / 18) - 1] )
    
    return mod + number
