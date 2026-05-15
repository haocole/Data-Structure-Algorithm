# class StudentList:
#     def __init__(self):
#         self.dssv = []

#     def nhap_danh_sach(self, n):
#         for i in range(n):
#             print(f"\nNhập SV thứ {i+1}:")
#             ms = input("Mã số: ")
#             hten = input("Họ tên: ")
#             dlt = float(input("Điểm LT: "))
#             dth = float(input("Điểm TH: "))
#             dtb = (dlt + dth) / 2
#             # Lưu mỗi SV thành một Dictionary và bỏ vào List
#             self.dssv.append({'ms': ms, 'hten': hten, 'dlt': dlt, 'dth': dth, 'dtb': dtb})

#     def sap_xep(self, tang_dan=True):
#         # Sử dụng hàm sort có sẵn của Python, cực kỳ tối ưu
#         self.dssv.sort(key=lambda x: x['dtb'], reverse=not tang_dan)
#         print(f"--> Đã sắp xếp {'TĂNG' if tang_dan else 'GIẢM'} dần theo ĐTB.")

#     def xuat_ds(self):
#         print(f"\n{'MS':<10} | {'HỌ TÊN':<20} | {'ĐTB':<5}")
#         print("-" * 40)
#         for sv in self.dssv:
#             print(f"{sv['ms']:<10} | {sv['hten']:<20} | {sv['dtb']:.2f}")

# # Chạy thử Bài 1
# print("--- BÀI 1: LƯU VÀO LIST ---")
# bai1 = StudentList()
# bai1.nhap_danh_sach(2)
# bai1.sap_xep(tang_dan=True)  # Sắp tăng
# bai1.xuat_ds()
# bai1.sap_xep(tang_dan=False) # Sắp giảm
# bai1.xuat_ds()
class StudentList:
    def __init__(self):
        # Khởi tạo mảng với dữ liệu gán sẵn (Hard-code)
        self.dssv = [
            {'ms': 'SV03', 'hten': 'Gia Huy', 'dlt': 5.0, 'dth': 4.0, 'dtb': 4.5},
            {'ms': 'SV01', 'hten': 'Nguyen Tuong', 'dlt': 9.0, 'dth': 8.0, 'dtb': 8.5},
            {'ms': 'SV02', 'hten': 'Tran Bao', 'dlt': 7.0, 'dth': 6.0, 'dtb': 6.5},
            {'ms': 'SV04', 'hten': 'Minh Khoa', 'dlt': 8.0, 'dth': 9.0, 'dtb': 8.5}
        ]

    def selection_sort(self, tang_dan=True):
        n = len(self.dssv)
        # Thuật toán Selection Sort (Sắp xếp chọn)
        for i in range(n - 1):
            # Giả định phần tử tại i là nhỏ nhất (tăng) hoặc lớn nhất (giảm)
            idx_chon = i 
            for j in range(i + 1, n):
                # Kiểm tra điều kiện để cập nhật lại vị trí được chọn
                if tang_dan:
                    if self.dssv[j]['dtb'] < self.dssv[idx_chon]['dtb']:
                        idx_chon = j
                else:
                    if self.dssv[j]['dtb'] > self.dssv[idx_chon]['dtb']:
                        idx_chon = j
            
            # Sau khi tìm được phần tử tối ưu, đổi chỗ nó với vị trí i
            if idx_chon != i:
                self.dssv[i], self.dssv[idx_chon] = self.dssv[idx_chon], self.dssv[i]
        
        print(f"--> Đã Selection Sort {'TĂNG' if tang_dan else 'GIẢM'} dần.")

    def xuat_ds(self):
        print(f"\n{'MS':<10} | {'HỌ TÊN':<20} | {'ĐTB':<5}")
        print("-" * 40)
        for sv in self.dssv:
            print(f"{sv['ms']:<10} | {sv['hten']:<20} | {sv['dtb']:.2f}")

# --- CHẠY THỬ ---
bai1 = StudentList()

print("DANH SÁCH GÁN SẴN BAN ĐẦU:")
bai1.xuat_ds()

# Sắp xếp tăng dần
bai1.selection_sort(tang_dan=True)
bai1.xuat_ds()

# Sắp xếp giảm dần
bai1.selection_sort(tang_dan=False)
bai1.xuat_ds()