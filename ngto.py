pt = int(input("Nhập số phần tử có trong danh sách: "))

A = []
A_ngto = []

for i in range(0, pt):
    A.append(int(input("Nhập phần tử: ")))

def so_nguyen_to(so):
    for j in range(2, so):
        if so % j == 0:
            return
        else:
            continue
    A_ngto.append(so)

for z in range(0, pt):
    so_nguyen_to(A[z])

print(A_ngto)