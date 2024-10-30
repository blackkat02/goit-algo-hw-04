def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def merge_k_lists(k_lists):
    if not k_lists:
        return []

    # Починаємо з 1-го списку, як left
    merged = k_lists[0]

    # Ітерація всіх списків з k_lists для подання як right
    for i in range(1, len(k_lists)):
        merged = merge(merged, k_lists[i])
        print(f"After merging {i + 1} lists : {merged}")

    return merged


lists = [[1, 4, 5], [1, 3, 4], [2, 6], [3, 5, 8], [0]]
result = merge_k_lists(lists)
print("Final merged list:", result)
