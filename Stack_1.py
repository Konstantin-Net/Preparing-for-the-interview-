class Stack:

    lst = []

    def is_empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop(-1)

    def peek(self):
        return self.lst[-1]

    def size(self):
        return len(self.lst)
