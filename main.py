some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
new_list = []

for item in some_list:
    i = some_list.count(item)
    if i != 1:

        if item not in new_list:
            new_list.append(item)

print(new_list)
