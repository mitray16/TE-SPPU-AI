def ctu_partitioning(ctu_size, max_depth):
    # Check if the CTU size is valid
    if ctu_size % 16 != 0:
        raise ValueError("CTU size must be a multiple of 16.")

    # Recursive function to generate the CTU partitioning
    def partition_ctu(x, y, size, depth):
        if depth == max_depth:
            # Leaf node reached, process the CTU
            print(f"Processing CTU at ({x}, {y}) with size {size}")
            # Add your processing logic here
        else:
            # Divide the CTU into four equal-sized sub-CTUs
            sub_size = size // 2
            partition_ctu(x, y, sub_size, depth + 1)
            partition_ctu(x + sub_size, y, sub_size, depth + 1)
            partition_ctu(x, y + sub_size, sub_size, depth + 1)
            partition_ctu(x + sub_size, y + sub_size, sub_size, depth + 1)

    # Start the CTU partitioning from the top-left corner
    partition_ctu(0, 0, ctu_size, 0)


# Example usage
ctu_size = 64  # CTU size in pixels
max_depth = 3  # Maximum depth for CTU partitioning
ctu_partitioning(ctu_size, max_depth)
