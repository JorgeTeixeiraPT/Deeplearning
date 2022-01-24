# -*- coding: utf-8 -*-
"""TerceiraEntregaDeep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lyul9qaHQr7kzdR0Eh0QxSprr_f8Lq11
"""

from google.colab import drive
drive.mount('/content/gdrive',force_remount=True)

!git clone https://github.com/AlexeyAB/darknet

# Commented out IPython magic to ensure Python compatibility.
# change makefile to have GPU and OPENCV enabled
# %cd darknet
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile

# verify CUDA
!/usr/local/cuda/bin/nvcc --version

# make darknet (build)
!make

# copy the .zip file into the root directory of cloud VM
!cp /content/gdrive/MyDrive/Weapons_Detection_YOLOv3-master/data/obj.zip ../

# unzip the zip file and its contents should now be in /darknet/data/obj
!unzip /content/gdrive/MyDrive/Weapons_Detection_YOLOv3-master/data/obj.zip -d data/

#.cfg

#Comentar Batch e Subdivisions =1 ; e retirar comentado das mesmas a seguir;
#MUDAR: 
	#Max_batches= 2000*class
	#steps= 80% of Max_batches,90% of Max_batches
	#CRL+F "yolo" (para todos)
		#Classes = Class
		#(convolutional)Filters = (Class+5)*3
		#(se der erros de memoria ou mais rapido) random= 0

!cp /content/gdrive/MyDrive/Weapons_Detection_YOLOv3-master/data/yolov3-tiny_mod.cfg ./cfg

# upload the obj.names and obj.data files to cloud VM from Google Drive
!cp /content/gdrive/MyDrive/Weapons_Detection_YOLOv3-master/data/yolo.names ./data
!cp /content/gdrive/MyDrive/Weapons_Detection_YOLOv3-master/data/yolo_mod.data  ./data

# upload the generate_train.py script to cloud VM from Google Drive
#!cp /content/gdrive/MyDrive/Weapons_Detection_YOLOv3-master/data/Generate_train_mod.py ./
#!python Generate_train_mod.py

# verify train.txt can be seen in our darknet/data folder
#!ls data/

!cp /content/gdrive/MyDrive/Weapons_Detection_YOLOv3-master/data/val.txt ./data
!cp /content/gdrive/MyDrive/Weapons_Detection_YOLOv3-master/data/train.txt ./data

# upload pretrained convolutional layer weights
!wget http://pjreddie.com/media/files/darknet53.conv.74

"""TIP: This training could take several hours depending on how many iterations you chose in the .cfg file. You will want to let this run as you sleep or go to work for the day, etc. However, Colab Cloud Service kicks you off it's VMs if you are idle for too long (30-90 mins).

To avoid this hold (CTRL + SHIFT + i) at the same time to open up the inspector view on your browser.

Paste the following code into your console window and hit Enter
"""

function ClickConnect(){
console.log("Working"); 
document.querySelector("colab-toolbar-button#connect").click() 
}
setInterval(ClickConnect,60000)

#!./darknet detector train <path to obj.data> <path to custom config> darknet53.conv.74 -dont_show

# train your custom detector
!./darknet detector train data/yolo_mod.data cfg/yolov3-tiny_mod.cfg darknet53.conv.74 -dont_show

imShow('chart.png')

!./darknet detector train data/yolo_mod.data cfg/yolov3-tiny_mod.cfg /content/gdrive/MyDrive/backup/yolov3-tiny_mod_last.weights -dont_show

# This stops 'Run all' at this cell by causing an error
assert False
# Zona de testes de tudo um pouco

# get yolov3 pretrained coco dataset weights
!wget https://pjreddie.com/media/files/yolov3.weights

# run darknet detection
!./darknet detect /content/gdrive/MyDrive/weapon_detection/yolov3_testing.cfg /content/gdrive/MyDrive/weapon_detection/yolov3_training_2000.weights /content/gdrive/MyDrive/weapon_detection/arma.jpg
#!./darknet detect cfg/yolov3.cfg yolov3.weights data/person.jpg

# show image using our helper function
imShow('predictions.jpg')

#!./darknet detector demo /content/gdrive/MyDrive/weapon_detection/yolov3_testing.cfg /content/gdrive/MyDrive/weapon_detection/yolov3_training_2000.weights -dont_show /content/gdrive/MyDrive/weapon_detection/ak47.mp4 -i 0 -out_filename /mydrive/videos/results.avi
!./darknet detector demo /content/gdrive/MyDrive/Weapons_Detection_YOLOv3-master/data/yolo_mod.data /content/gdrive/MyDrive/Weapons_Detection_YOLOv3-master/data/yolov3-tiny_mod.cfg /content/gdrive/MyDrive/weapon_detection/yolov3_training_2000.weights -dont_show /content/gdrive/MyDrive/weapon_detection/ak47.mp4 -i 0 -out_filename /content/gdrive/MyDrive/results2.avi

# This stops 'Run all' at this cell by causing an error
assert False