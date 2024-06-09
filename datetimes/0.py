import datetime

def adjust_time(input_time_str):
    # Parse the input datetime string
    input_time = datetime.datetime.strptime(input_time_str, '%Y-%m-%d %H:%M:%S')
    
    # Subtract three hours
    adjusted_time = input_time - datetime.timedelta(hours=3)
    
    # Return the adjusted datetime as a string
    return adjusted_time.strftime('%Y-%m-%d %H:%M:%S')

# Example usage
input_time_str = "2024-05-20 01:00:00"
adjusted_time_str = adjust_time(input_time_str)
print(f"Original time: {input_time_str}")
print(f"Adjusted time: {adjusted_time_str}")



