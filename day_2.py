
"""
h1)The Spam Detector (Search in Stream) - linear search
A cybersecurity intern has a blacklist of spam sender IDs. The blacklist is not sorted. Check whether an incoming sender ID exists in the blacklist.
"""

blacklist = ["info3", "prama", "hack101", "info1"]

sender = input("Enter Sender ID: ")

for index in range(len(blacklist)):
    if blacklist[index] == sender:
        print("Spam sender found at index:", index)
        break
else:
    print("Sender is safe.")

"""
h2)The E-Commerce Price Filter (First occurrence ≥ Target) – Binary Search (Lower Bound)
Problem

Products are sorted by price. Find the first product whose price is greater than or equal to ₹50,000.
"""

def first_product(prices, target):
    left = 0
    right = len(prices) - 1
    result = -1

    while left <= right:
        middle = (left + right) // 2

        if prices[middle] >= target:
            result = middle
            right = middle - 1
        else:
            left = middle + 1

    return result


prices = [58000,64000,74000,92000,44000,124000]

target = int(input("Enter target price: "))

position = first_product(prices, target)

if position == -1:
    print("No product found")
else:
    print("First product:", prices[position])
    print("Position:", position)

"""
h3)Merge Sort - The IRCTC Waitlist Merger
IRCTC has two separately sorted waitlists - one from its mobile app, one from railway counters. 
To produce a final unified waitlist, they don't re-sort from scratch. They merge both sorted lists 
in one pass - compare the front of each list, pick the smaller token, advance. This is exactly merge 
sort's merge step.
"""

mobile_app = [20,14,67,25]
railway_counter = [10,20,30,40,50]

x = 0
y = 0
merge = []

while x < len(mobile_app) and y < len(railway_counter):

    if mobile_app[x] <= railway_counter[y]:
        merge.append(mobile_app[x])
        x += 1
    else:
        merge.append(railway_counter[y])
        y += 1

merge.extend(mobile_app[x:])
merge.extend(railway_counter[y:])

print("Merged Waitlist:")
print(merge)
