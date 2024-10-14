def binary_search(arr, x):
    iterations = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return iterations, arr[low] if low < len(arr) else None

# Приклад вхідного відсортованого масиву з дробовими числами
arr = [0.1, 0.5, 1.3, 2.7, 3.5, 5.8, 8.2, 10.6]

# Шукане значення
x = 2.5

# Виклик функції binary_search
iterations, upper_bound = binary_search(arr, x)

# Виведення результатів
print("Кількість ітерацій:", iterations)
if upper_bound is not None:
    print("Верхня межа:", upper_bound)
else:
    print("Елемент, більший або рівний заданому значенню, не знайдено.")