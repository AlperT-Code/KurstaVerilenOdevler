import random

list1 = [random.randint(1, 50) for _ in range(10)]
list2 = [random.randint(1, 50) for _ in range(10)]

combined_list = list1 + list2

unique_combined_list = list(set(list1 + list2))

common_elements = list(set(list1) & set(list2))

unique_elements = list(set(list1) ^ set(list2))

min_max_list = [min(list1), max(list1), min(list2), max(list2)]

print("Liste 1:", list1)
print("Liste 2:", list2)
print("Birleşik Liste:", combined_list)
print("Tekrarsız Birleşik Liste:", unique_combined_list)
print("Ortak Öğeler:", common_elements)
print("Benzersiz Öğeler:", unique_elements)
print("Min ve Max Değerler:", min_max_list)
