n=int(input("enter anumber:"))
i=2
while i<=n-1:
    if n%i==0:
        break
    i+=1
    if i==n:
        print("prim ")
else:print("not primeS") 