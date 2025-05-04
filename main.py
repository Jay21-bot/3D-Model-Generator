from visualizer import show_3d_model

import os
from model_generator import process_text_prompt, process_image_input

def main():
    print("Welcome to the 3D Model Generator!")
    choice = input("Enter input type (text/image): ").strip().lower()

    if choice == 'text':
        prompt = input("Enter your text prompt (e.g., 'a toy car'): ")
        output_path = process_text_prompt(prompt)
        print(f"3D model generated from text and saved to: {output_path}")
        show_3d_model(output_path)

        

    elif choice == 'image':
        image_name = input("Enter image filename (place inside 'inputs/' folder): ").strip()
        image_path = os.path.join("inputs", image_name)
        if not os.path.exists(image_path):
            print("Image not found in 'inputs/' folder.")
            return
        output_path = process_image_input(image_path)
        print(f"3D model generated from image and saved to: {output_path}")
        show_3d_model(output_path)


    else:
        print("Invalid choice. Please enter 'text' or 'image'.")

if __name__ == "__main__":
    main()
