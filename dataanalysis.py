import csv
dataset_path = "life-expectancy.csv"
# Function to load the dataset
def load_dataset(dataset_path):
    data = []
    with open(dataset_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header
        for row in reader:
            data.append(row)
    return data

# Function to find the lowest and highest life expectancies
def find_min_max_life_expectancy(data):
    life_expectancies = [float(row[3]) for row in data]
    min_life_expectancy = min(life_expectancies)
    max_life_expectancy = max(life_expectancies)
    return min_life_expectancy, max_life_expectancy

# Function to find the year and country with the lowest and highest life expectancies
def find_year_country_min_max(data):
    min_life_row = min(data, key=lambda x: float(x[3]))
    max_life_row = max(data, key=lambda x: float(x[3]))
    return min_life_row[2], min_life_row[0], max_life_row[2], max_life_row[0]

# Function to find the average life expectancy for a given year
def average_life_expectancy_for_year(data, year):
    year_data = [row for row in data if row[2] == str(year)]
    if not year_data:
        return None, None, None

    life_expectancies = [float(row[3]) for row in year_data]
    average_life_expectancy = sum(life_expectancies) / len(life_expectancies)
    min_life_row = min(year_data, key=lambda x: float(x[3]))
    max_life_row = max(year_data, key=lambda x: float(x[3]))

    return average_life_expectancy, min_life_row[0], max_life_row[0]

# Main program
if __name__ == "__main__":
    # Load the dataset
    dataset_path = "life-expectancy.csv"
    dataset = load_dataset(dataset_path)

    # Milestone Requirements
    min_life, max_life = find_min_max_life_expectancy(dataset)
    print(f"The lowest life expectancy is: {min_life}")
    print(f"The highest life expectancy is: {max_life}")

    # Final Requirements
    min_life_year, min_life_country, max_life_year, max_life_country = find_year_country_min_max(dataset)
    print(f"The year and country with the lowest life expectancy: {min_life_year} ({min_life_country})")
    print(f"The year and country with the highest life expectancy: {max_life_year} ({max_life_country})")

    # Allow the user to input a year
    user_year = int(input("Enter the year of interest: "))
    avg_life, min_life_country, max_life_country = average_life_expectancy_for_year(dataset, user_year)

    # Display the results for the user-inputted year
    if avg_life is not None:
        print(f"\nFor the year {user_year}:")
        print(f"The average life expectancy across all countries was: {avg_life:.2f}")
        print(f"The max life expectancy was in {max_life_country} with {max_life:.2f}")
        print(f"The min life expectancy was in {min_life_country} with {min_life:.2f}")
    else:
        print(f"No data available for the year {user_year}.")