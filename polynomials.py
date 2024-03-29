class Polynomial:
    def __init__(self, *nums):
        if len(nums) == 0:
            self.coefficients = [0]
            self.degree = 0
        else:
            self.coefficients = list(nums)
            self.degree = len(nums) - 1
    def __str__(self) -> str:
        string = ''
        for i in range(len(self.coefficients)):
            string += f" {self.coefficients[i]}x^{self.degree - i} "
        return string.strip().replace("  ", " + ")