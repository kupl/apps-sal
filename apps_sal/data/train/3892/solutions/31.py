def grader(score):
    return 'A' if score==1 else {9:'A',8:'B',7:'C',6:'D'}.get(int(score*10),'F')

