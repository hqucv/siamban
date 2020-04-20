# SiamBAN

This project hosts the code for implementing the SiamBAN algorithm for visual tracking, as presented in our paper: 

```
@inproceedings{siamban,
  title={Siamese Box Adaptive Network for Visual Tracking},
  author={Chen, Zedu and Zhong, Bineng and Li, Guorong and Zhang, Shengping and Ji, Rongrong},
  booktitle={Proceedings of the IEEE International Conference on Computer Vision},
  year={2020}
}
```

The full paper is available [here](https://arxiv.org/abs/2003.06761). The raw results are [here](https://drive.google.com/file/d/1-RaD5deAqXdISCBSFG5q62ialrxegsCa/view?usp=sharing). The code based on the [PySOT](https://github.com/STVIR/pysot).



<div align="center">
  <img src="demo/output/bag_tracking.gif" width="480px" />
  <p>Example SiamBAN outputs.</p>
</div>



## Installation

Please find installation instructions in [`INSTALL.md`](INSTALL.md).

## Quick Start: Using SiamBAN

### Add SiamBAN to your PYTHONPATH

```bash
export PYTHONPATH=/path/to/siamban:$PYTHONPATH
```

### Download models

Download models in [Model Zoo](MODEL_ZOO.md) and put the `model.pth` in the correct directory in experiments

### Webcam demo

```bash
python tools/demo.py \
    --config experiments/siamban_r50_l234/config.yaml \
    --snapshot experiments/siamban_r50_l234/model.pth
    # --video demo/bag.avi # (in case you don't have webcam)
```

### Download testing datasets

Download datasets and put them into `testing_dataset` directory. Jsons of commonly used datasets can be downloaded from [here](https://drive.google.com/drive/folders/10cfXjwQQBQeu48XMf2xc_W1LucpistPI). If you want to test tracker on new dataset, please refer to [pysot-toolkit](https://github.com/StrangerZhang/pysot-toolkit) to setting `testing_dataset`. 

### Test tracker

```bash
cd experiments/siamban_r50_l234
python -u ../../tools/test.py 	\
	--snapshot model.pth 	\ # model path
	--dataset VOT2018 	\ # dataset name
	--config config.yaml	  # config file
```

The testing results will in the current directory(results/dataset/model_name/)

### Eval tracker

assume still in experiments/siamban_r50_l234

``` bash
python ../../tools/eval.py 	 \
	--tracker_path ./results \ # result path
	--dataset VOT2018        \ # dataset name
	--num 1 		 \ # number thread to eval
	--tracker_prefix 'model'   # tracker_name
```

###  Training :wrench:

See [TRAIN.md](TRAIN.md) for detailed instruction.

## License

This project is released under the Apache 2.0 license. 