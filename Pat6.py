#inverted number pyramid
row=int(input('enter: '))
for i in range(1,row):
    for j in range(i,0,-1):
        print(j,end=' ')
    print(' ')