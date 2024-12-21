# Load only addresses starting with '1'

# Function to filter addresses starting with '1'
def filter_addresses(input_path, output_path):
    try:
        with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
            for line in infile:
                address = line.strip()
                # Check if the address starts with '1'
                if address.startswith('1'):
                    outfile.write(address + '\n')
        print(f"Filtered addresses have been saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the filtering function
filter_addresses("./all_addresses.txt", "./filtered_addresses.txt")