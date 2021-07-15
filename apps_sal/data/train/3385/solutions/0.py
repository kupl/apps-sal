import re

reg = re.compile('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*')

def longest(s):
    return max(reg.findall(s), key=len)
