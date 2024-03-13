def false(f,a,b,tol,n):
    if f(a)*f(b)>0:
        print("The method fails without any iteration ")
        return None
    i=0
    while(i<=n):

         p=(a*f(b)-b*f(a))/(f(b)-f(a))
         print("pass-",i," a=",a," b=",b," p=",p," f(p)=",f(p))
         if abs(f(p))<=tol:
             print("The solution is =",p)
             return None
         if f(p)<0:
             a=p
         else:
             b=p

         i=i+1
    print("The method fails")
    return None
f=lambda x:x**3-x-1
print("Take a :")
x=input()
a=int(x)
print("Take b :")
x=input()
b=int(x)
false(f,a,b,0.009,100)