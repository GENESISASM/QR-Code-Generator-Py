#Before start please install library using this command
# "python -m pip install qrcode" or "pip install qrcode"

import qrcode #Import qrcode Library from Python

def generate_qr_code(url):
    # Generate QR code
    qr = qrcode.QRCode( # type: ignore
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, # type: ignore
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    #Create an image from the QR code
    image = qr.make_image(fill_color="black", back_color="white") #qr code colour
    image.save("qrcode.png") #save the image using .png / .jpg / .jpeg file
    print("QR code was generated Sucessfully") #Notification that qr code was generated successfully

# Convert website URL to QR code
website_url = "https://forms.gle/iuV3m45nhn1apSpt8"  # Replace with your website URL
generate_qr_code(website_url)
