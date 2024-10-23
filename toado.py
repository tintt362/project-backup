import cv2

# Hàm callback để xử lý sự kiện chuột
def get_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Kiểm tra xem có nhấn chuột trái không
        print(f"Tọa độ: ({x}, {y})")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f"({x},{y})", (x, y), font, 0.5, (255, 0, 0), 2)

# Đọc video
cap = cv2.VideoCapture(r'D:\tin\pythonProjectTinV2\output2_video.mp4')

# Kiểm tra xem có mở được video không
if not cap.isOpened():
    print("Không thể mở video.")
    exit()

# Thiết lập hàm callback cho cửa sổ hiển thị video
cv2.namedWindow("Video")
cv2.setMouseCallback("Video", get_mouse_click)

# Vòng lặp đọc và hiển thị từng frame trong video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Không thể đọc frame, có thể video đã hết.")
        break

    # Hiển thị frame
    cv2.imshow("Video", frame)

    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên sau khi hoàn thành
cap.release()
cv2.destroyAllWindows()
