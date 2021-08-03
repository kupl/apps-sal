T = int(input())
for t in range(T):
    my_str = input()
    unique_list = []
    for ch in my_str:
        if ch not in unique_list:
            unique_list.append(ch)
    print(len(unique_list))
