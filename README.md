# Lectaroom

<h2><b>Submission for Microsoft Engage 2021</b></h2>
Functional prototype of a platform that gives students an array of digital academic and social tools<br>
<br>
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
<b>C:\Users\{System_Name}\AppData\Local\Programs\Python\Python39</b>
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
<br><br>
<h2><b>Features and Interfaces</b></h2>
<h3>Commmon Features and Interfaces</h3>
1. Landing Page<br>
<img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Landing%20Page.JPG"></img>
<img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Login.JPG"></img>
<img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Sign%20Up.JPG"></img>
2. Dashboard<br>
<img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/1_dashboard.JPG"></img>
<h3>Teacher Specific Features and Interfaces</h3>
1. Create Classroom<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/1_create_class_1.JPG"></img><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/create_class_1.JPG"></img><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/created_class.JPG"></img>
2. Add Stream<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/add_stream_1.JPG"></img><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/add_stream_2.JPG"></img>
3. View people<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/People.JPG"></img>
4. Create Assignment<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Assignment_creation.JPG"></img><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/2_assignmentcreate.JPG"></img>
5. Create Exam<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/1_create_exam.JPG"></img><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/1_create_exam_1.JPG"></img>
6. View created Assignments<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Assignment_teacher.JPG"></img>
7. View created Exams<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/1_exam_teacher.JPG"></img>
8. View Submitted Assignments<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Submitted%20Assignments.JPG"></img><br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Submitted%20Assignments_1.JPG"></img>
9. View Submitted Exams<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/1_exam_submissions.JPG"></img><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/1_exam_submissions1.JPG"></img>
<h3>Student Specific Features and Interfaces</h3>
1. Join Classroom<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Join%20class.JPG"></img><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Join%20class_1.JPG"></img>
2. Add Stream<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/add_stream_1.JPG"></img><br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/add_stream_2.JPG"></img>
3. Leave Classroom<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Leave_class_1.JPG"></img>
4. View people<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/People.JPG"></img>
5. View Assignment<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/Assignment_student.JPG"></img>
6. Submit Assignment<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/submit_answer.JPG"></img><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/submit_answer_1.JPG"></img>
7. View Exam<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/1_exam_teacher.JPG"></img>
8. Submit Exam<br><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/1_submitexam.JPG"></img><img src="https://github.com/gowri-gs/Lectaroom/blob/master/media/others/1_submitexam1.JPG"></img>


