# Geometric Calculations Project Documentation

## Overview
This project provides a set of functions to calculate the area and perimeter of basic geometric shapes: circle, rectangle, and triangle.  
Each function includes a docstring with usage examples.

## Project Functions

### Circle

#### `circle_area(r)`
**Description**: Calculates the area of a circle.  
**Parameters**:  
- `r` (float): Radius of the circle.  
**Returns**:  
- `float`: Area of the circle.  
**Example**:  
```python
area(3)  # 28.274333882308138
```

#### `circle_perimeter(r)`
**Description**: Calculates the perimeter (circumference) of a circle.  
**Parameters**:  
- `r` (float): Radius of the circle.  
**Returns**:  
- `float`: Perimeter of the circle.  
**Example**:  
```python
perimeter(3)  # 18.84955592153876
```

### Rectangle

#### `rectangle_area(a, b)`
**Description**: Calculates the area of a rectangle.  
**Parameters**:  
- `a` (float): Length of the rectangle.  
- `b` (float): Width of the rectangle.  
**Returns**:  
- `float`: Area of the rectangle.  
**Example**:  
```python
rectangle_area(4, 5)  # 20
```

#### `rectangle_perimeter(a, b)`
**Description**: Calculates the perimeter of a rectangle.  
**Parameters**:  
- `a` (float): Length of the rectangle.  
- `b` (float): Width of the rectangle.  
**Returns**:  
- `float`: Perimeter of the rectangle.  
**Example**:  
```python
rectangle_perimeter(4, 5)  # 18
```

### Triangle

#### `triangle_area(a, h)`
**Description**: Calculates the area of a triangle using its base and height.  
**Parameters**:  
- `a` (float): Base of the triangle.  
- `h` (float): Height perpendicular to the base `a`.  
**Returns**:  
- `float`: Area of the triangle.  
**Example**:  
```python
triangle_area(6, 4)  # 12.0
```

#### `triangle_perimeter(a, b, c)`
**Description**: Calculates the perimeter of a triangle using its three sides.  
**Parameters**:  
- `a` (float): First side of the triangle.  
- `b` (float): Second side of the triangle.  
- `c` (float): Third side of the triangle.  
**Returns**:  
- `float`: Perimeter of the triangle.  
**Example**:  
```python
triangle_perimeter(3, 4, 5)  # 12
```

## Change History
- `c34f7a7`: Added docstrings to functions.
- `bef572f`: Update documentation.md
- `b708113`: Update readme.md