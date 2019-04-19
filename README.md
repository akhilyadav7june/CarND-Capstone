
# CarND-Capstone

This is the project repo for the final project of the Udacity Self-Driving Car Nanodegree: Programming a Real Self-Driving Car.

[image1]: ./imgs/sim.jpg "Simulator"
[image2]: ./imgs/real.jpg "Real"

#### Name (udacity account email)
#### Akhilesh Kr. Yadav (akhilyadav7june@gmail.com)

* This project divide into three parts
    
    * The perception subsystem detects traffic lights and obstacles. Here i used tensorflow object detection API to detect and classify traffic light color. Following steps performed for this subsystem:

        * Gathering of the image data
        * Label and annotate the images
            * I tried the data but one of the great person [Anthony Sarkis](https://medium.com/@anthony_sarkis) who made his annotated data-set openly available. I downloaded and used that data to train my models.
        * Training the Model
            * We first need to convert our data into the TFRecord format. This basically takes images and the yaml file of annotations and combines them into one that can be used as input for the training.    
            * We need to also download [tensorflow object detection apis](https://github.com/tensorflow/models/tree/289a2f99a7df528f6193a5ab3ee284ff3112b731), trained [inference model](https://github.com/tensorflow/models/blob/289a2f99a7df528f6193a5ab3ee284ff3112b731/object_detection/g3doc/detection_model_zoo.md). Installation process and all its dependencies required to run use object detection apis are [here](https://github.com/tensorflow/models/blob/289a2f99a7df528f6193a5ab3ee284ff3112b731/object_detection/g3doc/installation.md).
            * We need to choose the model and parameters in the config file. I choose ssd model instead of faster_rcnn because ssd is faster. I knew that accuracy is better with faster_rcnn. But i choosed ssd due to performance. Below parameter i setted in config
              1. num_classes: 4  (because we have 4 classes for traffic lights, red, green, yellow and none) 
              2. fine_tune_checkpoint (set the location of the pre-trained model check point file)
              3. input_path (set the location of TFRecord file which you created in 1st step)
              4. label_map_path (this file contains all the four classes with there id)
              5. num_examples (number if image files for training)
              6. num_steps (number for iteration)
            * After training we have to export the trained model into frozen inference graph so that we can use this into our code for detection and classification of traffic lighht color.
        * Below is the working result images of both simulator and real:
            ![image1]
            
            ![image2]
    * The planning subsystem (node waypoint updater) updates the waypoints and the associated target velocities.
       
        * Find the nearest n waypoints ahead of the vehicle where n is defined as a set number of waypoints.
        * Determine if a red traffic light falls in the range of waypoints ahead of the traffic light.
        * Calculate target velocities for each waypoint.
        * Publish the target waypoints with velocities to the final_waypoints topic.
    * The control subsystem actuates the throttle, steering, and brake to navigate the waypoints with the target velocity.Here i implemented the controllers which requires to navigate the vechicle safely. And DBW node which implements logic to accept target linear and angular velocities and publish throttle, brake, and steering commands to respective topics.


Please use **one** of the two installation options, either native **or** docker installation.

### Native Installation

* Be sure that your workstation is running Ubuntu 16.04 Xenial Xerus or Ubuntu 14.04 Trusty Tahir. [Ubuntu downloads can be found here](https://www.ubuntu.com/download/desktop).
* If using a Virtual Machine to install Ubuntu, use the following configuration as minimum:
  * 2 CPU
  * 2 GB system memory
  * 25 GB of free hard drive space

  The Udacity provided virtual machine has ROS and Dataspeed DBW already installed, so you can skip the next two steps if you are using this.

* Follow these instructions to install ROS
  * [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu) if you have Ubuntu 16.04.
  * [ROS Indigo](http://wiki.ros.org/indigo/Installation/Ubuntu) if you have Ubuntu 14.04.
* [Dataspeed DBW](https://bitbucket.org/DataspeedInc/dbw_mkz_ros)
  * Use this option to install the SDK on a workstation that already has ROS installed: [One Line SDK Install (binary)](https://bitbucket.org/DataspeedInc/dbw_mkz_ros/src/81e63fcc335d7b64139d7482017d6a97b405e250/ROS_SETUP.md?fileviewer=file-view-default)
* Download the [Udacity Simulator](https://github.com/udacity/CarND-Capstone/releases).

### Docker Installation
[Install Docker](https://docs.docker.com/engine/installation/)

Build the docker container
```bash
docker build . -t capstone
```

Run the docker file
```bash
docker run -p 4567:4567 -v $PWD:/capstone -v /tmp/log:/root/.ros/ --rm -it capstone
```

### Port Forwarding
To set up port forwarding, please refer to the [instructions from term 2](https://classroom.udacity.com/nanodegrees/nd013/parts/40f38239-66b6-46ec-ae68-03afd8a601c8/modules/0949fca6-b379-42af-a919-ee50aa304e6a/lessons/f758c44c-5e40-4e01-93b5-1a82aa4e044f/concepts/16cf4a78-4fc7-49e1-8621-3450ca938b77)

### Usage

1. Clone the project repository
```bash
git clone https://github.com/udacity/CarND-Capstone.git
```

2. Install python dependencies
```bash
cd CarND-Capstone
pip install -r requirements.txt
```
3. Make and run styx
```bash
cd ros
catkin_make
source devel/setup.sh
roslaunch launch/styx.launch
```
4. Run the simulator

### Real world testing
1. Download [training bag](https://s3-us-west-1.amazonaws.com/udacity-selfdrivingcar/traffic_light_bag_file.zip) that was recorded on the Udacity self-driving car.
2. Unzip the file
```bash
unzip traffic_light_bag_file.zip
```
3. Play the bag file
```bash
rosbag play -l traffic_light_bag_file/traffic_light_training.bag
```
4. Launch your project in site mode
```bash
cd CarND-Capstone/ros
roslaunch launch/site.launch
```
5. Confirm that traffic light detection works on real life images
