# Decimal to Binary converter.


def dtbconverter(num, decimal_accuracy = 7):
    """ Function inputs a float value and returns a list as output """
    decimal_accuracy = 7

    # The part before decimal point in List<string> format
    whole = []
    # The part after decimal point in List<string> format
    fractional = ['.']

    # Extract fractional number part of decimal
    mantissa = round(num % 1, decimal_accuracy)
    # Extract whole number part of decimal.
    w_num = int(num)

    i = 0     # Counter

    # Loop to find binary of mantissa part
    while i < decimal_accuracy:
        mantissa = mantissa * 2
        mantissa = int(mantissa // 1)
        fractional.append(str(mantissa))
        # Extacting mantissa
        mantissa = round(mantissa % 1, decimal_accuracy)
        if mantissa == 0:
            break  # Removes trailing zeros.
        i = i + 1

    # Loop to find binary of whole number part.
    while w_num != 0:
        whole.append(w_num % 2)
        w_num = w_num // 2
    whole.reverse()

    binary = whole + fractional
    return "".join(binary)

def main():
    print("Call the function as dtbconverter(Number [, Decimal Accuracy (7) ] ) \n")
    print(print("The Binary Equivalant of 1: " + dtbconverter(1))
    print(print("The Binary Equivalant of 2: " + dtbconverter(2))
    print(print("The Binary Equivalant of 10: " + dtbconverter(10))
    print(print("The Binary Equivalant of 55: " + dtbconverter(55))
    print(print("The Binary Equivalant of 55.55: " + dtbconverter(55.55))
    print(print("The Binary Equivalant of 0.3: " + dtbconverter(0.3))
    print(print("The Binary Equivalant of 9876.4321: " + dtbconverter(9876.4321))
         

if __name__ == '__main__':
    main()

