# Python Fraction Class
Ultra simple fraction class for Python. Only created for the purposes of learning about classes/objects in Python.

Do whatever you want with it!

# Examples
```python 
# Example values
sampleFractionOne = Fraction(10, 30) # simplifies to 1/3
sampleFractionTwo = Fraction(100, 300) # 1/3 again

# Print fraction
print (sampleFractionOne) # prints "Fraction (1, 3)"
print (sampleFractionTwo) # prints "Fraction (1, 3)"

# Add fractions
addition = sampleFractionOne + sampleFractionTwo
print (addition) # prints "Fraction (2, 3)"

# Remove fractions
subtraction = sampleFractionOne - sampleFractionTwo
print (subtraction) # prints "Fraction (0, 1)" same as 0

# Multiply fractions
multiply = sampleFractionOne * sampleFractionTwo
print (multiply) # prints "Fraction (1, 9)"

# Divide fractions
divide = sampleFractionOne / sampleFractionTwo
print (divide) # prints "Fraction (1, 1)"

# Equate fractions
is_equal = sampleFractionOne == sampleFractionTwo
print (is_equal) # prints True

# Greatest Common Factor
gcf = Fraction.greatestCommonFactor(24, 32)
print (gcf) # prints 8

# Approximate
approx = Fraction(1, 3).approx()
print (approx)
```
