#! /usr/bin/env python

from math import ceil as ceil

def parent(index):
 return int(ceil(index / 2) - 1);

while True:
 length = int(input());

 if length == 0:
  break;

 numbers = input().split();
 tree = [0] * len(numbers);

 for i in range(0, len(numbers)):
  tree[i] = int(numbers[i]);

 lastIndex = len(tree) - 1;

 if lastIndex & 1:
  tree[parent(lastIndex)] = tree[parent(lastIndex)] * tree[lastIndex];
  --lastIndex;

 for i in range(lastIndex, 0, -2):
  parentIndex = parent(i);
  tree[parentIndex] = max(tree[parentIndex] * tree[i], 
            tree[parentIndex] * tree[i - 1]);

 print((tree[0] % 1000000007));

