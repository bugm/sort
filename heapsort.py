#小顶堆
def heap_adjust(type,x,i,j):  #type 表示堆的类型，小于零为小顶堆
    if type<0:
        while 2 * i + 1 < j:
            tempindex = 2 * i + 1
            if tempindex + 1 < j and x[tempindex + 1] < x[tempindex]:
                tempindex += 1
            if x[i] > x[tempindex]:
                tempnumber = x[i]
                x[i] = x[tempindex]
                x[tempindex] = tempnumber
                i = tempindex
            else:
                break
    else:
        while 2 * i + 1 < j:
            tempindex = 2 * i + 1
            if tempindex + 1 < j and x[tempindex + 1] > x[tempindex]:
                tempindex += 1
            if x[i] < x[tempindex]:
                tempnumber = x[i]
                x[i] = x[tempindex]
                x[tempindex] = tempnumber
                i = tempindex
            else:
                break



def heap_sort(heaptype,x):
    for each in range(int(len(x)/2)-1,-1,-1):
        print(each)
        heap_adjust(heaptype,x,each,len(x))
    for index in range(len(x)-1,0,-1):
        temp = x[index]
        x[index] = x[0]
        x[0] = temp
        heap_adjust(heaptype,x,0,index)
    return x

test = [2,3,5,4,1]
heaptype = int(input("input the type of heap:"))
sorted_test = heap_sort(heaptype,test)
if heaptype <0 :
    sorted_test.reverse()
print(sorted_test)

