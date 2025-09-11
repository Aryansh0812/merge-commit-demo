class Calculator:
   def __init__(self, a, b):
       self.a = a
       self.b = b

   def add(self):
       return self.a + self.b
    
   def multiply(self):
       return self.a * self.b

   def substract(self):
      return self.a-self.b

test_obj = Calculaor(10,20)
s = test_obj.add()
print(s)

test_obj2 = Calculaor(11,22)
m = test_obj2.multiply
print(m)
