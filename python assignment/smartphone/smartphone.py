# Base Class
class Smartphone:
    def __init__(self, brand, model, battery_life, os):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
        self.os = os

    def introduce(self):
        print(f"{self.brand} {self.model} powered by {self.os} with {self.battery_life}h battery life.")

    def call(self, number):
        print(f"{self.model} is calling {number}...")

    def battery_status(self):
        print(f"{self.model} battery: {self.battery_life} hours left.")


# Derived Class (Inheritance)
class StarletSmartphone(Smartphone):
    def __init__(self, model, battery_life, os, ai_features):
        # Starlet brand fixed
        super().__init__("Starlet Technologies", model, battery_life, os)
        self.ai_features = ai_features

    # New method
    def showcase_ai(self):
        print(f"{self.model} showcases AI: {', '.join(self.ai_features)}.")

    # Overriding method (Polymorphism)
    def battery_status(self):
        print(f"Starlet {self.model} has optimized battery management: {self.battery_life} hours remaining.")


# Example usage
phone1 = Smartphone("Generic", "XPhone 10", 20, "Android")
phone1.introduce()
phone1.call("123-456-7890")
phone1.battery_status()

starlet_phone = StarletSmartphone("Nova X1", 30, "StarOS", ["Face ID+", "Smart Assistant", "Battery Saver AI"])
starlet_phone.introduce()
starlet_phone.showcase_ai()
starlet_phone.battery_status()
