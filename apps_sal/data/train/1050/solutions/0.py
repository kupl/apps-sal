# cook your dish here
t = int(input())
for j in range(t):
    s = input()
    st = []
    ans = 0

    for i in range(len(s)):

        if(s[i] == '>'):
            if(len(st) != 0 and st[-1] == '<'):
                st.pop()
                if(len(st) == 0):
                    ans = i + 1
            else:
                break

        else:
            st.append('<')

    print(ans)
