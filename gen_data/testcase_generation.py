import random

def generate_test_cases(num_tests, max_boxes, max_containers, output_dir):
    """
    Generate test cases for the 2D bin packing problem.

    Parameters:
    - num_tests: Number of test cases to generate.
    - max_boxes: Maximum number of boxes per test case.
    - max_containers: Maximum number of containers per test case.
    - output_dir: Directory to save the generated test cases as separate TXT files.

    Each test case will be saved to a separate file.
    """
    for test_index in range(0, num_tests):
        num_boxes = max_boxes + test_index*1000
        num_containers = max_containers + test_index*1000

        output_path = f"{output_dir}/test_case_{num_boxes}.txt"
        with open(output_path, "w") as file:
            # Write number of boxes and containers
            file.write(f"{num_boxes} {num_containers}\n")

            # Generate boxes with random dimensions
            for _ in range(num_boxes):
                width = random.randint(1, 10)  # Random width between 10 and 100
                height = random.randint(1, 10)  # Random height between 10 and 100
                file.write(f"{width} {height}\n")

            # Generate containers with random dimensions and costs
            for _ in range(num_containers):
                width = random.randint(10, 30)  # Random width between 100 and 200
                height = random.randint(10, 30)  # Random height between 100 and 200
                cost = random.randint(5, 20)  # Random cost between 5 and 20
                file.write(f"{width} {height} {cost}\n")

        print(f"Test case {test_index} saved to {output_path}")

# Example usage
output_directory = "test_cases"
import os
os.makedirs(output_directory, exist_ok=True)
generate_test_cases(num_tests= 10, max_boxes=1000, max_containers=1000, output_dir=output_directory)
