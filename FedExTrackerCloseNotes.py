# using pyperclip module to copy the final text output to the clipboard (windows) / https://pypi.org/project/pyperclip/
import pyperclip

your_name = input("Enter Your Name: ")
tracking_number = input("Enter FedEx Tracking Number: ")
user_first_name = input("Enter user's First Name: ")

# Link generated is wrapped with the [code] tags to format the html hyperlink in Service Now links
tracking_link = f'[code]<a href="https://www.fedex.com/fedextrack/?trknbr={tracking_number}">click here</a>[/code]'

rma_notes = f"""Hello {user_first_name},

Thank you for your order. Please {tracking_link} and navigate to the FedEx website to track your RMA request. Note that it may take up to 24 hours for your package to appear in the FedEx system.

Thank you,

{your_name}

"""

print(rma_notes)
pyperclip.copy(rma_notes)
print("✅ RMA notes copied to clipboard! 📋")