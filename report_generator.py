import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Function to read data from a CSV file
def read_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    print("Data read from CSV:", data)  # Debug print
    return data

# Function to analyze the data
def analyze_data(data):
    # Example analysis: count the number of students and calculate the average age
    num_students = len(data) - 1  # excluding header
    total_age = sum(int(row[1]) for row in data[1:])
    average_age = total_age / num_students
    print("Number of students:", num_students)  # Debug print
    print("Average age:", average_age)  # Debug print
    return num_students, average_age

# Function to generate a PDF report
def generate_pdf_report(data, num_students, average_age, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Add Title
    title = "Student Report"
    c = canvas.Canvas(filename)
    c.drawString(100, 750, title)

    # Add Analysis
    analysis = f"Number of Students: {num_students}\nAverage Age: {average_age:.2f}"
    c.drawString(100, 730, analysis)

    # Create Table
    table_data = data
    table = Table(table_data)

    # Add Table Style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)
    elements.append(table)

    doc.build(elements)
    c.save()

# Main execution
if __name__ == "__main__":
    data = read_data('data.csv')
    num_students, average_age = analyze_data(data)
    generate_pdf_report(data, num_students, average_age, 'report.pdf')
    print("PDF report generated successfully!")  # Debug print
