n=int(input("enter a no"))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n//10
    print("sum of digits",sum)
