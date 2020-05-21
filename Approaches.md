## In Data Preparation NoteBook
1) Data aumented to 600 images per class.
2) Data is splitted to 80% Training & 20% validation.
3) Same Training and val data used for all approaches to correctly compare between them.

## First Apprach  
### Basic CNN-Model
	-  Training Accuracy = 0.9024
	- Validation Accuracy = 0.9029

	![alt CNN_Training_Accuracy](https://github.com/Naghamm/Scene_Recognition/blob/images/CNN_10_epochs_256_imres_Accuracy.png?raw=true)
    ![alt CNN_Train_Val_Plot](https://github.com/Naghamm/Scene_Recognition/blob/images/CNN_10_epochs_256_imres_Accuracy.png?raw=true)

## Second Approach
### Mobilenet-Model
	-  Training Accuracy = 0.9913
	- Validation Accuracy = 0.9587

	![alt Mobilenet_Training_Accuracy](https://github.com/Naghamm/Scene_Recognition/blob/images/Mobilenet_30_epochs_150_imres_Accuracy.png?raw=true)
    ![alt Mobilenet_Train_Val_Plot](https://github.com/Naghamm/Scene_Recognition/blob/images/Mobilenet_30_epochs_150_imres_Plot.png?raw=true)

## Third Approach (Best one)
### VGG16-Model 
	-  Training Accuracy = 0.9960
	- Validation Accuracy = 0.9749

	![alt VGG16_Training_Accuracy](https://github.com/Naghamm/Scene_Recognition/blob/images/VGG16_16_epochs_256_imres_Accuracy.png?raw=true)
    ![alt VGG16_Train_Val_Plot](https://github.com/Naghamm/Scene_Recognition/blob/images/VGG16_16_epochs_256_imres_PLot.png?raw=true)

    Docker container built on weights of this Approach