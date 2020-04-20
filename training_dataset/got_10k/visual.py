import cv2
import json
import glob
import numpy as np
from os.path import join
from os import listdir


visual = True

GOT_10k_base_path = './GOT_10k'

sub_sets = sorted({'train_data', 'val_data'})

for sub_set in sub_sets:
    sub_set_base_path = join(GOT_10k_base_path, sub_set)
    for video_set in sorted(listdir(sub_set_base_path)):
        videos = sorted(listdir(join(sub_set_base_path, video_set)))
        for vi, video in enumerate(videos):
            print('subset: {}, video_set: {}, video id: {:04d} / {:04d}'.format(sub_set, video_set, vi, len(videos)))
            video_base_path = join(sub_set_base_path, video_set, video)
            gts_path = join(video_base_path, 'groundtruth.txt')
            gts = np.loadtxt(open(gts_path, "rb"), delimiter=',')

            # get all im name
            jpgs = sorted(glob.glob(join(video_base_path, '*.jpg')))

            for idx, img_path in enumerate(jpgs):
                gt = gts[idx]
                bbox = [int(g) for g in gt]   # (x,y,w,h)

                bbox = [bbox[0], bbox[1], bbox[0] + bbox[2], bbox[1] + bbox[3]] # (x_min, y_min, x_max, y_max)

                if visual:
                    im = cv2.imread(img_path)
                if visual:
                    pt1 = (int(bbox[0]), int(bbox[1]))
                    pt2 = (int(bbox[2]), int(bbox[3]))
                    cv2.rectangle(im, pt1, pt2, (0, 0 ,255), 3)
                if visual:
                    cv2.imshow('img', im)
                    cv2.waitKey(1)
