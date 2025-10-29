List = [1, 5, 3, 2]
print("Original List:", List)

n = len(List)

# Bubble Sort Logic
for i in range(n):
    for j in range(n - i - 1):
        if List[j] > List[j + 1]:
            # Swap if the current element is greater than the next
            List[j], List[j + 1] = List[j + 1], List[j]

    print(f"After pass {i+1}: {List}")

print("Sorted List:", List)
