# cook your dish here
test_case = int(input())
for i in range(0, test_case):
    string = input()
    if (string.count("10") + string.count("01")) > 2:
        print("non-uniform")
    else:
        print("uniform")
