import shutil

# Get disk usage statistics
total, used, free = shutil.disk_usage("/")

# Calculate percentage of used space
used_percentage = (used / total) * 100

# Print percentage of used space
print("Percentage of used space:", used_percentage)
