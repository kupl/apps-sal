def max_tri_sum(numbers):
    ans = []
    numbers.sort(reverse=True)
    for x in numbers:
        if x not in ans:
            ans.append(x)
    return sum(ans[:3])
