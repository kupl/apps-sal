"""And who are you, the proud lord said,
That I must bow so low?
Only a cat of a different coat,
That's all the truth I know.
In a coat of gold or a coat of red,
A lion still has claws,
And mine are long and sharp, my lord,
As long and sharp as yours.
And so he spoke, and so he spoke,
That lord of Castamere,
But now the rains weep o'er his hall,
With no one there to hear.
Yes now the rains weep o'er his hall,
And not a soul to hear."""
import math
t = int(input())
for _ in range(t):
    z = input().split()
    x = int(z[0])
    r = int(z[1])
    a = int(z[2])
    b = int(z[3])
    length = 2 * math.pi * r
    if b > a:
        temp = a
        a = b
        b = temp
    first_meet = length / (a - b)
    total_time = x * length / a
    if first_meet == total_time:
        ans = 0
    else:
        ans = int(total_time / first_meet)
    print(ans)
