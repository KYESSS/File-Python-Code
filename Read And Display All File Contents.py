try:
  
  # open the file in 'read mode' so we can read the file contents, the open 
  # function will return a file object
  file = open("Test File.txt", "r")

  # the file object has a read() method that will return all the file contents
  # as a string when we call it like we do below 
  contents = file.read()

  # print out the contents of the string
  print(contents)

  # close the file
  file.close()

# if an exception is raised in the try block we can handle the exception 
# with this except block
except:

  # output an error message for the user
  print("Error reading file.")