import os
from models import RekamMedis

def table(data):
  # header
  column = [ "| "+" | ".join([key for key in data[0].keys()])+" |"]
  data = ["| "+" | ".join([str(values) for values in item.values()])+" |" for item in data]
  return column + data

def formInput():
  os.system("cls")
  try:
    data = {
      "nama" : input("Nama Pasien: "),
      "nik" : input("Nik Pasien: "),
      "tanggal" : input("Tanggal Lahir Pasien: "),
      "gender" : input("Gender Pasien [Pria/Wanita]: ").lower(),
      "alamat" : input("Alamat Pasien: "),
      "Umur" : int(input("Umur Pasien : ")),
      "keluhan": input("Keluhan Pasien : ")
    }
    return data
  except ValueError as e:
    input("Terjadi kesalahan input ulangi lagi! [ENTER]")
    formInput()
    

def display(data):
  os.system("cls")
  print('''
    1. Read Data
    2. Add Data
    3. Edit Data
    4. Delete Data
  ''')
  menu = input("Pilih Menu : ")

  if menu == "1":
    count =  data.count() 

    print("[x] Data Tidak ada....." if count == 0 else "\n".join(table(data.result())))
  elif menu == "2":
    form = formInput()
    print("berhasil ditambah [ENTER]" if data.store(form).catch() == None else "Gagal Ditambah  [ENTER]")
  elif menu == "3":
    count =  data.count() 
    fetch = table(data.result())
    print("[x] Data Tidak ada....." if count == 0 else "\n".join(fetch))
    nik = input("Masukan NIK Pasien: ")
    os.system("cls")
    print(data.getOne(nik))
    input("Enter untuk melanjutkan....")
    form = formInput()
    print("berhasil diedit [ENTER]" if data.edit(nik, form).catch() == None else "Gagal diedit  [ENTER]")
  elif menu == "4":
    count =  data.count() 
    print("[x] Data Tidak ada....." if count == 0 else "\n".join(table(data.result())))
    nik = input("Masukan NIK Pasien: ")
    print("berhasil dihapus [ENTER]" if data.delete(nik).catch() == None else "Gagal dihapus  [ENTER]")
    
  input("Enter any where....")
  display(data)

if __name__ == "__main__":
  data = RekamMedis()
  data = data.load()
  display(data)