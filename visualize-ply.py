import os
import numpy as np
import matplotlib.pyplot as plt
import gudhi as gd
from open3d import io, visualization

def main():
    # Path
    pathToData = os.path.join(os.getcwd(), 'data', 'bags', 'bag_0')

    # Read Data
    pointCloud = io.read_point_cloud(os.path.join(pathToData, 'cloud_final.ply')) # Read point cloud
    print(pointCloud)
    pointCloudArray = np.asarray(pointCloud.points)

    # Visualize point cloud
    visualize = False
    if visualize:
        visualization.draw_geometries([pointCloud])

    # # Create alpha complex
    alphaComplex = gd.AlphaComplex(points = pointCloudArray)

    # # Create simplex tree object
    simplexTree = alphaComplex.create_simplex_tree()

    # Create persistence diagram
    persistenceDiagram = simplexTree.persistence()
    gd.plot_persistence_diagram(persistenceDiagram, legend=True)
    plt.show()

if __name__ == "__main__":
    main()