def animals(heads, legs):
    if heads == 0 and legs == 0:
        return (0, 0)
    if legs % 2 == 1 or heads <= 0 or legs <= 0 or heads * 4 < legs or heads * 2 > legs:
        return "No solutions"
    else:
        ch = heads
        co = 0
        for i in range(1, heads + 1):
            if ch * 2 + co * 4 < legs:
                ch -= 1
                co += 1
            if ch * 2 + co * 4 == legs:
                break
        return (ch, co)
