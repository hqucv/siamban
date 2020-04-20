import cv2
import json
import glob
import numpy as np
from os.path import join
from os import listdir

visual = True

LaSOT_base_path = './LaSOT'

for video_set in sorted(listdir(LaSOT_base_path)):
    if 'txt' not in video_set:
        videos = sorted(listdir(join(LaSOT_base_path, video_set)))
        for vi, video in enumerate(videos):
            print('video_set: {}, video id: {:04d} / {:04d}'.format(video_set, vi, len(videos)))
            video_base_path = join(LaSOT_base_path, video_set, video)
            gts_path = join(video_base_path, 'groundtruth.txt')
            gts = np.loadtxt(open(gts_path, "rb"), delimiter=',')

            # get all im name
            jpgs = sorted(glob.glob(join(video_base_path, 'img', '*.jpg')))

            for idx, img_path in enumerate(jpgs):

                gt = gts[idx]
                bbox = [int(g) for g in gt]   # (x_min,y_min,w,h)

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
