# cook your dish here
n=int(input())
d={"B":"BattleShip",
"C" :	"Cruiser",
"D" : 	"Destroyer",
"F" : 	"Frigate"}
for i in  range(n):
    m=input().upper()
    print(d[m])

