# TASK 11.1 
Create a Python Flask `cat.py` that displays random cat pix. For this i create a directory called flask-learn where i'll create the following files:
```
cat.py
requirements.txt
templates/index.html
```
<img src="screenshots/1.png">

I check the application is working. Works!
<img src="screenshots/2.png">

I am building a Docker image with my `cat.py` application. Since my application is written in Python, I am building my own Alpine-based Python image using the Dockerfile.
Create Dockerfile
<img src="screenshots/3.png">

I Build the image `docker build -f Dockerfile -t random_cat:v0.1.0 .`
<img src="screenshots/4.png">
<img src="screenshots/5.png">

I Run my image and see if it actually works.
<img src="screenshots/6.png">
<img src="screenshots/7.png">
<img src="screenshots/8.png">
<img src="screenshots/9.png">

