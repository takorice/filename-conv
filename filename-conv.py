import glob
import os

# image ディレクトリ配下の画像名をリネームする
# print(glob.glob('./image/*'))
for index, path in enumerate(glob.glob('./image/*')):
    os.rename(path, './image/target_image'+str(index)+'.jpeg')
