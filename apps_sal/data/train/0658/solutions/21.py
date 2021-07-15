from sys import stdin
for __ in range(int(stdin.readline())):
    n, nums = int(stdin.readline()), list(map(int, stdin.readline().split()))
    longest = [1]*n  # First one is smaller
    opp_longest = [1]*n
    best = 1
    for i in range(n-2, -1, -1):

        if nums[i] <= nums[i+1]:
            if nums[i] == nums[i+1]:
                opp_longest[i] += longest[i+1]
            longest[i] += opp_longest[i+1]
            best = max(longest[i], best)
            if i + longest[i] < n:
                if longest[i] % 2:
                    best = max(best, longest[i] + longest[i + longest[i]])
                else:
                    best = max(best, longest[i] + opp_longest[i + longest[i]])
        else:
            opp_longest[i] += longest[i+1]
    print(max(best, opp_longest[0]) + 1)
