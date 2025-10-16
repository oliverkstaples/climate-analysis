# Todo: Code is a bit unclear

def fahrenheit_to_celcius(fahr):
    celcius = (fahr - 32) * (5 / 9)
    return celcius

def fahrenheit_to_kelvin(fahr):
    celcius = fahrenheit_to_celcius(fahr)
    kelvin = celcius + 273.15
    return kelvin

# print(fahrenheit_to_celcius(212))   # Expect 100.0
# print(fahrenheit_to_kelvin(32))     # Expect 273.15