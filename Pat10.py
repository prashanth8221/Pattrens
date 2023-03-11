num=int(input('enter: '))
for i in range(0,num):
    for j in range(num,i,-1):
        print(j,end=" ")
    print(' ')
    for i in range(num):
        print(i,end=' ')