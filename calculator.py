class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        des = 1
        if (a < 0 or b < 0) and (a > 0 or b > 0):
            des = -1
            if (a < 0):
                a = -a
            elif (b < 0):
                b = -b
        while a >= b:
            a = self.subtract(a, b)
            result += des
        return result
    
    def modulo(self, a, b):
        start_a = a
        start_b = b
        if (a < 0 or b < 0) and (a > 0 or b > 0):
            b = -b
        while True:
            a = a-b
            if start_b < 0:
                if start_a > 0 and a - b < start_b:
                    break
                elif start_a < 0 and a - b > 0:
                    break
            elif start_b > 0:
                if start_a < 0 and a - b > start_b and a > 0:
                    break
                elif start_a > 0 and a - b < 0:
                    break
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))