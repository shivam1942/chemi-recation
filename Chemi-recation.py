#read readme.md first

author = "Shivam pandey"

print("welcome to chemi recation app")
print(" ")
print("To see recation of any two chemical put number and see the recation")
print(" ")
print("1. oxygen+carbon")
print("2. oxygen+hydrogen")
print("3. oxygen+chlorine")
print("4. chlorine+carbon")
print("5. chlorine+hydrogen")
print("6. carbon+hydrogen")
print(" ")
chemical = input("put number which recation you want to see  ")

if chemical == "1" :
	print("C+ O2 -> CO2")
	print("In this reaction carbon reacts with oxygen to form carbon dioxide")
	
if chemical == "2" :
	print("H2+O -> H2O")
	print("In this reaction hydrogen reacts with oxygen to form water")

if chemical == "3" :
	print("O+Cl2 -> OCL+CL")
	print("In this reaction chlorine reacts with oxygen to form chlorine dioxide")
	
if chemical =="5" :
	print("H+CL -> HCL")
	print("In this reaction hydrogen reacts with chlorine to form hydrogen cloride")
	
if chemical == "4" :
	print("C + Cl2 -> CCl4")
	print("In this reaction carbon reacts with chlorine to form carbon tetrachloride")
	
if chemical == "6" :
	print("C+H -> C-H bond")
	print("In this reaction chlorine reacts with hydrogen to form carbon-hydrogen bond")

else :
	print("The number you have put is not there in the list try to put number which is in   list")
