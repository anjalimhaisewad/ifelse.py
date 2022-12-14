# n=4
# arr = [ [1 for x in range(n)] for x in range(n)]

# x=0
# y=0
# z=1

# for ot in range((n//2)+1):
#     if ot == n//2:
#         z-=1
    
#     for j in range(y,n-y):
#         arr[x][j] = z
#         z+=1
    
#     for i in range(x+1,n-x-1):
#         arr[i][n-y-1]=z
#         z+=1
    
#     for j in range(n-y-1,y-1,-1):
#         arr[n-x-1][j]=z
#         z+=1

#     for i in range(n-x-2,x,-1):
#         arr[i][y]=z
#         z+=1
    
#     x+=1
#     y+=1
# for a in range(n):
#     for b in range(n):
#         print("{:2d}".format(arr[a][b]),end=" ")
#     print()

# i=int(input("enter a number"))
# rev=0
# while i>0:
#     rev =(rev*10)+i%10
#     i=i//10
# print("reverse=",rev)   


# i=1
# while i<=3:
#     print("inner loop",i)
#     i+=1
#     j=1
#     while j<=5:
#         print("inner loop",j)
#         j+=1
# print("rest of the code")        
# =int(input("enter a number"))
# b=0
# p=1
# num
# n=num
# while n>0:
#     rem =n%2
#     b+=rem*p
#     p=p*10
#     n=n/2
#     print("binary valu:")




n=int(input("enter anumber"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(chr(64+j),end=" ")
        j=j+1
    print()    




