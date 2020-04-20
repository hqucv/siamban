from os.path import join
from os import listdir
import json
import numpy as np

print('loading json (raw lasot info), please wait 20 seconds~')
lasot = json.load(open('lasot.json', 'r'))

def check_size(frame_sz, bbox):
    min_ratio = 0.1
    max_ratio = 0.75
    # only accept objects >10% and <75% of the total frame
    area_ratio = np.sqrt((bbox[2]-bbox[0])*(bbox[3]-bbox[1])/float(np.prod(frame_sz)))
    ok = (area_ratio > min_ratio) and (area_ratio < max_ratio)
    return ok


def check_borders(frame_sz, bbox):
    dist_from_border = 0.05 * (bbox[2] - bbox[0] + bbox[3] - bbox[1])/2
    ok = (bbox[0] > dist_from_border) and (bbox[1] > dist_from_border) and \
         ((frame_sz[0] - bbox[2]) > dist_from_border) and \
         ((frame_sz[1] - bbox[3]) > dist_from_border)
    return ok


with open(join('./LaSOT/testing_set.txt')) as f:
    test_set = f.read().splitlines()

train_snippets = dict()
val_snippets = dict()

n_videos = 0
count = 0
for subset in lasot:
    for video in subset:
        n_videos += 1
        frames = video['frame']
        snippet = dict()
        for f, frame in enumerate(frames):
            frame_sz = frame['frame_sz']
            bbox = frame['bbox']  # (x_minx, y_min, w, h)
            if bbox[2] <= 0 or bbox[3] <= 0 or bbox[0] < 0 or bbox[1] < 0 or (bbox[0] + bbox[2]) > frame_sz[0] or (bbox[1] + bbox[3]) > frame_sz[1]:
                count += 1
                print("count, [w, h], [x_min, y_min, x_max, y_max], frame_sz: ",
                 count, [bbox[2], bbox[3]], [bbox[0], bbox[1], bbox[0]+bbox[2], bbox[1]+bbox[3]], frame_sz)
                continue

            snippet['{:06d}'.format(f)] = [bbox[0], bbox[1], bbox[0]+bbox[2], bbox[1]+bbox[3]]  # (x_min, y_min, x_max, y_max)
        
        if video['base_path'].split("/")[-1] in test_set:
            val_snippets[video['base_path']] = dict()
            val_snippets[video['base_path']]['{:02d}'.format(0)] = snippet.copy()
        else:
            train_snippets[video['base_path']] = dict()
            train_snippets[video['base_path']]['{:02d}'.format(0)] = snippet.copy()

json.dump(train_snippets, open('train.json', 'w'), indent=4, sort_keys=True)
json.dump(val_snippets, open('val.json', 'w'), indent=4, sort_keys=True)
print('video: {:d}'.format(n_videos))
print('done!')
