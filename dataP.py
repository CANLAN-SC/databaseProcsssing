import os
import shutil
import random


def split_dataset(input_folder, output_folder, train_ratio=0.8):
	# 创建输出目录
	os.makedirs(output_folder, exist_ok=True)
	
	# 获取所有类别文件夹，过滤掉系统文件
	classes = [class_name for class_name in os.listdir(input_folder) if not class_name.startswith('.')]
	
	# 遍历每个类别
	for class_name in classes:
		class_path = os.path.join(input_folder, class_name)
		
		# 获取该类别下所有图像文件，过滤掉系统文件
		images = [image for image in os.listdir(class_path) if not image.startswith('.')]
		
		# 计算分割点，将数据集分成 train 和 val
		split_point = int(len(images) * train_ratio)
		
		# 随机打乱图像列表
		random.shuffle(images)
		
		# 分割 train 部分
		train_images = images[:split_point]
		train_output_path = os.path.join(output_folder, 'train', class_name)
		os.makedirs(train_output_path, exist_ok=True)
		for image in train_images:
			src_path = os.path.join(class_path, image)
			dest_path = os.path.join(train_output_path, image)
			shutil.copy(src_path, dest_path)
		
		# 分割 val 长部分
		val_images = images[split_point:]
		val_output_path = os.path.join(output_folder, 'val', class_name)
		os.makedirs(val_output_path, exist_ok=True)
		for image in val_images:
			src_path = os.path.join(class_path, image)
			dest_path = os.path.join(val_output_path, image)
			shutil.copy(src_path, dest_path)



# 调用函数进行数据集分割
input_folder = '/Users/suncheng/PycharmProjects/finalReport/garbage_classification'
output_folder = '/Users/suncheng/PycharmProjects/finalReport/database_good'
split_dataset(input_folder, output_folder, train_ratio=0.8)
