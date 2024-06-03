# Sort string datetimes
datetimes = [
    '2023-04-16 15:47',
    '2023-04-17 13:12', 
    '2023-04-16 14:48',
    '2023-04-16 18:39',
    '2023-04-17 12:12', 
]

sorted_datetimes = sorted(datetimes, key=lambda x: (x[:10], x[11:]))
print(sorted_datetimes)

