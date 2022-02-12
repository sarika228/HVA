a=[4,4,1,3]
i=0
max=0
c=0
while i<len(a):
    if a[i]>max:
        max=a[i]
        a[i]=max
    if max==a[i]:
        c=c+1
    i=i+1
print(max)
print(c)
