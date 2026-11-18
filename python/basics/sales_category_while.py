
sales = {
    "January": 1200,
    "February": 800,
    "March": 1500,
    "April": 600,
    "May": 1800
}

items = list(sales.items())
i = 0

high_count = 0
medium_count = 0
low_count = 0

while i < len(items):
    if items[i][1] > 1500:
        print(items[i][0], "High")
        high_count = high_count + 1
    elif 700 <= items[i][1] <= 1500:
        print(items[i][0], "Medium")
        medium_count = medium_count + 1
    else:
        print(items[i][0], "Low")
        low_count = low_count + 1

    i = i + 1

print("High", high_count)
print("Medium", medium_count)
print("Low", low_count)
