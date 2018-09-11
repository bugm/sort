def merge(first,second):
    temp = []
    f_index = 0
    s_index = 0
    while f_index < len(first) and s_index < len(second):
        if first[f_index] > second[s_index]:
            temp.append(second[s_index])
            s_index += 1
        else:
            temp.append(first[f_index])
            f_index += 1
    if f_index< len(first):
       temp.extend(first[f_index:])
    if s_index < len(second):
        temp.extend(second[s_index:])
    return temp
#recursion
def mergesort(x,l,r):
    if l<r:
        mid = int((l+r)/2)
        mergesort(x,l,mid)
        mergesort(x,mid+1,r)
        a = x[l:mid]
        b = x[mid:r]
        c = merge(x[l:mid],x[mid:r])
        x[l:r] = merge(x[l:mid],x[mid:r])

x= [1,4,5,2,3,2]
length = 1
while length<len(x):
    left = 0
    while left+length<len(x):
        right = left+2*length if left+2*length<len(x) else len(x)
        mid = left+length
        x[left:right] = merge(x[left:mid],x[mid:right])
        left = right
    length*=2
print (x)



