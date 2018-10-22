import tensorflow as tf
import numpy as np
import os,glob,cv2
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

image_size=64
num_channels=3
images = []

path = 'car3.jpg'
image = cv2.imread(path) ## read the image for predict
# Resizing the image to our desired size and preprocessing will be done exactly as done during training
image = cv2.resize(image, (image_size, image_size),0,0, cv2.INTER_LINEAR)
images.append(image)
images = np.array(images, dtype=np.uint8)
images = images.astype('float32')
images = np.multiply(images, 1.0/255.0) 
#The input to the network is of shape [None image_size image_size num_channels]. Hence reshape.
x_batch = images.reshape(1, image_size,image_size,num_channels)

## Restore the saved model
sess = tf.Session()
# Step-1: Recreate the network graph. At this step only graph is created.
saver = tf.train.import_meta_graph('./bus-car-model/bus-car.ckpt-15990.meta')
# Step-2: Now load the weights saved using the restore method.
saver.restore(sess, './bus-car-model/bus-car.ckpt-15990')

# Accessing the default graph which we have restored
graph = tf.get_default_graph()

# Get hold of the op that we can be processed to get the output.
# In the original network y_pred is the tensor that is the prediction of the network
y_pred = graph.get_tensor_by_name("y_pred:0")

## Feed the images to the input placeholders
x= graph.get_tensor_by_name("x:0") 
y_true = graph.get_tensor_by_name("y_true:0") 
y_test_images = np.zeros((1, 2)) 


### Creating the feed_dict that is required to be fed to calculate y_pred 
feed_dict_testing = {x: x_batch, y_true: y_test_images}
result=sess.run(y_pred, feed_dict=feed_dict_testing)
# result is of this format [probabiliy_of_rose probability_of_sunflower]
# bus [1 0]
res_label = ['bus','car']
print(res_label[result.argmax()])
