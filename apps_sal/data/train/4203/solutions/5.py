def caffeineBuzz(n):
    return ['mocha_missing!','Java','JavaScript','CoffeeScript'][sum([n%3==0,n%4==0,n%2==0])]
