from django.db import models

# Create your models here.
class Institute(models.Model):
    inst_name=models.CharField(max_length=20,primary_key=True)
    branch=models.CharField(max_length=20)

    def __str__(self):
        return self.inst_name

class Trainer(models.Model):
    tname=models.CharField(max_length=20)
    tid=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.tname

class Student(models.Model):
    sname=models.CharField(max_length=20)
    sid=models.IntegerField(primary_key=True)
    smob=models.IntegerField()
    sfee=models.IntegerField()

    def __str__(self):
        return self.sname

class Course(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)
    inst_name=models.ForeignKey(Institute,on_delete=models.CASCADE)
    tid=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.cname