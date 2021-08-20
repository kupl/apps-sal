def S(n):
    return n * (n + 1) // 2


string = input()
string_list = string.split()
(a, b) = (int(string_list[0]), int(string_list[1]))
itog = S(b - 1) * (S(a) * b + a)
itog = int(itog % 1000000007)
print(itog)
