import cv2
from ultralytics import YOLO

def run_realtime_detection():
    # 1. Load the pretrained YOLOv8 model (yolov8n.pt is nano - lightweight & fast)
    # Replace with 'runs/detect/train/weights/best.pt' if using a custom fine-tuned model
    print("Loading YOLO model...")
    model = YOLO("yolov8n.pt")

    # 2. Open the primary webcam (device index 0)
    cap = cv2.VideoCapture(0)

    # Set frame dimensions (optional)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Error: Could not access webcam.")
        return

    print("Webcam feed started. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # 3. Run YOLO inference on the current frame
        # conf=0.5 ignores predictions with confidence lower than 50%
        results = model.predict(source=frame, conf=0.5, verbose=False)

        # 4. Extract annotated frame (bounding boxes + labels rendered by Ultralytics)
        annotated_frame = results[0].plot()

        # 5. Display the output window
        cv2.imshow("YOLO Real-Time Object Detection", annotated_frame)

        # Press 'q' to close the video stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_realtime_detection()
