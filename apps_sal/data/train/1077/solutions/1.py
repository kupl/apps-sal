# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 22:17:11 2012

@author: anant
"""

T = int(input())
for i in range(0,T):
    l = []
    l2 = []
    n = int(input())
    for j in range(0,n):
      l.append(input())
    length = len(l)
    word = l[length-1].split();
    direction = word[0]
    city = l[length-1][l[length-1].find("on")+3:]
    temp = "Begin on "+city
    l2.append(temp)
    for i in range(2,length+1):
      
      word = l[length-i].split();
      if direction == "Right":
        direction = "Left"
      else:
        direction = "Right"
      city = l[length-i][l[length-i].find("on")+3:]
      temp = direction + " on "+city
      l2.append(temp)
      
      direction = word[0]
     # l2.append(direction + "on" + l[length-i][])
     
    for sentence in l2:
      print(sentence)
    print("")
      
      
      
    

