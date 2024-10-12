import numpy as np
import cv2 as cv

def video_capture():
    # 摄像头
    #cap = cv.VideoCapture(1)
    #视频文件
    cap = cv.VideoCapture('../assets/videos/test.mov')

    cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()


        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv.imshow('frame',gray)
        # OpenCV 中 waitKey() 函数的返回值包含其他信息（高位字节），而 0xFF 是用于屏蔽多余的高位字节，使得我们只关心按键的低位字节
        # 如果你使用的计算机是64位，不必加 & 0xFF
        # 使用 & 0xFF 是为了兼容不同平台，确保我们得到的只是实际按键的值。
        if cv.waitKey(1) == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

def video_save():
    cap = cv.VideoCapture(1)
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    # 文档示例中size为(640,480)，结果视频打不开，改为这个尺寸后正常
    size = (width, height)
    #print(size)
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter.fourcc(*'X264')
    out = cv.VideoWriter('../tmp/output.mkv', fourcc, 20.0, size)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv.flip(frame, 0)

            # write the flipped frame
            out.write(frame)

            cv.imshow('frame',frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    #video_capture()
    video_save()
