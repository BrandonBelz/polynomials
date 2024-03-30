class Polynomial:
    def __init__(self, *nums: int):
        values = list(nums)
        while values[0] == 0:
            values.remove(0)
        if len(nums) == 0:
            self.coefficients = [0]
            self.degree = 0
        else:
            self.coefficients = values
            self.degree = len(nums) - 1
    def __str__(self) -> str:
        string = ''
        if self.degree == 0:
            return f'{self.coefficients[0]}'
        elif self.degree == 1:
            if self.coefficients[0] == 1:
                if self.coefficients[1] == 0:
                    return "x"
                elif self.coefficients[1] < 0:
                    return f"x - {-self.coefficients[1]}"
                else:
                    return f"x + {self.coefficients[1]}"
            elif self.coefficients[0] == -1:
                if self.coefficients[1] == 0:
                    return "-x"
                elif self.coefficients[1] < 0:
                    return f"-x - {-self.coefficients[1]}"
                else:
                    return f"-x + {self.coefficients[1]}"
            else:
                if self.coefficients[1] == 0:
                    return f"{self.coefficients[0]}x"
                elif self.coefficients[1] < 0:
                    return f"{self.coefficients[0]}x - {-self.coefficients[1]}"
                else:
                    return f"{self.coefficients[0]}x + {self.coefficients[1]}"
        else:
            for i in range(len(self.coefficients)):
                if i == 0:
                    if self.coefficients[0] == -1:
                        string += f"-x^{self.degree}"
                    elif self.coefficients[0] == 1:
                        string += f"x^{self.degree}"
                    else:
                        string += f"{self.coefficients[i]}x^{self.degree}"
                elif self.degree == i:
                    if self.coefficients[i] < 0:
                        string += f" - {-self.coefficients[i]}"
                    elif self.coefficients[i] > 0:
                        string += f" + {self.coefficients[i]}"
                elif self.degree == i + 1:
                    if self.coefficients[i] < 0:
                        string += f" - {-self.coefficients[i]}x"
                    elif self.coefficients[i] > 0:
                        string += f" + {self.coefficients[i]}x"
                elif self.coefficients[i] == -1:
                    string += f" - x^{self.degree - i}"
                elif self.coefficients[i] == 1:
                    string += f" + x^{self.degree - i}"
                elif self.coefficients[i] < 0:
                    string += f" - {-self.coefficients[i]}x^{self.degree - i}"
                elif self.coefficients[i] > 0:
                    string += f" + {self.coefficients[i]}x^{self.degree - i}"
            return string
    def __add__(self, other):
        if isinstance(other, Polynomial):
            sum = []
            if self.degree == other.degree:
                for i in range(self.degree + 1):
                    sum.append(self.coefficients[i] + other.coefficients[i])
                return Polynomial(*sum)
            elif self.degree > other.degree:
                for i in range(self.degree - other.degree):
                    sum.append(self.coefficients[i])
                for i in range(self.degree - other.degree, self.degree + 1):
                    sum.append(self.coefficients[i] + other.coefficients[i - self.degree + other.degree])
                return Polynomial(*sum)
            else:
                for i in range(other.degree - self.degree):
                    sum.append(other.coefficients[i])
                for i in range(other.degree - self.degree, other.degree + 1):
                    sum.append(other.coefficients[i] + self.coefficients[i - other.degree + self.degree])
                return Polynomial(*sum)
        if isinstance(other, int):
            sum = self.coefficients
            sum[-1] += other
            return Polynomial(*sum)
    def __sub__(self, other):
        if isinstance(other, Polynomial):
            diff = []
            if len(self.coefficients) == len(other.coefficients):
                for i in range(len(self.coefficients)):
                    diff.append(self.coefficients[i] - other.coefficients[i])
                return Polynomial(*diff)
        if isinstance(other, int):
            diff = self.coefficients
            diff[-1] -= other
            return Polynomial(*diff)
    def __rsub__(self, other):
        if isinstance(other, int):
            diff = self.coefficients
            for i in range(len(diff) - 1):
                diff[i] *= -1
            diff[-1] = other - diff[-1]
            return Polynomial(*diff)
    def __mul__(self, other):
        if isinstance(other, int):
            product = []
            for coefficient in self.coefficients:
                product.append(coefficient * other)
            return Polynomial(*product)
    def __rmul__(self, other):
        return self * other
    def __neg__(self):
        return 0 - self
    
