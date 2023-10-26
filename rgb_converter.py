# rgb_normalized = (0.753000020980835, 1.0, 1.0)

# # Convert to 8-bit RGB
# rgb_original = tuple(int(component * 255) for component in rgb_normalized)

# print("Original RGB Color:", rgb_original)

# ================================================================

# my_tuple = (1, 2, 3, 2, 4, 3, 5, 6, 6, 7, 8, 7, 9)

# # Create an empty dictionary to store element counts
# element_counts = {}

# # Count the distinct elements and repetitions
# for element in my_tuple:
#     if element in element_counts:
#         element_counts[element] += 1
#     else:
#         element_counts[element] = 1

# # Print the distinct elements and their counts
# for element, count in element_counts.items():
#     print(f"Element {element} appears {count} times.")
# ------------------------------------------------------------------

# Sample list of tuples
my_list = [(255, 255, 0), (192, 255, 255), (255, 138, 255), (157, 157, 255), (255, 113, 113), (154, 231, 154), (192, 255, 255), (255, 255, 0), (192, 255, 255), (255, 113, 113)]

# Create an empty dictionary to store tuple counts
tuple_counts = {}

# Count the repetitions of tuples
for my_tuple in my_list:
    if my_tuple in tuple_counts:
        tuple_counts[my_tuple] += 1
    else:
        tuple_counts[my_tuple] = 1

# Print the distinct tuples and their counts
for my_tuple, count in tuple_counts.items():
    print(f"Tuple {my_tuple} appears {count} times.")
