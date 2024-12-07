import time                     # Importing time module to use delay functionality
from plyer import notification  # Importing plyer module to display desktop notifications

if __name__ == "__main__":      # Ensures the script runs only when executed directly
    while True:                 # Infinite loop to send notifications repeatedly
        notification.notify(
            title = "Please Drink Water Now !!!",  # Title of the notification
            message = "About 3.7 liters of fluids a day for men. About 2.7 liters of fluids a day for women.", # Message to display in the notification
            app_icon = "F:\\Python Learning Journey\\Drink Water Notify Project\\icon.ico",   # Path to the icon file for the notification
            timeout = 7      # Duration (in seconds) the notification will stay visible
        )
        time.sleep(60 * 30)  # Wait for 30 minutes before showing the next notification
