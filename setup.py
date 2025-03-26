from setuptools import setup
import os


# Function to automatically find all files in a specific directory
def find_files(directory):
    for path, directories, files in os.walk(directory):
        for file in files:
            print(file)
            yield os.path.join(path, file)

requires = [
"numpy==1.24",
"cellpose==2.1.0",
"charset-normalizer==3.3.2",
"matplotlib",
"munkres",
"opencv_python_headless",
"pandas==1.5.0",
"patchify==0.2.3",
"PyQt5==5.15.10",
"pyqtgraph==0.13.0",
"scikit_image",
"scikit_learn",
"scipy",
"torch==1.12.0",
"tqdm",
"trackpy",
"torchvision==0.13.1",
"chardet==5.2.0",
"memory-profiler",
"QSwitchControl"]

try:
    import torch
    a = torch.ones(2, 3)
    major_version, minor_version, _ = torch.__version__.split(".")
    if major_version == "2" or int(minor_version) >= 12:
        requires.remove("torch==1.12.0")
        requires.remove("torchvision==0.13.1")
except:
    pass


github_only_text  = '''
## Enhance time-series resolution with generative AI
<img src="https://raw.githubusercontent.com/berkyalcinkaya/yeastvision/main/yeastvision/docs/figs/interp.gif?raw=True" width="2000" height="600" />
'''

with open("README.md", "r") as fh:
    long_description = fh.read()
    # remove github only text from long description
    long_description = long_description.replace(github_only_text, "")

packages = [
            "fungalvision","fungalvision.data",  "fungalvision.plot", 
            "fungalvision.track", "fungalvision.track.fiest", "fungalvision.models", 
            "fungalvision.ims", "fungalvision.ims.rife_model", 
            "fungalvision.docs", "fungalvision.docs.figs",
            "fungalvision.ims.rife_model.pytorch_msssim", "fungalvision.parts", 
            "fungalvision.flou", "fungalvision.disk", "fungalvision.models.proSeg", 
            "fungalvision.models.budSeg", "fungalvision.models.budSeg",
            "fungalvision.models.matSeg", "fungalvision.models.spoSeg", 
            "fungalvision.models.flouSeg"
        ]

setup(
    name="fungalvision",
    version="0.0.1",  # first PyPI release
    description="Deep learning-enabled image analysis of the full yeast life cycle",
    author="Berk Yalcinkaya",
    url="https://github.com/berkyalcinkaya/fungalvision",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email="berkyalcinkaya55@gmail.com",
    license="BSD",
    packages=packages,
    install_requires=requires,
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'fungalvision = fungalvision.__main__:main'
        ]
    }
)
