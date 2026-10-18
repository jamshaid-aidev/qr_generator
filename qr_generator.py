
import qrcode
import random
import string
import os

def generate_random_text(length=12):
    """Generate random text for the QR code."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_qr_code(data, filename="my_qr_code.png"):
    """Generate and save a QR code."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    image.save(filename)
    print(f"\nQR code saved as: {os.path.abspath(filename)}")
    print(f"QR code content: {data}")

    # Open the generated QR code image
    image.show()


def main():
    print("=== QR Code Generator ===")
    print("1. Generate QR from your own text or URL")
    print("2. Generate QR with random text")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        data = input("Enter text or website URL: ").strip()
        if not data:
            print("Error: Please enter some text.")
            return

    elif choice == "2":
        data = generate_random_text()
        print(f"Generated random text: {data}")

    else:
        print("Invalid option. Please choose 1 or 2.")
        return

    filename = input(
        "Enter image filename (press Enter for default): "
    ).strip()

    if not filename:
        filename = "my_qr_code.png"

    if not filename.lower().endswith(".png"):
        filename += ".png"

    generate_qr_code(data, filename)


if __name__ == "__main__":
    main()

# This script allows users to generate QR codes either from their own input text or from randomly generated text. It uses the `qrcode` library to create the QR code and saves it as an image file. The user can specify a filename for the saved QR code image, and if no filename is provided, it defaults to "my_qr_code.png". The generated QR code image is also displayed after creation.