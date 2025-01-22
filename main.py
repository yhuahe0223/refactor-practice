
#refactor this into an abstrated method
if not isinstance(hat, Hat):
    return False

current_fashion = get_fashion()
weather_outside = self.look_out_of_window()
is_stylish = self.evaluate_style(hat, current_fashion)

if weather_outside.is_raining:
    print("Damn.")
    return True
else:
    print("Great.")
    return is_stylis




 if weather == "rainy":
            return "Take an umbrella."
        elif weather == "sunny":
            return "Wear sunglasses."
        elif weather == "cold":
            return "Wear a jacket."
        else:
            return "Weather unknown. Dress comfortably."




if budget < 100:
            return "Local day trips."
        elif budget < 500:
            return "Nearby cities."
        else:
            return "International travel!"