#!/bin/bash

if [ $# -lt 2 ]; then
    echo "ARGS ERROR!"
    echo "  bash install.sh /path/to/your/conda env_name"
    exit 1
fi

set -e

conda_path=$1
env_name=$2

source $conda_path/etc/profile.d/conda.sh

echo "****** create environment " $env_name "*****"
# create environment
conda create -y --name $env_name python=3.7
conda activate $env_name

echo "***** install numpy pytorch opencv *****"
# numpy
conda install -y numpy
# pytorch
conda install pytorch=1.3.1 torchvision cudatoolkit=10.1 -c pytorch
# opencv
pip install opencv-python

echo "***** install other libs *****"
# libs
pip install pyyaml yacs tqdm colorama matplotlib cython tensorboard future mpi4py optuna


echo "***** build extensions *****"
python setup.py build_ext --inplace
