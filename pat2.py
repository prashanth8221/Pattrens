#inverted pyramid
r=int(input('enter row: '))
count=0
for i in range(r,0,-1):
    count+=1
    for j in range(1,i+1):
        print(count,end=' ')
    print('\r')