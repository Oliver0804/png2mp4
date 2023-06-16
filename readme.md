# 圖片轉換成視頻

這個Python腳本可以將指定目錄中的PNG圖片轉換成MP4視頻。

## 使用方式

請確保您的電腦已經安裝了`OpenCV` 和 `tqdm`兩個Python套件。如果還未安裝，可以使用下列指令安裝：

```sh
pip install opencv-python
pip install tqdm
```

您可以在命令列中使用下列語法來執行這個Python腳本：

```sh
python png2mp4.py <folder_path>
```

例如，如果您的圖片目錄是/home/user/images，那麼您可以使用以下的命令：

```sh
python png2mp4.py ../png2mp4/
```