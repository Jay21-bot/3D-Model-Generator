# 3D Model Generator Prototype

## 📝 Description

This prototype converts either a **text prompt** or an **image** into a simple 3D model (STL format). It uses placeholder shapes (cube/sphere) to simulate text-to-3D and image-to-3D generation.

## 📥 Input Options

- Text (e.g., "A toy car")
- Image (e.g., `car.png` in `inputs/`)

## ⚙️ How It Works

- Text → Generates a cube `.stl`
- Image → Generates a sphere `.stl`
- 3D model is shown in a window using `matplotlib`

## 🧠 Thought Process

This is a functional prototype showing the pipeline from input → 3D model generation → output → visualization. In a full version, we can replace the logic with AI-based tools like **Shap-E** or **Point-E**.

## ▶️ Run Instructions

```bash
git clone <your_repo_link>
cd 3d_model_generator_project
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py
```
