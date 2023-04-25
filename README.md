# Vision

### <ins>Question 1</ins>
The process of estimating the parameters of a camera is called camera calibration.
This means we have all the information (parameters or coefficients) about the camera required to determine an accurate relationship between a 3D point in the real world and its corresponding 2D projection (pixel) in the image captured by that calibrated camera.

Write a python script to automatically find the camera calibration parameters using a 6x8 checkerboard pattern. 
Record a video (or share photographs) to show how the calibration setup works.

You can find the checkerboard pattern here: 

https://raw.githubusercontent.com/MarkHedleyJones/markhedleyjones.github.io/master/media/calibration-checkerboard-collection/Checkerboard-A4-30mm-8x6.pdf


### <ins>Question 2</ins>
###### Task 1:
Download the dataset from the following Google Drive link: 
This dataset consists of various images containing people at an industrial site
Implement any person detection model, such as MobileNet, YOLOv3, or YOLOv5, to detect individuals in the images. You can use any programming language of your choice.
###### Task 2:
To enhance the performance of your small object detection model, several techniques can be useful. These include capturing higher-resolution images, using a higher input resolution for your model, dividing images into smaller tiles, generating additional data using augmentation methods, and automatically determining model anchors.
Your task is to divide each image into smaller tiles (you can use 12 tiles- 4x3; they may overlap - check out the example here) and apply your person detection model to each tile separately. Compare the results with and without the implementation of the technique to demonstrate if it has improved the performance of the detection model.

#### Include the accuracy and precision of the model before and after the implementation of the chosen technique. You can also include visualizations of the detected individuals in the images to illustrate the impact of the technique on the model's performance.
