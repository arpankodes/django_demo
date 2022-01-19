from django.db import models

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class emp_info(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    joining_year = models.IntegerField()
    ctc = models.FloatField(max_length=4)
    rating = models.FloatField(max_length=2)

class project(models.Model):
    emp_id = models.ForeignKey(emp_info, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)

