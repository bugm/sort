import collections
x = [4,4,1,1,1,1,2,2,2,3,3]
counter = collections.Counter(x)
print (counter.most_common(3))
print(sorted(counter))
print(sorted(counter.elements()))
for each in counter.items():
    print(each)
x= [1,2,3,4]

temp = (1,2)
temp[0] +=1
print(temp)
