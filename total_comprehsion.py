# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here

print("--------------")
mapped_list = [n * 100 for n in my_numbers]
print("MAPPED LIST", mapped_list)

print("--------------")
print("FILTERED LIST W/ MATCHES", list(filter(lambda n: n>3, my_numbers)))

print("--------------")
print("FILTERED LIST W/O MATCHES", list(filter(lambda n: n>8, my_numbers)))

print("--------------")
mapped_filtered_list= [n*100 for n in my_numbers if n>3]
print("MAPPED AND FILTERED LIST", mapped_filtered_list)
