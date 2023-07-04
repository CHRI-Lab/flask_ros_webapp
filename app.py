from flask import Flask, render_template, request # Flask

# ROS imports to setup the node
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Imports for threading operations
import signal, sys
from threading import Thread, Event

new_image = None # Global variable to hold the image name

event = Event()

##### Setting up the ROS node:
def listener_callback(msg):
    global new_image
    node.get_logger().info('I heard: "%s"' % msg.data)
    new_image = msg.data
    event.set()


# Initializing the node
rclpy.init(args=None)
node = rclpy.create_node('Show_image_python')

Thread(target=lambda:node).start() # Starting the Thread with a target in the node

subscription = node.create_subscription(String,'image_name', listener_callback, 10)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/change_image', methods=['POST'])
def change_image():
    new_image = request.form.get('image')
    return render_template('index.html', new_image=new_image)




## Function that finish the actual context
def signal_handler(signal, frame):
    rclpy.shutdown()
    sys.exit(0)

signal.signal(signal.SIGINT,signal_handler) # Calls the 'signal_handler' and finish the actual signal (like a Ctrl + C)
 
## Main funcion, only initiate the Flask app
def main(args=None):
    app.run(host='0.0.0.0', port=8080 ,debug=True)


if __name__ == '__main__':
    main()


    
