class RingBuffer:
    def __init__(self, capacity):
        self.capacity = int(capacity)
        self.inventory = []

    def append(self, item):
                
        while len(self.inventory) <= self.capacity:
            if len(self.inventory) <= self.capacity:
                self.inventory.append(item)
            elif len(self.inventory) > self.capacity:
                # self.inventory.pop(0)
                # self.inventory.insert(0, item)

    def get(self):
        new_list = []
        for el in self.inventory:
            if el is not None:
                new_list.append(el)