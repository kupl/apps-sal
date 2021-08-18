from collections import defaultdict


def fix_progression(arr):

    global_max = 1

    for i, ele in enumerate(arr):

        maxi = 1
        things = defaultdict(lambda: 1)

        for j in range(i + 1, len(arr)):

            comp = arr[j]
            diff = (comp - ele) / (j - i)

            if diff.is_integer():

                left = ele - diff * i
                right = ele + diff * (len(arr) - i - 1)

                things[(left, right)] += 1
                maxi = max(maxi, things[(left, right)])
                global_max = max(maxi, global_max)

    return len(arr) - global_max
