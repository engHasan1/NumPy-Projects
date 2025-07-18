import numpy as  np
print("welcome to the Student Grade Analysis Program")

print("plase enter how many students you want to enter grades for")
numStudent=int(input("Enter number of students: "))
print("please enter how many classes you want to enter grades for")
numClass=int(input("Enter number of classes: "))


class_Name = []
for i in range(numClass):
    print("please enter the name of class", i+1)
    className = input("Enter class name: ")
    class_Name.append(className)

StudentName=[]
student_Grades = {}   
for i in range(numStudent):
    print("please enter the name of student", i+1)
    studentName = input("Enter student name: ")
    StudentName.append(studentName)
    grades={}
    for classname in class_Name:
        print("please enter the grade for", studentName, "in", classname)
        grade = float(input("Enter grade: "))
        grades[classname] = grade
    student_Grades[studentName] = grades    
avglist = []
for name in StudentName:
    avg = np.mean(list(student_Grades[name].values()))
    print("the average grade for", name, "is", avg)
    avglist.append(avg)
bestStudent= np.argmax(avglist)

print("the best student is: ",StudentName[bestStudent], ".with an average grade of ", avglist[bestStudent])

subject_totals = {subject: [] for subject in class_Name}
for student in StudentName:
    for subject in class_Name:
        subject_totals[subject].append(student_Grades[student][subject])

subject_avgs = {subject: np.mean(scores) for subject, scores in subject_totals.items()}
hardest_subject = min(subject_avgs, key=subject_avgs.get)
best_subject = max(subject_avgs, key=subject_avgs.get)

print(f"\n📉 Hardest subject: {hardest_subject} (Average: {subject_avgs[hardest_subject]:.2f})")
print(f"🏅 Easiest subject: {best_subject} (Average: {subject_avgs[best_subject]:.2f})")
