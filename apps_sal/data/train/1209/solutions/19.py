for _ in range(int(input())):
    v1, t1, v2, t2, v3, t3 = map(int, input().split())
    ans = "NO"
    if(t3 >= t1 and t3 <= t2 and v3 <= v1 + v2):
        T = (t3 - t1) / (t2 - t1)
        vy = v3 * T  # New Volume
        vx = v3 - vy
        if vx <= v1 and vy <= v2:
            ans = "YES"
    print(ans)
