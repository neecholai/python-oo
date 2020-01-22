"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        "Initialize a number generator with a default start number of 100."
        self.start = start
        self.serial = start

    def __repr__(self):
        return f"<Serial Generator start={self.start} next={self.serial}>"
    
    def generate(self):
        "Increment serial number by one and return. First call returns start number."
        prev_num = self.serial
        self.serial += 1
        return prev_num

    def reset(self):
        "Reset number to intial start value."
        self.serial = self.start 

