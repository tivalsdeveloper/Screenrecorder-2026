import cv2
import numpy as np
from PIL import ImageGrab
import time

def manual_screen_recorder():
    # 1. Setup Screen & Video Writer
    # Use 'mp4v' or 'avc1' for MP4 format
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    # Get initial screen size
    screen = ImageGrab.grab()
    width, height = screen.size
    
    # Initialize the output file
    # Note: We set a standard FPS (e.g., 20.0)
    out = cv2.VideoWriter('long_recording_tivals.mp4', fourcc, 20.0, (width, height))
    
    print("Recording started...")
    print("Go to the small preview window and press 'q' to STOP recording.")

    try:
        while True:
            # 2. Capture the current screen frame
            img = ImageGrab.grab()
            frame = np.array(img)
            
            # 3. Convert RGB to BGR (required for OpenCV)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # 4. Add the Watermark (tivalsdeveloper)
            # Position: bottom right
            cv2.putText(frame, "tivalsdeveloper", (width - 250, height - 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            
            # 5. Write the frame to the file
            out.write(frame)
            
            # 6. Show a tiny preview window to allow keyboard input
            # We resize it so it doesn't take up your whole screen
            cv2.imshow('Recording Status (Press Q to Stop)', cv2.resize(frame, (480, 270)))
            
            # 7. Check for 'q' key press to break the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # 8. Clean up
        out.release()
        cv2.destroyAllWindows()
        print("Recording stopped and saved as long_recording_tivals.mp4")

if __name__ == "__main__":
    manual_screen_recorder()