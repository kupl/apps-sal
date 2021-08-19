from collections import defaultdict


def fix_progression(arr):

    global_max = 1

    for i, ele in enumerate(arr):

        maxi = 1
        things = defaultdict(lambda: 1)  # dictionary to store the first and last elements of progression including arr[i]

        for j in range(i + 1, len(arr)):

            comp = arr[j]
            diff = (comp - ele) / (j - i)  # would be arithmetic progression constant between arr[i] and arr[j]

            if diff.is_integer():

                # calculate the first and last elements of the "would be" arithmetic progression

                left = ele - diff * i
                right = ele + diff * (len(arr) - i - 1)

                # if the same left and right exist already, that means the current left, right pair is the same
                # as a arithmetic progression seen for arr[i], meaning we have += 1 points sharing the arithmetic progression
                # eg [1, 10, 2, 12, 3, 14]. the pair 10,12 and 10,14 have the same left and right points, meaning they
                # are collinear and so thats one less point which we need to change in order to make arithmetic prog.

                things[(left, right)] += 1
                maxi = max(maxi, things[(left, right)])
                global_max = max(maxi, global_max)

    return len(arr) - global_max
