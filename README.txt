CLAUSE LOGIC THEOREM PROVER
Tennessee Bonner and Gerald Zapata 
October 29, 2019

Try running the following: 	python main3.py demo.in

main3.py is a theorem prover that uses the resolution principle to test whether or not a specific clause is 
valid. There is only one argumet passed to the program, a filename. The file listed must be of a specific format 
with sentences in conjunctive(clausal) normal form. ANDs are represented by a line break, ORs are represented
by a single space and NOTs are represented by a '~'. 

All of the lines in the file(sentences) with the exception of the last will make up the knowledge base which we 
will use to test the test clause. The test clause is the last line in the file.


The program begins by reading the input file to build the knowledge base and negating the test clause. After this
the program loops through every sentence in the knowledge base to check if a contradiction is found. If one is 
found then the test clause is proven true by the resolution principle.


Included with main3.py are several files which can be used to test it. These are broken into two types of files:
	IN Files (input files containing a KB and test clause):
		demo.in
		task1.in
		task2.in
		task3.in
		task5.in
		task6.in
		task7.in
	OUT Files (output files containing the results for some of the input files):
		demo.out
		task6.out
		task7.out