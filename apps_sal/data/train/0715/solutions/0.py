s = input().strip()
start_w = 27
w_dict = {}
words = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for word in words:
    w_dict[word] = start_w
    start_w = start_w - 1

total_wt = 0
for c in s:
    total_wt = total_wt + w_dict[c]

print(total_wt)
