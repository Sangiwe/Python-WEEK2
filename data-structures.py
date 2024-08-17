my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.remove(70)
index = my_list.index(30)
print("Index Of 30 is:", index)
print(my_list)