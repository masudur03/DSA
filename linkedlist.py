# make a node class
class node:

    def __init__(self, data=None):
        # the data is default by None, but user can put any data into the value
        self.data = data
        self.next = None


class linked_list:

    def __init__(self):
        self.head = node()

    def push(self, data):
        # first make a new node
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next

        # once we are out of the while loop curr is the last node
        curr.next = new_node

    def display(self):
        curr = self.head
        while curr.next != None:
            curr = curr.next
            print(curr.data)

    def len(self):
        count = 0
        curr = self.head
        while curr.next != None:
            curr = curr.next
            count += 1
        return count

    def remove(self, index):
        # check if index is out of bound
        if index >= self.len():
            print("index out of bound")
            return
        curr_index = -1
        curr = self.head
        prev = None
        while curr_index != index:
            prev = curr
            curr = curr.next
            curr_index += 1
        # here we are the desired node
        prev.next = curr.next
        return

    # removes the last element
    def pop(self):
        curr = self.head
        prev = None
        while curr.next != None:
            prev = curr
            curr = curr.next
        prev.next = None
        return


my_list = linked_list()

my_list.push(1)
my_list.push(2)
my_list.push(3)
my_list.push(4)


my_list.display()

my_list.pop()
print("after removig last index: \n")
my_list.display()
