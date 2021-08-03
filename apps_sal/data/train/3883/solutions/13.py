def solve(s):
    count1 = [sum(1 for i in s if i in "aeiou"), "".join(sorted(i for i in s if i in "aeiou"))]
    count2 = [sum(1 for i in s if i not in "aeiou"), "".join(sorted(i for i in s if i not in "aeiou"))]
    if abs(count1[0] - count2[0]) >= 2:
        return "failed"
    if len(count1[1]) == len(count2[1]):
        return "".join(i + j for (i, j) in zip(count1[1], count2[1]))
    elif len(count1[1]) > len(count2[1]):
        return "".join(i + j for (i, j) in zip(count1[1], count2[1])) + count1[1][-1]
    else:
        return "".join(i + j for (i, j) in zip(count2[1], count1[1])) + count2[1][-1]
