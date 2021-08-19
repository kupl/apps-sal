from math import sqrt
nums = []
for i in range(11):
    nums.append(int(input()))
nums.reverse()
for i in nums:
    neg = i < 0
    a = sqrt(abs(i))
    b = i ** 3
    b *= 5
    if not 400 < a + b:
        print('f(' + str(i) + ') = {:0.2f}'.format(a + b))
    if 400 < a + b:
        print('f(' + str(i) + ') = MAGNA NIMIS!')
