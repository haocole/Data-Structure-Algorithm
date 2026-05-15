# Định nghĩa cấu trúc 1 mắt xích
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Định nghĩa danh sách liên kết
class LinkedList:
    def __init__(self):
        self.head = None # Điểm bắt đầu

    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"-> Đã thêm {data} vào đầu")

    def show(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Chạy thử
my_list = LinkedList()
my_list.add_to_front("Node_1")
my_list.add_to_front("Node_2")
my_list.show() # Kết quả: Node_2 -> Node_1 -> None