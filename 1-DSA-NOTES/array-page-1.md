# Array Indexing — Why Does an Array Start at Index 0?

## 1. What is an Array?

An **array** is a collection of elements stored in a sequence.

For example:

```python
arr = [10, 20, 30, 40, 50]
```

The elements are:

```text
10  20  30  40  50
```

Each element can be accessed using an **index**.

```python
arr[0]   # 10
arr[1]   # 20
arr[2]   # 30
arr[3]   # 40
arr[4]   # 50
```

In Python, C, and C++, array indexing starts at **0**.

---

# 2. What Does an Index Actually Mean?

A common mistake is to think:

> Index = position number

A better way to think about it is:

> **Index = offset from the beginning of the array**

Consider:

```text
Index:     0      1      2      3
           ↓      ↓      ↓      ↓
Array:    [10]   [20]   [30]   [40]
```

The index represents how many elements you need to move from the beginning.

```text
Index 0 → move 0 elements from the beginning
Index 1 → move 1 element
Index 2 → move 2 elements
Index 3 → move 3 elements
```

Therefore, the first element has an offset of `0`.

This is the fundamental reason **0-based indexing is so natural for arrays**.

---

# 3. Understanding It Through Memory

To understand this deeply, we need to think about how arrays are stored in memory.

Suppose we have:

```python
arr = [10, 20, 30, 40]
```

Assume:

- Starting memory address = `1000`
- Each integer occupies `4 bytes`

The array could look conceptually like this:

```text
Index       Value       Memory Address

  0          10              1000
  1          20              1004
  2          30              1008
  3          40              1012
```

Notice something important:

```text
1000 → 1004 → 1008 → 1012
```

Every element is exactly `4 bytes` apart.

---

# 4. How Does the Computer Find `arr[i]`?

The address of an array element can be calculated using:

[
\boxed{
\text{Address} =
\text{Base Address} +
(\text{Index} \times \text{Element Size})
}
]

Where:

- **Base Address** = address of the first element
- **Index** = index of the element
- **Element Size** = number of bytes occupied by one element

---

## Example: `arr[0]`

Base address = `1000`

Element size = `4 bytes`

[
1000 + (0 \times 4)
]

[
= 1000
]

So:

```text
arr[0] → address 1000
```

---

## Example: `arr[1]`

[
1000 + (1 \times 4)
]

[
= 1004
]

So:

```text
arr[1] → address 1004
```

---

## Example: `arr[2]`

[
1000 + (2 \times 4)
]

[
= 1008
]

So:

```text
arr[2] → address 1008
```

---

## Example: `arr[3]`

[
1000 + (3 \times 4)
]

[
= 1012
]

So:

```text
arr[3] → address 1012
```

---

# 5. Why Does Starting at 0 Make the Formula Simple?

This is the key idea.

The first element is located exactly at the **base address**.

There is no offset.

Therefore:

```text
Index 0 → offset 0
Index 1 → offset 1 × element size
Index 2 → offset 2 × element size
Index 3 → offset 3 × element size
```

So the formula is simply:

[
\boxed{
\text{Address} = \text{Base} + \text{Index} \times \text{Size}
}
]

No additional subtraction is necessary.

---

# 6. What If Indexing Started From 1?

It is completely possible to design a programming language where arrays start from `1`.

For example:

```text
Index       Value

  1          10
  2          20
  3          30
  4          40
```

The first element is still at address `1000`.

But now, to calculate the address, we would need:

[
\boxed{
\text{Address}
==============

\text{Base}

- ((\text{Index}-1)\times\text{Element Size})
  }
  ]

For `arr[1]`:

[
1000 + ((1-1)\times4)
]

[
=1000
]

For `arr[2]`:

[
1000 + ((2-1)\times4)
]

[
=1004
]

For `arr[3]`:

[
1000 + ((3-1)\times4)
]

[
=1008
]

So 1-based indexing is possible.

However, **0-based indexing makes the index directly represent the offset from the beginning**.

---

# 7. 0-Based Indexing Is Not a Mathematical Rule

It is important to understand:

> **Arrays do not have to start at 0.**

It is a **design choice made by programming languages**.

Many modern programming languages use 0-based indexing, including:

- C
- C++
- Python
- Java
- JavaScript
- Rust
- Go

Some languages or systems can use different indexing conventions.

So don't think:

> "An array must always start at 0."

Instead think:

> "In languages like Python, C, and C++, the first element is assigned index 0."

---

# 8. Why Does an Array of `n` Elements End at `n - 1`?

