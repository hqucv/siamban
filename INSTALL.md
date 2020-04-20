# Installation

This document contains detailed instructions for installing dependencies for SiamBAN. We recommand using the [install.sh](install.sh). The code is tested on an Ubuntu 18.04 system with Nvidia GPU (We recommand 1080TI / TITAN V).

### Requirments
* Conda with Python 3.7
* Nvidia GPU
* PyTorch 1.3.1
* pyyaml
* yacs
* tqdm
* matplotlib
* OpenCV

## Step-by-step instructions

#### Create environment and activate
```bash
conda create --name siamban python=3.7
source activate siamban
```

#### Install numpy/pytorch/opencv
```bash
conda install numpy
conda install pytorch=1.3.1 torchvision cudatoolkit=10.1 -c pytorch
pip install opencv-python
```

#### Install other requirements
```bash
pip install pyyaml yacs tqdm colorama matplotlib cython tensorboard future mpi4py optuna
```

#### Build extensions
```bash
python setup.py build_ext --inplace
```


## Try with scripts
```bash
bash install.sh /path/to/your/conda siamban
```

