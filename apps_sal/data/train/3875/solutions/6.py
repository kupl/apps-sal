def draw(waves):
    # your code
    #■□
    result = ""
    height = max(waves)
    weight = len(waves)
    for i in range(height):
        for j in range(weight):
            if(waves[j] >= height - i):
                result += "■"
            else:
                result += "□"
        if(i != height-1):
            result += "\n"
    
    return result 
