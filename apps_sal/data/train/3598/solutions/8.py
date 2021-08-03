# import this
# Явное лучше, чем неявное.
# Простое лучше, чем сложное.
# Если реализацию легко объяснить — идея, возможно, хороша.
def plane_seat(a):
    num2 = a[0] + a[1]
    num1 = a[0]
    let = a[-1]
    if let == 'I' or let == 'J':
        return ('No Seat!!')
    elif len(a) == 3:
        if int(num2) > 60:
            return ('No Seat!!')
        elif int(num2) >= 1 and int(num2) <= 20:
            if let == 'A' or let == 'B' or let == 'C':
                return ('Front-Left')
            if let == 'D' or let == 'E' or let == 'F':
                return ('Front-Middle')
            if let == 'G' or let == 'H' or let == 'K':
                return ('Front-Right')
        elif int(num2) >= 21 and int(num2) <= 40:
            if let == 'A' or let == 'B' or let == 'C':
                return ('Middle-Left')
            if let == 'D' or let == 'E' or let == 'F':
                return ('Middle-Middle')
            if let == 'G' or let == 'H' or let == 'K':
                return ('Middle-Right')
        elif int(num2) >= 41 and int(num2) <= 60:
            if let == 'A' or let == 'B' or let == 'C':
                return ('Back-Left')
            if let == 'D' or let == 'E' or let == 'F':
                return ('Back-Middle')
            if let == 'G' or let == 'H' or let == 'K':
                return ('Back-Right')
    elif len(a) == 2:
        if int(num1) >= 1 and int(num1) <= 20:
            if let == 'A' or let == 'B' or let == 'C':
                return ('Front-Left')
            if let == 'D' or let == 'E' or let == 'F':
                return ('Front-Middle')
            if let == 'G' or let == 'H' or let == 'K':
                return ('Front-Right')


'''    
1-20 - front
21-40 - middle
41-60 - back

A,B,C - left
D,E,F - middle
G,H,K - right
'''
