while True:
    text = input("Enter a text: ")

    if text.isalpha():
        reversed_text = text[::-1]
        print("The reversed text is: ", reversed_text)
        break
    else:
        print("Error Reported! Enter text only.")
