"""
Problem Statement: https://www.codechef.com/COMT2020/problems/BHPORSRP
Author: striker
"""


def main():
    for _ in range(int(input().strip())):
        college_name = input().strip().lower()
        if "berhampore" in college_name and "serampore" in college_name:
            print("Both")
        elif "berhampore" in college_name:
            print("GCETTB")
        elif "serampore" in college_name:
            print("GCETTS")
        else:
            print("Others")


def __starting_point():
    main()


__starting_point()
