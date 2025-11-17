# TreeSet

A Python implementation of a TreeSet data structure using a Red-Black Tree as the underlying data structure. This project provides a sorted set implementation with guaranteed logarithmic time complexity for basic operations.

## Description

TreeSet is a collection that stores unique elements in sorted order, implemented using a self-balancing Red-Black Tree. The implementation ensures that all basic operations (add, remove, search) maintain O(log n) time complexity by preserving the Red-Black Tree properties through rotations and recoloring.

## Features

- **Sorted Collection**: Elements are automatically maintained in sorted order
- **Unique Elements**: Duplicate values are not allowed in the set
- **Type Safety**: All elements in a TreeSet must be of the same type
- **Self-Balancing**: Uses Red-Black Tree properties to maintain balanced structure
- **Efficient Operations**: O(log n) time complexity for insertion, deletion, and search operations

## Structure

The project consists of four main components:

### Node.py
Defines the `Node` class that represents individual nodes in the Red-Black Tree:
- `data`: The value stored in the node
- `left`: Reference to the left child node
- `right`: Reference to the right child node
- `color`: Color of the node (0 for red, 1 for black)
- `before`: Reference to the parent node
- `tipo`: Type of data stored in the node

### Tree.py
Implements the `Tree` class, which provides the Red-Black Tree functionality:
- **Insertion**: Adds nodes while maintaining Red-Black Tree properties
- **Deletion**: Removes nodes and rebalances the tree
- **Search**: Finds nodes with specific values
- **Rotations**: Left and right rotations for tree balancing
- **Recoloring**: Adjusts node colors to maintain Red-Black Tree properties
- **In-order Traversal**: Returns nodes in sorted order

### TreeSet.py
Implements the `TreeSet` class, which provides a high-level interface for the sorted set:
- Wraps the Red-Black Tree implementation
- Provides set-specific operations
- Ensures uniqueness of elements

### Pruebas.py
Contains comprehensive unit tests for the TreeSet implementation using Python's `unittest` framework.

## Usage

### Basic Operations

```python
from Tree import Tree
from TreeSet import TreeSet

# Create an empty TreeSet
tree = Tree(None, 0, None)
ts = TreeSet(tree)

# Add elements
ts.add(5)
ts.add(3)
ts.add(7)

# Add multiple elements at once
ts.add_all([1, 2, 4, 6, 8])

# Check if element exists
if ts.contains(5):
    print("Element 5 is in the set")

# Get the size
print(f"Size: {ts.size()}")

# Check if empty
if ts.is_empty():
    print("TreeSet is empty")
else:
    print("TreeSet has elements")

# Remove an element
ts.remove(3)

# Clear all elements
ts.clear()
```

### Navigation Methods

```python
from Tree import Tree
from TreeSet import TreeSet

tree = Tree(None, 0, None)
ts = TreeSet(tree)
ts.add_all([10, 20, 30, 40, 50])

# Get the smallest element
first = ts.first()
print(f"First element: {first.data}")

# Get the largest element
last = ts.last()
print(f"Last element: {last.data}")

# Get smallest element >= given value
ceiling = ts.ceiling(25)
print(f"Ceiling of 25: {ceiling}")

# Get smallest element > given value
higher = ts.higher(30)
print(f"Higher than 30: {higher}")

# Get largest element <= given value
floor = ts.floor(35)
print(f"Floor of 35: {floor.data}")

# Remove and return the first element
first_removed = ts.poll_first()
print(f"Removed first element: {first_removed}")

# Remove and return the last element
last_removed = ts.poll_last()
print(f"Removed last element: {last_removed}")
```

### Cloning

```python
from Tree import Tree
from TreeSet import TreeSet

tree = Tree(None, 0, None)
ts1 = TreeSet(tree)
ts1.add_all([1, 2, 3])

# Create a deep copy of the TreeSet
ts2 = ts1.clone()
```

## Available Methods

### TreeSet Methods

| Method | Description | Return Type |
|--------|-------------|-------------|
| `add(dato)` | Adds an element to the set if not already present | `bool` |
| `add_all(dataset)` | Adds all elements from a list to the set | `bool` |
| `ceiling(data)` | Returns the least element >= data, or None | Value or `None` |
| `higher(data)` | Returns the least element > data, or None | Value or `None` |
| `floor(data)` | Returns the greatest element <= data, or None | Node or `None` |
| `first()` | Returns the first (smallest) element | Node or `None` |
| `last()` | Returns the last (largest) element | Node or `None` |
| `clear()` | Removes all elements from the set | `None` |
| `clone()` | Creates a deep copy of the TreeSet | `TreeSet` |
| `contains(data)` | Checks if an element exists in the set | `bool` |
| `is_empty()` | Checks if the set is empty | `bool` |
| `remove(data)` | Removes an element from the set | `bool` |
| `size()` | Returns the number of elements in the set | `int` |
| `poll_first()` | Removes and returns the first element | Value or `None` |
| `poll_last()` | Removes and returns the last element | Value or `None` |

### Tree Methods (Internal)

| Method | Description |
|--------|-------------|
| `search(dato)` | Searches for a value in the tree |
| `insert(dato)` | Inserts a node into the tree |
| `delete()` | Deletes a node from the tree |
| `fix_insertion(node)` | Restores Red-Black Tree properties after insertion |
| `fix_extraction(node)` | Restores Red-Black Tree properties after deletion |
| `rotate_left(node)` | Performs left rotation |
| `rotate_right(node)` | Performs right rotation |
| `in_order()` | Returns nodes in sorted order |
| `num_nodes()` | Returns the number of nodes |

## Red-Black Tree Properties

The implementation maintains the following Red-Black Tree properties:

1. Every node is either red (0) or black (1)
2. The root is always black
3. All leaves (None) are black
4. Red nodes cannot have red children
5. All paths from a node to its descendant leaves contain the same number of black nodes

These properties ensure that the tree remains balanced, guaranteeing O(log n) time complexity for operations.

## Testing

The project includes comprehensive unit tests in `Pruebas.py`. To run the tests:

```bash
python main.py
```

The test suite covers:
- Basic operations (add, remove, contains)
- Set properties (empty, size)
- Navigation methods (first, last, ceiling, floor, higher)
- Edge cases (duplicate insertion, type safety)
- Tree balancing and recoloring
- Cloning functionality

All 28 tests verify the correctness of the TreeSet implementation.

## Requirements

- Python 3.x

## Type Safety

The TreeSet enforces type consistency - all elements must be of the same type as the first element added. Attempting to add an element of a different type will result in the operation returning `False`.

```python
tree = Tree(None, 0, None)
ts = TreeSet(tree)
ts.add(1)        # int - succeeds
ts.add(2)        # int - succeeds
ts.add("hello")  # string - fails, returns False
```

## License

This project is open source and available for educational and personal use.
