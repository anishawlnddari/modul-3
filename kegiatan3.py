random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk memisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
str_values = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai data int yang di dalam dictionary dipisahkan menjadi satuan, puluhan, dan ratusan
def map_int_values(value):
    if isinstance(value, int):
        return {"ratusan": value // 100, "puluhan": (value // 10) % 10, "satuan": value % 10,}
mapped_int_values = list(map(map_int_values, int_values))

# Output
print("Data Float: \n", float_values)
print("Data Int: \n", mapped_int_values)
print("Data String: \n", str_values)
