n = int(input())
s = input()

departures, arrivals = 0, 0

for _ in range(n):
    s1, s2 = input().split('->')
    if s1 == s:
        departures += 1
    if s2 == s:
        arrivals += 1

if departures != arrivals:
    print("contest")
else:
    print("home")
