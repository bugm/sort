x = [3,2,1,-1,-2,4,6,7]
for i in range(0,len(x)-1):
    min = x[i]
    minindex = i
    for j in range(i+1,len(x)):
        if x[j] < min:
            min = x[j]
            minindex = j
    temp = x[i]
    x[i] = min
    x[minindex] = temp
print (x)


