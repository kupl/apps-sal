def solve(s):
    nums=[]
    num=''
    for letter in s+'k':
        if letter.isalpha():
            print(num, letter)
            if num !='':
                nums.append(int(num))
            num=''
        if letter.isalpha()==False:
            print(letter)
            num+=letter
    return max(nums)
