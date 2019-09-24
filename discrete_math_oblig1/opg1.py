# Formula: a +m b = (a + b) mod m
class Arithmetic_Modulo:
    def __init__(self, _a, _b, _m):
        self.a = _a
        self.b = _b
        self.m = _m

    def addMod(self):
        mod = (self.a + self.b) % self.m
        print("(%i + %i) mod %i = %i" % (self.a, self.b, self.m, mod))

    def multiMod(self):
        mod = (self.a * self.b) % self.m
        print("(%i * %i) mod %i = %i" % (self.a, self.b, self.m, mod))

am = Arithmetic_Modulo(7, 9, 11)
am.addMod()
am.multiMod()