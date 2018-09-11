map = []
height= 4
wigth = 4
for each in range(height):
    temp = input()
    map.append([int(value) for value in temp.split(',')])
start = (1,1)
end = (2,2)
direction = [0]
path = [start]
temp = start
can = False
while temp!=end:
    last = len(direction)-1
    if direction[last]<4:
        direction[last]+=1
        canmove = 0
        if direction[last]==1 and temp[1]>0 and map[temp[0]][temp[1]-1]>0:
            map[temp[0]][temp[1] - 1]-=1
            temp = (temp[0],temp[1]-1)
            canmove = 1
        if direction[last]==2 and temp[0]<wigth-1 and map[temp[0]+1][temp[1]]>0:
            map[temp[0] + 1][temp[1]]-=1
            temp = (temp[0]+1,temp[1])
            canmove = 1
        if direction[last]==3 and temp[1]<height-1 and map[temp[0]][temp[1]+1]>0:
            map[temp[0]][temp[1] + 1]-=1
            temp = (temp[0],temp[1]+1)
            canmove=1
        if direction[last]==4 and temp[0]>0 and map[temp[0]-1][temp[1]]>0:
            map[temp[0] - 1][temp[1]]-=1
            temp = (temp[0]-1,temp[1])
            canmove=1
        if canmove:
            path.append(temp)
            direction.append(0)


    else:
        direction.pop(len(direction)-1)
        path.pop(len(path)-1)
        temp = path[len(path)-1]
        if len(path)==1:
            break

    if temp ==end:
        can = True

if can:
    print(path)
else:
    print('can not reach there')

