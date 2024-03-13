import math
def newton(f,f1,p0,tol,no):
    i=0
    print('  n','        p0 ','        p-p0')
    while(i<=no):
        p=p0-f(p0)/f1(p0)
        if(abs(p-p0))<tol:
            print('The solution is ',format(p,'5.5f'))
            return None
        print(format(i,'3d'),'      ',format(p0,'5.5f'),'     ',format(abs(p-p0),'5.5f'))
        i=i+1
        p0=p
    print('Program finished without no iteration')
    return None
f=lambda x:math.cos(x)-x
f1=lambda x:-math.sin(x)-1
newton(f,f1,math.pi/4,0.000001,20)

