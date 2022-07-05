class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push_front(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def push_end(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next
    # def add_arr(self):
    #     arr=[]
    #     temp=self.head
    #     while (temp):
    #         arr.append(temp.data)
    #         temp=temp.next
    #     print(arr)

new_list=LinkedList()
ll=[20,21,22,23,24,25,26]
for l in ll:
    new_list.push_front(l)
# new_list.push_front(20)
# new_list.push_front(20)
# new_list.push_end(19)
# new_list.push_front(20)
# new_list.push_front(20)
# new_list.push_front(20)
# new_list.add_arr()
new_list.print_list()