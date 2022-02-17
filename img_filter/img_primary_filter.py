import re
import os
import cv2
import shutil
import numpy as np
import argparse

# 检测输入图像是否需要
def check_img(img_path):
    img = cv2.imread(img_path, flags=cv2.IMREAD_COLOR)

    # file info - resolution
    file_size = os.path.getsize(img_path)
    img_height, img_width = img.shape[:2]
    if file_size < 10 * 1024 or img_width < 256 or img_height < 256:
        return False

    # file info - Aspect ratio
    # if file_size < 10 * 1024 or img_width < 256 or img_height < 256:
    #     return False

    # image basic feature
    img_dy = img[:img_height-1] - img[1:]
    img_dx = img[:, :img_width-1] - img[:, 1:]
    img_gradient = np.mean(np.abs(img_dx)) + np.mean(np.abs(img_dy))
    print(img_path, "img_gradient =", img_gradient)
    if img_gradient < 50:
        return False

    return True

def MyMakeDir(dir_path):
    # 判断文件存在，不存在新建
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


parser = argparse.ArgumentParser(description="img_primary_filter")
parser.add_argument('--root_dir', default="../Image-Downloader-master/download_images/parrot", help='root dir')
parser.add_argument('--file_sff', default="jpeg|jpg|png", help='file_suffix')
parser.add_argument('--rm_dir', default="/remove", help='remove dir,based on root dir')
args = parser.parse_args()

if __name__ == '__main__':

    root_dir = args.root_dir
    file_suffix = args.file_sff
    remove_dir = root_dir + args.rm_dir

    MyMakeDir(remove_dir)

    for img_name in os.listdir(root_dir):
        # 对处理文件的类型进行过滤
        if re.search(file_suffix, img_name) is None:
            continue
        img_path = root_dir + "/" + img_name
        # 根据图片进行初步筛选
        if not check_img(img_path):
            output_path = remove_dir + "/" + img_name
            shutil.move(img_path, output_path)
