def q():
    test=int(input())
    while(test>0):
        ip=int(input())
        st=input()
        l=list(st)
        flg=-1;i=0
        vowel={'A','E','I','O','U'}
        if ip is 1:
            print('No')
        else:
            while i<ip:
                if (l[i] in vowel and l[i+1]in vowel):
                    flg=0
                    break
                else:
                    flg=1
                i+=1
            if l[ip-1] in vowel and l[0] in vowel:
                flg=0
            if flg is 0:
                print('Yes')
            else:
                print('No')
        test-=1

q()

