from PIL import Image
import numpy as np

def encrypt_decrypt_image(image_path, key, output_path):
   
    img = Image.open(image_path)
    img_array = np.array(img)

 
    key_byte = key % 256

   
    encrypted_array = img_array ^ key_byte

    
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Saved output image as {output_path}")

def main():
    print("=== Simple Image Encryption Tool ===")
    image_path = input("Enter the image file path: ")
    key = int(input("Enter a numeric key (0-255): "))
    action = input("Encrypt or Decrypt? (E/D): ").strip().upper()
    
    if action == 'E':
        output_path = "encrypted_image.png"
    elif action == 'D':
        output_path = "decrypted_image.png"
    else:
        print("Invalid choice! Exiting...")
        return

    encrypt_decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()