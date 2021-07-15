def alphabet_war(t):
    a,b = 0, 0
    A,B = ['s', 'b', 'p', 'w'], ['z', 'd', 'q', 'm']
    for i in t:
        if i in A:
            a += A.index(i) + 1
        elif i in B:
            b += B.index(i) + 1
    return f"{['Right', 'Left'][a > b]} side wins!" if a != b else "Let's fight again!"
    

