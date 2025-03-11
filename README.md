# Quarterback Lab

In this lab you will be using Python special methods and private methods to create a quarterback class and compute a quarterback's passer rating. Below is the formulas for calculating passer rating:  
<img width="760" alt="Screenshot 2024-03-01 at 12 25 31 PM" src="https://github.com/lmraine/quarterback-dunder-lab/assets/55120024/6ab1ec76-1034-4c03-bf01-a3a4bb425706">

## Set Up
<ol>
	<li>Create new anaconda environment using these commands</li>
	<ul>
		<li>conda create --name quarterback_lab python=3.13.1</li>
		<li>conda activate quarterback_lab</li>
	</ul>
	<li>Pull starter code from GitHub Classroom</li>
	<li>Open in VS code and switch to the quarterback_lab anaconda environment</li>
	<li>When the lab is complete, push code to GitHub Classroom</li>
</ol>

## Instructions
In the quarterback.py file create a class called Quarterback class with the following attributes and methods:  
<ol>
  <li><strong>Attributes</strong></li>
  <ol>
    <li>required: name, team, att, cmp, yds, td, intc attributes</li>
    <li>create the following instance attrubutes: a, b, c d. These should all be private instance attributes. These will get their values from the methods outlined below.</li>
    <li>Create an instance attribute called passer_rating. It will get it's value from the method outlined below.</li>
  </ol>
  <li><strong>Methods</strong></li>
  <ol>
    <li>calc_a(): calculates the value of a using the above formula</li>
    <li>calc_b(): calculates the value of b using the above formula</li>
    <li>calc_c(): calculates the value of c using the above formula</li>
    <li>calc_d(): calculates the value of d using the above formula</li>
    <li>calc_passer_rating(): calculates the value of passer rating</li>
    <li>Overload the str special method to return a string formatted like this "{quarterback name} plays for {quarterback team}"</li>
    <li>Overload the less than (lt) special method to customize how quarterbacks are compared. If two quarterbacks have the same passer rating, return "These quarterbacks are equal", if one quarterback's passer rating is greater than the other, return "{quarterback name} is a better quarterback than {other quarterback name}</li>
  </ol>
  <li>main.py</li>
  In main.py file complete the following:
  <ol>
    <li>Import any necessary classes</li>
    <li>Create two quarterbacks: brady and montana based on their NFL stats</li>
    <li>Tom Brady played for the New England Patriots and here are his stats: https://www.espn.com/nfl/player/stats/_/id/2330/tom-brady</li>
    <li>Joe Montana played for the San Francisco 49ers and his stats are here: https://www.espn.com/nfl/player/stats/_/id/6445/joe-montana</li>
    <li>create a variable called brady_pr to store brady's passer rating rounded to a single decimal place.</li>
    <li>create a variable call montana_pr to store montana's passer rating rounded to a single decimal place.</li>
    <li>create a variable called comparison to store the result of comparing the brady and montana objects using the "<" symbol</li>
      <li>Feel free to print these results out to test your results</li>
      <li>Feel free to create other object to test out your results (Dan Marino, Peyton Manning, Tony Romo, etc)</li>

  </ol>
</ol>
