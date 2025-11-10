# ARRAY 
mahasiswa_list = ["Mutia", "Aulia", "Rahma", "Nurma", "Kristia"]
print("Daftar Nama Mahasiswa:", mahasiswa_list)

# Mengakses array
print("Mahasiswa pertama:", mahasiswa_list[0])

# Menambah elemen
mahasiswa_list.append("Misqul")
print("Setelah menambah Misqul:", mahasiswa_list)

# Menghapus elemen
mahasiswa_list.remove("Mutia")
print("Setelah menghapus Mutia:", mahasiswa_list)



# DICTIONARY

mahasiswa = {
    "nama": "Hijriah",
    "nim": "D0425313",
    "jurusan": "Sistem Informasi",
    "kelas": "Sisfo A",
    "angkatan": 2025,
    "alamat": "Konja, Sulawesi Barat",

    "nilai": {
        "algoritma_pemrograman":89,
        "struktur_data": 85,
        "basis_data": 88,
        "pemrograman_python": 90
    },

    "mata_kuliah_diambil": [
        "Algoritma Pemrograman",
        "Basis Data",
        "Pemrograman Python",
        "Kalkulus Informatika"
    ]
}

# Menampilkan data
print("\nData Mahasiswa:", mahasiswa)

# Mengakses data
print("Nama:", mahasiswa["nama"])
print("Kelas:", mahasiswa["kelas"])
print("Nilai Python:", mahasiswa["nilai"]["pemrograman_python"])

# Update nilai
mahasiswa["nilai"]["pemrograman_python"] = 90
print("Nilai Python Setelah Update:", mahasiswa["nilai"]["pemrograman_python"])

# Menambah data baru
mahasiswa["status"] = "Aktif"
print("Setelah menambah status:", mahasiswa)
