# TASK 8.1
## Jenkins Simple Task 
I start an instance in AWS and install Jenkins
<img src="screenshots/1.png">

So, Jenkins has installed and it's ready to go
<img src="screenshots/2.png">
<img src="screenshots/3.png">

Created the first job - `simple_item` saved it, launched it. The first build will appear in Build History. The main thing is the status. Blue color means that the job was completed successfully. Inside the build there is very detailed information about what Jenkins does and the output of my script
<img src="screenshots/4.png">
<img src="screenshots/5.png">
<img src="screenshots/6.png">

Now, I will try to complete the job not successfully. But before that I will install two plugins: the first will replace the blue balls with green ones, the second one will give me Chuck Noris
<img src="screenshots/7.png">


Edited the job again. I make the job run every minute
<img src="screenshots/8.png">

## Jenkins. CI/CD

    
    The workflow is:
    I start an instance in AWS and install Jenkins. Then i create a git repository where I will store the code and tests. I upload my calculator and tests there. Jenkins' role here is that it will do git clone (download the entire repository) from the github and run tests. This is CI. After the tests, if they succeed, the jenskins will copy my calc.py application by ssh and run it there (there will be one more instance for this) - this is CD.


Create a git repository where I will store the code and tests and upload my calculator and tests
<img src="screenshots/9.png">

Jenkins do git clone (code and tests) from the github
<img src="screenshots/10.png">

Jenkins runs tests every minute, they succeed
<img src="screenshots/11.png">
<img src="screenshots/12.png">

 I create another instance so that Jenkins will copy my calculator to it by ssh and launch my application 
 <img src="screenshots/13.png">

 Made a pipeline (clone from GitHub to Jenkins, run tests and deploy to a web server) Jenkins successfully cloned the code from GitHub, ran the tests and copied it to the server by scp
<img src="screenshots/14.png">
<img src="screenshots/15.png">