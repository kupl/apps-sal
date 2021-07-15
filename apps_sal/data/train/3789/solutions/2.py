def score_throws(radii):    
    score = sum(10 if r < 5 else 5 if r <= 10 else 0 for r in radii) 
    return score + 100 if score and len(radii) * 10 == score else score
