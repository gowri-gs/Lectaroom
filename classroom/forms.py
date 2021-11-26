from django import forms
from .models import Assignment, Exam, AssignmentSubmission, ExamSubmission


# ASSIGNMENT CREATE FORM
class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'content', 'marks', 'duration']

    def __init__(self, *args, **kwargs):
        super(AssignmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Assignment Name"
        self.fields['content'].label = "Content"
        self.fields['marks'].label = "Marks"
        self.fields['duration'].label = "Duration"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Enter A Name',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Content',
            }
        )

        self.fields['marks'].widget.attrs.update(
            {
                'placeholder': 'Enter Marks',
            }
        )

        self.fields['duration'].widget.attrs.update(
            {
                'placeholder': '3 hours, 2 hours etc ...',
            }
        )

    def is_valid(self):
        valid = super(AssignmentCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(AssignmentCreateForm, self).save(commit=False)
        if commit:
            course.save()
        return course


# EXAM CREATE FORM
class ExamCreateForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'content', 'marks', 'duration']

    def __init__(self, *args, **kwargs):
        super(ExamCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Assignment Name"
        self.fields['content'].label = "Content"
        self.fields['marks'].label = "Marks"
        self.fields['duration'].label = "Duration"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Enter A Name',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Content',
            }
        )

        self.fields['marks'].widget.attrs.update(
            {
                'placeholder': 'Enter Marks',
            }
        )

        self.fields['duration'].widget.attrs.update(
            {
                'placeholder': '3 hours, 2 hours etc ...',
            }
        )

    def is_valid(self):
        valid = super(ExamCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(ExamCreateForm, self).save(commit=False)
        if commit:
            course.save()
        return course


# ASSIGNMENT SUBMISSION FORM

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['name', 'university_id', 'content', 'file']

    def __init__(self, *args, **kwargs):
        super(AssignmentSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = " Name"
        self.fields['university_id'].label = "University Id"
        self.fields['content'].label = "Answer"
        self.fields['file'].label = "Or Upload File"

        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Write Your Name',
            }
        )

        self.fields['university_id'].widget.attrs.update(
            {
                'placeholder': 'Write Your Id',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Write Your Answer Here',
            }
        )

        self.fields['file'].widget.attrs.update(
            {
                'placeholder': 'Upload Your FILE Here',
            }
        )

    def is_valid(self):
        valid = super(AssignmentSubmissionForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(AssignmentSubmissionForm, self).save(commit=False)
        if commit:
            course.save()
        return course

# EXAM SUBMISSION FORM
class ExamSubmissionForm(forms.ModelForm):
    class Meta:
        model = ExamSubmission
        fields = ['name', 'university_id', 'content', 'file']

    def __init__(self, *args, **kwargs):
        super(ExamSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = " Name"
        self.fields['university_id'].label = "University Id"
        self.fields['content'].label = "Answer"
        self.fields['file'].label = "Or Upload File"

        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Write Your Name',
            }
        )

        self.fields['university_id'].widget.attrs.update(
            {
                'placeholder': 'Write Your Id',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Write Your Answer Here',
            }
        )

        self.fields['file'].widget.attrs.update(
            {
                'placeholder': 'Upload Your FILE Here',
            }
        )

    def is_valid(self):
        valid = super(ExamSubmissionForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(ExamSubmissionForm, self).save(commit=False)
        if commit:
            course.save()
        return course
