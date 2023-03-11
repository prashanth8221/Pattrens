#inverted same digit number
number=int(input('enter number: '))
row=number
for i in range(row,0,-1):
    for j in range(0,i):
        print(number,end=' ')
    print(' ')

