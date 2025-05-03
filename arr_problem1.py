arr=[2,7,-1,4,-2,-9,0,3,-6,5]
a=[x for x in arr if x<0]
b=[y for y in arr if y>=0]
print(arr)
a.sort()
b.sort()
print(a)
print(b)

