PERMITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
PermitsForDomian = "-"
NotPermits = "._"
validTLD = ["com" , "net" , "org" ,"tech"]
NotPermitForDomian ="_"
def validate(email):
    # split @ and .
    if "@" in email and "." in email:
        parts = email.split("@")
        username = parts[0]
        domain = parts[1]
        DomainPart = email.split(".")
        afterdot = DomainPart[-1]
        if len(username) < 3:
            return "Email is invalid"
        if len(username) > 24:
            return "Email is invalid"
        if len(domain) - len(afterdot) < 3:
            return "Email is invalid"
        if len(domain) - len(afterdot) > 12:
            return "Email is invalid"
        if afterdot not in validTLD:
            return "Email is invalid"

    # check if email start or end with ._ 
    if email[0] in NotPermits or email[-1] in NotPermits:
        return "Email is invalid"
    
    # check if email doesn't contain those rules
    for letter in email:
        if letter not in PERMITS and letter !="@" and letter not in PermitsForDomian:
            return "Email is invalid"
        if email.count("@") !=1:
            return "Email is invalid"
    
    # check if domain_name have _ or not
    for letter in domain:
        if letter in NotPermitForDomian:
            return "Email is invalid"
    return "Email is valid"

def main():
    email = str(input("Enter email:\n"))
    result = validate(email)
    print (result) 
if __name__ == "__main__":
    main()