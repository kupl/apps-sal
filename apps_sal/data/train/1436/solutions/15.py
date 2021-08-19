# cook your dish here
def isPalindrome(s):
    return(s == s[::-1])


t = int(input())
for i in range(t):
    word = input()
    if(isPalindrome(word)):
        print(1)
    else:
        print(2)