Suppose:

```python
arr = [10, 20, 30, 40, 50]
```

There are:

```text
n = 5 elements
```

Their indexes are:

```text
Index:     0    1    2    3    4
           ↓    ↓    ↓    ↓    ↓
Value:    10   20   30   40   50
```

The first index is `0`.

Therefore:

[
\text{Last Index} = n - 1
]

For `n = 5`:

[
5 - 1 = 4
]

So:

```text
Number of elements = 5
Valid indexes = 0, 1, 2, 3, 4
```

---

# 9. Number of Elements vs Last Index

This distinction is extremely important in DSA.

### Number of elements:

```text
5
```

### Last index:

```text
4
```

They are **not the same**.

For an array of size `n`:

[
\boxed{\text{Number of elements}=n}
]

[
\boxed{\text{Last index}=n-1}
]

---

# 10. Why Do Loops Usually Use `< n`?

This is why you commonly see:

### C++

```cpp
for (int i = 0; i < n; i++) {
    cout << arr[i];
}
```

### Python

```python
for i in range(len(arr)):
    print(arr[i])
```

Suppose:

```text
n = 5
```

Then the indexes are:

```text
0
1
2
3
4
```

The loop condition:

```cpp
i < 5
```

allows:

```text
0, 1, 2, 3, 4
```

but stops before:

```text
5
```

Because `arr[5]` would be outside a 5-element array.

---

# 11. Python's `range()` Makes This Very Clear

Suppose:

```python
arr = [10, 20, 30, 40, 50]
```

Then:

```python
len(arr)
```

returns:

```text
5
```

And:

```python
range(len(arr))
```

means:

```text
range(5)
```

which produces:

```text
0 1 2 3 4
```

Exactly the valid indexes of the array.

Therefore:

```python
for i in range(len(arr)):
    print(arr[i])
```

is safe.

---

# 12. The Most Important Mental Model

When working with arrays, don't primarily think:

```text
Index = position
```

Instead, think:

```text
Index = offset from the beginning
```

For example:

```text
              Beginning
                  ↓
Index:       0    1    2    3
             ↓    ↓    ↓    ↓
Array:      [10] [20] [30] [40]
```

Think:

```text
0 → 0 steps from beginning
1 → 1 step from beginning
2 → 2 steps from beginning
3 → 3 steps from beginning
```

This mental model becomes very useful when you learn:

- Arrays
- Strings
- Pointers
- Memory addresses
- Linked lists
- 2D arrays
- Matrix problems
- Sliding window
- Two pointers

---

# 13. Connection With C/C++ Pointers

This is one of the most important reasons to understand 0-based indexing if you're learning DSA.

In C/C++, an array name can behave like a pointer to its first element.

Conceptually:

```cpp
arr
```

refers to the beginning of the array.

Then:

```cpp
arr + 0
```

points to the first element.

```cpp
arr + 1
```

points to the second element.

```cpp
arr + 2
```

points to the third element.

So:

```cpp
arr[i]
```

is closely related to:

```cpp
*(arr + i)
```

This works naturally because `i` represents the **offset from the beginning**.

For example:

```cpp
arr[0]
```

means:

```cpp
*(arr + 0)
```

and:

```cpp
arr[3]
```

means:

```cpp
*(arr + 3)
```

This is a major reason why 0-based indexing fits naturally with low-level memory operations.

---

# 14. Array Indexing Summary

For:

```python
arr = [10, 20, 30, 40, 50]
```

we have:

```text
Index:      0    1    2    3    4
            ↓    ↓    ↓    ↓    ↓
Value:     10   20   30   40   50
```

### Important rules:

[
\boxed{\text{First Index}=0}
]

[
\boxed{\text{Last Index}=n-1}
]

[
\boxed{\text{Valid Index Range}=0\text{ to }n-1}
]

[
\boxed{\text{Number of Elements}=n}
]

And for contiguous memory:

[
\boxed{
\text{Address}
==============

\text{Base Address}

- (\text{Index}\times\text{Element Size})
  }
  ]

  ***

# ⭐ Final Concept to Remember

Don't memorize:

> "Arrays start from zero because programming languages decided so."

Understand this instead:

> **The first element is at the beginning of the array, so its offset from the beginning is 0. The next element is one element away, so its offset is 1, and so on.**

That's why 0-based indexing gives us the elegant relationship:

```text
Index = Offset
```

and the simple memory calculation:

```text
Address = Base Address + Index × Element Size
```

This is the fundamental idea behind 0-based array indexing.
