import json
path = "Ground_vehicles/_annotations.coco.json"

images_a     = []
categories_a = []
annotation_a = []
info         = []    
license      = []


with open(path) as file:
    tmp_j = json.load(file)
    images_a        = tmp_j['images']
    categories_a    = tmp_j['categories']
    annotation_a    = tmp_j["annotations"]
    info            = tmp_j["info"]
    license         = tmp_j["licenses"]

dic={'images': images_a, 'categories':categories_a, 'annotations':annotation_a}

with open('Ground_vehicles/settings.json', 'w') as outfile:
    json.dump(dic, outfile,  sort_keys=False, indent=4)