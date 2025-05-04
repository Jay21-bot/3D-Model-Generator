import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def show_3d_model(filepath):
    mesh = trimesh.load(filepath)

    # Extract vertices and faces
    vertices = mesh.vertices
    faces = mesh.faces

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for face in faces:
        tri = vertices[face]
        x, y, z = zip(*tri)
        x += (x[0],)
        y += (y[0],)
        z += (z[0],)
        ax.plot(x, y, z, color='blue')

    ax.set_title(f"3D Model: {filepath}")
    plt.show()
