#Finding the percentage



dict_1 = {}
input_1 = int(input())
for i in range(input_1):
    input_2 = list(map(str, input().split(" ")))
    input_3 = list(map(float, input_2[1:]))
    dict_1.update({input_2[0]: input_3})
input_4 = input()
evaluation = dict_1[input_4][0] + dict_1[input_4][1] + dict_1[input_4][2]
total = evaluation / 3
total_2 = "%.2f" % total
print(total_2)
