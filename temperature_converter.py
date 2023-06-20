#TASK:
# Create a new file called temperature_converter.py.
# In the file, define two functions: celsius_to_fahrenheit and fahrenheit_to_celsius.
# Each function should take one argument (the temperature to convert) and return the converted temperature.
# In the main part of the program, prompt the user to enter a temperature and its unit (C or F).
# Call the appropriate function based on the unit and print the converted temperature to the console.

def celsius_to_fahrenheit(temperature):
    return (temperature * 9/5) + 32

def fahrenheit_to_celsius(temperature):
    return (temperature - 32) * 5/9

def main():
    temperature = float(input("Please enter the temperature: "))
    unit = input("Please enter the unit (C or F): ")

    if unit.upper() == "C":
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"The temperature in Fahrenheit is: {converted_temperature}°F")
    elif unit.upper() == "F":
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"The temperature in Celsius is: {converted_temperature}°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
