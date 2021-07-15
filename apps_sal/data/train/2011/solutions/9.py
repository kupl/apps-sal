def main():
    n = int(input())
    results = foo(n)
    print(len(results))
    for i in results:
        print(i)


def foo(n):
    results = []
    min_border = n - len(str(n)) * 9

    for i in range(max(min_border, 0), n):
        if i + sum_of_digits(i) == n:
            results.append(i)
    return results


def sum_of_digits(n, result=0):
    while n > 0:
        result += (n % 10)
        n = n // 10
    return result


def test1():
    assert foo(21) == [15]


def test2():
    assert foo(20) == []


def test3():
    foo(1000000)


def __starting_point():
    main()

__starting_point()
