class Laundry:
  def __init__(self, nama_pelanggan, berat):
    self.nama = nama_pelanggan
    self.berat = berat
    self.harga_per_kg = 7000
    self.total = 0
    self.status = "Belum selesai"
    self.estimasi = 0
    self.__kode_transaksi = self.__generate_kode()  

  def __generate_kode(self):
    import random
    return f"TRX{random.randint(1000,9999)}"

  def hitung_biaya(self):
    self.total = self.berat * self.harga_per_kg
    return self.total

  def hitung_estimasi(self):
    self.estimasi = self.berat // 2
    if self.estimasi == 0:
      self.estimasi = 1

  def selesai(self):
    self.status = "Selesai"

  def tampilkan_info(self):
    print(f"Nama: {self.nama}")
    print(f"Berat: {self.berat} kg")
    print(f"Total Biaya: Rp{self.total}")
    print(f"Estimasi: {self.estimasi} hari")
    print(f"Status: {self.status}")
    print("======================")