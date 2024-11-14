import qrcode

# Replace this URL with your form's URL
form_url = "put your full link here"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border
)
qr.add_data(form_url)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill="black", back_color="white")
img.save("form_qr_code.png") # Rename img if needed

print("QR code generated and saved as form_qr_code.png.")
