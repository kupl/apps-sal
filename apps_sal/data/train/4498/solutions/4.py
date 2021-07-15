def solution(roman): 
    romanic={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1} 
    number=0
    prev_num=0
    for i in roman:  
        number+=romanic[i] 
        if romanic[i]>prev_num: 
            number=number-(2*prev_num)
        prev_num=romanic[i]
    return number

