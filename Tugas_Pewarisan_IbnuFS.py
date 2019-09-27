class radio(object):
   def __init__(self, a, g, r):
      self.panjang = a
      self.lebar = g
      self.tinggi = r

   def hitungvolume(self):
      return self.panjang * self.lebar * self.tinggi

   def cetakA(self):
      print("Panjang = ", self.panjang)
      print("lebar = ", self.lebar)
      print("tinggi = ", self.tinggi)
      print("Warna = ", self.warna)

   def cetakvolumeA(self):
      print("Volume\t= ", self.hitungvolume())

class tape(object):
   def __init__(self, y, n, t):
      self.panjang = y
      self.lebar = n
      self.quantity = t

   def hitungluas(self):
      return self.panjang * self.lebar

   def cetakB(self):
      print("panjang = ", self.panjang)
      print("lebar = ", self.lebar)
      print("Kuantitas = ", self.quantity)

   def cetakluasB(self):
      print("Volume\t= ", self.hitungluas())

class pemutarmusik(radio, tape):
   def __init__(self, a, g, r, y, n, i, t):
      radio.__init__(self, a, g, r)
      tape.__init__(self, y, n, i)
      self.warna = t
   def cetakC(self):
      print("Warna = ", self.warna)

def main():

   objek = pemutarmusik (2, 3, 4, 5, 6, "DUA", "HIJAU")


   objek.cetakA()
   objek.cetakvolumeA()

   objek.cetakB()
   objek.cetakluasB()

   objek.cetakC()

if __name__ == "__main__":
   main()
