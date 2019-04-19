import numpy as np
from styx_msgs.msg import TrafficLight
from traffic_light_classifier import load_graph
from traffic_light_classifier import detect_traffic_light
import rospy


class TLClassifier(object):
    def __init__(self,classifier_model_type):
        
	self.label = {1:'green',2:'red',3:'yellow',4:'none'}

	if(classifier_model_type=='sim'):
	    self.score_threshold = 0.30
	    graph_folder_path='light_classification/models/inference_graph_sim/'
	else:
    	    self.score_threshold = 0.10
	    graph_folder_path='light_classification/models/inference_graph_real/'

	graph_file_path = graph_folder_path+'frozen_inference_graph.pb'
	#category_index = graph_folder_path+'label_map.pbtxt'
	
	rospy.loginfo('model %s',graph_file_path)
	self.detection_graph = load_graph(graph_file_path)

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO:done implement light color prediction
	
	cls,scores=detect_traffic_light(image,self.detection_graph)
	cl=cls[0]
	score=scores[0]
	light_color=self.label[cl]
	#rospy.loginfo('%s--%s',cls,scores)
	rospy.loginfo('(%s-%s-%s)',cl,score,light_color)
	#rospy.loginfo('%s,%s',cl,light_color)

	#index=np.argmax(output['detection_scores'])
	#rospy.loginfo('index-',index,',class-',output['detection_classes'][index])
	#print(output['detection_classes'])
	#print(output['detection_scores'])
	#rospy.loginfo('score-%s',output['detection_scores'][index])
        #predict_str = self.category_index[output['detection_classes'][index]]['name']
        #predict_id = self.category_index[output['detection_classes'][index]]['id']
       	#rospy.loginfo('(%s-%s-%s-%s)',TrafficLight.RED,TrafficLight.YELLOW,TrafficLight.GREEN,TrafficLight.UNKNOWN)
	

	if(score>self.score_threshold):

		if(light_color=='red'):
		    return TrafficLight.RED
		elif(light_color=='yellow'):
		    return TrafficLight.YELLOW
		elif(light_color=='green'):
		    return TrafficLight.GREEN

        return TrafficLight.UNKNOWN



