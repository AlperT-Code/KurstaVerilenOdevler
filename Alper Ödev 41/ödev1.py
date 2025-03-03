def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def merge_lists(*lists):
    return [num for lst in lists for num in lst]

def unique_merge_lists(*lists):
    all_elements = [num for lst in lists for num in lst]
    unique_elements = []
    for num in all_elements:
        if all_elements.count(num) == 1:
            unique_elements.append(num)
    return unique_elements

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]
    list4 = [7, 8, 9, 10, 11]
    
    choice = input("Görev 1 için 1, Görev 2 için 2 girin: ")
    order = input("Artan sıralama için 'a', azalan sıralama için 'z' girin: ")
    target = int(input("Aranacak sayıyı girin: "))
    
    if choice == '1':
        merged_list = merge_lists(list1, list2, list3, list4)
        sorted_list = sorted(merged_list, reverse=(order == 'z'))
        print("Birleştirilmiş ve sıralanmış liste:", sorted_list)
        index = linear_search(sorted_list, target)
    
    elif choice == '2':
        unique_list = unique_merge_lists(list1, list2, list3, list4)
        sorted_list = sorted(unique_list, reverse=(order == 'z'))
        print("Benzersiz elemanlarla birleştirilmiş ve sıralanmış liste:", sorted_list)
        index = binary_search(sorted_list, target)
    
    else:
        print("Geçersiz seçim!")
        return
    
    if index != -1:
        print(f"{target} değeri listede bulundu, indeksi: {index}")
    else:
        print(f"{target} değeri listede bulunamadı.")

if __name__ == "__main__":
    main()

#chatgpt yardım etti