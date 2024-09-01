from tabulate import tabulate
from datetime import datetime

print("Welcome to Crestview Manor")

user_location=[]
days_staying=[]
kids =[]
adults = []
room_type = []
user_name=[]
user_phonenumber=[]
user_email=[]
stay_cost = []

print('''
Kindly enter the following details.
 ''')

while True:

    name = input("Your name: ")
    if name.isalpha()== True:
        name.title()
        user_name.append(name)
        break
    else:
        print("enter a valid name")


while True:
    age = input("\nAge: ")
    if age.isdigit() == True:
        if int(age) >= 18:
            break
        else:
            print("We only accept reservations from guests 18 years and older.")
    else:
        print("Enter a valid age")

print("")

while True:
    phone = (input("Phone number (+91----------): "))
    if phone.isdigit() == True and len(phone)==10:
        user_phonenumber.append(phone)
        break
    else:
        print("enter a valid phone number")

print("")

email_id = (input("email id:  "))
user_email.append(email_id)



print('''
      
      
__________Our offered locations__________
      
Mumbai \t Pune \t Hyderabad \t Goa\t Banglore
''')



while True:
    location = input("\nWhere would you like to book the hotel? Please specify the location: ")
    location.capitalize()
    location_cap = location.upper()


    if location_cap == 'MUMBAI':

        print('''
Regions available in Mumbai
Wadala \t Bandra\t Chembur
''')
        
        while True:
             mumbai_region = input("Enter region: ")
             if mumbai_region.upper() == 'BANDRA' or mumbai_region.upper() == 'WADALA' or mumbai_region.upper() == 'CHEMBUR':
               user_location.append(mumbai_region)
               address_hotel = (f'Street No 12, Clifton Lake, {mumbai_region}, Mumbai')
               location_region =mumbai_region.capitalize()
               break
             else:
                 print('''
Please enter a valid location.''')
        break
        
    elif location_cap == 'PUNE':
        print('''
Regions available in Pune
Aundh \t Shivajinagar \t Sinhagad
              ''')

        while True:
            pune_region = input("Enter region: ")
            if pune_region.upper() == 'AUNDH' or pune_region.upper() == 'SHIVAJINAGAR' or pune_region.upper() == 'SINHAGAD':
                user_location.append(pune_region)
                address_hotel = (f'Street No 12, Clifton Lake, {pune_region}, Pune')
                location_region =pune_region.capitalize()
                break
            else:
                print('''
Please input correct location''')
        break

    elif location_cap == 'HYDERABAD':
        print("\nRegions available in Hyderabad \nGachibowli \t Miyarpur \t Madharpur \n")

        while True:
            hyderabad_region = input("Enter region: ")
            if hyderabad_region.upper() == 'GACHIBOWLI' or hyderabad_region.upper() == 'MIYARPUR' or hyderabad_region.upper() == 'MADHARPUR':
                user_location.append(hyderabad_region)
                address_hotel = (f'Street No 12, Clifton Lake, {hyderabad_region}, Hyderabad')
                location_region =hyderabad_region.capitalize()
                break
            else:
                print('''
Please input correct location''')
        break

    elif location_cap == 'GOA':
        print("\nRegions available in Goa \nPanaji \t Mapusa \t Aldona \n")

        while True:
            goa_region = input("Enter region: ")
            if goa_region.upper() == 'PANAJI' or goa_region.upper() == 'MAPUSA' or goa_region.upper() == 'ALDONA':
                user_location.append(goa_region)
                address_hotel = (f'Street No 12, Clifton Lake, {goa_region}, Goa')
                location_region =goa_region.capitalize()
                break
            else:
                print('''
Please input correct location''')
        break

    elif location_cap == 'BANGLORE':
        print("\nRegions available in Banglore \nIndiranagar \t Banashankari \n")
        while True:
            banglore_region = input("Enter region: ")
            if banglore_region.upper() == 'INDIRANAGAR' or banglore_region.upper() == 'BANASHANKARI':
                user_location.append(banglore_region)
                address_hotel = (f'Street No 12, Clifton Lake, {banglore_region}, Banglore')
                location_region =banglore_region.capitalize()
                break
            else:
                print('''
Please input correct location''')
        break

    else:
        print("\nHotel not available at the given location.\n")



print("")
print("__________________________________")
print("")

while True:

    check_in_str = input("Enter the check-in date (DD-MM-YYYY): ")
    check_in_date = datetime.strptime(check_in_str, "%d-%m-%Y")

    check_out_str = input("Enter the check-out date (DD-MM-YYYY): ")
    check_out_date = datetime.strptime(check_out_str, "%d-%m-%Y")

    if check_out_date >= check_in_date:
        duration = check_out_date - check_in_date
        break
    else:
        print("Invalid date range. Check-out date should be after or equal to check-in date.")


