D = {0: [1, 4, 5], 1: [0, 2, 6], 2: [1, 3, 7], 3: [2, 4, 8], 4: [0, 3, 9], 5: [0, 7, 8], 6: [1, 8, 9], 7: [2, 5, 9], 8: [3, 5, 6], 9: [4, 6, 7]}
E = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
for _ in range(eval(input())):
    S = input()
    solved = False
    for i in range(10):
        if not solved:
            if E[i] == S[0]:
                solved = True
                ans = str(i)
                for x in S[1:]:
                    for y in D[int(ans[-1])]:
                        if E[y] == x:
                            ans += str(y)
                            break
                    else:
                        solved = False
    if solved:
        print(ans)
    else:
        print(-1)
