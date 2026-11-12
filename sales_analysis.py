sales = {
    "January": 1200,
    "February": 800,
    "March": 1500,
    "April": 600,
    "May": 1800
}
items = list(sales.items())
i = 0
total = 0
while i < len(items):
    if items[i][1]> 1000:
        print(items[i][0])
        total = total + items[i][1]
    i = i + 1
print(total)  
