def ulam_sequence(u0, u1, n):
    print(u0, u1, n)
    ans, curr, seto = [u0, u1], u1 + 1, {u0, u1}
    while len(ans) < n:
        temp, ways = 0, 0
        for mo in ans:
            if curr - mo in seto and mo != (curr - mo):
                temp = curr
                ways += 1
                if ways > 2:
                    break
        if ways == 2:
            ans.append(temp)
            seto.add(temp)
        curr += 1
    return ans
