#Display current time

from datetime import datetime

current_time = datetime.now()

print("Current time:", current_time.strftime("%I:%M:%S %p"))

