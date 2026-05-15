class StudentList:
    def __init__(self):
        # Khởi tạo mảng với dữ liệu gán sẵn (Hard-code)
        self.dssv = [
            {'ms': 'SV03', 'hten': 'Gia Huy', 'dlt': 5.0, 'dth': 4.0, 'dtb': 4.5},
            {'ms': 'SV01', 'hten': 'Nguyen Tuong', 'dlt': 9.0, 'dth': 8.0, 'dtb': 8.5},
            {'ms': 'SV02', 'hten': 'Tran Bao', 'dlt': 7.0, 'dth': 6.0, 'dtb': 6.5},
            {'ms': 'SV04', 'hten': 'Minh Khoa', 'dlt': 8.0, 'dth': 9.0, 'dtb': 8.5}
        ]

    def insertion_sort(self, tang_dan=True):
        n = len(self.dssv)
        # Bắt đầu từ sinh viên thứ 2 (vị trí 1)
        for i in range(1, n):
            key = self.dssv[i] # Lấy sinh viên này ra để chèn
            j = i - 1
            
            # Kiểm tra điều kiện và "đẩy" các sinh viên đứng trước sang phải
            while j >= 0:
                if tang_dan:
                    condition = self.dssv[j]['dtb'] > key['dtb']
                else:
                    condition = self.dssv[j]['dtb'] < key['dtb']
                
                if condition:
                    self.dssv[j + 1] = self.dssv[j]
                    j -= 1
                else:
                    break
            
            # Chèn sinh viên vào vị trí trống đã tạo ra
            self.dssv[j + 1] = key
            
        print(f"--> [List] Đã Insertion Sort {'TĂNG' if tang_dan else 'GIẢM'} dần.")

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
bai1.insertion_sort(tang_dan=True)
bai1.xuat_ds()

# Sắp xếp giảm dần
bai1.insertion_sort(tang_dan=False)
bai1.xuat_ds()