def caffeineBuzz(n):
    a = ['mocha_missing!'] * 12
    a[::3] = ['Java'] * 4
    a[::6] = ['CoffeeScript', 'JavaScript']
    return a[n % 12]
