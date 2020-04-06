# data-cleaning-pandas: SHARK ATTACK PROJECT: 

<img src="./INPUT/babyshark.jpg" alt="Sharks"
	title="Very aggresive sharks" width="2000" height="300"/>

<p>&nbsp;&nbsp;&nbsp;&nbsp;Ironhack project on data cleaning with pandas using the 'Global Shark Attack' dataset.

## Objective
<p>&nbsp;&nbsp;&nbsp;&nbsp;In this project I will be using the Shark attack database from http://www.sharkattackfile.net.

<p>&nbsp;&nbsp;&nbsp;&nbsp;As other carnivore species, sharks are more active during the night and during the firt and last hours of the day. I want to investigate whether this peak in shark activity reflects a more aggressive behavour measured as the lethality of the attacks. In short: <strong><em>are shark attacks more lethal during the night?</em></strong> 
<p>&nbsp;&nbsp;&nbsp;&nbsp;Moreover, I want to look deeper into it and investigate whether this lethality changes with any activity that the victim is doing (a particular activity may increase the shark response during the day or during the night), and whether this lethality has changed over the years. <strong><em>Is the lethality of an attack time dependant or dependant on any activity?</em></strong>
<p>&nbsp;&nbsp;&nbsp;&nbsp;As a bonus question, I want to know <strong><em>how many total deaths by shark has a country per million inhabitants?</em></strong>

## Methodology
### Cleaning
&nbsp;&nbsp;&nbsp;&nbsp;The data cleaning process is included in the jupyter notebook `Cleaning.ipynb`. This procces consists in a serie of techniques such as <em>duplicate removal</em>, <em>null handeling</em>, <em>string manipulation</em>, <em>unusful columns removal</em>, or <em>column calculation</em> among others. This proccess relies on several custom functions defined in the file `cleaning_functions.py`. Some of these functions rely on the python module `re`, for regex patterns. Likewise, the bonus question uses an external python module called `countryinfo` to extract the total population of each country. 
### Analysis
&nbsp;&nbsp;&nbsp;&nbsp;To answer the questions stated above, I use a series of <em>bar plots</em>, <em>pie plots</em>, and <em>scatter plots</em> which construction is included in the jupyter notebook `Analysis.ipynb`. The analysis process relies heavily on the custom function `fatality` defined in the file `cleaning_functions.py`. This function calculates the percentage of fatal attacks over the total number of attacks by using the fatal columns ('Y'/'N').
## Conclusion
&nbsp;&nbsp;&nbsp;&nbsp;In general, shark attacks are 6.3% more lethal during the night than during the day. 

<p align="center">
<img src="./INPUT/sharkmeme.jpg" alt="Sharks"
	title="Could I please eat you?"/>
</p>