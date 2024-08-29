# Person-Car-Detector
In this repository, I will train a yolov7 detector model for detecting person and car

## Downloading Dataset 
Download dataset from given link and unzip the tar file
```
wget https://evp-ml-data.s3.us-east-2.amazonaws.com/ml-interview/openimages-personcar/trainval.tar.gz
tar -xvf trainval.tar.gz
rm trainval.tar.gz
```
## Preparing Yolo labels from Annotations
Now we will prepare yolo labels from given annotation json file.
```
mkdir trainval/labels/
python json_to_yolo.py
```

## Split dataset into train, val and test set
We have totol 2239 images, We will take 70% (1567 images) in training set, 20% (448 images) in valididation set and 10% (224 images) in test set.
So I have created 3 text file for training, validation and testing set respectively in shuffle order. 

## Creating custom.yaml for training
I have created custom.yaml file with taking refrence of original `data/coco.yaml` file, this custom file will be used in traingin phase.

## Training Model
I have Nvidia RTX2060 6G, I am able to train yolo model with batch size of 4.
```
cp custom.yaml yolov7/data/
cd yolov7/
python train.py --workers 8 --device 0 --batch-size 4 --data data/custom.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --weights '' --name yolov7 --hyp data/hyp.scratch.p5.yaml
```
## Testing model
After 300 epoch training we got some best checkpoint which we will test on some video
```
cd yolov7
python detect.py --weights runs/train/yolov74/weights/best.pt --conf 0.25 --img-size 640 --source ../sample_720p.mp4
```

## Result of model testing
![avatar](detect_test.gif)

## Performance:
Model's precesion is fluctuating in range of  70-75, not able to converge after 75%.
Find the precesion and recall graph wrt to epoch below:

```
Class      Images      Labels         P           R      mAP@.5       mAP@.5:.95
all         448        3232       0.761       0.613       0.672       0.359
person      448        2060        0.71       0.568        0.62       0.277
car         448        1172       0.812       0.658       0.723        0.44
```

![alt text](https://raw.githubusercontent.com/Nitin286roxs/Person-Car-Detector/main/precision_recall_vs_epochs.png)
