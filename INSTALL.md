## Installation Instructions

<!--
```bash
git clone https://github.com/TalalWasim/Video-FocalNets
cd Video-FocalNets
``` -->

- Create a conda virtual environment and activate it:

```bash
conda create -n [env_name] python=3.10 -y
conda activate [env_name]
```

- Install `PyTorch==2.3.0` and `torchvision==0.18.0` with `CUDA==12.1`:

```bash
conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 cudatoolkit=12.1 -c pytorch
```

- Clone our `OD-VIRAT` repository:
```bash
git clone https://github.com/hayatkhan8660-maker/OD-VIRAT.git
cd OD-VIRAT
```

- Install the following prerequisite libraries:
```bash
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.0"
```

- Now install  `mmdetection`:
```bash
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -v -e .
```   

- Verify the `mmdetection` installation using the following command:
  
**Step1:** Download the config and checkpoint files:
```bash
mim download mmdet --config rtmdet_tiny_8xb32-300e_coco --dest .
```
**Step2:** Run the following command to check the successful installation of `mmdetection`:
```bash
python demo/image_demo.py demo/demo.jpg rtmdet_tiny_8xb32-300e_coco.py --weights rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth --device cpu
```
  
- Install other requirements:
```bash
pip install numpy==1.24.3 pandas==2.0.3 opencv-python==4.7.0.72 yacs==0.1.8 PyYAML==6.0 natsort==8.4.0 pycocotools==2.0.7
```
