L = list(map(int, input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ").split(',')))

# Sắp xếp các số chẵn lên đầu danh sách
L.sort(key=lambda x: x % 2 == 0 and x != 0, reverse=True)

print("Danh sách sau khi sắp xếp: ", L)

