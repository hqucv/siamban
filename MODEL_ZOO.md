# SiamBAN Model Zoo

## Introduction

All configurations for these baselines are located in the [`experiments`](experiments) directory. The tables below provide results about inference. Links to the trained models as well as their output are provided. 

## Visual Tracking Baselines

### Short-term Tracking

| Model(arch+backbone) | VOT2018(EAO/A./R.) | OTB100(AUC/Prec.) | URL                                                          |
| -------------------- | :----------------: | :---------------: | ------------------------------------------------------------ |
| siamban_r50_l234     | 0.452/0.597/0.178  |         -         | [model](https://drive.google.com/file/d/1SJwPUpTQm6xL44-8jLvDrSMhOzVsbLAZ/view?usp=sharing) |
| siamban_r50_l234_otb |         -          |    0.696/0.910    | [model](https://drive.google.com/file/d/1d_z_7azA56PrnyQWkRFnZmxb1IGU-72E/view?usp=sharing) |

Note:

-  `r50_lxyz` denotes the outputs of stage x, y, and z in [ResNet-50](https://arxiv.org/abs/1512.03385).
- The suffixes `otb` is designed for the [OTB](http://cvlab.hanyang.ac.kr/tracker_benchmark/benchmark.html), the default (without suffix) is designed for [VOT short-term tracking challenge](http://www.votchallenge.net/index.html).
- All the above models are trained on [VID](http://image-net.org/challenges/LSVRC/2017/), [YOUTUBEBB](https://research.google.com/youtube-bb/), [DET](http://image-net.org/challenges/LSVRC/2017/), [COCO](http://cocodataset.org), [GOT10K](http://got-10k.aitestunion.com/), [LASOT](https://cis.temple.edu/lasot/). 




## License

All models available for download through this document are licensed under the [Creative Commons Attribution-ShareAlike 3.0 license](https://creativecommons.org/licenses/by-sa/3.0/).
