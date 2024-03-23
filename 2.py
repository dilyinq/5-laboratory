my_list = [21, 2, 1, 21, 8, 5, 9, 1]
duplicates = []
for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
if duplicates:
    print("Повторяющиеся элементы в списке:", duplicates)
else:
    print("В списке нет повторяющихся элементов.")