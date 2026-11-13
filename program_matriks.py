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

def penjumlahan_matriks(matriks1,matriks2):
    matriks = []
    for index_colomn, values in enumerate(matriks1): # 0 [1,3] kolom 1
        isi_matriks = []
        for index_raw, value in enumerate (values): # 0 1 kolom 1 baris 1 , 0 3 kolom 1 baris 2
            print(index_colomn,values)
            isi = matriks2[index_colomn][index_raw]
            hasil=isi+value
            isi_matriks.append(hasil)
        matriks.append(isi_matriks)
    return matriks

hasil = penjumlahan_matriks(matriks1, matriks2)
print(hasil)
  
        