duration = int(duration.days)
duration = duration + 1 #NO OF DAYS IS THIS
no_of_nights = duration -1 

print("\nYour Stay includes", duration, 'days and' , no_of_nights ,'nights')  #EDIT THIS STATEMENTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

print("_______________________________")

#room types
print('''

We offer a selection of room options, including:
      
Standard- 2 single bed | Non AC
Deluxe- 1 King Size Bed | AC | Bigger Rooms 
''')


while True:
    user_room = input("\nSpecify you room preference: ")
    if user_room.upper()=='STANDARD' or user_room.upper()== 'DELUXE':
        if user_room.upper() == 'STANDARD':
            room_type.append(user_room) 
            cost_of_room = 5000
            living_cost = duration * cost_of_room
            stay_cost.append(living_cost)
            break


        elif user_room.upper() == 'DELUXE':
            room_type.append(user_room)

            cost_of_room = 8000
            living_cost = duration * cost_of_room
            stay_cost.append(living_cost)
            break
        
    else:
        print("\nWe don't have that room type available. Please try again.")

print('''
      
      ''')





while True:
    no_of_adults =(input("How many adults are going to stay in the given duration: "))
    no_of_kids= (input("\nWhat about kids? "))
    
    if no_of_kids.isdigit() == True and no_of_adults.isdigit()==True:

        if int(no_of_adults) >= 0 and int(no_of_kids) >=0:
            no_of_adults = int(no_of_adults)
            no_of_kids = int(no_of_kids)
            kids.append(no_of_kids)
            adults.append(no_of_adults)
            break
    else:
        print("Please enter a valid number: ")




#Meals Included/ Not Included

print('''
___________________________________________________

Do you want to include meals during your stay?
      
(meals include breakfast, lunch and dinner)
''')

# meal cost for baccha log is 200 per day and 300 for adults


while True:
    meal_input = input('''Type yes or no: ''')
    if meal_input.upper()=='YES':
        meal_cost = (200 * duration * no_of_kids) + (300 * duration * no_of_adults)
        break
    if meal_input.upper()=='NO':
        meal_cost = 0
        break
    else:
        print("please enter a valid answer")


#Extra Utilities (if any)

#price for extra bed is 200 rupees

print("\nWould you like to add an extra Bed? ")
while True:
    extra_stuff = input("\nEnter yes or no: ")
    if extra_stuff.upper()=='YES':
        bed_cost = 200
        break
    elif extra_stuff.upper()=='NO':
        bed_cost =0
        break
    else:
        print("please enter a valid input")

print("__________________________________")

#COST TILL NOW

#living_cost
#meal cost
#bed_cost

cost_without_discount = living_cost + meal_cost + bed_cost




#Discount (coupen code) (Govt Job) / Price 

print("\nDo you have any voucher/code?")

print("\nPlease note that the discount code is exclusively for your room charges")

while True:
    discount = input("\nEnter yes or no: ")
    if discount.upper()=='YES':
        discount_code = input("\nEnter code: ")
        if discount_code == 'AFD643BL' or discount_code == 'DNB6890AZ' or discount_code == 'COMZ343B' or discount_code == 'LPQ234Z':
            print("\nDiscount code valid")
            living_cost_with_discount = living_cost * 0.3
            cost_with_discount = living_cost_with_discount + meal_cost + bed_cost
            break

        else:
            print("\nDiscount code invalid")
            cost_with_discount = living_cost + meal_cost + bed_cost
            break

    elif discount.upper()=='NO':
        cost_with_discount = living_cost + meal_cost + bed_cost
        break
    else:
        print("please enter a valid input ")

print("_________________________________")


#Payment Method
print("")
payment_method = input("What is your preferred payment method: ")



# Assuming you have your details stored in a dictionary called 'user_details'
user_details = {
    'Name': name,
    'Age': age,
    'Phone Number': phone,
    'Email Address': email_id,
    'Location Selected': f'{location}, {location_region}',
    'Hotel Address': address_hotel,
    'Stay Duration': f'{duration} Days and {no_of_nights} Nights',
    'Room Type': room_type,
    'Cost Before Discount': cost_without_discount,
    'Cost After Discount': cost_with_discount,
    'Payment Method': payment_method
}

table = tabulate(user_details.items(), tablefmt="pretty")

hotel_info = f'''
Hotel Crestview Manor
{address_hotel}
'''

output = f'''
{hotel_info}

Guest details
{table}
'''

print(output)
