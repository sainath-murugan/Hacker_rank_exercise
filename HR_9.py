#Lists


list_1 = []
input_1 = int(input())
j = 0
while j < input_1:
  [*store] = input().split(" ")
  
  if store[0] == "insert":
   list_1.insert(int(store[1]),int(store[2]))

  elif store[0] == "remove":
   list_1.remove(int(store[1]))

  elif store[0] == "sort":
     list_1.sort()
     
  elif store[0] == "append":
      list_1.append(int(store[1]))
      
  elif store[0] == "pop":
     list_1.pop()
     
  elif store[0] == "reverse":
     list_1.reverse()
     
  elif store[0] == "print":
      print(list_1)
  j = j+1

