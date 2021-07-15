import math

numberColor = {'R': 0, 'G': 1, 'B': 2}
back = {0: 'R', 1: 'G', 2: 'B'}

def triangle(row):
    if len(row) == 1:
        return row
    
    n = len(row)
    faqN = math.factorial(n - 1)
    sum = 0
    for k in range(n):
        sum += faqN/(math.factorial(n - k - 1) * math.factorial(k)) * numberColor[row[k]]
    
    sum *= (-1) ** (n - 1)
    r = sum % 3
    
    return back[r]
