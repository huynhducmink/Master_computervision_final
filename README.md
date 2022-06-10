# Mask R-CNN for Object Detection and Segmentation
## Huynh Duc Minh - 20212456M


This is a custom repository modified from the implementation of Mask R-CNN of matterport (https://github.com/matterport/Mask_RCNN) to be the final project of the computer vision class.

Environment:
```
python 3.6
numpy 1.17.0
scipy 1.5.2
Pillow
cython 0.29.24
matplotlib 3.3.4
scikit-image 0.16.2
tensorflow-gpu 1.13.1
keras 2.0.8
opencv 4.5.5
h5py 2.10.0
imgaug 0.4.0
IPython[all]
```

Running on GL752VW laptop with a GTX-960M GPU with conda environment

```
cudatoolkit 10.0.130
```

Dataset:

[Dataset link](https://drive.google.com/drive/folders/1_g5FIpFXYjfRnY1Hep6owKcFfcMy6N4x?classId=fd7662fb-3dda-418f-b24c-8099ad9601c2&assignmentId=6123f0e6-6f88-4753-8206-641861e96fa7&submissionId=097ea163-0959-f7e2-dfea-95ed76b8db74)

(put the dataset folder under the project root folder)

Pretrained weight:

[Pretrained weight link](https://drive.google.com/drive/folders/1yGumncJJD2oVI13_bMUZgYhExxGc0a7y?classId=fd7662fb-3dda-418f-b24c-8099ad9601c2&assignmentId=6123f0e6-6f88-4753-8206-641861e96fa7&submissionId=097ea163-0959-f7e2-dfea-95ed76b8db74)

(put the logs folder under the project root folder)

2 file with the custom implementation are:
```
project_root/samples/Compvision_final_resnet50.ipynb
project_root/samples/Compvision_final_resnet101.ipynb
```

Because of the limitation of hardware, this implementation only use a very small batch size and image dimension.