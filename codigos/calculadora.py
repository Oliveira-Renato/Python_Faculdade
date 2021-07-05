class Calculadora:
  def somar(self, n1, n2):
    return n1 + n2
  def subtrair(self, n1, n2):
    return n1 - n2
  def multiplicar(self, n1, n2):
    return n1 * n2
  def dividir(self, n1, n2):
    return n1 / n2
  def dividir_resto(self, n1, n2):
    return n1 % n2

calc1 = Calculadora()
print(calc1.somar(3,4))

calc2 = Calculadora()
print(calc2.somar(6,4))
print(calc1.somar(3,4))