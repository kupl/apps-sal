x = [1, 2, 3, 4, 5, 6, 7]  # take list to check palindrome or not
for i in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))  # take list
    revli = li[::-1]  # reverse the list
    dupli = set(li)  # remove duplicates from list to compare order of         nos.
    if(li == revli and list(dupli) == x):  # check conditions
        print("yes")
    else:
        print("no")
