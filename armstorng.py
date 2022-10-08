
n=int(input("Enter the number"))
s=0
t=n
while n>n:
    r=n%10
    s=s+pow(r,3)
    n=n//10
if t==s:
    print("Armstrong")
def armstorng(n):
    s=0
    t=n
    while n>0:
          r=n%10
          s=s+pow(r,3)
          n=n//10
    if t==s:
        print("Armstrong")
    else:
        print("Not armstrong")
