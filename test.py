import collections
x = [4,4,1,1,1,1,2,2,2,3,3]
counter = collections.Counter(x)
print (counter.most_common(3))
print(sorted(counter))
print(sorted(counter.elements()))
for each in counter.items():
    print(each)
x= [1,2,3,4]

print (x[1:1])
print (x[3:4])
