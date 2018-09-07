x= [15,200,18,19,50,55]
max = x[0]
for each in x:
    if each >max:
        max = each
result = [0 for each in x]
bucket = []
for each in range(10):
    bucket.append([])
k = 10