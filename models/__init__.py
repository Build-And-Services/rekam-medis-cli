import utils
import os

path = os.path.abspath(os.getcwd()) +  "/data/rekam.json"


# fungsi pendukung
def filter(data, fn):
  return [] if len(data) == 0 else [data[0]] + filter(data[1:], fn) if fn(data[0]) else filter(data[1:], fn)

def search(data, fn):
  return {} if len(data) == 0 else data[0] if fn(data[0]) else search(data[1:], fn)

def searchIndex(data, fn, n = 0):
  return None if len(data) == 0 else n if fn(data[0]) else searchIndex(data[1:], fn, n + 1) 

# pengolah data
class RekamMedis:
  def __init__(self):
    self.data = []
    self.error = None
  
  def load(self):
    # mengload semua data dari database
    self.data, self.error = utils.load(path)
    return self

  def store(self, newData):
    # untuk append ke data class ini
    self.data.append(newData)
    # untuk menyimpan di database
    self.error = None if utils.store(self.data, path) else "gagal menyimpan data"
    return self

  def getOne(self, nik):
    # kondisi nik sama
    kondisi = lambda n: True if n["nik"] == nik  else False
    # mengembalikan item yang nik nya sama
    return search(self.data, kondisi)

  def delete(self, nik):
    # cek nik
    kondisi = lambda n: True if n["nik"] != nik  else False
    # filter yang bukan nik yg dipilih
    self.data = filter(self.data, kondisi)
    self.error = None if utils.store(self.data, path) else "gagal menghapus data"
    return self

  def edit(self, nik, form):
    # mencocokan nik
    kondisi = lambda n: True if n["nik"] == nik  else False
    #  get index
    index = searchIndex(self.data, kondisi)
    self.data[index] = form 
    # menyimpan di database
    self.error = None if utils.store(self.data, path) else "gagal mengedit data"
    return self
  
  def count(self):
    return len(self.data)

  def result(self):
    return self.data

  def catch(self):
    return self.error