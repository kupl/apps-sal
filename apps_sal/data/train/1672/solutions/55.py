import math
arrInput = []
for i in range(11):
    inp = int(input())
    arrInput.append(inp)
arrReverse = list(reversed(arrInput))
for item in arrReverse:
    a = math.sqrt(abs(item))
    b = item * item * item * 5
    res = a + b
    if res > 400:
        print(f"f({item}) = MAGNA NIMIS!")
    else:
        formattedRes = '{:.2f}'.format(res)
        print(f"f({item}) = {formattedRes}")
