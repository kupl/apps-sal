import pdb


def gen_sig(arr):
    sig = ';'.join(map(str, arr))
    return sig


def solve(arr, cache):
    l = len(arr)
    cnt = 0
    for i in range(l - 1):
        if arr[i] > 0 and arr[i + 1] > 0:
            if i == l - 2:
                arr[i] -= 1
                arr[i + 1] -= 1
                arr.append(1)
                sig = gen_sig(arr)
                if (sig in cache) == False:
                    cache[sig] = 1
                    ret = solve(arr, cache)
                    if ret >= 0:
                        cnt += ret + 1
                arr.pop(-1)
                arr[i + 1] += 1
                arr[i] += 1
            else:
                arr[i] -= 1
                arr[i + 1] -= 1
                arr[i + 2] += 1
                sig = gen_sig(arr)
                if (sig in cache) == False:
                    cache[sig] = 1
                    ret = solve(arr, cache)
                    if ret >= 0:
                        cnt += ret + 1
                arr[i] += 1
                arr[i + 1] += 1
                arr[i + 2] -= 1
    return cnt


def __starting_point():
    T = int(input())
    for t in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        cache = {}
        cache[gen_sig(arr)] = 1
        solve(arr, cache)
        print(len(cache))


__starting_point()
