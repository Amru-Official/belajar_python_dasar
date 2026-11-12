matriks1 = [[1,2],[4,5]]
matriks2 = [[1,2],[3,4],[1,3]]
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


if len(matriks1) == len(matriks2):
    for isi1 in matriks1 : 
        for isi2 in matriks2 : 
            for isinya1 in isi1 : 
                for isinya2 in isi2 : 
                    if matriks1.index(isi1) == matriks2.index(isi2) and isi1.index(isinya1) == isi2.index(isinya2):
                        print(f"{isinya1}+{isinya2} = {isinya1+isinya2}") 
else:
    print("maaf input matriks anda memiliki ordo yang berbeda")

  
            
        
