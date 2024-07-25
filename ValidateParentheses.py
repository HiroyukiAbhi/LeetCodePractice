class Solution:

    def isValid(self, s: str) -> bool:
        myStack = []
        validOpen = {"{", "[", "("}
        validClosed = {"}", "]", ")"}
        for c in s:
            if c in validOpen:
                myStack.append(c)
