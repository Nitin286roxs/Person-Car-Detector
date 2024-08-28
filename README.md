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
