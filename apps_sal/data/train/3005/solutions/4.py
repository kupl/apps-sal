fib = [1,2]
for _ in range(1000): fib.append(fib[-2]+fib[-1])
def f(n): return fib[n]-1
