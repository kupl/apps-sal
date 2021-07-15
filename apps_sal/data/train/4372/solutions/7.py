def lostSheep(friday,saturday,total):
    sheeps =0
    for i in range(len(friday)):
        sheeps+=friday[i]
    for i in range(len(saturday)):
        sheeps+=saturday[i]
    return total-sheeps
