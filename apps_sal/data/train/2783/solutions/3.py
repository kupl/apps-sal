scores = {10: 'A', 9: 'A', 8: 'B', 7: 'C', 6: 'D'}

def get_grade(*args):
    mean = sum(args) / len(args)
    return scores.get(mean // 10, 'F')    
