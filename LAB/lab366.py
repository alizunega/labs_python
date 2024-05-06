my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list.sort()

list_def = []

for i in range(len(my_list)):
    if i+1 < len(my_list):
        if my_list[i] != my_list[i+1]:
            list_def.append(my_list[i])
    elif list_def[-1] != my_list[-1]:
        list_def.append(my_list[-1])  
        
print("La lista con elementos únicos:" ,list_def)
print(my_list)

