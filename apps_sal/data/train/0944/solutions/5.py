def splitting(arr):
    if len(arr) == len(set(arr)):
        return 0
    ev_od = {}
    occur = {}
    ans = 0
    for i, n in enumerate(arr):
        if i == 0:
            ev_od[i] = [0, 0, 0]
        else:
            if arr[i - 1] & 1 == 1:
                ev_od[i] = [ev_od[i - 1][0], ev_od[i - 1][1] + 1, ev_od[i - 1][2] + arr[i - 1]]
            else:
                ev_od[i] = [ev_od[i - 1][0] + 1, ev_od[i - 1][1], ev_od[i - 1][2] + arr[i - 1]]
        if n in occur:
            if n & 1 == 1:
                num_of_odd = ev_od[i][1] - ev_od[occur[n]][1] - 1
                if num_of_odd & 1 == 1:
                    tmp_sum = ev_od[i][2] - ev_od[occur[n]][2] - n
                else:
                    tmp_sum = 0
            else:
                num_of_even = ev_od[i][0] - ev_od[occur[n]][0] - 1
                if num_of_even & 1 == 0:
                    tmp_sum = ev_od[i][2] - ev_od[occur[n]][2] - n
                else:
                    tmp_sum = 0
            ans = max(ans, tmp_sum)
        occur[n] = i
    return ans


try:
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(splitting(arr))
except:
    pass
