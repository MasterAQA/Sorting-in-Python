def shaker_sort(array):
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1

    while (swapped == True):

        swapped = False

        # проход слева направо
        for i in range(start_index, end_index):
            if (array[i] > array[i + 1]):
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        # если не было обменов прерываем цикл
        if (not (swapped)):
            break

        swapped = False

        end_index = end_index - 1

        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if (array[i] > array[i + 1]):
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start_index = start_index + 1


print("Шейкерная сортировка")
arr = []
length = int(input("Введите длину массива: "))
for i in range(0, length):
    element = int(input("arr[" + str(i + 1) + "] = "))
    arr.append(element)
shaker_sort(arr)
print("Отсортированный массив: ")
print(arr)