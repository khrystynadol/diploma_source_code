import matplotlib.pyplot as plt

# years = [2020, 2021, 2022, 2023, 2024, 2025]
# results = [2150, 2900, 3950, 4830, 5830, 1960]

# SER
# 2025 1,960
# 2024 5,830
# 2023 4,830
# 2022 3,950
# 2021 2,900
#
# 2020 2,150
# 2015 687
# 2010 269
# 2005 77
# 2000 3
# years = [2020, 2021, 2022, 2023, 2024, 2025]
# results = [2150, 2900, 3950, 4830, 5830, 1960]
# years = [2000, 2005, 2010, 2015, 2020, 2021, 2022, 2023, 2024, 2025]
# results = [3, 77, 269, 687, 2150, 2900, 3950, 4830, 5830, 1960]

# TEС
# 2025 122
# 2024 421
# 2023 311
# 2022 272
# 2021 180
#
# 2020 106
# 2015 17
# 2010 7
# 2005 0
# 2000 0

# years = [2020, 2021, 2022, 2023, 2024, 2025]
# results = [2150, 2900, 3950, 4830, 5830, 1960]
years = [2000, 2005, 2010, 2015, 2020, 2021, 2022, 2023, 2024, 2025]
results = [0, 0, 7, 17, 106, 180, 272, 311, 421, 122]

plt.figure(figsize=(10, 6))
# plt.plot(years, results, marker='o', linestyle='-', color='navy')
plt.bar(years, results, color='skyblue')

plt.title('Number of Google Scholar Results per Year (Text emotion recognition)')
plt.xlabel('Year')
plt.ylabel('Number of Results')
plt.xticks(years, rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()
