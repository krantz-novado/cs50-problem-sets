

def convert(emoji):
    emoji = emoji.replace(":)", "🙂")

    emoji = emoji.replace(":(", "🙁")

    return(emoji)



def main():
    faces = input("How are you feeling today? ")

    print(convert(faces))

main()