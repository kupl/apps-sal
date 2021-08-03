from collections import Counter
for _ in range(int(input())):
    data = input()
    each_char_count = Counter(data)
    count_ = 0
    status = False
    for i in each_char_count:
        if each_char_count[i] % 2 != 0:
            count_ += 1
        if count_ > 2:
            status = True
            break
    if status == False:
        print("YES")
    else:
        print("NO")
