import matplotlib.pyplot as plt
import numpy as np

student_name = "Aritra"
subjects = ["English", "Math", "Physics", "Life-Sc", "Sports"]
marks = [50, 80, 78, 39, 45]

avg = np.average(marks)

x = np.arange(len(subjects))  # the label locations
width = 0.5  # the width of the bars

fig, ax = plt.subplots()


rects = ax.bar(x-width/10, marks, width, label='Marks')

ax.set_title('-------- Marks Analysis --------\nStudent: '+student_name+"\nAverage Marks: "+str(avg))

ax.set_ylabel('Marks')
ax.set_xlabel('<--------------Subjects------------>')

ax.set_xticks(x)
ax.set_xticklabels(subjects)
# ax.legend()

ax.bar_label(rects, padding=3)

fig.tight_layout()

plt.show()