print('Enter the number of values :')
n=int(input())
print('Enter the value of x:')
arrx=[]
i=0
for i in range(n):
    arrx.append(float(input()))
    i=i+1
print('Enter the value of y:')
arry=[]
i=0
for i in range(n):
    arry.append(float(input()))
    i=i+1
print('Enter the value :')
value=float(input())
p=0
i=0
k=0
for i in range(n):
    l=1
    for k in range(n):
        if k!=i:
            l = l * (value - arrx[k]) / (arrx[i] - arrx[k])

        k+=1
    p=p+l*arry[i];
    i=i+1
print('The interpolation of ',value,' is ',p)


