class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False
        self.apps = []

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now turned on.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} is now turned off.")

    def install_app(self, app_name):
        if self.is_on:
            self.apps.append(app_name)
            print(f"{app_name} has been installed on {self.brand} {self.model}.")
        else:
            print("Please turn on the phone to install apps.")

    def list_apps(self):
        if self.apps:
            print(f"Apps installed on {self.brand} {self.model}:")
            for app in self.apps:
                print(f"- {app}")
        else:
            print("No apps are installed yet.")

# Create a child class to demonstrate inheritance
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, camera_mp):
        super().__init__(brand, model, storage)
        self.camera_mp = camera_mp

    def take_photo(self):
        if self.is_on:
            print(f"Taking a {self.camera_mp}MP photo with {self.brand} {self.model}.")
        else:
            print("Please turn on the phone to take photos.")

# Example usage
my_phone = Smartphone("Apple", "iPhone 15 pro max", "512GB")
my_phone.turn_on()
my_phone.install_app("WhatsApp")
my_phone.install_app("Instagram")
my_phone.list_apps()
my_phone.turn_off()

pro_phone = SmartphonePro("Samsung", "Galaxy S24 Ultra", "256GB", 108)
pro_phone.turn_on()
pro_phone.install_app("Camera Pro")
pro_phone.install_app("Snapchat")
pro_phone.take_photo()
pro_phone.turn_off()