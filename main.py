from pyscript import document
import matplotlib.pyplot as mp
import numpy as np

months = np.array([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

absences = np.zeros(12, dtype=int)


def add_absence(e):
    index = int(document.getElementById("month").value)
    value = int(document.getElementById("absence_num").value)

    absences[index] += value

    
    mp.bar(months, absences)
    mp.title("Absences Plot")
    mp.xlabel("Months")
    mp.ylabel("Absences")
    mp.show()

    document.getElementById("error").innerHTML = ""