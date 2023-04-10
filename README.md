# Duplicate Image Detectio using Multiprocessing

## Instructions to run

- Directions to install

```bash
git clone https://github.com/MaheshReddy-05/Duplicate-Image-Detection-using-Multiprocessing.git 
cd Duplicate-Images-Detection-using-Parallel-Processing
#create Virtural Environment
pip install virtualenv
#Name it 
virtualenv env
#redirect to that vm
env\scripts\activate
#If get error then you need to open powershell and run as admin and run: set-executionpolicy remotesigned and choose as Y )
Now again run: env\scripts\activate
#boom now u can install in VM what ever you want
#to exit run:'deactivate'

pip install -r requirements.txt
python '.\Duplication Detecting Scripts\detect_duplicate_single_core.py' 
python '.\Duplication Detecting Scripts\detect_duplicate_multiple_core.py' 
python '.\Duplication Detecting Scripts\detect_duplicate_multiple_thread.py'
```
