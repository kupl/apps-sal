ns, x, y = list(map(int, input().split()))
shifts = list(map(int, input().split()))
dis = 0.02 * y
shift_amt = [x + y] + [(x + (y - (i * dis))) for i in range(1, 6)]

amt = 0
for sn in shifts:
    amt += shift_amt[sn - 1]

if(amt < 300):
    print("NO", end="")
else:
    print("YES", end="")
