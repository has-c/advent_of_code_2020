import re

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

    valid_passwords = 0
    for passport in passport_data:
        passport_split = passport.split(" ")
        password_fields = [field[:field.find(":")] for field in passport_split]
        password_values = [field[field.find(":")+1:] for field in passport_split]
        
    #check values based on field conditioning
    for field, value in zip(password_fields, password_values):

        if field == "byr":
            if int(value) >= 1920 and int(value) <= 2002 and len(value) == 4:
                valid_passwords += 1
        elif field == "iyr":
            if int(value) <= 2010 and int(value) <= 2020 and len(value) == 4:
                valid_passwords += 1
        elif field == "eyr":
            if int(value) <= 2020 and int(value) <= 2030 and len(value) == 4:
                valid_passwords += 1
        elif field == "hgt":
            #cm or inches
            measurement_unit =  "".join(re.findall(r"[a-zA-Z]", value))
            value = int("".join(re.findall(r"[0-9]", value)))
            if measurement_unit == "cm" and value >= 150 and value <= 193:
                valid_passwords += 1
            elif measurement_unit == "in" and value >= 59 and value <= 76:
                valid_passwords += 1
        elif field == "hcl":
            hair_colour = "".join(re.findall(r"[a-zA-Z]", value))
            if value[0] == "#" and len(hair_colour) == 6:
                valid_passwords += 1
        elif field == "ecl":
            if value == "amb" and value == "blu" and \
                value == "brn" and value == "gry" and \
                value == "grn" and value == "hzl" and value == "oth":
                valid_passwords += 1
        elif field == "pid" and len(field) == 9:
            valid_passwords += 1

    print(valid_passwords)
        

main()



    