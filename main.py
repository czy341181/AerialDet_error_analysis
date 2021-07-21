# The bare-bones example from the README.
# Run coco_example.py first to get mask_rcnn_bbox.json
from tidecv import TIDE, datasets
import pickle
import time
import json

if __name__ =="__main__":
    '''
    gt json  
    dict{
        info
        licenses
        images: list len(5000)   每一个元素是 dict,存储的图片信息 
        annotations： list len(36781)  每一个元素是一个dict，存储的该标注的信息  'area' 'iscrowd' 'image_id' 'bbox' 'category_id' 'id'
        categories: list len(80)    每一个元素是一个dict，存储的该类的标注信息  {'supercategory': 'animal', 'id': 23, 'name': 'bear'}
    }
    
    pred json
    list: 每一个元素
    {'image_id': 15335, 'bbox': [297.3739318847656, 253.46319580078125, 35.197113037109375, 15.361846923828125], 'score': 0.06487670540809631, 'category_id': 90}
    
    '''
    # with open("/data1/czy/2D/tide/mask_rcnn_coco/results.bbox.json", 'r') as json_file:
    #     cocojson = json.load(json_file)


    tide = TIDE()
    tide.evaluate(datasets.COCO(path='/data1/czy/2D/tide/mask_rcnn_coco/instances_val2017.json'), datasets.COCOResult('/data1/czy/2D/tide/mask_rcnn_coco/results.bbox.json'), mode=TIDE.BOX)
    tide.summarize()
    tide.plot()
