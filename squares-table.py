def main():
  # print the table headings
  print('Number\tSquare')
  print('--------------')

  # print the numbers 1 to 1 and squares

  for number in range(1,11):
    square = number ** 2
    print(number, '\t', square)

main()
