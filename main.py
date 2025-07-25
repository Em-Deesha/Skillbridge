from tabulate import tabulate

# Your introduction data
introduction = [
    ["Name", "Adeesha Waheed"],
    ["Degree", "BS Computer Science"],
    ["Institution", "Fazaia College Nur Khan Base"],
    ["Internships", "ML & Data Visualization, WordPress (current)"] ,
    ["Current Activity", "Agentic AI Bootcamp (Skillbridge)"]
]

# Print the introduction as a table
print(tabulate(introduction, headers=["Field", "Details"], tablefmt="grid"))

# If you don't have tabulate installed, run:
# pip install tabulate
