def animals(heads, legs):
    if heads == legs == 0: return (0,0)
    a = (4*heads - legs)/2
    b = (legs - 2*heads)/2
    if a<0 or b<0: return 'No solutions'
    if [a%1,b%1] == [0,0]: return (a,b)
    return 'No solutions'


