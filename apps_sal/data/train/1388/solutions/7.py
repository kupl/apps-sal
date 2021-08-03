# cook your dish here
# cook your dish here
N = int(input())
while(N):
    income = int(input())
    tax = 0
    if income <= 250000:
        tax = 0
    if income > 250000 and income <= 500000:
        tax += (income - 250000) * 0.05
    elif income > 500000:
        tax += 12500
    if income > 500000 and income <= 750000:
        tax += (income - 500000) * 0.10
    elif income > 750000:
        tax += 25000
    if income > 750000 and income <= 1000000:
        tax += (income - 750000) * 0.15
    elif income > 1000000:
        tax += 37500
    if income > 1000000 and income <= 1250000:
        tax += (income - 1000000) * 0.2
    elif income > 1250000:
        tax += 50000
    if income > 1250000 and income <= 1500000:
        tax += (income - 1250000) * 0.25
    elif income > 1500000:
        tax += 62500
    if income > 1500000:
        tax += (income - 1500000) * 0.30
    print(int(income - tax))
    N -= 1
