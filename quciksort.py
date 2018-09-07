def quicksort(x,l,r):
    temp = x[l]
    origil = l
    origir = r
    while l<r:
        while x[r] > temp and l<r:
            r-=1
        if(l<r):
            x[l] = x[r]
            l+=1
        while x[l] < temp and l<r:
            l+=1
        if(l<r):
            x[r] = x[l]
            r-=1
    x[l] = temp
    if l-1>origil:
        quicksort(x,origil,l-1)
    if r+1 < origir:
        quicksort(x,r+1,origir)
x = [-3,-3,-3,-1,-2,23,23,123,1232,1,4,5,6,7,-3,-3]
quicksort(x,0,len(x)-1)
print(x)

