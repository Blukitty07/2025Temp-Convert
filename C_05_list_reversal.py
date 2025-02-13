all_calculations = ['10.0°F to -12°C', '20.0°F to -7°C',
                    '30.0°F to -1°C', '40.0°F to 4°C', '50.0°F to 10°C',
                    '60.0°F to 16°C']

newest_first = list(reversed(all_calculations))


print("==== Oldest to Newest for File ====")
for item in all_calculations:
    print(item)

print()

print("==== Most Recent First ====")
for item in newest_first:
    print(item)

