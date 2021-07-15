def get_score(arr):
    score = 0
    level = 0
    lines = 0
    for i in arr:
        if i == 4:
            score += 1200*(level+1)
            lines += 4
        elif i == 3:
            score += 300*(level+1)
            lines += 3
        elif i == 2:
            score += 100*(level+1)
            lines += 2
        elif i == 1:
            score += 40*(level+1)
            lines += 1
        else:
            continue
    
        if lines >= 10:
            level += 1
            lines -= 10
            
    return score
