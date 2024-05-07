def map_value(value, from_min, from_max, to_min, to_max):
    # Scale the value from the original range to a value between 0 and 1
    scaled_value = (value - from_min) / (from_max - from_min)
    
    # Map the scaled value to the new range
    mapped_value = to_min + (scaled_value * (to_max - to_min))
    
    return mapped_value

# Example usage:
original_value = 50
mapped_value = map_value(original_value, 1, 100, 1, 150)
print("Mapped value:", mapped_value)

