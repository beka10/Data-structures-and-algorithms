'''
Implementation of the class Fraction

Author: Beka Beriashvili

'''

#!/usr/bin/env python3


def gcd(num_a, num_b):
    '''Helper function to simplify fractions'''
    while num_a % num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_b


class Fraction:
    '''Class Fraction'''
    def __init__(self, numerator, denominator) -> None:
        '''Constructor'''
        if type(numerator) is not int:
            raise TypeError("Numerator must be an integer number")
        if type(denominator) is not int:
            raise TypeError("Denominator must be an integer number")
        
        self._numerator = numerator // gcd(numerator, denominator)
        self._denominator = denominator // gcd(numerator, denominator)
    
    def get_numerator(self) -> int:
        '''Return fraction numerator'''
        return self._numerator

    numerator = property(get_numerator)

    def get_denominator(self) -> int:
        '''Return fraction denominator'''
        return self._denominator

    denominator = property(get_denominator)

    def __str__(self) -> str:
        '''Object as a string'''
        if self._numerator > self._denominator:
            return str(self._numerator // self._denominator) + ' ' + \
                str(self._numerator % self._denominator) + '/' + str(self._denominator)
        else:
            return str(self._numerator) + '/' + str(self._denominator)

    def __repr__(self) -> str:
        '''Object representation'''
        return 'Fraction({}, {})'.format(self._numerator, self._denominator)

    def __eq__(self, other: object) -> bool:
        '''Equality comparison'''
        if isinstance(other, Fraction):
            return self._numerator * other._denominator == other._numerator * self._denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __gt__(self, other: object) -> bool:
        '''Greater than comparison'''
        if isinstance(other, Fraction):
            return self._numerator / self._denominator > other._numerator / other._denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __ge__(self, other: object) -> bool:
        '''Greater than or equal comparison'''
        if isinstance(other, Fraction):
            return self._numerator / self._denominator >= other._numerator / other._denominator
        else:
            raise TypeError('Can only compare Fractions')

    def __add__(self, other: object) -> object:
        '''Add two fractions'''
        if type(other) is not Fraction:
            raise TypeError("Can only add two Fractions")
        new_num = self._numerator * other._denominator + other._numerator * self._denominator
        new_den = self._denominator * other._denominator
        return Fraction(new_num, new_den)
        
    def __sub__(self, other: object) -> object:
        '''Subtract two fractions'''
        if type(other) is not Fraction:
            raise TypeError("Can only subtract two Fractions")
        new_num = self._numerator * other._denominator - other._numerator * self._denominator
        new_den = self._denominator * other._denominator
        return Fraction(new_num//gcd(new_num,new_den), new_den//gcd(new_num,new_den))

    def __mul__(self, other: object) -> object:
        '''Multiply two fractions'''
        if type(other) is not Fraction:
            raise TypeError("Can only multiply two Fractions")
        new_num = self._numerator * other._numerator
        new_den = self._denominator * other._denominator
        return Fraction(new_num//gcd(new_num,new_den), new_den//gcd(new_num,new_den))

    def __truediv__(self, other: object) -> object:
        '''Divide two fractions'''
        if type(other) is not Fraction:
            raise TypeError("Can only divide two Fractions")
        new_num = self._numerator * other._denominator
        new_den = self._denominator * other._numerator
        return Fraction(new_num//gcd(new_num,new_den), new_den//gcd(new_num,new_den))


if __name__ == "__main__":
    print("Working with Classes")
    fr_1 = Fraction(10, 4)
    print("Fraction 1 is %s" % fr_1)
    fr_2 = Fraction(10, 12)
    print("Fraction 2 is %s" % fr_2)
    fr_3 = Fraction(3, 4)
    print("Fraction 3 is %s" % fr_3)
    print("Its id is %s" % id(fr_3))
    fr_4 = Fraction(3, 4)
    print("Fraction 4 is %s" % fr_4)
    print("Its id is %s" % id(fr_4))

    print("Comparison")
    if fr_3 == fr_4:
        print("%s and %s are equal!" % (fr_3, fr_4))
    else:
        print("%s and %s are different!" % (fr_3, fr_4))

    print("%s + %s = %s" % (fr_1, fr_2, fr_1 + fr_2))

    print(Fraction(1, 3) - Fraction(2, 3))
