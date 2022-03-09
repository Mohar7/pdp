class Information:

    def __init__(self):
        self.queue = []

    def enque(self, element):
        self.queue = [element] + self.queue
        # self.queue = [element].extend((self.queue))

    def deque(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def get_queue(self):
        return self.queue[:]


information: Information = Information()



information.enque(1)
information.enque(2)
information.enque(3)
information.enque(4)
information.enque(5)

print(information.get_queue())

print(information.deque())
print(information.get_queue())

'''Boshqacha ishlash yoli'''
# class Information:
#
#     def __init__(self):
#         self.queue = []
#
#     def enque(self, element):
#         # self.queue = [element] + self.queue
#         self.queue.extend([element])
#         print(self.queue)
#
#     def deque(self):
#         return self.queue.pop()
#
#     def size(self):
#         return len(self.queue)
#
#     def get_queue(self):
#         return self.queue[::-1]
#
#
# information: Information = Information()
#
# information.enque(1)
# information.enque(2)
# information.enque(3)
# information.enque(4)
# information.enque(5)
#
#
# print(information.deque())
# print(information.get_queue())
#
