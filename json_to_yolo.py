import json
import cv2
import os

json_file = open("trainval//annotations/bbox-annotations.json", "r")
json_data = json.load(json_file)
images = json_data['images']
annotation = json_data['annotations']
prev_image_id = None
cv_img = None
file_object = None
for ith_annotation in annotation:
    current_category = ith_annotation['category_id'] - 1
    bbox=ith_annotation['bbox']
    cls = ith_annotation['category_id']
    image_id = ith_annotation['image_id']
    image_name = images[image_id]['file_name']
    image_width=images[image_id]['width']
    image_height=images[image_id]['height']
    print(image_name, bbox)
    if not prev_image_id:
        prev_image_id = image_id
        cv_img = cv2.imread(f"trainval/images/{image_name}")
        file_object = open(f"trainval/labels/{os.path.splitext(image_name)[0]}.txt", "a")
    if prev_image_id != image_id:
        file_object.close()
        #file_to_saved = images[prev_image_id]['file_name']
        #print(f"file_to_saved: {file_to_saved}")
        #cv2.imwrite(f"plot_test/{file_to_saved}", cv_img)
        cv_img = cv2.imread(f"images/{image_name}")
        file_object = open(f"trainval/labels/{os.path.splitext(image_name)[0]}.txt", "a")

        prev_image_id = image_id
    print(cv_img.shape)

    start_point = bbox[0], bbox[1]
    end_point = bbox[0]+bbox[2], bbox[1]+bbox[3]
    
    # Finding midpoints
    x_centre = (start_point[0] + end_point[0])/2
    y_centre = (start_point[1] + end_point[1])/2

    # Normalization
    x_centre = x_centre / image_width 
    y_centre = y_centre / image_height 
    w = bbox[2] / image_width
    h = bbox[3] / image_height

    # Limiting upto fix number of decimal places
    x_centre = format(x_centre, '.6f')
    y_centre = format(y_centre, '.6f')
    w = format(w, '.6f')
    h = format(h, '.6f')

    # Writing current object
    file_object.write(f"{current_category} {x_centre} {y_centre} {w} {h}\n") 
