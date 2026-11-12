matriks1 = [[1,2],[4,5]]
matriks2 = [[1,2],[3,4],[1,3]]

def ukuran_matriks(value,ukuran=None):
    if ukuran==None:
        ukuran = {}
        baris = len(value)
    for matriks in value:
        if len(matriks)==len(value[0]):
            pass
        else:
            print("panjang baris anda tidak sama")
    print("panjang baris sama")
ukuran_matriks(values)
if len(matriks1) == len(matriks2):
    for isi1 in matriks1 : 
        for isi2 in matriks2 : 
            for isinya1 in isi1 : 
                for isinya2 in isi2 : 
                    if matriks1.index(isi1) == matriks2.index(isi2) and isi1.index(isinya1) == isi2.index(isinya2):
                        print(f"{isinya1}+{isinya2} = {isinya1+isinya2}") 
else:
    print("maaf input matriks anda memiliki ordo yang berbeda")

  
            
        
