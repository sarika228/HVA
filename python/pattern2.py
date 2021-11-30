n=int(input("enter a size:"))

for i in range(1,n+1):
    if i%2!=0:
        for j in range(0,n+1):
            if j==n:
                print(i+1,end=" ")
            else:
                print(i,end=" ")
    else:
        for j in range(0,n+1):
            if j==0:
                print(i+1,end=" ")
            else:
                print(i,end=" ")  
    print()
