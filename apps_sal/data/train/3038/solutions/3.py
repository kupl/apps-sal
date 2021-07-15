def solve(st):
    highestVal = 0
    mvc = None
    for c in st:
        firstIdx = st.index(c)
        lastIdx = st.rindex(c)                 
        value = lastIdx - firstIdx
        if not mvc or value > highestVal:
            highestVal = value
            mvc = c
        elif value == highestVal:
            if c < mvc: 
                highestVal = value
                mvc = c
    return mvc            

