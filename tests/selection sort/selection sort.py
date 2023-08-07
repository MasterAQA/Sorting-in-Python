def swap(arr, a, b):
    """ переставляем элементы a и b в массиве """
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    # возвращаем массив

def selection_sort(self, unsorted, n):
    # итерируемся по массиву
    for i in range(0, n):

        # инициализируемся первым значеним
        current_min = unsorted[i]

        # инициализируем минимальный индекс
        min_index = i

        # итерируемся по оставшимся элементам массива
        for j in range(i, n):

            # проверяем, если j-тое значение меньше текушего минимального
            if unsorted[j] < current_min:
                # обновляес минимальные значение и индекс
                current_min = unsorted[j]
                min_index = j

        # меняем i-тое и j-тое значения
        swap(unsorted, i, min_index)

