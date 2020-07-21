class RingBuffer:
    def __init__(self, capacity):
        self.capacity = int(capacity)
        self.items = [None] * capacity
        self.count = 0
        self.used_space = 0

    def __str__(self):
        return f'{self.items}'

    def append(self, item):
        self.items[self.count % len(self.items)] = item
        self.count += 1

        if self.used_space < len(self.items):
            self.used_space += 1

    def get(self):
        for i in self.items:
            if i is not None:
                return self.items