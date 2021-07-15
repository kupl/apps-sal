ans='FFFFFFDCBA'
def grader(score):
    s = int(round(score/0.1))
    try:
        return ans[s]
    except:
        if score == 1:
            return 'A'
        return 'F'
