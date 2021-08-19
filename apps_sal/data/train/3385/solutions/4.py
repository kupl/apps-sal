import re


def longest(s):
    regex = 'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*'

    def group(x):
        return x.group()
    return max(map(group, re.finditer(regex, s)), key=len)
