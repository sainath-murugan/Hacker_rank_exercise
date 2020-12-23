#Find the Runner-Up Score!

input_1 = int(input())
list_1 = list(map(int, input().split(" ")))
none = None
for i in list_1:
    if none == None:
        none = i
    elif i > none:
        none = i
    else:
        continue
none_1 = None
for i in list_1:
    if i == none:
        continue
    elif none_1 == None:
        none_1 = i
    elif i > none_1:
        none_1 = i
    else:
        continue
print(none_1)


