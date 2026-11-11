# #program daftar nama kelas
# from itertools import zip_longest
# daftar_nama_siswa = ["Oman","Andre","Ilham","Dedi","Ziman"]
# daftar_hobi_siswa = ["Berpikir","Membaca","Main Game","Menonton"]
# for nama,hobi in zip_longest(daftar_nama_siswa, daftar_hobi_siswa,fillvalue="Empety"):
#     print(f"{nama} : {hobi}")
# daftar_nomor = [1,2,3]

# all_list=[daftar_hobi_siswa,daftar_nama_siswa,daftar_nomor]
# for isi in all_list:
#     print(isi)
# nama =input("masukan nama :")
# umur =int(input("masukan umur :"))
# def sapa(nama,umur):
#     print(f"hai namaku {nama}, umurku {umur} tahun")
# sapa(nama,umur)
# print(daftar_hobi_siswa.append("Awal"))

daftar=["satu","dua","tiga"]
for minuman in daftar:
    print(daftar.index(minuman),minuman)
    print(type(daftar.index(minuman)))