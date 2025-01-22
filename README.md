# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLOUTIONS

*NAME*: KEESARI SHYAMSUNDAR REDDY

*INTERN ID*: CT6WNYN

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

*PLATFORM USED*: VISUAL STUDIO CODE

*DESCRIPTION*:

The code begins with reading data from a CSV file. The read_data function is responsible for opening the CSV file, reading its contents line by line, and storing each row in a list. This data is then printed for debugging purposes. This function returns a list of lists, where each inner list represents a row of data from the CSV file.

Next, the code analyzes the data using the analyze_data function. The analysis is simple and illustrative. It calculates the number of students (excluding the header row) and the average age of students. The function first calculates the total number of students by subtracting one from the length of the data list (to exclude the header row). It then calculates the total age by summing the ages from each row, converting them to integers. The average age is obtained by dividing the total age by the number of students. Both the number of students and the average age are printed for debugging purposes and returned by the function.

PDF Report Generation
The core functionality of the code revolves around generating a PDF report, which is handled by the generate_pdf_report function. This function takes the data, the number of students, the average age, and a filename as input parameters. It uses the ReportLab library to create the PDF report.

First, a SimpleDocTemplate object is created with the specified filename and page size (letter size in this case). An empty list elements is initialized to store the elements that will be added to the PDF.

Adding Title and Analysis
A title ("Student Report") is added to the PDF using a Canvas object. The drawString method places the title at a specified position on the page. Similarly, the analysis text, which includes the number of students and the average age, is added to the PDF at a position slightly below the title.

Creating and Styling the Table
The data is then formatted into a table using the Table class from the ReportLab library. The Table object takes the data as input and arranges it in rows and columns.

Styling is applied to the table using the TableStyle class. Various styling options are specified, including background color, text color, alignment, font, padding, and grid lines. The header row is styled differently from the rest of the table, with a grey background and white text color. The setStyle method applies the styling to the table.

The styled table is then appended to the elements list, which contains all the elements to be added to the PDF.

Building and Saving the PDF
The build method of the SimpleDocTemplate object is called with the elements list as an argument. This method assembles the PDF by adding each element from the list to the document. Finally, the save method of the Canvas object is called to save the generated PDF file.

Main Execution
In the __main__ section, the code executes the functions in sequence. It starts by calling read_data to read data from the CSV file. The analyze_data function is then called to perform the analysis on the data, and the results are stored in num_students and average_age. Finally, the generate_pdf_report function is called with the data, analysis results, and output filename to create the PDF report. A print statement confirms the successful generation of the PDF report.

*Summary of the Process*:

Install the reportlab library using pip.

Create a CSV file with the required data.

Save and run the Python script to read the data, perform analysis, and generate the PDF report.

Verify the output by checking the terminal for debug prints and opening the generated PDF file.

*OUTPUT*:

![Image](https://github.com/user-attachments/assets/3440487b-118f-4946-8ec5-c006dba19caf)
