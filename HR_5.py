#List Comprehensions



list_1 = []
x = int(input())
y = int(input())
z = int(input())
n = int (input())
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:

                list_1.append([i, j, k])
print(list_1)

