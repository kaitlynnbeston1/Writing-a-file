#-----------------------------------------------------------------------------
# Title: Writing and Reading a File Example
# Version: 001
# Coder: Kaitlynn Beston
#-----------------------------------------------------------------------------
''' Example Code - writing to an external file.

    Syntax of Python open file function.
        file_object = open("filename", "mode")
    
    filename: gives name of the file that the file object has opened.
    mode: attribute of a file object tells you which mode a file was opened in.
    
    By adding a second argument to the open function, we can specify the mode:
    
    "r" means open in read mode, which is the default.
    "w" means write mode, for rewriting the contents of a file.
    "a" means append mode, for adding new content to the end of the file.
    “b” means open in binary mode, for non-text files such as images. 
        Binary mode must be added to another one of the above modes.

    Using write mode, the program will create a file if there is none and will
    overwrite the file if there is one.
    
    Using a with statement eliminates the need to close the file.
    with open(filename, mode) as temp_name:
'''
#-----------------------------------------------------------------------------
# Imports and Global Variables -----------------------------------------------
# Database
Marvel_Superheros = {
        "Spiderman" : {
                 "Name" : "Peter Parker", 
                 "Weapons" : ["Webbing"],
                 "Super Powers" : ["Speed", "Reflexes",
                                   "Spider-Sense"], 
                 "Weaknesses" : ["Ethyl Chloride Pesticide"] },
        "Thing" : {
                 "Name": "Ben Grimm",
                 "Weapons": ["Fists"],
                 "Super Powers": ["Immortal", "Super Strength",
                            "Enhanced Lung Capacity", "Good Fighter"],
               "Weaknesses": [None] },  
        "Baby_Groot" : {
                 "Name" : "Baby Groot",
                 "Weapons" : ["Strong Branches"],
                 "Super Powers" : ["Self-Healing", "Controls Plant", 
                                  "Immune to Fire"],
                 "Weaknesses" : ["Termites"] },
        "Ironman" : {
                 "Name" : "Tony Stark",
                 "Weapons" : ["Ironman Suit", "AI", "Blasters"], 
                 "Super Powers" : ["Smart", "Rich"],
                 "Weaknesses" : ["Arrogant"] },
        "Deadpool" : {
                 "Name" : "Wade Wilson",
                 "Weapons" : ["Katanas", "Grenade", "Gun"],
                 "Super Powers" : ["Speed", "Bullet Proof",
                                   "Self-Healing"],
                 "Weaknesses" : ["Women", "Ugly"] },
        "Antman" : {
                 "Name" : "Scott Lang",
                 "Weapons" : ["Antman Suit"],
                 "Super Powers" : ["Communication with Insects", 
                                   "Sound Amplification"],
                 "Weaknesses" : ["Lacks Ability Control"]}
}

# Functions ------------------------------------------------------------------
def hero_details(heroChoice):
    """Print out the inventory for the choosen character in an external file"""
    name = Marvel_Superheros[heroChoice]["Name"]
    # append/add the charaters name to the new file
    with open("character.txt", "w") as c:
         c.write(f"Hero name: {heroChoice}\n")
         c.write(f"Real name: {name}\n")
         c.write("Weapons: \n")
         for weapon in Marvel_Superheros[heroChoice]["Weapons"]:
             c.write(f"{weapon} \n")
         c.write("Super Powers: \n")
         for power in Marvel_Superheros[heroChoice]["Super Powers"]:
            c.write(f"{power} \n")
         c.write("Weaknesses: \n")
         for weakness in Marvel_Superheros[heroChoice]["Weaknesses"]:
          c.write(f"{weakness} \n")
      



def hero_choice():
    """User chooses character to play"""
    print("Possible characters: ")
    for hero in Marvel_Superheros:
      print(f"- {hero}")
    user = input("What player do you choose? ").title()
    if user.title() in Marvel_Superheros:
        hero_details(user.title())
        print("Print to external file successful!")
    else:
      print("Invalid choice!")

# Main -----------------------------------------------------------------------
hero_choice()
# confirm file worked by reading and printing it



