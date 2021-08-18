from functools import lru_cache
__import__("sys").setrecursionlimit(2600)

fib = lru_cache(maxsize=None)(lambda n: n if n < 2 else fib(n - 1) + fib(n - 2))
fizz_buzz = lru_cache(maxsize=None)(lambda n: "FizzBuzz" if not n % 15 else "Buzz" if not n % 5 else "Fizz" if not n % 3 else n)
fibs_fizz_buzz = lru_cache(maxsize=None)(lambda n: ([] if n == 1 else fibs_fizz_buzz(n - 1)) + [fizz_buzz(fib(n))])
