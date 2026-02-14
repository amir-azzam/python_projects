import pywhatkit
import time

TARGET_NUMBER = "+201********" 
FIVE_HOURS = 5 * 60 * 60 

def get_manual_med_input():
    """Logic from your original code combined into a single message string"""
    medTime = input("\nEnter time (morning/noon/night/before bed): ").lower().strip()
    
    if medTime == "morning":
        morningTime = input("Before breakfast or after: ").lower().strip()
        if "before" in morningTime:
            return "Morning Meds (Before Breakfast): Estrapex-Trio, Esovaxole, Insulin"
        elif "after" in morningTime:
            return "Morning Meds (After Breakfast): Vildagluse plus, Cortizon, Vitamin D, B, B12"
        else:
            return "Morning Meds: Invalid timing input."

    elif medTime == "noon":
        return "Noon Meds: Take Zytiga (2 hours after breakfast)."

    elif medTime == "night":
        return "Night Meds: Take Plavix, Concor, Aspirin (1 hour after Zytiga)."

    elif medTime == "before bed":
        return "Bedtime Meds: Take Ator."
    
    return "Invalid input. No specific meds identified."

print("Medication Bot Started...")

while True:
    message_to_send = get_manual_med_input()
    
    print(f"Sending to WhatsApp: {message_to_send}")
    
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=TARGET_NUMBER, 
            message=message_to_send, 
            wait_time=15, 
            tab_close=True
        )
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

    print(f"\nWaiting 5 hours until the next reminder...")
    time.sleep(FIVE_HOURS)
