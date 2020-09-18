# Please add your answers to the **_Analysis of Algorithms_** exercises here

## Exercise I

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

O(n)

- a increases by n\*n every time it increments ...
- this grows in direct proportion with n, therefore O(n)

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

O(n\*log(n))

- the for loop has no way to break out on its own (must go all the way thru -- O(n))
- the while loop is nested inside a for lop (O(log(n)))

```
c) **** def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

O(n)

- decrements by 1 every time -- directly proportional with number of bunnies

---

## Exercise II

I would solve this using a binary search type approach

- start at middle floor and drop an egg
- if egg doesn't break, we know f is above
  - find a new floor above to check (using binary search halving technique)
- if egg does break
  - we may be at f or above it
  - find a new floor below to check

this approach would have an O(log(n)) runtime because we are using a BST