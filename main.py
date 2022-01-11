p = print
nm=[]
nim=[]
mtkul=[]


print("Masukan data mahasiswa")
mtp = input("Nama      :")
op= int(input("NIM       :"))
ov = input("matakuliah     :")


while (True):
    o = ''
    o = input ("T)ambah, U)bah, H)apus, C)ari, B)erhenti: ")

    if o.lower() == 'B':
        break

    elif o == 'T':
        pass
        nama = input("O      :")
        nm.append(nama)
        Nim = int(input("NIM       :"))
        nim.append(Nim)
        matkul = input("matakuliah     :")
        mtkul.append(matkul)

    elif o == 'H':
        pass
        del nm[0]
        del nim[0]
        del mtkul[0]
        print ("")

    elif o == 'U':
        target = input(" Masukan Nama : ")
        objek = input (" Masukan nim : ")
        predikat = input  (" masukan mata kuliah")
        nm = []
        for l in '':
            if l == '':
                pass
            else:
                target = l.replace('Nama : ', '')
                objek = l.replace('Nim : ',"")
                predikat = l.replace('matkul :''')

                if  str(target, objek, predikat):
                    p('BERHASIL MENGHAPUS Data %s' % (target, objek, predikat))
                    pass
                else:
                    nm.append(str(l) + '\n')

    elif o == 'C':
        pass
    maka = True
    for i in range (len(nim)):
        if maka:
            print("nama\tnim\tmatkul")
            print(nim[i]['nama'],'\t',nim[i]["nim"],'\t',nim[i]["matkul"])
            penentu = False
