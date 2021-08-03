T = int(input())

for i in range(T):
    x = input().replace("=", "")
    max_right = 0
    max_left = 0
    curr_right = 0
    curr_left = 0
    right = False
    left = False

    for j in x:
        if j == ">":
            curr_right += 1
            if not right:
                right = True

            if left:
                left = False
                if max_left < curr_left:
                    max_left = curr_left

                curr_left = 0

        elif j == "<":
            curr_left += 1
            if not left:
                left = True

            if right:
                right = False
                if max_right < curr_right:
                    max_right = curr_right

                curr_right = 0

    if curr_left > max_left:
        max_left = curr_left
    if curr_right > max_right:
        max_right = curr_right

    print(max(max_right, max_left) + 1)
