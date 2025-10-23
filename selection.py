# Selection Sort Algorithm

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # نفترض أن العنصر الحالي هو الأصغر
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # نبدّل بين العنصر الأصغر والعنصر الحالي
        arr[i], arr[min_index] = arr[min_index], arr[i]

# مثال للتجربة
numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print("بعد الترتيب:", numbers)
