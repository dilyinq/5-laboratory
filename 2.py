def zud (list):
    unique_elems = []
    for elem in list:
        if elem in unique_elems:
            print(f"Повторяющийся элемент: {elem}")
            break
        unique_elems.append(elem)
    else:
        print("Повторяющиеся элементы отсутствуют")
my_list = [21, 7, 3, 9, 5, 3, 9, 7, 1]
zud (my_list)