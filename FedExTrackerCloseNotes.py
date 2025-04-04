                                                     
tracking_number = input("Enter FedEx Tracking Number: ")
user_first_name = input("Enter user's First Name: ")

tracking_link = f'[code]<a href="https://www.fedex.com/fedextrack/?trknbr={tracking_number}">click here</a>[/code]'

print(tracking_link)

print(f"Hello {user_first_name},\n\nThank you for your order. Please {tracking_link} and navigate to the FedEx website to track your RMA request; note that it may take up to 24 hours for your package to appear in the FedEx system.\n\nThank you,")