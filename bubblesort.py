x= [10,9,2,1,3,4]
flag = True
last = len(x)
index = len(x)
while index >0:
    for each in range(0,index-1):
        if x[each] > x[each+1]:
            last = each + 1
            temp = x[each]
            x[each] = x[each+1]
            x[each+1] = temp
            flag = True
    index-=1
    if last < index:
        index = last
    last = 0
print (x)
