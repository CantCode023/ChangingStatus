from mydiscord import Client
import time
import traceback
import ctypes

# Set window title
def setTitle(str):
  ctypes.windll.kernel32.SetConsoleTitleW(str)

setTitle("Changing Status V1.0.0 - Loaded!")

# Webhook Link

# Token Input
a = str(input("Please input your Discord token: "))

# MyDiscord Client
client = Client(a)

nasi = True

# Input
while nasi:
    b = int(input("How many messages do you want?: "))
    if b == 1:
        print("That's too low!")
    else:
        # Appending messages to a list
        list = []
        for i in range(1,b+1):
            c = str(input(f"Message {str(i)}: "))
            list.append(c)

        d = float(input("Cooldown time: "))
        if "." not in str(d):
            d = float(str(d) + ".0")

        barbie = True

        while barbie:
            for i in list:
                try:
                    a = client.setStatus(i)
                    if "NoneType: None" in a:
                        print("That token doesn't exist! Please input a real token.")
                        barbie = False
                        nasi = False
                except Exception:
                    print("There was an error!{}".format(traceback.format_exc()))
                    barbie = False
                    nasi = False
                time.sleep(d)
