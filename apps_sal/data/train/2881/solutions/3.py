def validate(n):
    step1 = [int(x) * 2 if idx % 2 else int(x) for idx, x in enumerate(str(n)[::-1])]
    step2 = [x - 9 if x > 9 else x for x in step1[::-1]]
    step3 = sum(step2)
    return not step3 % 10
