a=[1,7,2,4]
b=[]
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        c=a[i]+a[j]
        b.append(c)
        j=j+1
    i=i+1
print(b)

#  o/p:-[8,3,5,9,11,6]