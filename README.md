# Heatmap Photo

Python program to overlay a heatmap on a photo from Unity outputted coordinates.

Dependencies:
- numpy
  $ pip install numpy
- matplotlib
  $ pip install matplotlib
- tkinter
  $ pip install tk

To run: 
1. From project directory, run main.py $ python main.py
2. Use the tkinter GUI to import one csv data file and one png image file. The input data must be of the format:
 ![Example CSV Image](exampleCSV.png "Example CSV")
** Note that the headings do not matter **
4. Click 'Run'
5. The resulting image will be located in the project directory, named "input_csv_name"_heatmap.png

