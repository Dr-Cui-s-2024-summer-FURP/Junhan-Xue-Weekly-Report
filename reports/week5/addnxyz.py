import numpy as np
import open3d as o3d

def load_points(file_path):
    """加载点云数据"""
    data = np.loadtxt(file_path, delimiter=' ')
    points = data[:, :3]  # 提取x, y, z坐标
    return points

def save_points_with_normals(points, normals, output_file):
    """将点云数据和法线保存到.txt文件"""
    combined_data = np.hstack((points, normals))
    np.savetxt(output_file, combined_data, fmt='%.6f', header='x y z nx ny nz')

def compute_normals(points):
    """计算点云的法线"""
    # 创建Open3D点云对象
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    
    # 计算法线
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    
    # 获取法线
    normals = np.asarray(pcd.normals)
    return normals

def main(input_file, output_file):
    points = load_points(input_file)
    normals = compute_normals(points)
    save_points_with_normals(points, normals, output_file)
    print(f'Processed data saved to {output_file}')

if __name__ == '__main__':
    input_file = 'point_cloud_data.txt'  # 输入的点云文件
    output_file = 'output_point_cloud_with_normals.txt'  # 输出的点云文件
    main(input_file, output_file)

