# Linked Lists


class Node:  # this corresponds to the HashTableEntry class
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:  # this corresponds to the HashTable Class
    def __init__(self):
        self.head = None

    def find(self, val):
        cur = self.head

        while cur is not None:
            if cur.value == val:
                return cur

            cur = cur.next

        return None  # if we haven't found the val by the end of the loop

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def delete(self, value):
        # special case of deleting the head of the list
        if self.head.value == value:
            old_head = self.head
            self.head = self.head.next
            return old_head

        # general case of deleting from rest of list
        prev = self.head
        cur = prev.next

        while cur is not None:
            if cur.value == value:
                # cut the old node out
                prev.next = cur.next
                return cur

            prev = prev.next
            cur = cur.next

