# What do a Tree and the Human Brain have in Common - A not so Serious Introduction to Digital Pathology
This repository contains the minimalistic example code and some further literature for above mentioned talk from PyCon DE & PyData 2025.


----
## Example Notebook
The notebook `conventional_cv.ipynb` shows the power of the most fundamental conventional CV method: basic thresholding.<br>
To run the notebook first install all requirements via `pip install -r requirements.txt`.<br>
Note: the requirements were generated with Python 3.13 other Python and package version may also work well.

---
## Tools, Frameworks, and Datasets
This section introduces some frameworks, tools and datasets which could be the beginning of your medical CV journey.

### Handling these large Images (correctly)
To handle the Whole-Slide Images correctly you can use [OpenSlide](https://openslide.org/api/python/).

### Machine Learning
For Machine Learning two frameworks are especially important:
- [MONAI](https://github.com/project-monai/monai) the defacto standard for medical image segmentation tasks (with it's own [tutorial repository](https://github.com/Project-MONAI/tutorials/tree/main))<br>
and
- [AUCMEDI](https://github.com/frankkramer-lab/aucmedi), the smaller spiritual sibling with a focus on classification.

### Evaluation
[Metrics Reloaded](https://metrics-reloaded.dkfz.de) from the German Cancer Research Center (DKFZ) provides a beautiful overview of machine learning metrics and when/how to use them. This could be your first address, if you are not sure on how to measure success.

### AutoML
For segmentation tasks in medical imaging always consider [deepfash2](https://github.com/matjesg/deepflash2) and [nnU-Net v2](https://github.com/MIC-DKFZ/nnUNet) your first options.<br>
While nnU-Net v2 is the more popular option with a better support, deepflash2 has proven itself superior on consumer hardware and less data in first tests. It was able to beat nnU-Net v2 and a manual implementation with MONAI on a tumor segmentation task in our internal testing (nnU-Net v2 vs deepflash2 [Paper](https://ebooks.iospress.nl/doi/10.3233/SHTI240487)).

For classification [AUCMEDI](https://github.com/frankkramer-lab/aucmedi) provides a simple AutoML option. 

## Datasets
You don't have to work at a hospital to have access to medical data. By now large (sometimes fully labeled) datasets are available publicly. If you don't want to focus your computer vision work to rare diseases the choices are large.<br>
In the pathological domain, the most popular datasets are most likely:
- the [PANDA challenge](https://www.kaggle.com/competitions/prostate-cancer-grade-assessment/data), allowing for both segmentation and classification,<br>
as well as
- the [CAMELYON challenge](https://www.kaggle.com/c/histopathologic-cancer-detection/data), focusing on classification.

A new challenging classification dataset was recently released, focusing on the detection of atypical cell constructs: [AMi-Br](https://github.com/DeepMicroscopy/AMI-Br).

Besides those large amounts of data are available both on [zenodo](https://zenodo.org) as well as [kaggle](https://www.kaggle.com).

---
## Images
The images in the `ìmages` dir are licensed for educational purposes. Please do not reuse them outside of this context.

If you want to try the thresholding on the same pathology image as shown in the notebook and during PyCon De you can download it here: https://glioblastoma.alleninstitute.org/ish/specimen/show/308886351.