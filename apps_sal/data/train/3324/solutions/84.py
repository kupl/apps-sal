def sale_hotdogs(n):

    return (n * 100) * (n < 5) + (n * 95) * (n >= 5 and n < 10) + (n * 90) * (n >= 10)
