class Calculadora:
    def __init__(self, batteryMax):
        self.display = 0.0
        self.battery = 0
        self.batteryMax = batteryMax  
        
    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def charge(self, increment):
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax