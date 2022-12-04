contacts = {
    "TEJESH":8317652279,"SOMA SEKHAR": 7981184515,"YESHWANTH":7995939179,"CHANUKYA":7569669189,"VENKY":+919063559343,"DARSHAN":7569827366,"THARUN":9948338123,
    "SHUBHAM":9693964520,"PRADEEP":9177455989,"PREM":6206407406,"SUMIT":9310083947,"MOHAN":8919889419,"AABID KHAN":7319661231,
    "VINAYAK":9177411877,"LOKESHWARAN":9345148191,"PIYUSH":9997725596,"ABHI":6301190340,"SAHIL KHAN":6002634110,"SAAWAN":6207802116,
    "VIKRAM JHA":7742130488,"NISHANTH":7970922655,"HARSHA VARDHAN CHAUHAN":8791681219,"SHUBHAM AGRAWAL":8932951318,"ARYEN DEY":9365272613,
    "AJAY":9494818978,"DEEPIKA":9695102274,"VED":9798741907
}


# Searches the dictionary and prints the key value pair incase the key isn't present, it adds it to the dict and prints it''

def single_search():
    name = input(">>>Enter the name of the contact you wish to search for: ").upper()
    if name in contacts:
        print(f"\n{name}: {contacts[name]}")
    else:
        b = input("\nNo such contact found.").lower()


# Searches the dictionary and prints multiple key value pair and incase any key isn't present, it adds it to the dict and prints it along with the others.

def multiple_search():
    result = {}
    name1 = input(">>>Enter the names of the contacts seperated by commas : ").split(",")
    for i in name1:
        i = i.upper()
        if i in contacts:
            result[i] = contacts[i]
        else:
            print("contact not found")
    print(result)

choice = int(input(
    "Would you like to: \n\n1. Search for a single contact \n2. List all the contacts \n3. Search for multiple contacts \n \n>>>Enter your choice: "))

if choice == 1:
    single_search()

elif choice == 2:
    for key, value in contacts.items():
        print(key,':',value)

elif choice == 3:
    multiple_search()

else:
    print("Choose from the given options!")