# 1. Tính S = 1 + 2 + 3 + ... + n
def tinh_tong_1(n):
    if n == 1: return 1 # Điểm dừng
    return n + tinh_tong_1(n - 1)

# 2. Tính S = 2 + 4 + 6 + ... + 2n
def tinh_tong_2(n):
    if n == 1: return 2 # Điểm dừng (số hạng đầu tiên là 2)
    return (2 * n) + tinh_tong_2(n - 1)

# 3. Tính S = 1 + 3 + 5 + ... + (2n-1)
def tinh_tong_3(n):
    if n == 1: return 1 # Điểm dừng (số hạng đầu tiên là 1)
    return (2 * n - 1) + tinh_tong_3(n - 1)
def Q(a, b):
    # Định nghĩa đệ quy theo đề bài
    if a < b:
        return 0
    else:
        return Q(a - b, b) + 1

# Nhập dữ liệu và kiểm tra
try:
    a_input = int(input("Nhập số nguyên dương a: "))
    b_input = int(input("Nhập số nguyên dương b: "))
    
    if a_input > 0 and b_input > 0:
        result = Q(a_input, b_input)
        print(f"Kết quả Q({a_input}, {b_input}) là: {result}")
    else:
        print("Vui lòng nhập số nguyên dương!")
except ValueError:
    print("Vui lòng chỉ nhập số nguyên.")