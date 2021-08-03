def deficiently_abundant_amicable_numbers(n1, n2):
    d1, d2 = (sum(d for d in range(1, n // 2 + 1) if n % d == 0) for n in (n1, n2))
    perf = " ".join("abundant" if n < d else "deficient" if d < n else "perfect" for (n, d) in ((n1, d1), (n2, d2)))
    is_amic = "" if n1 != n2 and (n1, n2) == (d2, d1) else "not "
    return f"{perf} {is_amic}amicable"
