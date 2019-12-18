"""
CLAUSE LOGIC THEOREM PROVER
Tennessee Bonner and Gerald Zapata 
October 29, 2019

This is a theorem prover that uses the resolution principle to test whether or not a specific clause is valid.

Takes one argument: The file containing an existing knowledge base followed by the test clause on the last line of the file 
Example:            python main3.py demo.in
Three Functions: 
 -main reads the arguments, builds a testable knowledge base and calls resolution to test it
 -resolution loops through every clause in the KB to either expand it or prove that the test clause is 
 -negate negates the clause passed by main so it can be used in resolution
"""
import sys;

#This returns a list of clauses that result from negating the clause passed to this function
def negate(clause):

	negatedClause = []
	for x in clause:
		if x[0] == "~":
			negatedClause.append(x[1:])

		else:
			negator = "~" + x
			negatedClause.append(negator)
	return negatedClause

#Uses resolution rule to generate new clauses and check for any contradictions
def resolution(KBList, KBSize):

	itterator = 0

	#Runs until the itterator has made it to the end of the knowledge base
	while (itterator != KBSize):

		#Goes through every clause x in the expanding Knowledge Base,...
		for x in range(itterator, KBSize):
			
			#...For every clause that precedes x,...
			for y in range(0, x):
				
				setX = KBList[x].copy()
				setY = KBList[y].copy()

				#...Check if both clauses could lead to a contradiction, ...
				possibleContradiction = False
				if (len(setX) == 1 and len(setY) == 1):
					possibleContradiction = True
				
				#...Remove elements from both clauses if they oppose each other(i.e A and !A), ...
				elementRemoved = 0
				for z in KBList[x]:
					antithesis = ""
					if z[0] == "~":
						antithesis = z[1:]
					else:
						antithesis = "~" + z

					if antithesis in setY:
						elementRemoved += 1
						setX.remove(z)
						setY.remove(antithesis)
				
				#...Assemble the remainder of these clauses into a testSet, ...
				testSet = setX|setY

				#...and Test if testSet is already in the knowledge base(If so add it to the KB).
				if elementRemoved == 1 and possibleContradiction == False:
					if testSet not in KBList:
						KBSize += 1
						clasueString = str(KBSize) + ". "
						for z in testSet:
							clasueString = clasueString + z + " "
						clasueString = clasueString + "{" + str(x+1) + "," + str(y+1) + "}"
						print (clasueString)
						KBList.append(testSet)
				

				#If the single elemnts contradict one another then flag a contradiction and return true(The Test Clause is valid!)
				if elementRemoved > 0 and possibleContradiction:
					KBSize += 1
					clasueString = str(KBSize) + ". Contradiction {" + str(x+1) + "," + str(y+1) + "}"
					print(clasueString)
					return True
			
			itterator += 1
		#By now if a clause was added to the knowledge base, it would be compared against all it's preceding clauses by using the while loop to account for the expanding Knowledge Base size
	
	return False

#Builds The initial Knowledge base and uses resolution principle to test the test clause
class main:

	#If the number of arguments passed is two
	if len(sys.argv) == 2:
		
		KBList = []						#Create the knowledge base
		tempSet = set()					#Empty set to hold 
		file = open(sys.argv[1], "r")	#The file being read from
		KBSize = 0						#Size of the knowledge base

		#For every line in the file the clauses are added as a set to the Knowledge Base
		for line in file:
			tempSet.clear()
			line = line.replace('\n', '')
			tempList = line.split(" ")
			for x in range(len(tempList)):
				tempSet.add(tempList[x])
			KBList.append(tempSet.copy())
			KBSize += 1

		#The last element of the Knowledge Base(the test clause) is removed
		del KBList[-1]
		KBSize -=1

		#The test clause is then Negated, ...
		file.seek(0)
		line = file.readlines()[-1]
		negatedClauseList = negate(line.split(" "))
		file.close()

		#... and added to the Knowledge Base, in order to prove it using the resolution principle.
		for x in range(len(negatedClauseList)):
			KBSize += 1
			tempSet = set()
			tempStr = negatedClauseList[x]
			tempSet.add(tempStr)
			KBList.append(tempSet)
		
		#All of the ellements of the now existing Knowledge Base are printed
		for x in range(len(KBList)):
			clasueString = str(x+1) + ". "
			for y in KBList[x]:
				clasueString = clasueString + y + " "
			clasueString = clasueString + "{}"
			print (clasueString)

		#We then check to see if the clause is valid by contradiction (Using the resolution principle)
		validity = resolution(KBList, KBSize)

		#If it is we print "Valid"
		if validity:
			print("Valid")

		else:
			print("Invalid")

	else:
		print("Invalid number of Arguments. Please try again.")