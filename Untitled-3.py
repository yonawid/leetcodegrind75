# Implement Queue using Stacks
# Space Complexity: O(N) overall, where N is the total number of elements in the queue.
# Time Complexity:
# - push(): O(1) 
# - pop(): Amortized O(1) (Worst case O(N) when pouring, but averages out to O(1))
# - peek(): Amortized O(1)
# - empty(): O(1)
class MyQueue:
    def __init__(self):
        # The frying pan (new arrivals)
        self.in_stack = []
        # The plate (where we eat from)
        self.out_stack = []

    def push(self, x: int) -> None:
        # Everyone goes straight into the frying pan
        self.in_stack.append(x)

    def pop(self) -> int:
        # If the plate is empty, we pour the entire pan onto the plate
        if not self.out_stack:
            while self.in_stack:
                element = self.in_stack.pop()
                self.out_stack.append(element)
        # Eat a pancake off the plate
        return self.out_stack.pop()

    def peek(self) -> int:
        # If the plate is empty, we pour the entire pan onto the plate
        if not self.out_stack:
            while self.in_stack:
                element = self.in_stack.pop()
                self.out_stack.append(element)
        # Look at the pancake on the plate (without eating it!)
        return self.out_stack[-1]

    def empty(self) -> bool:
        # It's only empty if BOTH the pan and the plate are totally empty
        return self.out_stack == [] and self.in_stack == []
