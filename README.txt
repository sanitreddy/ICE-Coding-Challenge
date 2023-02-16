In-Person Programming Exercise: Word Processing


Background
The purpose of this exercise is to gauge how you approach a problem and implement
a solution. The problem in this example is not one you are likely to approach in 
your day-to-day tasks on the team but should offer a decent opportunity for us to
evaluate whether you would be a good fit for the team.


Problem
Given a source text input we would like you to calculate some statistics about the
quantity and frequency of various letters and words. The text is stored as a basic
ASCII file and is titled "chapter1.txt" (chapter 1 of A Tale of Two Cities). 

Your solution should be in the form of a re-usable package/module. A "main" script
should import this library and leverage any functionality you build.


Requirements
    - Output paragraph count
	- Output a count of total lines
    - Output a count of lines with text
    - Output total word count
    - Output a count of all letters (e.g. [a, b, c, ...], case insensitive)
    - Output a count of vowels [a, e, i, o, u, case insensitive]
    - Output a count of consonants (case insensitive)
    - Output the top five words with the highest use frequency (case insensitive)
	- Output the top 3 longest words in descending order (case insensitive)
    
    
Example Output (not necessarily actual values):
==================================
Text Statistics for "chapter1.txt"
    Paragraphs  : 6
    Lines       : 94
    Words       : 1,238
    Letters     : 18,392
      Vowels    : 8,902
      Consonants: 9,490
    Top 5 Words:
        1. "and" appeared 202 times
        2. "i" appeared 190 times
        3. "the" appeared 170 times
        4. "an" appeared 150 times
        5. "two" appeared 202 times
	Top 3 Longest Words:
		1. "something"
		2. "fairly"
		3. "long"
==================================
    


Notes and Restrictions
    - There is no time restriction but this is not meant to take a ton of time
		- Try to limit yourself to 90 minutes 
		- If you want to go beyond 90 minutes that's fine but be sure to note approximately what was completed 
		  by that point
    - Use a development environment of your choice but your solution should run against Python 3.8
	- Use the base language / standard libraries if possible
		- Avoid 3rd party libraries
	- Your analysis functions should be added to a python package/module where you'll leverage them in the main 
	  function
		- A stub "txtlib" has been created
		- More info: https://realpython.com/python-modules-packages/#python-packages
    - The chapter title should NOT be included in your calculations
		- You can assume that the chapter title is the first line of the file followed by two blank lines
		- All three lines should be considered the title and not included in your analysis
    - Try to keep your program functional so that when you submit it will still run even if partially complete
        - You may want to use version control and put enhancements on new branches
          that can be merged in when actually completed, but this is not required
    - You MAY use the internet and any resources - if you grab code wholesale please 
      document it.
    - Try to keep code in discreet functions if possible (i.e. avoid sprawling code)
    - Ideally your code should process the text minimal times and not re-open and loop
      for each statistic