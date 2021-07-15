# cook your dish here

d = { 'D': 238, 'T': 244, 'M': 138, 'B': 279, 'C': 186 }

s = list(input())
totalCal = 0

for i in range(len(s)):
    if s[i] == 'D':
        totalCal += d['D']
    if s[i] == 'T':
        totalCal += d['T']
    if s[i] == 'M':
        totalCal += d['M']
    if s[i] == 'B':
        totalCal += d['B']
    if s[i] == 'C':
        totalCal += d['C']

R = totalCal // 50
Rm = totalCal % 50
C = Rm // 5
Cm = Rm % 5
x = totalCal - (R * 50 + C * 5)
# print(totalCal - R * 50 + C * 5)
W = int(x * 4 * 0.5)
# print(R * 50 + C * 5 + W * 0.5)
print(R)
print(C)
print(W)
