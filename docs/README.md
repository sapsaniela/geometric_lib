# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle s = a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Description solution
## Project consists of formauls
- Area for circle, triangle, rectangle, square
- Perimeter for circle, triangle, rectangle, square

# circle.py
## Function area(r)
### Function parameters:
- r - circle radius
### Output:
- Circle area - (math.pi * r * r)  
### Example
- input(1)
- area(1)
- return math.pi * 1 * 1
- output(math.pi)
## Function perimeter(r)
### Function parameters:
- r - circle radius
### Output:
- Circle perimeter - (2 * math.pi * r) 
### Example:
- input(1)
- perimeter(1)
- return  2 * math.pi * 1
- output(2 * math.pi)

# rectangly.py
## Function area(a, b)
### Function parameters:
- a - first rectangle side
- b - second rectangle side
### Output:
- Rectangle area (sides(a, b))
### Пример:
- input(1, 2)
- area(1, 2)
- return 1 * 2
- output(2)
## Function perimeter(a, b)
### Function parameters:
- a - first rectangle side
- b - second rectangle side
### Output:
- Rectangle perimeter (sides(a, b))
### Example:
- input(1, 2)
- area(1, 2)
- return 2 * (1 + 2)
- output(6)

# rectangly.py
## Function area(a)
### Function parameters:
- a - square side
### Output:
- Square area (side(a))
### Example:
- input(2)
- area(2)
- return 2 * 2
- output(4)
## Function perimeter(a)
### Function parameters:
- a - square side
### Output:
- Square repimeter (side(a))
### Example:
- input(2)
- area(2)
- return 4 * 2
- output(8)

# triangly.py
## Function area(a, h)
### Function parameters:
- a - triangle side
- h - height drown to side (a)
### Output:
- Triangle area (side(a), height(h))
### Example:
- input(1, 2)
- area(1, 2)
- return 1 * 2 / 2
- output(1)
## Function perimeter(a, b, c)
### Function parameters:
- a - first triangle side
- b - second triangle side
- c - third triangle side
### Output:
- Triangle perimeter (sides(a, b, c))
### Example:
- input(1, 2, 3)
- area(1, 2, 3)
- return 1 + 2 + 3
- output(6)

# Commit log
- 641deb97e2a7a4f21ddaf7f6b4600ff1fc7c12f9: added rectangle.py
- 4bc42432dad9735d0445f07f6ad6fbcbb259539f: added triangle.py
- 4fcd6b8cacbb1ac41b0e1dbf231f30852990c496: fixed mistake in triangle.py
- -381cf5f6e072d0d85283d4f1385986a047272006: added commentaries for rectangle.py, circle.py, triangle.py, square.py
  
