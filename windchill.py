def calculate_wind_chill(temperature, wind_speed):
    """
    Calculate wind chill based on the given temperature (in Fahrenheit) and wind speed (in mph).
    """
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16 + 0.4275 * temperature * wind_speed**0.16
    return wind_chill

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (celsius * 9/5) + 32

def main():
    # Get user input for temperature and unit (Fahrenheit or Celsius)
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").upper()

    # Convert Celsius to Fahrenheit if needed
    if unit == 'C':
        temperature = celsius_to_fahrenheit(temperature)

    # Loop through wind speeds and calculate wind chill
    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature:.2f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

if __name__ == "__main__":
    main()
