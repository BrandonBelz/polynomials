The goal of this project is to provide an interesting way to work with polynomials in Python. I'm not sure if anyone's done this before,
or even if it has any particular use-case, but I just learned about classes and objects as a computer science major, and I thought this sounded fun.
I am trying to add as many features as I can think of, including doing operations between polynomials, differentiating and integrating them, evaluating them at points, etc.
This is mostly for fun, but if someone can find a use for it then I'd be very excited!

A Polynomial object is created with the Polynomial() constructor with any number of integer arguments. These arguments become the coefficients of your polynomial,
with the last being the constant and the first being the coefficient of the highest degree term. This means that the degree of the polynomial is one less than the
number of arguments passed. For example,

     Polynomial(1, -3, 4, 7)

would be the polynomial

     x^3 - 3x^2 + 4x + 7

As of right now, the only things you can do with these polynomials is add, subtract, multiply, and divide them
together and with integers, as well as represent them as strings.
