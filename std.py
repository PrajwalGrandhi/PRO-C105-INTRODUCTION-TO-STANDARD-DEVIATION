import csv
import math

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    data_len=len(data)
    total=0
    for i in data:
        total+=int(i)
    mean=total/data_len
    return mean

sq_list=[]

for num in data:
    a=int(num)-mean(data)
    a=a**2
    sq_list.append(a)

sum=0
for i in sq_list:
    sum+=i

result=sum/(len(data)-1)
std=math.sqrt(result)

print(std)
