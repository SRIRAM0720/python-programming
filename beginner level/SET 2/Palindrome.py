 num=input('Enter a number')
  try:
    val=int(num)
    if num == str(num)[::-1]:
      print('The given number is Palindrome')
    else:
      print('The given number is not a palindrome')
except ValueError:
  print("That's not a valid number")
