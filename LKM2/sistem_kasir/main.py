from sistem_kasir import Produk, Keranjang

p1 = Produk("Kopi Kenangan", 25000, 7)
p2 = Produk("Susu UHT", 18000, 7)
p3 = Produk("Keyboard Gaming", 250000, 7)


keranjang_saya = Keranjang()
keranjang_saya.tambah_produk(p1, 2)
keranjang_saya.tambah_produk(p2, 1)
keranjang_saya.tambah_produk(p3, 1)

keranjang_saya.hapus_produk(p2, 1)
keranjang_saya.cetak_struk(member=True)
keranjang_saya.bayar(500000, member=True)