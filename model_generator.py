import trimesh
import os

def process_text_prompt(prompt):
    print(f"[INFO] Generating 3D model from text: {prompt}")

    # For now, generate a cube for any prompt
    mesh = trimesh.creation.box(extents=(1, 1, 1))

    filename = f"{prompt.replace(' ', '_')}.stl"
    output_path = os.path.join("outputs", filename)
    mesh.export(output_path)

    return output_path

def process_image_input(image_path):
    print(f"[INFO] Generating 3D model from image: {image_path}")

    # For now, also generate a sphere for image input as placeholder
    mesh = trimesh.creation.icosphere(radius=0.5)

    filename = os.path.splitext(os.path.basename(image_path))[0] + ".stl"
    output_path = os.path.join("outputs", filename)
    mesh.export(output_path)

    return output_path
