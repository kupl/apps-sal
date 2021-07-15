def solution(n):
    return "M" * (n//1000) + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]

