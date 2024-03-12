import json

with open('video.json', 'r') as f:
    raw_data = json.load(f)
    
dict = { 
        "1.mp4" : [],
        "2.mp4" : []
    }

for id in range(len(raw_data)):
    for i in range(len(raw_data[0]['annotations'][0]['result'])):
        ele = {
            "start_frame": str(raw_data[id]['annotations'][0]['result'][i]['value']['sequence'][0]['frame']),
            "end_frame": str(raw_data[id]['annotations'][0]['result'][i]['value']['sequence'][1]['frame']),
            "action_type": raw_data[id]['annotations'][0]['result'][i]['value']['labels'][0],
            "down_coordinate": None,
            "up_coordinate": None,
            "type_word": None
        }
        if ele['action_type'] == 'click':
            x = raw_data[id]['annotations'][0]['result'][i]['value']['sequence'][0]['x']
            y = raw_data[id]['annotations'][0]['result'][i]['value']['sequence'][0]['y']
            w = raw_data[id]['annotations'][0]['result'][i]['value']['sequence'][0]['width']
            h = raw_data[id]['annotations'][0]['result'][i]['value']['sequence'][0]['height']
            pair = [int(round(x + w/2, 1)), int(round(y + h/2, 1))]
            ele['down_coordinate'] = ele['up_coordinate'] = pair
        if ele['action_type'] == 'swipe':
            x = raw_data[id]['annotations'][0]['result'][i]['value']['sequence'][0]['x']
            y = raw_data[id]['annotations'][0]['result'][i]['value']['sequence'][0]['y']
            h = raw_data[id]['annotations'][0]['result'][i]['value']['sequence'][0]['height']
            ele['down_coordinate'] = [int(x), int(round(y-h,0))]
            ele['up_coordinate'] = [int(x), int(round(y,0))]
        if ele['action_type'] == 'type':
            if id == 0:
                ele['type_word'] = "fed"
            if id == 1:
                ele['type_word'] = 'bbc' 
        
        if id == 0:
            dict['1.mp4'].append(ele)
            
        if id == 1:
            dict['2.mp4'].append(ele)     
         
  


with open('annotate.json', 'w' ) as ann:
    json.dump(dict, ann, indent=4)