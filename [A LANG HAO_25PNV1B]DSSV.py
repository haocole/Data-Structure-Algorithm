class Node:
    def __init__(self, ms, hoten, dlt, dth):
        self.ms = ms
        self.hoten = hoten
        self.dlt = dlt
        self.dth = dth
        self.dtb = (dlt + dth) / 2
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # --- HÀM HỖ TRỢ NHẬP DỮ LIỆU ---
    def nhap_sv(self):
        print("\n--- Nhập thông tin sinh viên ---")
        ms = input("Mã số: ")
        hoten = input("Họ tên: ")
        try:
            dlt = float(input("Điểm Lý Thuyết: "))
            dth = float(input("Điểm Thực Hành: "))
            return Node(ms, hoten, dlt, dth)
        except ValueError:
            print("(!) Lỗi: Điểm phải là số. Vui lòng thực hiện lại.")
            return None

    # --- NHÓM CHỨC NĂNG THÊM ---
    def them_dau(self):
        new_node = self.nhap_sv()
        if new_node:
            new_node.next = self.head
            self.head = new_node
            print("--> Đã thêm vào ĐẦU hàng.")

    def them_cuoi(self):
        new_node = self.nhap_sv()
        if not new_node: return
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print("--> Đã thêm vào CUỐI hàng.")

    def bo_sung_sau_ms(self, ms_tim):
        temp = self.head
        while temp and temp.ms != ms_tim:
            temp = temp.next
        if temp:
            new_node = self.nhap_sv()
            if new_node:
                new_node.next = temp.next
                temp.next = new_node
                print(f"--> Đã chèn thành công sau mã {ms_tim}.")
        else:
            print(f"(!) Không tìm thấy mã {ms_tim} trong danh sách.")

    # --- NHÓM CHỨC NĂNG XÓA ---
    def xoa_dau(self):
        if self.head:
            print(f"--> Đã xóa đầu: {self.head.hoten}")
            self.head = self.head.next
        else:
            print("(!) Danh sách đang rỗng.")

    def xoa_cuoi(self):
        if not self.head:
            print("(!) Danh sách đang rỗng.")
            return
        if not self.head.next:
            print(f"--> Đã xóa người duy nhất: {self.head.hoten}")
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        print(f"--> Đã xóa cuối: {temp.next.hoten}")
        temp.next = None

    def xoa_diem_zero(self):
        curr = self.head
        prev = None
        count = 0
        while curr:
            if curr.dtb == 0:
                count += 1
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        print(f"--> Đã quét xong. Xóa tổng cộng {count} sinh viên điểm 0.")

    # --- NHÓM CHỨC NĂNG TÌM KIẾM & SẮP XẾP ---
    def tim_ms_hien_bang(self, ms_tim):
        temp = self.head
        while temp:
            if temp.ms == ms_tim:
                print(f"\n{'MS':<10} | {'HỌ TÊN':<20} | {'ĐTB':<5}")
                print("-" * 45)
                print(f"{temp.ms:<10} | {temp.hoten:<20} | {temp.dtb:.2f}")
                return
            temp = temp.next
        print(f"(!) Không tìm thấy sinh viên có mã {ms_tim}.")

    def sap_xep_tang_dan(self):
        if not self.head or not self.head.next: return
        i = self.head
        while i:
            j = i.next
            while j:
                if i.dtb > j.dtb:
                    # Hoán đổi dữ liệu (Swap data)
                    i.ms, j.ms = j.ms, i.ms
                    i.hoten, j.hoten = j.hoten, i.hoten
                    i.dlt, j.dlt = j.dlt, i.dlt
                    i.dth, j.dth = j.dth, i.dth
                    i.dtb, j.dtb = j.dtb, i.dtb
                j = j.next
            i = i.next
        print("--> Đã sắp xếp danh sách tăng dần theo ĐTB.")

    # --- NHÓM CHỨC NĂNG IN ẤN ---
    def in_ds(self, chi_lay_dat=False):
        temp = self.head
        if not temp:
            print("\n[!] Danh sách rỗng.")
            return
        
        tieu_de = "SV CÓ ĐTB >= 5" if chi_lay_dat else "TẤT CẢ SINH VIÊN"
        print(f"\n--- {tieu_de} ---")
        print(f"{'MS':<10} | {'HỌ TÊN':<20} | {'ĐTB':<5}")
        print("-" * 45)
        
        found = False
        while temp:
            if not chi_lay_dat or temp.dtb >= 5:
                print(f"{temp.ms:<10} | {temp.hoten:<20} | {temp.dtb:.2f}")
                found = True
            temp = temp.next
        if not found: print("Không có dữ liệu phù hợp.")

# --- CHƯƠNG TRÌNH CHÍNH (MENU) ---
ql = LinkedList()

while True:
    print("\n" + "="*15 + " MENU CHUẨN " + "="*15)
    print("1. Thêm ĐẦU          | 2. Thêm CUỐI")
    print("3. Xóa ĐẦU           | 4. Xóa CUỐI")
    print("5. Xóa SV điểm = 0   | 6. Bổ sung sau Mã số")
    print("7. Sắp xếp ĐTB tăng  | 8. Tìm kiếm Mã số (Hiện bảng)")
    print("9. In TẤT CẢ         | 10. In SV có ĐTB >= 5")
    print("0. THOÁT")
    
    chon = input("\nLựa chọn của bạn (0-10): ")
    
    if chon == '1': ql.them_dau()
    elif chon == '2': ql.them_cuoi()
    elif chon == '3': ql.xoa_dau()
    elif chon == '4': ql.xoa_cuoi()
    elif chon == '5': ql.xoa_diem_zero()
    elif chon == '6': ql.bo_sung_sau_ms(input("Nhập mã số gốc: "))
    elif chon == '7': ql.sap_xep_tang_dan()
    elif chon == '8': ql.tim_ms_hien_bang(input("Nhập mã số cần tìm: "))
    elif chon == '9': ql.in_ds(chi_lay_dat=False)
    elif chon == '10': ql.in_ds(chi_lay_dat=True)
    elif chon == '0':
        print("Kết thúc chương trình. Tạm biệt!")
        break
    else:
        print("(!) Lựa chọn không hợp lệ, vui lòng chọn lại.")