from fractions import Fraction
def decompose(n):
    answer=[]
    current_number=Fraction(n)
    if current_number>1:
        answer.append(str(current_number//1))
        current_number=Fraction(current_number-(current_number//1))
    if current_number==0:
        return answer
    x=2
    while True:
        if Fraction(1,x)<current_number:
            answer.append(str(Fraction(1,x)))
            current_number=Fraction(current_number-Fraction(1,x))
        if current_number.numerator==1:
            answer.append(str(current_number))
            break
        else:
            x=(current_number.denominator//current_number.numerator)+1           
    return answer
