# 3D Model Generator Prototype

## 📝 Overview

This project is a **3D Model Generator** prototype that converts either a **text prompt** or an **image** into a basic 3D model (STL format). The prototype uses placeholder 3D shapes (cube, sphere) and generates models based on the input type. Later, you can enhance this system by integrating advanced AI models for **text-to-3D** and **image-to-3D** generation.

## 📥 Input Options

- **Text input**: Provide a simple description (e.g., `"A toy car"`) and generate a 3D model.
- **Image input**: Provide an image (e.g., `chair.png`) and generate a 3D model of the object.

## ⚙️ How It Works

- **Text → 3D Model**: Generates a placeholder 3D model (cube or sphere) based on a text prompt.
- **Image → 3D Model**: Generates a 3D model based on an input image.
- The generated model is saved in the **STL** format and is visualized in a 3D plot using `matplotlib`.

## 🧠 Thought Process

This is a simple prototype that demonstrates the basic pipeline for **input processing**, **model generation**, and **3D visualization**. In the future, this can be extended using models like **Shap-E** or **Point-E** for generating more complex 3D models directly from text or images.

## 📦 Project Structure

