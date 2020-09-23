def gcd(m,n):
    fm=[]
    for i in range (1,m+1):
        if (m%i) == 0 :
            fm.append(i)
    
    fn=[]
    for j in range (1,n+1):
        if(n%j) == 0:
            fn.append(j)
    
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
    
    return (cf[-1])
num1 = input("input first number")
num2 = input("input second number")
num3 = gcd(int(num1),int(num2))
print(num3)