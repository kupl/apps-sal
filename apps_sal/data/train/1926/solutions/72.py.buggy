class Solution:
\tdef closestDivisors(self, num: int) -> List[int]:
\t\tfrom math import sqrt
\t\tdef factor(n):
\t\t\td = int(sqrt(n))
\t\t\tif d*d == n:
\t\t\t\treturn [d, d]
\t\t\tdefault = [1, n]
\t\t\tfor i in range(2, d+1):
\t\t\t\tx, m = divmod(n, i)
\t\t\t\tif not m:
\t\t\t\t\tdefault = [i, x]
\t\t\treturn default
\t\tx = factor(num+1)
\t\ty = factor(num+2)
\t\tif abs(x[0] - x[1]) < abs(y[0] - y[1]):
\t\t\treturn x
\t\treturn y


