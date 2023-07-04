from flask import Flask, render_template, request # Flask

# ROS imports to setup the node
import rclpy
from std_msgs.msg import String

# Imports for threading operations
import sys
from threading import Thread
import atexit

new_image = None # Global variable to hold the image name



##### Setting up the ROS node:
def listener_callback(msg):
    global new_image
    node.get_logger().info('I heard: "%s"' % msg.data)
    new_image = msg.data



# Initializing the node
rclpy.init(args=None)
node = rclpy.create_node('Show_image_python')

Thread(target=lambda:node).start() # Starting the Thread with a target in the node

subscription = node.create_subscription(String,'/image_name', listener_callback, 10)


app = Flask(__name__)

def get_image():
    rclpy.spin_once(node,timeout_sec=1.0)
    return new_image

@app.route('/')
def index():
    new_image = get_image()
    return render_template('index.html', new_image=new_image)

@app.route('/change_image', methods=['POST'])
def change_image():
    new_image = request.form.get('image')
    return render_template('index.html', new_image=new_image)


#defining function to run on shutdown
def close_running_threads():
    rclpy.shutdown()
    print("closed ROS")
    sys.exit(0)
    

## Main funcion, only initiate the Flask app
def main(args=None):
    atexit.register(close_running_threads)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    app.run(host='0.0.0.0', port=5000 ,debug=False)


if __name__ == '__main__':
    main()


    
