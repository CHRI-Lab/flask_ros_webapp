# Flask App README

This is a minimal template for a Flask application that subscribes to a ROS topic and changes the image rendered full screen on the client side.

## Requirements

- Python 3.x installed on your machine
- Flask and other dependencies (check the `requirements.txt` file)

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd flask_ros_webapp
```

```bash
pip install -r requirements.txt
```

## Usage

To start the Flask App, execute the following command:

```bash
python3 app.py
```

The application will be accessible at http://localhost:5000 
or using the PC IP address at http://IP:5000


To publish a new image called image1.jpg: 

```bash
ros2 topic pub /image_name std_msgs/String 'data: image1.jpg' -1
```

Note that the image must be placed in the folder /static to be accessible.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request to the repository.

## License

This app is licensed under the MIT License.

