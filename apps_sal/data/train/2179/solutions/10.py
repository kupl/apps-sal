cur, att_first, att_second = map(int, input().split())


input()
l = list(map(int, input().split()))

moneys = 0
for x in l:
    if att_first < x < att_second:
        moneys += 1
print(moneys)
