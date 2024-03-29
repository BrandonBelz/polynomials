class Polynomial:
    def __init__(self, *nums: int):
        if len(nums) == 0:
            self.coefficients = [0]
            self.degree = 0
        else:
            self.coefficients = list(nums)
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
            if len(self.coefficients) == len(other.coefficients):
                for i in range(len(self.coefficients)):
                    sum.append(self.coefficients[i] + other.coefficients[i])
                return Polynomial(*sum)
    def __sub__(self, other):
        if isinstance(other, Polynomial):
            diff = []
            if len(self.coefficients) == len(other.coefficients):
                for i in range(len(self.coefficients)):
                    diff.append(self.coefficients[i] - other.coefficients[i])
                return Polynomial(*diff)