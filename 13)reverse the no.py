# n=12345
# rev=0
# while n>0:
#     a=n%10
#     rev=rev*10+a
#     n=n//10
# print(rev)
# 0/p:54321


n=int(input("enter number"))
rev=0
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
print(rev)