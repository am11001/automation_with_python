import pywhatkit

phone_number = input("Enter phone number: ")

pywhatkit.sendwhatmsg(phone_number, "Test", 7, 21)
pywhatkit.sendwhatmsg(phone_number, "Test", 7, 25, 15, True, 2)

group_id = input("Enter group id: ")

pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 7, 31)


