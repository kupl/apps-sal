'''Large inputs are given because if you use a list comprehension iteration approach'''
#then your asymptomatic runtime will exceed the server threshold to stop the request
#Instead, treat this as a math problem to allow it to maintain 0(1)
def odd_count(n):
    return (n-1)/2 if n%2!=0 else n/2
