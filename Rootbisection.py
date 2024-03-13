def bisec(f, a, b, tol, no ):
    if f(a)*f(b)>0:
        print('The process failed without any iteration')
        return Noneone;
    i=0
    FA=f(a)
   # print('     n','      a','     b','      p ','      f(p)')
    while(i<no):
        p = (a+b)/2

        FP=f(p)
        print('  n=  ',i,'   a= ',a,'   b=  ',b,'   p=  ',p,'   f(p)=  ',f(p))
        if  abs(f(p))<tol:
            print('the solution is ',p)
            return None
        i=i+1
        if FA*FP>0:
            a=p
            FA=FP
        else:
            b=p
    print('The process failed without any iteration')
    return None
f=lambda x:x**3+4*x**2-10
bisec(f,1,2,0.000001,40)
