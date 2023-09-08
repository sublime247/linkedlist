class Node:
    def __init__(self, value):
        self.value= value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0
    #   Append Method
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        # prepend Method

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head =new_node
        self.length+=1
    # insert method
    def insert(self, index, value):
        new_node = Node(value) 
        if index < 0 or index>self.length:
            return False
        elif self.length ==0:
            self.head = new_node
            self.tail = new_node   
        elif index == 0 :
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next= temp_node.next
            temp_node.next = new_node
        self.length+=1
        return True
    # traverse method
    def traverse(self):
        current= self.head
        while current is not None:
            print(current.value)
            current = current.next
#    search method
    def search(self, value):
        current = self.head
        while current is not None:
            if current.value==value:
                return True
            current = current.next  
        return False 
    # getting element based on index 
    def get(self, index): 
        if index == -1:
            return self.tail.value
        if index<-1 or index>=self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    # setting of valuebase on indexx
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value= value
            return True
        return False 
    # pop first element
    def pop_first(self):
        pop_node = self.head
        self.head = self.head.next
        pop_node.next = None
        self.length-=1
        return pop_node
    # pop method
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        if self.length ==1:
            self.head = self.tail=None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp= temp.next
            self.tail =temp
            temp.next = None
            self.length -=1
        return popped_node
    
    # remove element based on index
    def remove(self, index):
        if index ==0:
            return self.pop_first()
        if index >= self.length or index<-1:
            return None
        if index==-1 or index== self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next= None
        self.length-=1
        return popped_node
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length=0
    # printing out linkedlist method
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next 
        return result
    
    


new_linked_list = LinkedList()
new_linked_list.append(20)              
new_linked_list.append(40)
new_linked_list.prepend(100)
new_linked_list.insert(0,70)
new_linked_list.insert(4,100)
print(new_linked_list.pop().value)
print(new_linked_list.remove(-2))
new_linked_list.delete_all()
print(new_linked_list)
