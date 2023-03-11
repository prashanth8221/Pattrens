#inverted descending pattren
r=int(input(''))
for i in range(r,0,-1):
    num=i
    for j in range(0,i):
        print(num,end=' ')
    print(' ')