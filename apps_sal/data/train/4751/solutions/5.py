def deficiently_abundant_amicable_numbers(n1,n2):
    def check(n):
        temp = set([1])
        for j in range(2, int(n**0.5)+1):
            if n%j == 0:
                temp.add(j)
                temp.add(n//j)
        x = sum(temp)
        return x
    lst = ["abundant", "perfect", "deficient"]
    a1, a2 = check(n1), check(n2)
    ans1 = lst[0] if a1 > n1 else (lst[1] if a1==n1 else lst[2])
    ans2 = lst[0] if a2 > n2 else (lst[1] if a2==n2 else lst[2])
    return "{} {} {}".format(ans1, ans2, "amicable" if a1==n2 and a2==n1 and n1 != n2 else "not amicable")
