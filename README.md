# Lectaroom

<h2><b>Submission for Microsoft Engage 2021</b></h2>
Functional prototype of a platform that gives students an array of digital academic and social tools<br>
<br>
<img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Landing%20Page.JPG"></img><br>
<img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Assignment_creation.JPG"></img><br>
<img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Assignment_student.JPG"></img><br>
<img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Submitted%20Assignments.JPG"></img><br>

To run this application,<br>
Clone the repository using the following command<br>
<div class="highlight highlight-source-shell position-relative overflow-auto">
  <pre>
git clone https://github.com/gowri-gs/Lectaroom.git</pre>
</div>
<br>
Install python interpreter (if not installed in the system) <br>
<b>https://www.python.org/downloads/release/python-399/</b><br>
<br>
Add Python to the Windows Path Environment Variable (if not added)<br>
<b>C:\Users\<<System_Name>>\AppData\Local\Programs\Python\Python39<b>
<br>
<br>
Open Command Prompt and move into the directory having the project files using the change directory command
<div class="highlight highlight-source-shell position-relative overflow-auto">
  <pre>
  cd Lectaroom</pre>
</div><br>
Create a virtual environment where all the required python packages will be installed<br>
<div class="highlight highlight-source-shell position-relative overflow-auto">
  <pre>
  python -m venv venv</pre>
</div>
<br>
Activate the virtual environment
<div class="highlight highlight-source-shell position-relative overflow-auto">
  <pre>
  .\venv\Scripts\activate</pre>
</div>
<br>
Apply migrations
<div class="highlight highlight-source-shell position-relative overflow-auto">
  <pre>
  python manage.py migrate</pre>
</div>
<br>
Run the development server
<div class="highlight highlight-source-shell position-relative overflow-auto">
  <pre>
  python manage.py runserver</pre>
</div>
