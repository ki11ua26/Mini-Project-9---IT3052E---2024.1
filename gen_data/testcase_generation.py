import random

def generate_test_cases(num_tests, min_boxes, min_containers, output_dir, jump):
    """
    Generate test cases for the 2D bin packing problem.

    Parameters:
    - num_tests: Number of test cases to generate.
    - min_boxes: Minimum number of boxes per test case.
    - min_containers: Minimum number of containers per test case.
    - output_dir: Directory to save the generated test cases as separate TXT files.

    Each test case will be saved to a separate file.
    """
    for test_index in range(0, num_tests):
        num_boxes = min_boxes + test_index*jump
        num_containers = min_containers + test_index*jump

        output_path = f"{output_dir}/test_case_{num_boxes}.txt"
        with open(output_path, "w") as file:
            # Write number of boxes and containers
            file.write(f"{num_boxes} {num_containers}\n")

            # Generate boxes with random dimensions
            for _ in range(num_boxes):
                width = random.randint(1, 10)  # Random width 
                height = random.randint(1, 10)  # Random height 
                file.write(f"{width} {height}\n")

            # Generate containers with random dimensions and costs
            for _ in range(num_containers):
                width = random.randint(10, 30)  # Random width 
                height = random.randint(10, 30)  # Random height 
                cost = random.randint(5, 20)  # Random cost 
                file.write(f"{width} {height} {cost}\n")

        print(f"Test case {test_index} saved to {output_path}")


output_directory = "test_cases"
import os
os.makedirs(output_directory, exist_ok=True)
num_tests, min_boxes, min_containers, jump = map(int, input().split())
generate_test_cases(num_tests, min_boxes, min_containers, output_dir=output_directory, jump=jump)
