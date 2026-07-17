class MinStack:

    def __init__(self):
        self.stack=[]
        self.temp_stack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.temp_stack)==0:
            self.temp_stack.append(val)
        elif val<=self.temp_stack[-1]:
            self.temp_stack.append(val)
    def pop(self) -> None:
        popped_element=self.stack.pop()
        if popped_element==self.temp_stack[-1]:
            self.temp_stack.pop()
        return popped_element
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.temp_stack[-1]

