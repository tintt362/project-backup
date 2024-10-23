import cv2
from flask import Flask, Response

app = Flask(__name__)


def generate_frames():
    camera = cv2.VideoCapture(0)  # 0 là webcam mặc định

    # Cập nhật độ phân giải (ví dụ 640x480 hoặc 320x240 cho tốc độ nhanh hơn)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Thay đổi kích thước khung hình (ví dụ 480x320 để phù hợp với điện thoại)
            frame = cv2.resize(frame, (480, 320))

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Tạo HTTP response stream dưới dạng multipart/x-mixed-replace
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
