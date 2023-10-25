def convert_to_minutes(weeks):
    def convert_days(days):
        def convert_hours(hours):
            def convert_minutes(minutes):
                return weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes
            return convert_minutes
        return convert_hours
    return convert_days

# Data input
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Proses konversi
output_data = []
for item in data:
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    
    result = convert_to_minutes(weeks)(days)(hours)(minutes)
    output_data.append(result)

# Output
print(output_data)
