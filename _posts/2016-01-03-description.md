---
layout: post
title: Course Description
comments: true
---

This course provides a broad survey introducing the many layers of the computer science discipline, emphasizing the computer’s role and limitations as a tool for describing, organizing, and manipulating information applicable to many disciplines. Topics include binary logic expressed in electronic circuitry, machine architecture, basic programming in the very accessible language Python, data organization, the potential and limitations of machines, and useful tools.

This course serves as a terminal course for students who want a one-course introduction to the field, as well as a preliminary course to upper-level computer science offerings.


#### Example script:

```python
'''Given: Two positive integers a and b.
Return: The integer corresponding to 
the square of the hypotenuse of the right 
triangle whose legs have lengths a and b.'''

def hypSq(x, y):
    hs = int(x)**2 + int(y)**2
    print("Hypotenuse squared = " + str(hs))

def main():
    a = input("Enter a positive integer: ")
    b = input("Enter another positive integer: ")
    hypSq(a, b)

main()
```