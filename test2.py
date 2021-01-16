class Buffer:
    def __init__(self):
        self.storage = []

    def add(self, *a):
        for element in a:
            self.storage.append(element)
            self.check()

    def get_current_part(self):
        return self.storage

    def check(self):
        if len(self.storage) >= 5:
                print(sum(self.storage[0:5]))
                del self.storage[0:5]

buf = Buffer()
buf.add(1, 2, 3, 99)
buf.add(1)
buf.get_current_part()
