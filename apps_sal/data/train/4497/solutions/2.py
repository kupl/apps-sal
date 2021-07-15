def positive_to_negative(arr):
    flip = [0 if n == 1 else 1 for n in arr]
    
    for i in range(len(flip)):
        if flip[-(i+1)] == 1:
            flip[-(i+1)] = 0
        else:
            flip[-(i+1)] = 1
            break
    return flip
