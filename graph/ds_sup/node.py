class Node:
    def __init__(self) -> None:
        pass

    def clone(self):
        raise NotImplementedError()

class BlockNode:
    def __init__(self, capacity) -> None:
        self.max_capacity = capacity
        self.current_capacity = 0

    def get_max_cap(self):
        return self.max_capacity
    
    def get_curr_cap(self):
        return self.current_capacity
    
    def clone(self):
        raise NotImplementedError()