matriks1 = [[1,3],[4,5],[3,1]]
matriks2 = [[2,2],[3,4],[1,3]]
# matriks2 = [[1,2],[3,4],[1,3]] baris 2 kolom 3

# fungsi menghitung ukuran matriks
def ukuran_matriks(value,ukuran=None):
    if ukuran==None:
        ukuran = {}
        kolom = len(value)
        ukuran["kolom"]=kolom
    for matriks in value:
        if len(matriks)!=len(value[0]):
            print("panjang antar baris anda tidak sama")
    ukuran["baris"]=len(value[0])
    # print(ukuran)
    return ukuran

ukuran_matriks1=ukuran_matriks(matriks1)
ukuran_matriks2=ukuran_matriks(matriks2)
print(ukuran_matriks2.get("kolom"))

# fungsi membandingkan ukuran matriks
def bandingkan_ukuran(value1,value2):
    if value1.get("baris")==value2.get("baris") and value1.get("kolom")==value2.get("kolom"):
        return True
    else: 
        print("ukuran matriks berbeda")
        return False
    
print(bandingkan_ukuran(ukuran_matriks1,ukuran_matriks2))

# fungsi penjumlahan matriks
# def penjumlahan_matriks(values1,values2):
#     if bandingkan_ukuran(ukuran_matriks1,ukuran_matriks2)==True:
#         for indeks1, value1 in enumerate(values1):
#             for isi_indeks1, isi_value1 in enumerate(value1):
#                 for indeks2, value2 in enumerate(values2):
#                     for isi_indeks2, isi_value2 in enumerate(value2):
#                         if indeks1 == indeks2 and isi_indeks1==isi_indeks2:
#                             print(isi_value1+isi_value2)
                

        
# penjumlahan_matriks(matriks1,matriks2)

def penjumlahan_matriks(values1, values2):
    # Buat list penampung utama (matriks hasil)
    hasil_matriks = []
    
    for indeks1, value1 in enumerate(values1):
        # Buat list penampung untuk setiap baris baru
        baris_baru = []
        for isi_indeks1, isi_value1 in enumerate(value1):
            # Ambil nilai pasangannya dari values2 secara langsung
            isi_value2 = values2[indeks1][isi_indeks1]
            
            # Jumlahkan
            jumlah = isi_value1 + isi_value2
            
            # Masukkan ke baris baru (TIDAK PERLU menulis: baris_baru = baris_baru.append(...))
            baris_baru.append(jumlah)
            
        # Masukkan baris yang sudah terisi ke matriks hasil
        hasil_matriks.append(baris_baru)
        
    return hasil_matriks

hasil = penjumlahan_matriks(matriks1, matriks2)
print(hasil)
  
            
        
