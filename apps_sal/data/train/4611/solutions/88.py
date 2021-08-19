def animals(heads, legs):
    (chicken, cows) = (2 * heads - legs / 2, legs / 2 - heads)
    if chicken < 0 or cows < 0 or (not chicken == int(chicken)) or (not cows == int(cows)):
        return 'No solutions'
    return (chicken, cows)
