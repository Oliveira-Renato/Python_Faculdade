class Televisao:
  def _init_(self):
    self.volume = 10
    
  def aumentar_volume(self):
    self.volume += 1
    print(self.volume)
    
  def diminuir_volume(self):
    self.volume -= 1
    print(self.volume)

    
tv = Televisao()
tv.aumentar_volume()
tv.diminuir_volume()
tv.diminuir_volume()