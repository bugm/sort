x = [2,5,8,7,-1,-2,2,2,3]
for i in range(1,len(x)):
    temp = x[i]
    j = i-1
    while j>=0 and x[j]>temp:
        x[j+1] = x[j]
        j=j-1
    x[j+1] = temp

print(x)