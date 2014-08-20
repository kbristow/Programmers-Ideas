def convert_fraction_str(fraction_str):
    """Attempts to create a Fraction object from a string.

    Args:
        fraction_str: String to try convert

    Returns:
        None if the fraction_str was not a valid fraction, otherwise the Fraction object
        representation of fraction_str
    """
    
    fraction_parts = fraction_str.split('/')
    fraction_return = None

    if len(fraction_parts) == 2:
        try:
            denominator = int(fraction_parts[1])

            #Perform to check for mixed fractions
            numerator_parts = fraction_parts[0].split(' ')

            numerator_parts_len = len(numerator_parts)            

            numerator = int(numerator_parts[numerator_parts_len -1])

            if numerator_parts_len == 2:
                #We then have a mixed fraction
                #Convert to a proper fraction
                numerator += int(numerator_parts[0]) * denominator

            fraction_return = Fraction(numerator, denominator)
        except ValueError:
            pass

    return fraction_return


def get_lcm(base1, base2):
    """Get the lowest common multiple of base1 and base2"""
    
    #Only look for positive numbers
    base1 = abs(base1)
    base2 = abs(base2)
    
    lcm_base = max(base1,base2)
    lcm_tester = min(base1,base2)
    lcm_candidate = lcm_base

    found_lcm = lcm_candidate%lcm_tester==0
    while not found_lcm:
        lcm_candidate += lcm_base
        found_lcm = lcm_candidate%lcm_tester==0

    return lcm_candidate

def get_gcd(base1, base2):
    """Get the greatest common divisor of base1 and base2"""
    
    #Only look for positive numbers
    base1 = abs(base1)
    base2 = abs(base2)
    
    gcd_candidate = min(base1,base2)
    is_gcd = base1 % gcd_candidate == 0 and base2 % gcd_candidate == 0

    if not is_gcd :
        gcd_candidate /= 2
        is_gcd = base1 % gcd_candidate == 0 and base2 % gcd_candidate == 0

        while (not is_gcd) and (gcd_candidate > 1):
            gcd_candidate -= 1
            is_gcd = base1 % gcd_candidate == 0 and base2 % gcd_candidate == 0

    return gcd_candidate

def convert_to_lcm(frac1, frac2):
    """Convert Fractions frac1 and frac2 to use lowest common multiple as their
    denominator.
    """
    lcm = get_lcm(frac1.denominator, frac2.denominator)
    frac1_multiplier = lcm/frac1.denominator
    frac2_multiplier = lcm/frac2.denominator

    frac1 *= frac1_multiplier
    frac2 *= frac2_multiplier


class Fraction(object):
    """A basic fraction class.

    Allows fraction addition, subtraction, multiplication and
    division. Also allows for the operation Fraction*=int/float. This could be extended
    to have more fraction functionality but it is appropriate for the given scope.

    Attributes:
        numerator: The fraction numerator.
        denominator: The fraction denominator.
    """
    
    def __init__(self, numerator, denominator):
        """Initialises the fraction using the given numerator and denominator but
        will convert to lower (lowest) terms if possible."""
        
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.to_lowest_terms()
        
    def to_lowest_terms(self):
        """Convert the fraction to lowest possible terms."""
        gcd = 1.0/get_gcd(self.numerator, self.denominator)
        self *= gcd

    def _div_fraction(self, other):
        """Divide by a fraction.

        Args:
            other: any Fraction object.
        """
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def _mul_fraction(self, other):
        """Multiply by a fraction.

        Args:
            other: any Fraction object.
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def _add_fraction(self, other):
        """Add a fraction.

        Args:
            other: any Fraction object.
        """
        convert_to_lcm(self, other)
        result = Fraction(self.numerator + other.numerator, self.denominator)
        self.to_lowest_terms()
        other.to_lowest_terms()
        return result

    def _sub_fraction(self, other):
        """Subtract a fraction.

        Args:
            other: any Fraction object.
        """
        convert_to_lcm(self, other)
        result = Fraction(self.numerator - other.numerator, self.denominator)
        self.to_lowest_terms()
        other.to_lowest_terms()
        return result

    def _imul_number(self, other):
        """Multiply self by a number.

        Args:
            other: any number.
        """
        self.numerator *= other
        self.denominator *= other
        

    def __add__(self, other):
        """Define + operator."""
        if type(other) is Fraction:
            return self._add_fraction(other)

    def __sub__(self, other):
        """Define - operator."""
        if type(other) is Fraction:
            return self._sub_fraction(other)

    def __mul__(self, other):
        """Define * operator."""
        if type(other) is Fraction:
            return self._mul_fraction(other)

    def __div__(self, other):
        """Define / operator."""
        if type(other) is Fraction:
            return self._div_fraction(other)

    def __imul__(self, other):
        """Define *= operator."""
        if type(other) in (int, float):
            self._imul_number(other)

    def __repr__(self):
        return "Fraction(numerator={0},denominator={1})".format(self.numerator,
            self.denominator)

    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)
