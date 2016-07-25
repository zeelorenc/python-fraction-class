class Fraction:
    '''Creates a fraction'''

    def __init__(self, numerator, denominator = 1):

        gcf = Fraction.greatestCommonFactor(numerator, denominator)

        self.numerator = numerator / gcf
        self.denominator = denominator / gcf

        return None

    def __str__(self):
        '''String representation'''
        return 'Fraction (%d, %d)' % (self.numerator, self.denominator)

    def __add__(a, b):
        '''Adds fractions'''        
        return Fraction(a.numerator * b.denominator + b.numerator * a.denominator, a.denominator * b.denominator)

    def __sub__(a, b):
        '''Subtracts fractions'''
        return Fraction(a.numerator * b.denominator - b.numerator * a.denominator, a.denominator * b.denominator)

    def __mul__(a, b):
        '''Multiplies fractions'''
        return Fraction(a.numerator * b.numerator, a.denominator * b.denominator)

    def __truediv__(a, b):
        '''Divides fractions'''
        return Fraction(a.numerator * b.denominator, a.denominator * b.numerator)

    def __eq__(a, b):
        '''Equates fractions'''
        return a.numerator == b.numerator and a.denominator == b.denominator

    def greatestCommonFactor(numerator, denominator):
        '''Discovers the greatest common factor'''
        
        while denominator:
            numerator, denominator = denominator, numerator % denominator

        return numerator

    def approx(self):
        '''Approximates a fraction'''
        return self.numerator / self.denominator
