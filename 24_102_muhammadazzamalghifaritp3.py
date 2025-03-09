
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
output = "Tahun kabisat antara 2001 hingga 2024 adalah: "

for year in range(2001, 2025):
    if is_leap_year(year):
        output += str(year) + " "
print(output)





