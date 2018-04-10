---
layout: page
title: Python to Assembler Exercises
permalink: /pip_example/
---

### Example 1
The `abs()` function in Python takes the absolute value of a number

```python
>>> abs(3)
3
>>> x = -3
>>> abs(x)
3
```

We want to translate the `abs()` function to assembler language. First think how we would do it in Python if we didn’t have the built in function:

```python
if x < 0:
    x = -1 * x
```

Now how would we write this in assembler language?


### Example 2
How would we write the following Python code in assembler?

```python
n = 3
sum = 0
while n >= 0:
    sum = sum + n
    n = n - 1
```

### Example 3
How would we write the following Python code in assembler?

```python
if x == 0:
    y = 3
else:
    y = 5
z = z + y
```

We will intialize x, y, and z by hand in the simulator to test our code.  