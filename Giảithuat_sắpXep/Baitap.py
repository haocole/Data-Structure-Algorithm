A = [44, 55, 12, 42, 94, 18, 30, 67]

# 1. SELECTION SORT
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        m_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[m_idx]: m_idx = j
        arr[i], arr[m_idx] = arr[m_idx], arr[i]
    return arr

# 2. INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 3. BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Kết quả Selection:", selection_sort(A.t))
print("Kết quả Insertion:", insertion_sort(A.t))
print("Kết quả Bubble:", bubble_sort(A.t))