<h1><b>english-meaning</b></h1>
I developed this project trying to make my search for meanings of english words easier. I really like to use the command line and, to me, opening either the browser or a new tab every single time I want to search a simple meaning is painful.
The program output is supposed to be a QUICK AND SIMPLE explanation.
<hr></hr>

<h1> How to use </h1>
Since it's written in python, you have to have python installed on your machine. To download this project you will need git and, of course, access to the internet.
<p></p>
<div>On Linux:</div>
<code>git clone git@github.com:leo-ventura/english-meaning.git</code>

<code>cd english-meaning</code>

<p> Finally, the command to run the program is: </p>
<code> python merriam-webster.py <word> </code>
  <p>where <code>word</code> is the word that you want to know the meaning.</p>
<hr></hr>

<h1> About Licenses </h1>
According to Merriam-Webster API page: "The Merriam-Webster Dictionary API is free as long as it is for non-commercial use, usage does not exceed 1000 queries per day per API key, and use is limited to two reference APIs."
Although this python code is not an API, I'm not developing this for commercial use. So, I'm publishing this JUST FOR purpose of education.
<hr></hr>

<h1> Final considerations </h1>
This project is aimed at Merriam-Webster but you can change the website on the source code to any dictionary you want, just make sure you're using the correct path (e.g. https://www.merriam-webster.com/dictionary/) since our <word> will come after the "/"
. You can assure that by typing any english word you want to know the meaning after that slash.
