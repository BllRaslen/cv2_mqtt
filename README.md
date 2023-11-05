# Image Publisher with MQTT

This Python script demonstrates an image publisher that captures images from a camera using OpenCV and publishes their URLs to an MQTT topic. This README provides information about the script, its usage, and configuration.

## Requirements
- Python 3.7 or later
- OpenCV (cv2)
- Paho MQTT library

You can install the required libraries using `pip`:
```bash
pip install opencv-python-headless paho-mqtt
```

## Usage

1. Clone or download the repository to your local machine.

2. Ensure you have an MQTT broker set up and running. You may need to modify the `mqtt_broker_address` and `mqtt_port` variables in the script to match your MQTT broker's address and port.

3. Configure your MQTT topic by modifying the `mqtt_topic` variable to your desired topic name.

4. If your MQTT broker requires authentication, set the `username` and `password` variables with your credentials.

5. Customize the `image_save_directory` variable to specify the directory where captured images will be saved.

6. Run the script using the following command:

```bash
python your_script_name.py
```

The script will capture images from the camera, save them to the specified directory, and publish their URLs to the MQTT topic.

## Script Description

- `ImagePublisher` class: The main class that handles image capture and MQTT publishing.
  - `__init__`: Initializes the MQTT client, camera, and other parameters.
  - `capture_and_publish`: Captures images from the camera, saves them, and publishes their URLs to the MQTT topic.
- `if __name__ == "__main__"`: The script entry point. It creates an instance of `ImagePublisher` and starts capturing and publishing images.

## Configuration

- `mqtt_broker_address`: Set this to the address of your MQTT broker.
- `mqtt_port`: Set this to the port number your MQTT broker is listening on.
- `mqtt_topic`: Set this to the MQTT topic where image URLs will be published.
- `username` and `password`: If your MQTT broker requires authentication, set these variables with your credentials.
- `image_save_directory`: Set this to the directory where captured images will be saved.

## Customization

You can further customize the script by modifying the image URL format and capture frequency as per your requirements.

## License

This script is provided under the MIT License. You are free to use, modify, and distribute it as needed.
