#reverse inverted pyramid
row=int(input('enter: '))
for i in range(row,0,-1):
    for j in range(0,i+1):
        print(j,end=' ')
    print(' ')