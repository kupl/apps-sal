# cook your dish here
import sys
import math


def main(arr):
    for i in range(1, len(arr) - 1):
        if arr[i] == arr[i - 1] and arr[i] == arr[i + 1]:
            return "Yes"
    return "No"


test = int(input())
for _ in range(test):
    b = int(input())
    arr = list(map(int, input().split()))
    print(main(arr))
