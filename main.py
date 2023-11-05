import paho.mqtt.client as mqtt
import cv2
import time
import tempfile
import os


class ImagePublisher:
    def __init__(self, mqtt_broker, mqtt_port, mqtt_topic, camera_index=0, username=None, password=None,
                 image_save_dir='images'):
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.mqtt_topic = mqtt_topic
        self.camera_index = camera_index
        self.username = username
        self.password = password
        self.client = mqtt.Client("image_publisher")
        self.image_save_dir = image_save_dir

        if self.username and self.password:
            self.client.username_pw_set(self.username, self.password)

        # Connect to the MQTT broker
        self.client.connect(self.mqtt_broker, self.mqtt_port, 60)

        # Open the camera
        self.cap = cv2.VideoCapture(self.camera_index)

        # Check if the camera opened successfully
        if not self.cap.isOpened():
            print("Error: Could not open the camera.")
            self.cap.release()
            cv2.destroyAllWindows()
            exit()

        # Create the image save directory if it doesn't exist
        os.makedirs(self.image_save_dir, exist_ok=True)

    def capture_and_publish(self):
        try:
            while True:
                # Capture an image from the camera
                ret, frame = self.cap.read()

                if not ret:
                    print("Error: Could not capture an image.")
                    break

                # Generate a unique image filename
                image_filename = os.path.join(self.image_save_dir, f"image_{int(time.time())}.jpg")

                # Save the image to the file
                cv2.imwrite(image_filename, frame)

                # Construct the URL for the saved image
                image_url = f"https://www.code-boot.com/{image_filename}"  # Replace with your website URL

                # Publish the image URL to the MQTT topic
                self.client.publish(self.mqtt_topic, payload=image_url, qos=0, retain=False)

                print(f"Image URL published to MQTT topic: {image_url}")

                # Add a delay (e.g., 10 seconds) before capturing and publishing the next image
                time.sleep(1)

        except KeyboardInterrupt:
            print("Image publisher stopped by the user")

        # Release the camera and close OpenCV window
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    mqtt_broker_address = "localhost"  # Change this to your MQTT broker's address
    mqtt_port = 1883  # Change this to your MQTT broker's port
    mqtt_topic = "image_links"  # Change this to your desired MQTT topic
    mqtt_topic = "cv2/pro"
    username = "bllraslen"
    password = "bll.raslen"
    image_save_directory = "images"  # Change this to the directory where you want to save the images

    image_publisher = ImagePublisher(mqtt_broker_address, mqtt_port, mqtt_topic, username=username, password=password,
                                     image_save_dir=image_save_directory)

    image_publisher.capture_and_publish()


