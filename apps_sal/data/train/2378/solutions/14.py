from collections import Counter
T = int(input())
for t in range(T):
    C = Counter(input())
    left_right_min = min(C["L"], C["R"])
    up_down_min = min(C["U"], C["D"])
    if left_right_min == 0 and up_down_min == 0:
        print(0)
        print()
    elif left_right_min == 0:
        print(2)
        print("UD")
    elif up_down_min == 0:
        print(2)
        print("LR")
    else:
        print((left_right_min+up_down_min)*2)
        print(("L"*left_right_min+"D"*up_down_min +
              "R"*left_right_min+"U"*up_down_min))

