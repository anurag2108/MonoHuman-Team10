# MonoHuman: Animatable Human Neural Field from Monocular Video (CVPR 2023)
Group 10 - Anurag Naren Kallakunta, Srinivas padigay, Nitin Talluri, Shravan chidrawar

# README for MonoHuman Project in Google Colab

## Introduction
This README provides step-by-step instructions for setting up and running the MonoHuman project in Google Colab. MonoHuman is a project focused on 3D human pose and shape estimation.

## Prerequisites
Before you begin, ensure you have a Google account and access to Google Colab.

## Installation Steps

### Step 1: Install Required Libraries
Run the following command in a Google Colab cell to install the necessary library:
```python
!pip install trimesh
```

### Step 2: Clone the MonoHuman Repository
Clone the MonoHuman repository from GitHub:
```python
!git clone https://github.com/Yzmblog/MonoHuman
```

### Step 3: Add Zjumocap to Google Drive
1. Visit the Zjumocap Google Drive link: [Zjumocap Drive](https://drive.google.com/drive/u/2/folders/16GgIYBidWL5a9rjcA13oKbX22wTT5xMo)
2. Add `zjumocap-public` as a shortcut to your Drive account where the Colab notebook is running.

### Step 4: Mount Google Drive
Mount your Google Drive in the Colab environment:
```python
from google.colab import drive
drive.mount('/content/drive')
```

### Step 5: Download and Setup the SMPL Model
1. Download the SMPL model with removed Chumpy objects from [here](https://drive.google.com/file/d/1i_pY4L8LjT6wImakKisS347oJEo81Tvz/view?usp=sharing).
2. Upload the SMPL model to `MonoHuman/third_parties/smpl/models`.

### Step 6: Modify Data Path
In the file `MonoHuman/tools/prepare_zju_mocap/377`, change the data path:
- Find the line `"zju_mocap_path: ../../dataset/zju_mocap"`
- Change it to `"zju_mocap_path: ../"`

### Step 7: Extract Zjumocap Data
Run the following code to extract the Zjumocap data:
```python
import tarfile
import shutil

# Define the paths
source_tar_gz = '/content/drive/MyDrive/zjumocap-public/CoreView_377.tar.gz'
output_directory = '/content/MonoHuman/tools'

# Extract the .tar.gz file
with tarfile.open(source_tar_gz, 'r:gz') as tar_ref:
    tar_ref.extractall(output_directory)
```

### Step 8: Prepare the Dataset
Navigate to the dataset preparation directory and run the preparation script:
```python
%cd /content/MonoHuman/tools/prepare_zju_mocap/
!python prepare_dataset.py --cfg 377.yaml
```

### Step 9: Navigate Back to Project Root
Return to the project root directory:
```python
%cd ../..
```

### Step 10: Organize Dataset Files
In `MonoHuman-main/dataset/zju_mocap/377`, move the files out of the folder "0" so that the data structure looks like this:
- `MonoHuman-main/dataset/zju_mocap/377/images`
- `MonoHuman-main/dataset/zju_mocap/377/masks`
- `MonoHuman-main/dataset/zju_mocap/377/cameras.pkl`

### Step 11: Modify Network.py File
In `MonoHuman/core/nets/monohuman/network.py`, change the following lines:
- Line 60: from `p_index = parent[min_index]` to `p_index = parent[min_index.to('cpu')]`
- Line 81: from `p_index = parent[min_index]` to `p_index = parent[min_index.to('cpu')]`

### Step 12: Training
Run training using the following command:
```python
!python train.py --cfg configs/monohuman/zju_mocap/377/377.yaml resume False
```

### Step 13: Rendering
Finally, run the rendering process:
```python
!python run.py --type movement --cfg configs/monohuman/zju_mocap/377/377.yaml
```

## Conclusion
Follow these steps to set up and run the MonoHuman project in Google Colab. For any issues or further information, refer to the official MonoHuman GitHub repository.
