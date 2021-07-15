def avg_diags(m):
    
    avg1 = []
    avg2 = []
    
    for i in range(len(m)):
        if i % 2 == 1 and m[i][i] >= 0:
            avg1.append(m[i][i])
        
        if i % 2 == 0 and m[-i-1][i] < 0:
            avg2.append(m[-i-1][i])
                        
    avg1 = round(sum(avg1) / len(avg1)) if len(avg1) else -1
    avg2 = round(abs(sum(avg2) / len(avg2))) if len(avg2) else -1
    
    return [avg1, avg2]
