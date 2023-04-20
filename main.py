class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def push(self, data):
        if data < self.data:
            if self.left:
                self.left.push(data)
            else:
                self.left = Tree(data)
        else:
            if data == self.data:
                return
            if self.right:
                self.right.push(data)
            else:
                self.right = Tree(data)

    def PrintTree(self, n=0):
        if self.right:
            self.right.PrintTree(n + 5)
        print(' ' * n + str(self.data))
        if self.left:
            self.left.PrintTree(n + 5)


T = Tree(10)
T.push(7)
T.push(11)
T.push(10)
T.push(9)
T.push(12)
T.PrintTree()
