import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [17, 20, 22, 25]

colors = ["Red","Blue","Green","Orange"]

plt.figure(figsize=(8, 4))
plt.bar(categories, values, color=colors) # You can use color names, hex codes, or RGB tuples
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Single Color Bar Chart')
plt.show()