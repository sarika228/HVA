a=[50,2,40,9,5,10]
i=0
max=0
min=a[0]
while i<len(a):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
    i=i+1
print(max)
print(min)