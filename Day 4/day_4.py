def d4_pl(passport_data):
    valid_passwords = 0
    for passport in passport_data:
        passport_split = passport.split(" ")
        password_fields = [field[:field.find(":")] for field in passport_split]
        if "byr" in password_fields and "iyr" in password_fields \
            and "eyr" in password_fields and "hgt" in password_fields \
            and "hcl" in password_fields and "ecl" in password_fields \
            and "pid" in password_fields: 
            valid_passwords += 1

    print(valid_passwords)


def main():
    #open and parse file
    passport_data = list()
    passport = str() 
    with open("d4_puzzle.txt", "r+") as f:
        for line in f:
            if line == "\n":
                passport_data.append(passport.strip())
                #new passport
                passport = str() 
            else:
                passport += " " + line

    passport_data.append(passport.strip()) #append last line as it has no newline

    d4_pl(passport_data)

main()



    