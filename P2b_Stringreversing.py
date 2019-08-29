my_string=str(input("Enter the string"))


split_result = my_string.split()

res = []
x = len(split_result) - 1
while x >= 0:
    res.append(split_result[x])
    x = x-1

result=" ".join(res)
print (result)
print(result[-1::-1])


