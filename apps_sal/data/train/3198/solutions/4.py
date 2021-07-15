NOTATION = {True: 4, False: -1}

def check_exam(ref, ans):
    return max(0, sum( NOTATION[r==a] for r,a in zip(ref,ans) if a) )
