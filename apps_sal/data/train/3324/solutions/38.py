def sale_hotdogs(n):
    return 100 * n if 0<n<5 else 95 * n if 5<=n<10 else 90 * n if n>=10 else 0
