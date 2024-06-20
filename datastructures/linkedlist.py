# NOTE: This class is not intended for manual manipulation
class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self, data):
        # NOTE: Makes a node with the current "head"
        node = Node(data, self.head)

        # NOTE: the node address updated and then is saved for the next node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        # NOTE: Go to the end of the list. Iter until "itr.None = None"
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, idx):
        if idx < 0 or idx >= self.get_length():
            raise Exception("Invalid index")

        if idx == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, idx, data):
        if idx < 0 or idx > self.get_length():
            raise Exception("Invalid index")

        if idx == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            # NOTE: MOdify the "next" pointer of the previous elemnet
            if count == idx - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print_ll(self):
        # NOTE: by defautl our "head" is Node, this means that we have not
        # created a single node
        if self.head is None:
            print("Empty linked list")
            return

        itr = self.head
        llstr = ""

        # NOTE: "itr" refers to the object or node of out head. As long as heas is
        # worth something and no None, we reassign "itr" to another node with
        # "itr.next"
        while itr:
            llstr += str(itr.data) + " -> "
            itr = itr.next

        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()

    # ll.insert_at_begining(1)
    # ll.insert_at_begining(2)
    # ll.insert_at_begining(3)
    #
    # ll.insert_at_end(4)

    ll.insert_values([1, 2, 3, 4])

    ll.remove_at(1)
    ll.insert_at(1, 5)

    ll.print_ll()
    print("linked list length:", ll.get_length())
