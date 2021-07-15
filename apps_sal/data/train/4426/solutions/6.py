def isMultiple(a, b, n):
    x=int((a/b-a//b)*10+0.5)
    return 0<x<10 and x%n==0
