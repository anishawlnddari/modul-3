# Data input
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi untuk mendapatkan nilai integer
def get_int_values(item):
    parts = item.split()
    return list(filter(lambda x: x.isdigit(), parts))

# Menggunakan fungsi filter untuk setiap elemen data
filtered_data = list(map(get_int_values, data))

# Output
print(filtered_data)

