def hollow_triangle(n):
    w, result = 2 * n - 1, [f"{'_' * (2*i-1):#^{2*i+1}}" for i in range(n - 1)]
    return [f"{l:_^{w}}" for l in result] + ["#" * w]
