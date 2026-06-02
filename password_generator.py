import random
import string
def generate_password(length):
    all_characters=string.ascii_letters+string.digits+string.punctuation
    password="".join(random.choice(all_characters) for i in range(length))
    return password
if __name__=="__main__":
    print("Secure password generator")
    user_length=int(input("Enter desired password length"))
    new_password=generate_password(user_length)
    print(f"Generated Password: {new_password}")