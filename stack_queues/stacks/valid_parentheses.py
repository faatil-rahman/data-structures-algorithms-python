
"""
Problem: Valid Parenthesis
Approach: Stack
Time Complexity: O(n)

Short Explanation:
We iterate through the string brackets and push opening brackets onto a stack list.
When we encounter a closing brackets, we check whether it matches
the most recent opening brackets. If not, the string is invalid.
which logically a LIFO Mechanism.
"""

def is_valid_parenthesis(s: str) -> bool:

    stack = []
    brackets_match = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }
    openers = set(brackets_match.values()) #set() doesn't allow duplicates.

    for brackets in s:
        if brackets in openers:
            stack.append(brackets) #Push Open Brackets to the Stack List
        elif brackets in brackets_match:
            if not stack: #Return False if Open Brackets doesn't exist
                return False
            elif stack.pop() != brackets_match[brackets]: #Return False if Most recent Opening Doesn't match closing Brackets
                return False
        else: #False if unwanted character exist
            return False

    return not stack #Return True only if there are zero unmatched opening brackets left.


# Testing
if __name__ == "__main__":
    tests = [
        "({[]})",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}"
    ]

    for t in tests:
        print(f"{t}: {is_valid_parenthesis(t)}")
