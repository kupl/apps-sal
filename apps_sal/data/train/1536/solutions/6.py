#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:03:29 2020

@author: shailesh
"""


def findD_and_start(A):
 first = A[1] - A[0]
 second = A[2] - A[1]
 third = A[3] - A[2]
 if first == second:
  return second,A[0]
 elif third == second:
  return third,A[3] - 3*third
 else:
  return (A[3] - A[0])//3,A[0]
T = int(input())

for t in range(T):
 N = int(input())
 A = [int(i) for i in input().split()]
 d,start = findD_and_start(A)
 
 s = ''
 if d ==0:
  for i in range(N):
   s+=str(start) + ' '
 else:
  for i in range(start,start + N*d,d):
   s+= str(i) + ' '
 print(s.strip())
