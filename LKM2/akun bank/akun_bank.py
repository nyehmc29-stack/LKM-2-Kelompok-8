class AkunBank:
  def __init__(self, nomor, pemilik, saldo):
    self.nomor = nomor 
    self.pemilik = pemilik
    self.saldo = saldo
    self.riwayat = []

  def cek_saldo(self):  
    print(f"Saldo {self.pemilik}: Rp{self.saldo}")
    
  def tarik_tunai(self, jumlah):
    if jumlah <= 0:
      print("Jumlah harus lebih dari 0!")
    elif jumlah <= self.saldo:
      self.saldo -= jumlah
      pesan = f"{self.pemilik} menarik Rp{jumlah}"
      self.riwayat.append(pesan)
      print (pesan)
    else:
      print("Saldo tidak cukup!")
  
  def transfer(self, tujuan, jumlah,):
    biaya_admin = 2500
    total = jumlah + biaya_admin
    if jumlah <= 0:
      print("Jumlah harus lebih dari 0!")
    elif self.saldo >= total:
      self.saldo -= total
      tujuan.saldo += jumlah
      pesan_kirim=f"Transfer Rp{jumlah} ke {tujuan.pemilik} Berhasil!. Biaya admin Rp.2500,saldo Rp{self.saldo}"
      pesan_terima = f"Menerima Rp{jumlah} dari {self.pemilik}, saldo Rp{tujuan.saldo}"
      self.riwayat.append(pesan_kirim)
      tujuan.riwayat.append(pesan_terima)
    else:
      print("Transfer Gagal: Saldo tidak cukup.")
  def tampilkan_riwayat(self):
    print(f"\nRiwayat transaksi {self.pemilik}:")
    for r in self.riwayat:
      print(r)
  
  #