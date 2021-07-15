def solution(x):
    table = [
        (1000,"M"),
        (900,"CM"),
        (500,"D"),
        (400,"CD"),
        (100,"C"),
        (90,"XC"),
        (50,"L"),
        (40,"XL"),
        (10,"X"),
        (9,"IX"),
        (5,"V"),
        (4,"IV"),
        (1,"I")
    ]
    for num, rep in table:
        if x >= num:
            return rep + solution(x-num)
    return str()
