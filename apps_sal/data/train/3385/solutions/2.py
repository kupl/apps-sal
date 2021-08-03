import re


def longest(s):
    return max(re.findall(r'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*', s), key=len)
