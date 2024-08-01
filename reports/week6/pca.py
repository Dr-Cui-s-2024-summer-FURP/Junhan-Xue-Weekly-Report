import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
# 读取点云数据
def load_point_cloud(file_path):
    point_cloud = np.loadtxt(file_path, delimiter=' ')
    return point_cloud

# 使用PCA进行数据预处理
def apply_pca_to_point_cloud(point_cloud):
    pca = PCA(n_components=2)
    point_cloud_pca = pca.fit_transform(point_cloud)
    return point_cloud_pca

# 保存处理后的点云数据
def save_point_cloud(file_path, point_cloud):
    np.savetxt(file_path, point_cloud, delimiter=' ')

# 主函数
def main():
    input_file_path = 'point_cloud_data.txt'
    output_file_path = 'point_cloud_pca2d.txt'

    # 读取点云数据
    point_cloud = load_point_cloud(input_file_path)
    print("原始点云数据：\n", point_cloud[:3])

    # 对点云数据进行PCA操作
    point_cloud_pca = apply_pca_to_point_cloud(point_cloud)
    print("PCA处理后的点云数据：\n", point_cloud_pca[:3])

    # 保存处理后的点云数据
    save_point_cloud(output_file_path, point_cloud_pca)
    print(f"PCA处理后的点云数据已保存到 {output_file_path}")
    
    #可视化
    plt.scatter(point_cloud_pca[:, 0], point_cloud_pca[:, 1], c='blue', marker='o')
    plt.title('2D Visualization of Point Cloud Data')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()


if __name__ == "__main__":
    main()

