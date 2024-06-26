class Polynomial:
    def __init__(self, *nums: int):
        values = list(nums)
        if len(values) == 0:
            self.coefficients = [0]
            self.degree = 0
            return
        while values[0] == 0:
            values.remove(0)
            if len(values) == 0:
                break
        if len(values) == 0:
            self.coefficients = [0]
            self.degree = 0
            return
        else:
            self.coefficients = values
            self.degree = len(values) - 1
            return
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
                    if self.coefficients[i] == 1:
                        string += " + x"
                    elif self.coefficients[i] == -1:
                        string += " - x"
                    elif self.coefficients[i] < 0:
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
            if self.degree == other.degree:
                for i in range(self.degree + 1):
                    diff.append(self.coefficients[i] - other.coefficients[i])
                return Polynomial(*diff)
            elif self.degree > other.degree:
                for i in range(self.degree - other.degree):
                    diff.append(self.coefficients[i])
                for i in range(self.degree - other.degree, self.degree + 1):
                    diff.append(self.coefficients[i] - other.coefficients[i - self.degree + other.degree])
                return Polynomial(*diff)
            else:
                for i in range(other.degree - self.degree):
                    diff.append(-other.coefficients[i])
                for i in range(other.degree - self.degree, other.degree + 1):
                    diff.append(self.coefficients[i - other.degree + self.degree] - other.coefficients[i])
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
        elif isinstance(other, Polynomial):
            product = Polynomial()
            for i in range(self.degree + 1):
                partial = []
                for num in other.coefficients:
                    partial.append(self.coefficients[i] * num)
                for j in range(self.degree - i):
                    partial.append(0)
                product = product + Polynomial(*partial)
            return product
    def __rmul__(self, other):
        return self * other
    def __neg__(self):
        return 0 - self
    def __floordiv__(self, other):
        if isinstance(other, Polynomial):
            quotient, remainder = Polynomial(), self
            while other.degree <= remainder.degree:
                factor_int = [remainder.coefficients[0] // other.coefficients[0]]
                if factor_int == [0]:
                    return quotient
                for i in range(remainder.degree - other.degree):
                    factor_int.append(0)
                quotient = Polynomial(*factor_int) + quotient
                remainder = remainder - other * Polynomial(*factor_int)
            return quotient
    def __mod__(self, other):
        if isinstance(other, Polynomial):
            remainder = self
            while other.degree <= remainder.degree:
                factor_int = [remainder.coefficients[0] // other.coefficients[0]]
                if factor_int == [0]:
                    return remainder
                for i in range(remainder.degree - other.degree):
                    factor_int.append(0)
                remainder = remainder - other * Polynomial(*factor_int)
            return remainder
    def __call__(self, x: int | float) -> int | float:
        if isinstance(x, int) or isinstance(x, float):
            y = 0
            for i in range(-1, -len(self.coefficients) - 1, -1):
                y += self.coefficients[i] * x**(-i - 1)
            return y
    def __iadd__(self, other):
        self = self + other
        return self
    def __isub__(self, other):
        self = self - other
        return self
    def __imul__(self, other):
        self = self * other
        return self
    def __imod__(self, other):
        self = self % other
        return self
    def __ifloordiv__(self, other):
        self = self // other
        return self
    def __pow__(self, other: int):
        if other < 0:
            return Polynomial()
        else:
            product = Polynomial(1)
            for _ in range(other):
                product *= self
            return product