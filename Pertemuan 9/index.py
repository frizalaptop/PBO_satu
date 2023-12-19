import tkinter as tk
from tkinter import ttk

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        # Fahrenheit input
        self.label_temperature = ttk.Label(root, text="Enter temperature:")
        self.label_temperature.grid(row=0, column=0, padx=10, pady=10)

        self.entry_temperature = ttk.Entry(root)
        self.entry_temperature.grid(row=0, column=1, padx=10, pady=10)

        # Unit selection
        self.label_unit = ttk.Label(root, text="Select unit:")
        self.label_unit.grid(row=1, column=0, padx=10, pady=10)

        self.unit_options = ["Fahrenheit", "Reamur", "Kelvin"]
        self.unit_combobox = ttk.Combobox(root, values=self.unit_options)
        self.unit_combobox.set(self.unit_options[0])
        self.unit_combobox.grid(row=1, column=1, padx=10, pady=10)

        # Convert button
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_temperature)
        self.convert_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Results labels
        self.label_results = ttk.Label(root, text="")
        self.label_results.grid(row=3, column=0, columnspan=2, pady=10)

    def convert_temperature(self):
        try:
            temperature = float(self.entry_temperature.get())
            selected_unit = self.unit_combobox.get()

            celsius_temperature = 0
            fahrenheit_temperature = 0
            reamur_temperature = 0
            kelvin_temperature = 0

            if selected_unit == "Fahrenheit":
                fahrenheit_temperature = temperature
                temperature_obj = Fahrenheit(temperature)
                celsius_temperature = temperature_obj.fahrenheit_to_celsius()
                kelvin_temperature = temperature_obj.fahrenheit_to_kelvin()
                reamur_temperature = temperature_obj.fahrenheit_to_reamur()

            elif selected_unit == "Reamur":
                reamur_temperature = temperature
                temperature_obj = Reamur(temperature)
                celsius_temperature = temperature_obj.reamur_to_celsius()
                kelvin_temperature = temperature_obj.reamur_to_kelvin()
                fahrenheit_temperature = temperature_obj.reamur_to_fahrenheit()

            elif selected_unit == "Kelvin":
                kelvin_temperature = temperature
                temperature_obj = Kelvin(temperature)
                celsius_temperature = temperature_obj.kelvin_to_celsius()
                fahrenheit_temperature = temperature_obj.kelvin_to_fahrenheit()
                reamur_temperature = temperature_obj.kelvin_to_reamur()

            results_text = (
                f"{temperature:.2f} {selected_unit} is equal to:\n"
                f"{celsius_temperature:.2f} Celsius\n"
                f"{fahrenheit_temperature:.2f} Fahrenheit\n"
                f"{kelvin_temperature:.2f} Kelvin\n"
                f"{reamur_temperature:.2f} Réaumur"
            )

            self.label_results.config(text=results_text)

        except ValueError:
            self.label_results.config(text="Invalid input. Please enter a valid number.")

class Fahrenheit:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def fahrenheit_to_celsius(self):
        return (self.fahrenheit - 32) * 5/9

    def fahrenheit_to_kelvin(self):
        return (self.fahrenheit + 459.67) * 5/9

    def fahrenheit_to_reamur(self):
        return (self.fahrenheit - 32) * 4/9

class Reamur:
    def __init__(self, reamur):
        self.reamur = reamur

    def reamur_to_celsius(self):
        return self.reamur * 5/4

    def reamur_to_kelvin(self):
        return (self.reamur * 5/4) + 273.15

    def reamur_to_fahrenheit(self):
        return (self.reamur * 9/4) + 32

class Kelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    def kelvin_to_celsius(self):
        return self.kelvin - 273.15

    def kelvin_to_fahrenheit(self):
        return (self.kelvin - 273.15) * 9/5 + 32

    def kelvin_to_reamur(self):
        return (self.kelvin - 273.15) * 4/5

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
