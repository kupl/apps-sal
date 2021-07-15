def get_grade(s1, s2, s3):
    curr = sum([s1,s2,s3]) // 3
    m = [[90,100,'A'], [80,90,'B'],[70,80,'C'],[60,70,'D']]
    for s,e,grade in m:
        if s<=curr<=e:
            return grade
    return 'F'
