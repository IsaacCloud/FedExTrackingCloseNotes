                                                     
tracking_number = input("Enter FedEx Tracking Number: ")
user_first_name = input("Enter user's First Name: ")
tracking_link = "https://www.fedex.com/fedextrack/?trknbr=" + tracking_number

print(tracking_link)

print(f"Hello {user_first_name},\n\nThank you for your order. Please click here and navigate to the FedEx website to track your RMA request; note that it may take up to 24 hours for your package to appear in the FedEx system.\n\nThank you,")