import qrcode

def generate_qr():
    data = input("Enter text or URL to generate QR Code: ")
    filename = input("Enter filename (without extension): ")

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(f"{filename}.png")

    print(f"\n✅ QR Code saved as {filename}.png")

if __name__ == "__main__":
    generate_qr()