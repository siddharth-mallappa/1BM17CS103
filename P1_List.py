lst=[]
lst2=[]

n=int(input("Enter the nunber of elements"))

for i in range (0,n):
	ele = int(input())
	lst.append(ele)
print(lst)

for i in  lst:
    if(i%2==0):
        lst2.append(i)

print(lst2)
