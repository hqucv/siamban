# -*- coding:utf-8 -*-
# ! ./usr/bin/env python
# __author__ = 'zzp'

import cv2
import json
import glob
import numpy as np
from os.path import join
from os import listdir

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir',type=str, default='./LaSOT', help='your lasot data dir')
args = parser.parse_args()

lasot_base_path = args.dir

lasot = []
for video_set in sorted(listdir(lasot_base_path)):
    if 'txt' not in video_set:
        videos = sorted(listdir(join(lasot_base_path, video_set)))
        s = []
        for vi, video in enumerate(videos):
            print('video_set: {}, video id: {:04d} / {:04d}'.format(video_set, vi, len(videos)))
            v = dict()
            v['base_path'] = join(video_set, video)
            v['frame'] = []
            video_base_path = join(lasot_base_path, video_set, video)
            gts_path = join(video_base_path, 'groundtruth.txt')
            # gts_file = open(gts_path, 'r')
            # gts = gts_file.readlines()
            gts = np.loadtxt(open(gts_path, "rb"), delimiter=',')

            # get image size
            im_path = join(video_base_path, 'img', '00000001.jpg')
            im = cv2.imread(im_path)
            size = im.shape  # height, width
            frame_sz = [size[1], size[0]]  # width,height

            # get all im name
            jpgs = sorted(glob.glob(join(video_base_path, 'img', '*.jpg')))

            f = dict()
            for idx, img_path in enumerate(jpgs):
                f['frame_sz'] = frame_sz
                f['img_path'] = img_path.split('/')[-1]

                gt = gts[idx]
                bbox = [int(g) for g in gt]   # (x,y,w,h)
                f['bbox'] = bbox
                v['frame'].append(f.copy())
            s.append(v)
        lasot.append(s)
print('save json (raw lasot info), please wait 1 min~')
json.dump(lasot, open('lasot.json', 'w'), indent=4, sort_keys=True)
print('lasot.json has been saved in ./')
