brr=[]
n=list(map(int,input().split()))
p=int(input("enter the no. of rotation"))
brr=n[len(n)-p:]
n=n[:len(n)-p]
brr=brr[::-1]
print(brr)
n=n[::-1]
for i in brr:
    n.append(i)
n=n[::-1]
print("after Right rotation using reversal algo.",n)
