# ML_Bench_Task
Mouse Paw detection with model deployment

Step1: Run the model.ipynb file in Google Colab

Step2: Run all the code sections.

*** Make sure you update all the paths according to your Pathsets if required***

Step3: Import dataset directly from roboflow account. 
I have provided the API Key to access the dataset directly. 
Please avoid sharing it further. 

Step4: After running all code sections please download the onnx format file. 

Step5(locally Launch): If you want to run locally, Open the app.py file in vscode.
       Move all the files( best.onnx, requirements.txt in same directory as app.py)
       Run app.py and click the link to launch locally.

step6(Launch on HuggingFace Space): Open the link to the Hugging face 
Link to Hugging Face Space:  https://huggingface.co/spaces/WadeelaG/ML_Bench_Task

Follow below instruction for Using Deployed Model. 

Instructions for Using the YOLOv8 Object Detection Model on Hugging Face Spaces

Overview:
This is an object detection model built with YOLOv8 and deployed on Hugging Face Spaces using Gradio for easy interaction. 
The model has been trained on custom data for detecting mouse paws. 
The interface allows you to upload images, adjust the confidence threshold and IoU (Intersection over Union) threshold, and get results with bounding boxes around detected objects.

"How to Use the Object Detection Model:"

Step1:	Access the Web Interface:

o	Visit the Hugging Face Spaces page where the model is deployed. The page URL will be something like this: 
o	https://huggingface.co/spaces/WadeelaG/ML_Bench_Task
o	You should see a user interface with an image upload button and sliders for adjusting the confidence and IoU thresholds.

Step2:	Upload an Image:

o	Click the "Upload Image" button, which will open a file explorer dialog.
o	Select an image (JPEG, PNG, or other supported formats) from your computer that you want to process with the model.

Step3:	Adjust the Confidence Threshold:

o	The "Confidence Threshold" slider allows you to control the minimum confidence level required for detecting an object.
o	The slider range is from 0 to 1, where: 
	A value closer to 1 requires higher confidence from the model to count an object as detected.
	A value closer to 0 will allow for lower confidence, which may result in more detections but potentially more false positives.
o	The default value is 0.25, but you can adjust it based on your needs.


Step4:	Adjust the IoU Threshold:

o	The "IoU Threshold" slider controls the minimum overlap required between the predicted bounding box and the ground truth to consider the detection valid.
o	The slider range is from 0 to 1, where: 
	A value closer to 1 will enforce a stricter condition for overlapping boxes, meaning fewer boxes will be considered valid.
	A value closer to 0 allows more overlap, which can result in multiple bounding boxes for the same object.
o	The default value is 0.45, but feel free to adjust it for better accuracy.

Step5:	Get Object Detection Results:
o	Once the image is uploaded and the thresholds are set, the model will process the image and display the result with bounding boxes around detected objects.
o	The result will show up on the right side of the interface, where you can see the detected objects with their confidence scores.


Step6:	View the Output:
o	The output will be the same image, but with bounding boxes drawn around any detected objects.
o	Each bounding box will be labeled with the object name (e.g., "mouse paw" if your dataset included that class) and the confidence score for the detection.

Summary:
1.	Go to the Hugging Face Spaces link.
2.	Upload an image.
3.	Set the confidence threshold and IoU threshold using sliders.
4.	See the object detection results with bounding boxes.
5.	Download or share the result if needed.
