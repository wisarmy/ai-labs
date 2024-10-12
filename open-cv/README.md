# OpenCV
## 图像
代码请查看 [test_image.py](./test_image.py)

cv.imread()函数用于读取图像，需要注意的是，该图像应该处在Python代码源文件或者已给出完整路径的工作目录中。

针对函数的第二个参数，通过以下几个例子分别说明各自功能。
  - cv.IMREAD_COLOR：默认参数，以彩色模式加载图像，图像的透明度将被忽略。
  - cv.IMREAD_GRAYSCALE：以灰度模式加载图像。
  - cv.IMREAD_UNCHANGED：以alpha通道模式加载图像。

注意：你也可以通过传递1，0，-1来代替上面三个函数功能。

# Matplotlib
代码请查看 [test_matplotlib.py](./test_matplotlib.py)

* 注意：OpenCV加载的彩色图像处于BGR模式，但Matplotlib以RGB模式显示。因此，如果使用OpenCV读取图像，则Matplotlib中的彩色图像将无法正确显示。

## 视频
代码请查看 [test_video.py](./test_video.py)
* 注意：确保已安装正确版本的ffmpeg或gstreamer。 若使用Video Capture遇到麻烦，可能原因是错误安装了ffmpeg/gstreamer。
