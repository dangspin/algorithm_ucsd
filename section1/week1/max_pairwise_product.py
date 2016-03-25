## This work calculate the maximum pairwise product for a given array, which has elements bigger than 
## two. It is allowed to have identical elements in the array.

## raw input and convert it to list
n = int(raw_input())
data = [int(x) for x in raw_input().split()]
assert(len(data)==n)

result = 0

## the maximum value
max_index=0
for i in range(len(data)):
    if data[i]>=data[max_index]:
        max_index=i

## the second maximum value
max_index2=max_index-1
for j in range(len(data)):
    if j!=max_index and data[j]>=data[max_index2]:
        max_index2=j

## pairwise product
result=data[max_index]*data[max_index2]

print result
