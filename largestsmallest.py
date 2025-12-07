l=[4,5,1,2,9,7,10,8]
print("The original list",l)
sum=0
for i in l:
    sum+=i
avg=sum/len(l)
print("Sum =",sum)
print("Average =",avg)
l.sort()
print(l)
print("The smallest element is",l[0])
print("The Largest element is",l[-1])
