# Sets

[Home](outline.md) | [Queues](1-queue.md) | [Trees](3-tree.md)

## Explanation

A set is a data structure who's purpose is to make finding data in it really fast. Sets can find data in them in O(1) time. Sets do that by placing data in the same location as the value of the data. Arrays have an index. If you want to find the number 10 in an array you would have to search each index in order to find it making it O(n). A set has an index too, but if you added 10 to the set it would place the 10 at index 10. Then when you search for it the set can go to the index of 10 immediately because it knows the value of 10 would be placed there. This is how sets can find data in O(1) time. The order of data in a set does not matter because you do not control where the data is placed, and you cannot have duplicates of data in a set because there is only one index for a value.

Not all data is numbers, so how would you associate other datatypes with an index? Sets do this by **Hashing**. Hashing is using an algorithm to convert something to a number. This way the data is placed in the index of the hash. When you search for that data, you would hash it and go to the index of the hash. For example, if you wanted to add the string "A" to a set you would hash the string and get a number, let's say "A" hashed to 3. Then, when you try to locate "A" you would hash "A" again and it would hash to 3 again. Then the set would go to index 3.

A python dictionary is a type of set. A dictionary creates a set of all the keys so it can find them really fast, it just associates a value with each key as well.

Python has a set datatype that you can make like this:

```python
name = set()
```

You can make a dictionary in two ways:

```python
name = dict()
name = {}
```

### Set Operations In Python

| Operation               | Python code       | Performance |
| ----------------------- | ----------------- | ----------- |
| Add to a set            | set.add(value)    | O(1)        |
| Remove from a set       | set.remove(value) | O(1)        |
| find something in a set | set[value]        | O(1)        |

## Example

Here is an example of a set being used in a program

```python

```

You can view the python file [here](./python/set-example.py)

## Problem to solve
