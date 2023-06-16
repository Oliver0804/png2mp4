import cv2
import os
import glob
import tqdm
import argparse

def convert_images_to_video(image_folder, video_name, fps):
    images = [img for img in sorted(glob.glob(os.path.join(image_folder, "*.png")))]
    frame = cv2.imread(images[0])
    height, width, _ = frame.shape
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    
    for i in tqdm.tqdm(range(len(images)), desc="轉換進度", ncols=70):
        video.write(cv2.imread(images[i]))
    video.release()

def main(conv_dir):
    subfolders = [f.path for f in os.scandir(conv_dir) if f.is_dir()]
    for folder in subfolders:
        video_name = folder + '.mp4'
        convert_images_to_video(folder, video_name, 24)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('conv_dir', type=str, help='輸入圖片的目錄')
    args = parser.parse_args()
    main(args.conv_dir)
