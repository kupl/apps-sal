def solution(stones):
    # Do some magic
    num = 0
    for i in range(len(stones) - 1):
        if stones[i] == stones[i + 1]:
            num += 1

    return num
#     if stones[0] == stones[1]:
#         stones.replace(stones[1], '', 1)
#     print(stones)
