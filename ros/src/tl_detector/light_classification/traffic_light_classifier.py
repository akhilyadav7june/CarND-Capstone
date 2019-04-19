import os
from PIL import Image
import numpy as np
import tensorflow as tf

#----Load a (frozen) Tensorflow model into memory.
def load_graph(graph_file):
    """Loads a frozen inference graph"""
    graph = tf.Graph()
    with graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(graph_file, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    return graph

#--- helper code
def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)


def detect_traffic_light(image,detection_graph):

	#detection_graph = load_graph(graph_file_path)

	with detection_graph.as_default():
	    with tf.Session(graph=detection_graph) as sess:
		image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
		detect_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
		detect_scores = detection_graph.get_tensor_by_name('detection_scores:0')
		detect_classes = detection_graph.get_tensor_by_name('detection_classes:0')
		num_detections = detection_graph.get_tensor_by_name('num_detections:0')
		
		#print(img_path)
		#image = Image.open(img_path)
		#image_np = load_image_into_numpy_array(image)
		image_expanded = np.expand_dims(image, axis=0)
		    
		(boxes, scores, classes, num) = sess.run(
		        [detect_boxes, detect_scores, detect_classes, num_detections],
		        feed_dict={image_tensor: image_expanded})
		    
		#print('SCORES')
		#print(scores[0])
		#print('CLASSES')
		#print(classes[0])
		#print('color')
		#print(label[classes[0][0]])
		
	return	classes[0],scores[0]
