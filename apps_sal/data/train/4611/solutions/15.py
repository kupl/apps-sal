def animals(heads, legs):
    if heads * 2 > legs or heads * 4 < legs or legs % 2:
        return 'No solutions'
    cows = legs // 2 - heads
    return (heads - cows, cows)
