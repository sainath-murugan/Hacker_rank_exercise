#Nested Lists

list_1 = []
input_1 = int(input())
for i in range(1, input_1+1):
    name_input = input()
    mark_input = float(input())
    total = [name_input, mark_input]
    list_1.append(total)
smallest = None
for elements in list_1:
    if smallest == None:
        smallest = elements[1]
        value = elements
    elif elements[1] < smallest:
        smallest = elements[1]
smallest_1 = None
for elements in list_1:
    if smallest == elements[1]: # "is" is not working
        pass
    elif smallest_1 == None:
        smallest_1 = elements[1]
    elif smallest_1 > elements[1]:
        smallest_1 = elements[1]
list_1.sort()
for item in list_1:
    if smallest_1 == item[1]:  # "is" is not working
        print(item[0])
