import cv2

# Use the identified camera index
camera_index = 1  # Replace with the correct index
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print(f"Failed to access camera {camera_index}")
else:
    print(f"Accessing camera {camera_index}")
    
    # Get initial resolution
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Frame width
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Frame height
    print(f"Initial camera resolution: {width} x {height}")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Display resolution on the frame
        resolution_text = f"Resolution: {width} x {height}"
        cv2.putText(frame, resolution_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Show the camera feed
        cv2.imshow("Camera Feed", frame)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
