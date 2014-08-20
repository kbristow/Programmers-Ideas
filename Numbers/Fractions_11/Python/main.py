import fractions
import operator

def get_operator():
    """Gets a function used to perform the user requested arithmetic
    operation.
    """
    new_operator = ""
    operator_map = {"add":operator.add,
                    "subtract":operator.sub,
                    "multiply":operator.mul,
                    "divide":operator.div}
    while not operator_map.has_key(new_operator):
        new_operator = raw_input("Enter operator (add, substract, multiply,divide): ").lower()

    return operator_map[new_operator]
    

def get_fractions():
    """Gets a list of user entered fractions."""
    fraction_list = []
    new_fraction_str = None
    while not new_fraction_str == "exit":
        new_fraction_str = raw_input("Enter a fraction (exit to stop):")
        new_fraction_obj = fractions.convert_fraction_str(new_fraction_str)
        if type(new_fraction_obj) == fractions.Fraction:
            fraction_list.append(new_fraction_obj)

    return fraction_list
        

frac_operator = get_operator()
fraction_list = get_fractions()

#Perform selected operation across all entered fractions
total_fraction = fraction_list[0]
for fraction in fraction_list[1:]:
    total_fraction = frac_operator(total_fraction, fraction)

print (total_fraction)
