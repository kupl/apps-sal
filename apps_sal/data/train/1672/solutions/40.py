from math import sqrt, pow

def f(x):
    sign = 1 if x > 0 else -1 if x < 0 else 0
    aresult = sqrt(abs(x))
    bresult = pow(x, 3)*5
    result = bresult + aresult
    # result *= sign
    return result

arr = []
for i in range(11):
    x = int(input())
    arr.append(x)

for x in reversed(arr):
    result = f(x)
    print(f"f({x}) = ", end="")
    if result >= 400:
        print("MAGNA NIMIS!")
    else:
        print(f"{result:.2f}")

