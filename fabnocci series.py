p=int(input())
a=0
b=1
sum=0
print(a)
print(b)
for i in range(3,p+1):
    sum=a+b
    a=b
    b=sum
    print(sum)