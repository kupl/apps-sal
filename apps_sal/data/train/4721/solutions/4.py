convert_temp = lambda z, s, d: int(round({
'C':lambda z:z-273.15,
'F':lambda z:z*9/5-459.67,
'K':lambda z:z,
'R':lambda z:z*9/5,
'De':lambda z:(373.15-z)*3/2,
'N':lambda z:(z-273.15)*33/100,
'Re':lambda z:(z-273.15)*4/5,
'Ro':lambda z:(z-273.15)*21/40+7.5
}[d]({
'C':lambda z:z+273.15,
'F':lambda z:(z+459.67)*5/9,
'K':lambda z:z,
'R':lambda z:z*5/9,
'De':lambda z:373.15-z*2/3,
'N':lambda z:z*100/33+273.15,
'Re':lambda z:z*5/4+273.15,
'Ro':lambda z:(z-7.5)*40/21+273.15
}[s](z))))
