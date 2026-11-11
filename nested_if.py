# belajar nested if 
cuaca=input("masukan cuaca hari ini (hujan,salju,semi,gugur)")
happyness=input("bagaimana kondisi anda (senang,sedih)")
# fungsi pilih menu minuman sesuai suasana hati

def pilih_minuman(value):
    if value=="senang":
        minuman_senang = ["soda gembira","susu gembira","madu gembira"]
        for minuman in minuman_senang:
            print(f"{minuman_senang.index(minuman)+1}. {minuman}")
        pilihan_minuman=int(input("masukan nomor minuman :"))
        return minuman_senang[(pilihan_minuman-1)]
    else:
        minuman_penyemangat=["soda semangat","susu semangat","madu semangat"]
        for minuman in minuman_penyemangat:
            print(f"{(minuman_penyemangat.index(minuman)+1)}. {minuman}")
        pilihan_minuman=int(input("masukan nomor minuman :"))
        return minuman_penyemangat[(pilihan_minuman-1)]

minuman=pilih_minuman(happyness)
    
if cuaca=="hujan":
    if happyness=="senang":
        print(f"enaknya cuaca {cuaca} dan hati {happyness} minum {minuman} sangat cocok")
    else:
        print(f"sayang sekali cuaca {cuaca} dan hati {happyness}, lebih baik minum {minuman} kemudian tidur saja...")
elif cuaca=="salju":
    if happyness=="senang":
        print(f"enaknya cuaca {cuaca} dan hati {happyness} minum {minuman} sangat cocok")
    else:
        print(f"sayang sekali cuaca {cuaca} dan hati {happyness}, lebih baik minum {minuman} kemudian tidur saja...")
elif cuaca=="semi":
    if happyness=="senang":
        print(f"enaknya cuaca {cuaca} dan hati {happyness} minum {minuman} sangat cocok")
    else:
        print(f"sayang sekali cuaca {cuaca} dan hati {happyness}, lebih baik minum {minuman} kemudian tidur saja...")
elif cuaca=="gugur":
    if happyness=="senang":
        print(f"enaknya cuaca {cuaca} dan hati {happyness} minum {minuman} sangat cocok")
    else:
        print(f"sayang sekali cuaca {cuaca} dan hati {happyness}, lebih baik minum {minuman} kemudian tidur saja...")