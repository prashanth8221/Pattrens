#NATURAL NUMBES IN A PATTREN
row=int(input('enter: '))
x=1
z=2
for i in range(row):
    for j in range(i,z):
        print(x,end=' ')
        x+=1
    print(' ')
    z+=2
