n = int(input());
if n % 2 == 0:
    print("NO");
else:
    ans = [];
    for i in range(2*n):
        ans.append(0);
    current = 1;
    for i in range(n):
        ans[i] = current if i % 2 == 0 else current+1;
        ans[n+i] = current+1 if i % 2 == 0 else current;
        current += 2;
    print("YES");
    for i in range(2*n):
        print("{} ".format(ans[i]), end='');
