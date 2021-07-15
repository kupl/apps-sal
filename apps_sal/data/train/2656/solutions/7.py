def bird_code(a):
    return [bird(b.upper()) for b in a]
    
def bird(s):
    b = s.replace('-', ' ').split()
    if len(b) == 1: return s[:4]
    if len(b) == 2: return b[0][:2] + b[1][:2]
    if len(b) == 3: return b[0][0] + b[1][0] + b[2][:2]
    if len(b) == 4: return b[0][0] + b[1][0] + b[2][0] + b[3][0]
