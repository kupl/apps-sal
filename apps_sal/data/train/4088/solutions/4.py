def tetris(arr) -> int:

    lines_cleared = 0
    sum = [0,0,0,0,0,0,0,0,0]
    dict = {'L4': 0, 'L3': 1, 'L2': 2,
            'L1': 3, 'L0': 4, 'R0': 4,
            'R1': 5, 'R2': 6, 'R3': 7, 'R4': 8}
    
    for i in arr:   
        sum[dict[i[-2:]]] += int(i[0])
        
        lines = min(sum)
        sum = [i - lines for i in sum] 
        lines_cleared += lines
        
        if max(sum) >= 30:
            break
            
    return lines_cleared
