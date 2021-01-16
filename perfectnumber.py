n=int(input("Enter a number to check if it is perfect number or not: "))
sum=0
for x in range(1,n):
    if n%x==0:
        sum=sum+x
if(sum==n):
    print(n," is a perfect number")
else:
    print(n," is not a perfect number")