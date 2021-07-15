def pattern(n):
    quarters = ("".join(str(j %10) if j == i else " " for j in range(1, n)) for i in range(1, n))
    half = "\n".join(f"{quarter} {quarter[::-1]}" for quarter in quarters) + "\n" + " " * (n - 1)
    return f"{half}{n % 10}{half[::-1]}" if n > 1 else "1" if n > 0 else ""
        

