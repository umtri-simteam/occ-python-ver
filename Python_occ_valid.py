def calculate_average(filename):
    total_sum = 0
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
     
            try:
                number = float(line.strip())
                total_sum += number
                count += 1
            except ValueError:
                print(f"skipping, type inconsistency")
    
    if count == 0:
        return 0
    
    average = total_sum / count
    return average

filename = 'Python_occlusion_validation.txt'
average = calculate_average(filename)
print(f"Average of real occulusion time: {average}")  # 0.5001940421569042

