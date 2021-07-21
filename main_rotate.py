# The bare-bones example from the README.
# Run coco_example.py first to get mask_rcnn_bbox.json
from tidecv_rotate import TIDE, datasets
import pickle
import time
import json

if __name__ == "__main__":


    tide = TIDE()
    tide.evaluate(datasets.COCO(path='/data1/czy/2D/tide/Aerial/new_val.json'),
                  datasets.COCOResult('/data1/czy/2D/tide/Aerial/course4-filterscore.box.json'), mode=TIDE.BOX)
    tide.summarize()
    tide.plot()
