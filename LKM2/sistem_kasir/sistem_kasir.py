class Produk:
  def __init__(self, nama, harga, stok):
    self.nama = nama
    self.harga = harga
    self.stok = stok

class Keranjang:
  def __init__(self):
    self.daftar_barang = {}
  
  def tambah_produk(self, produk_baru, jumlah):
    if jumlah > produk_baru.stok:
      print(f"Stok {produk_baru.nama} tidak cukup!")
    elif produk_baru.nama in self.daftar_barang:
      self.daftar_barang[produk_baru.nama]["jumlah"] += jumlah
    else:
      self.daftar_barang[produk_baru.nama] = {
        "produk": produk_baru,
        "jumlah": jumlah
      }
    produk_baru.stok -= jumlah
    print(f"Berhasil menambah: {produk_baru.nama} x{jumlah}")

  def hapus_produk(self, produk, jumlah):
    if produk.nama not in self.daftar_barang:
      print("Produk tidak ada di keranjang!")
    if jumlah > self.daftar_barang[produk.nama]["jumlah"]:
      print("Jumlah hapus melebihi isi keranjang!")
      return

    self.daftar_barang[produk.nama]["jumlah"] -= jumlah
    produk.stok += jumlah

    if self.daftar_barang[produk.nama]["jumlah"] == 0:
      del self.daftar_barang[produk.nama]

    print(f"{produk.nama} dihapus sebanyak {jumlah}")
    
  def hitung_total(self, member=False):
    total = 0
    for item in self.daftar_barang.values():
      total += item["produk"].harga * item["jumlah"]
    if member is True and total > 100000 :
      diskon = total * 0.15
      total -= diskon
      print(f"Diskon member (15%): -Rp{diskon}")
    elif member is False and total > 100000 :
      diskon = total_akhir * 0.1
      print(f"Diskon (10%): -Rp{diskon}")
      total_akhir -= diskon
    ppn = total * 0.11
    print(f"PPN 11%: Rp{ppn}")
    total += ppn
    return total
  
  def bayar(self, uang_diterima, member=False):
    total = self.hitung_total(member)
    print(f"Total bayar: Rp{total}")
    if uang_diterima < total:
      print("Uang tidak cukup!")
      return
    kembalian = uang_diterima - total
    print(f"Kembalian: Rp{kembalian}")
  
  def cetak_struk(self, member=False):
    print("\n=== Struk Belanja ===")
    for item in self.daftar_barang.values():
      produk = item["produk"]
      jumlah = item["jumlah"]
      print(f"- {produk.nama} x{jumlah} : Rp{produk.harga * jumlah}")

    total = self.hitung_total(member)
    print(f"Total Akhir: Rp{total}")
#