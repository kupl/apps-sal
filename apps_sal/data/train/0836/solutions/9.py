# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:28:56 2016

@author: Harry
"""
import collections
no_of_testcases = int(input())
for each in range(no_of_testcases):
    to_watch = []
    length = []
    rating = []
    no_of_movies = int(input())
    length = list(map(int, input().split()))
    rating = list(map(int, input().split()))
    for e in range(no_of_movies):
        l_x_r = length[e] * rating[e]
        to_watch.append(l_x_r)
    counter = collections.Counter(to_watch)
    test = max(counter.keys())
    if counter[test] > 1:
        rating_indexes = [0]
        i = 0
        for x in to_watch:
            if x == test:
                if rating[i] > rating_indexes[0]:
                    high_ratng = rating[i]
                    rating_indexes = [high_ratng]
            i = i + 1
        print(rating.index(high_ratng) + 1)
    else:
        print(to_watch.index(test) + 1)
