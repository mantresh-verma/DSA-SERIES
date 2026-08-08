# 📘 [Topic Name] (e.g., Linked Lists, Binary Search)

## 🧠 1. The Core Intuition (Explain it to a 5-year-old)
*What is this data structure/algorithm in plain English?*
* **Real-world analogy:** (e.g., "A Linked List is like a treasure hunt where each clue points to the next location.")
* **Why do we need it?** (What problem does this solve that Arrays or standard loops cannot?)

## 🎨 2. Visual Mental Model
*(Leave space here to draw. If using digital notes, take a screenshot of the Apna College animation and paste it here. ALWAYS draw pointers, nodes, or array indices.)*

## ⏱️ 3. Time & Space Complexity (The Cheat Sheet)
*(Memorize this for interviews)*
| Operation | Average Case | Worst Case | Space Complexity |
| :--- | :--- | :--- | :--- |
| Access | $O(...)$ | $O(...)$ | $O(...)$ |
| Search | $O(...)$ | $O(...)$ | $O(...)$ |
| Insertion | $O(...)$ | $O(...)$ | $O(...)$ |
| Deletion | $O(...)$ | $O(...)$ | $O(...)$ |

## 💻 4. The "Python Template" Code
*(Do NOT paste solutions to specific problems here. Only paste the standard, repetitive boilerplate code that you will use over and over again.)*
```python
# Example: Standard Singly Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example: Standard Traversal
def traverse(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next