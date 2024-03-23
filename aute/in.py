import csv

def read_csv_to_list(filename):
  """Reads a CSV file and returns the data as a list of lists.

  Args:
    filename: The name of the CSV file to read.

  Returns:
    A list of lists, where each inner list represents a row in the CSV file.
  """

  with open(filename, "r") as f:
    reader = csv.reader(f)
    data = list(reader)
  return data
