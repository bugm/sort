x = [2,2,4,3,5,8,1]
temp1 = []
max = x[0]
for each in x:
    temp1.append(-1)
    if each > max:
        max = each
temp2 = [0 for each in range(max+1)]
for each in x:
    temp2[each]+=1
for index in range(1,len(temp2)):
    temp2[index]+=temp2[index-1]
for each in x:
    temp1[temp2[each]-1] = each
    temp2[each]-=1
print (temp1)
