def blocks_to_collect(level):
    answer = {
    'total': sum([(i+3+i)**2 for i in range(level)]),
    'gold': sum([(i+3+i)**2 for i in range(0,level,4)]),
    'diamond': sum([(i+3+i)**2 for i in range(1,level,4)]),
    'emerald': sum([(i+3+i)**2 for i in range(2,level,4)]),
    'iron': sum([(i+3+i)**2 for i in range(3,level,4)]),
    }
    
    return answer
