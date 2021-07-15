N, L = map(int, input().split())
text_list = [input() for _ in range(N)]

sorted_list = sorted(text_list)

print(''.join(sorted_list))
