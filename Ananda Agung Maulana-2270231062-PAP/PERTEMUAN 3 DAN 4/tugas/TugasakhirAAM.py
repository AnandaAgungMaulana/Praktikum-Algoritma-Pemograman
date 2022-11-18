# NAMA  : ANANDA AGUNG MAULANA  
# NIM   : 2270231062
# KELAS : P2K

print("**TOKO KECANTIKAN L'OCITANE **")
print("\n")
PRODUK = {
    "ALMOND FIRMING MILK":5500000,
    "RESET OIL SERUM":1700000,
    "SHEA BUTTER":475000,
    "VERBENA EDT":580000,
    "LAVENDER":580000,
    "AROMACHOLOGY":5500000,
    "SHEA HOLIDAY":7500000
}
for i in PRODUK:
    print("Daftar: ", i,"\t Harga: ",PRODUK[i])
print("+++Pembelian di atas Rp2.500.000 diskon 30%+++")
print("FORMAT PEMESANAN MOHON DI ISI BRADER :)")
nama_pelanggan = input("Nama: ")
alamat = input("Alamat: ")
no = input("No Telfon: ")
beli = input("Nama Barang: ")
Jumlah = int(input("Jumlah Pembelian: "))
bayar = Jumlah*PRODUK[beli]
if bayar > 2500000:
    diskon = bayar * 30/100
    total = bayar - diskon
else:
    total = bayar
print("\n")

print("= = = = = = = RINCIAN PESANAN PRODUK  = = = = = = =")
print("Nama Pemesan                                 :",nama_pelanggan)
print("Alamat Pemesan                               :",alamat)
print("Nomer telfon                                 :",no)
print("Sparepart yang dipilih                       :",beli)
print("Jumlah Barang                                :",Jumlah)
print("Total Pembayaran                             : Rp.",bayar)
print("Total Keseluruhan dengan diskon/tanpa diskon : Rp.",total)
import datetime as dt
hari_ini = dt.date.today()
print("Tanggal Pembelian                            :",hari_ini)
print("\n")
print("PEMBAYARAN KE REK. BCA 5775715836")
print("A/N ANANDA AGUNG MAULANA")
print("T H A N K S B R A D E R")