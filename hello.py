class Node:
     def __init__(self,data): 
          self.data=data
          self.next=None 
class LL:
     def __init__(self): 
          self.head=None
     def insrert_at_begining(self,data): 
          new_node=Node(data) 
          new_node.next = self.head 
          self.head= new_node
     def display(self):
          current = self.head 
          while current:
               print(current.data, end=" -> ")
               current = current.next 
print("None")
L_L=LL() 
L_L.insrert_at_begining(1)
L_L.insrert_at_begining(2) 
L_L.insrert_at_begining(3) 
L_L.insrert_at_begining(4) 
L_L.insrert_at_begining(5)
L_L.display()