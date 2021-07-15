for _ in range(int(input())):
 n=int(input())
 s=input()
 uc=s.count('U')
 dc=s.count('D')
 lc=s.count('L')
 rc=s.count('R')
 ans=""
 if uc>dc:
  ans+="U"*(uc-dc)
 elif uc<dc:
  ans+="D"*(dc-uc)
 if lc>rc:
  ans+="L"*(lc-rc)
 elif lc<rc:
  ans+="R"*(rc-lc)
 print(n-len(ans))




