---
layout: page
title: Class Notes
permalink: /classnotes/
---


<!-- saved from url=(0059)http://webpages.cs.luc.edu/~cnaiman/COMP150/ClassNotes.html -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">


##Class Notes
Based on class notes (with permission) of Dr. Andrew N. Harrington<br>
</h1>
<span style="font-style: italic;"></span> 
<p>These notes are basically for everything except the <a href="http://anh.cs.luc.edu/python/hands-on/3.1">Hands-on
Python Tutorial</a>.&nbsp;
That is a free-standing unit that we take up after the <a href="http://hwheeler01.github.io/comp150/classnotes/#Class1">Course
Introduction</a>.&nbsp; <br>
</p>
<p>Videos for most of the sections below are in the `beyondPython`
folder
in GoogleDocs, discussed in the <a href="http://hwheeler01.github.io/comp150/resources/">Resources</a>.<br>
</p>
<p>Sections that correspond to the start of a video have (vid)
at the end of the title.</p>

<p>
</p>
<h2>Table of Contents</h2>
<ol>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Class1">Course
Introduction</a></li>
<ol style="list-style-type: upper-alpha;"><li><a href="http://hwheeler01.github.io/comp150/classnotes/#Areas">Computer
Science Areas</a></li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Introductory">Introductory
Approaches</a></li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Past">Past
Final Projects</a> (vid)</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Hands">Using
the Hands-on Python Tutorial</a><br>
</li>
</ol>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#AfterPython">After
Python and Underneath
Python</a> (vid)</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Binary">Binary
Arithmetic&nbsp;</a> (vid)
<ol style="list-style-type: upper-alpha;">
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#binToDec">Converting
binary to
decimal numerals</a></li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#decToBin">Converting
decimal&nbsp;to&nbsp;binary numerals</a> (vid)</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Hexadecimal">Hexadecimal
(Base 16)</a> (vid)<br>
</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#binToHex">Converting
Binary to
Hexadecimal</a></li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#hexToBin">Hexadecimal
to Binary</a></li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#formattingBases">Formatting
Binary,
Octal,
and Hexadecimal in Python</a> (vid)</li>
</ol>
</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Pip">Pip
Assembler</a> (vid)
<ol style="list-style-type: upper-alpha;">
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#pipSim">Pip
Assembler Simulator</a> (vid)<br>
</li>
<li> <a href="http://hwheeler01.github.io/comp150/classnotes/#machineLang">An
Introduction to Pip
Machine Language</a> (vid)<br>
</li>
<li> <a href="http://hwheeler01.github.io/comp150/classnotes/#morePipSim">More
on the Simulator
and Pip</a> (vid)</li>
<li> <a href="http://hwheeler01.github.io/comp150/classnotes/#Pip1">Format
of my Pip
assembler</a></li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Assignment_Translation_Applet">Assignment
Translation Applet Introduction</a> (vid)<br>
</li>
<li> <a href="http://hwheeler01.github.io/comp150/classnotes/#Loops_AddressLabels">Loops
and Symbolic
Address Labels</a> (vid)</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#pipJumps">Practice
Using jumps</a> (vid)<br>
</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#translationMachineAssem">Translation
Between Machine Language and Assembler</a> (vid)</li>
</ol>
</li>
<li><a href="./Class Notes_files/Class Notes.html">Boolean
Algebra, Truth
Tables, and Digital Circuits</a> (vid)
<ol style="list-style-type: upper-alpha;">
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#algrbraOverview">Boolean
Algebra and
Truth Tables</a> (vid)</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#BooleanAlgRules">Rules
of Boolean Algebra</a>
(vid) </li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#GatesCircuits">Transistors,
Gates, and
Circuits</a> (vid)</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#GatesApplet">Gates
Applet</a> (vid)<br>
</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#boolExprForTruthT">Finding
a Boolean
Expression for a truth table</a> (vid)</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#computerCircuits">Computer
Addition</a> (vid)</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Multiplexers">Mutiplexers</a>
(vid)</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Latch_Circuit">Latch
Circuit</a> (vid)</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#VLSI">Chip
Fabrication</a> (vid)</li>
</ol>
</li>
<li><a href="http://hwheeler01.github.io/comp150/classnotes/#Conclusion">Conclusion</a></li>
</ol>
<h2><a class="mozTocH2" name="Class1"></a>Course
Introduction --REWRITE</h2>
</h3><h3>Computer Science <a name="Areas"></a>Areas<br>
</h3>
<p>Computer Science centers on <i>algorithms</i>:
&nbsp;unambiguous, step by step instructions for how to accomplish
a
particular task in a finite amount of time. <br>
</p>
<p><a href="http://www.americanscientist.org/libraries/documents/20108101750328103-2010-09Denning-ComputingScience.pdf">Peter
J.
Denning</a> lists seven main categories in computing</p>
<ul>
<li>
<p style="margin-bottom: 0in;"><b>Computation</b>
<span style="font-weight: normal;">(meaning and limits
of computation)</span></p>
</li>
<li>
<p style="margin-bottom: 0in;"><b>Communication</b>
<span style="font-weight: normal;">(reliable data
transmission)</span><br>
</p>
</li>
<li>
<p style="margin-bottom: 0in;"><b>Coordination</b>
<span style="font-weight: normal;">(cooperation among
networked entities)</span> </p>
</li>
<li>
<p style="margin-bottom: 0in;"><b>Recollection</b>
<span style="font-weight: normal;">(storage and
retrieval of information)</span> </p>
</li>
<li>
<p style="margin-bottom: 0in;"><b>Automation</b>
<span style="font-weight: normal;">(meaning and limits
of automation)</span> </p>
</li>
<li>
<p style="margin-bottom: 0in;"><b>Evaluation</b>
<span style="font-weight: normal;">(performance
prediction and capacity
planning)</span> </p>
</li>
<li>
<p><b>Design</b> <span style="font-weight: normal;">(building
reliable software systems)</span> </p>
</li>
</ul>
<h3><a name="Introductory"></a>Introductory
Approaches<br>
</h3>
<p>&nbsp;With all there many&nbsp;aspects, college
introductions have
handled things
differently over time:</p>
<ol>
<li>
<p style="margin-bottom: 0in;">Historically students
usually
started with several heavy programming courses before anything else,
giving
little initial idea of all the other parts of computer science! </p>
</li>
<li>
<p style="margin-bottom: 0in;">Then there was a
reaction to
breadth-first, essentially no programming. &nbsp;This is partly
because
in the past popular languages had a steep learning curve.
&nbsp;Instead
of much&nbsp;programming in a real computer language, breadth-first
courses have brought&nbsp;algorithms written in English to a
central
place. </p>
</li>
<li>
<p>That brings us to the present with this course.
&nbsp;Programming is important, and now there is an excellent
recent
language&nbsp;Python: &nbsp;extremely simple to learn and
understand
(close to English) and very powerful&nbsp; - why do much in English
outlines when with about as much work you can demonstrate things on the
computer using Python? &nbsp;Plus, even beginners can write
programs to
simplify their own personal tasks. &nbsp;Hence we spend a fair
amount
of our time on algorithms actually working with Python. We still
keep the idea that Computer Science is much more than programming, and
look at history, applications, and their relationship to the WWW.
&nbsp;We dig down into the guts of a computer below what we see
from
the high-level language Python,&nbsp;to machine language and
assembler
code, and to the hardware underneath.&nbsp; We look beyond
Python to
application areas like graphics and web servers. </p>
</li>
</ol>
<p>In an introductory course we cannot cover a whole lot with any
depth, but we will deal at some level with all the areas:&nbsp; We
will
think about what we can compute.&nbsp; The last part of the section
using Python will involve communication and cooperation between web
client and server.&nbsp; We introduce a basic way to store
information,
in files. &nbsp; We will design, write and evaluate programs to
automate the solution of problems. </p>
<p>For the programming in Python, we use custom tutorials written
by Dr. Harrington,&nbsp; <a href="http://anh.cs.luc.edu/python/hands-on/3.1">Hands-on
Python Tutorial</a>.&nbsp; For the other areas, Dr. Harrington has written these
online
notes that you are reading. &nbsp;&nbsp; &nbsp;</p>
<p>We are not alone in choosing Python: &nbsp;Much of the
control of
Google is by Python (about 1/3 of the code they write for their own
applications, plus the Google App Engine providing free web sites to
anyone requires writing Python code), as is much of the
administration of Unix. &nbsp;Much scientific programming is done
in
Python. &nbsp;Microsoft now has a&nbsp;Python, too, for its own
.net
platform. &nbsp;Python is freely available for Windows, modern
Macs,
and Linux.</p>
<h3><a name="Past"></a>Past Final Projects
(vid)</h3>
Here are a couple of final Python projects from students from a past
semester.&nbsp; They give some idea where the programming can
head.&nbsp; These are easy to show off.&nbsp; Both are graphics
games,
though the final project is
open-ended, and others have done dynamic web projects, scientific data
analysis, ....<br>
<br>
Right click on the following link and select Save As.<a target="_blank" href="http://hwheeler01.github.io/comp150/pastGames.zip"><br>
samples to download and unzip</a>
<p>Further instructions (for Windows):</p>
<ol>
<li>Save the file. In a Loyola Windows
lab use d:\Userdata</li>
<li>Find that place in the file system, for
instance via My Computer, or your browser may have an Open Enclosing
Folder option.</li>
<li><i>Right</i> click on pastGames.zip, </li>
<li>Select Extract All....</li>
<li>Follow the default choices</li>
<li>When the
new directory pops up, double click on Python program <span style="font-weight: bold;">hole</span> or <span style="font-weight: bold;">asteroids</span></li>
<li>Play! Try the other game. </li>
</ol>
<h3>Using the <a name="Hands"></a>Hands-on
Python Tutorial<br>
</h3>

<p>Python topics are covered in the <a href="http://anh.cs.luc.edu/python/hands-on/3.1">Hands-on
Python Tutorial</a>.&nbsp; Homework exercise links and topic
timing are
in the Course Schedule. <br>
</p>
<p>While the tutorial introduces all the topics, there is more to
say
about using it effectively.&nbsp; There is way too much detail to
just
obsorb all at once,&nbsp; So what are the first things to
learn?&nbsp; <br>
</p>
<p>More imprtant than memorizing details is having an idea of the
building blocks available and how they are useful.&nbsp; For
the most direct exercises, you might&nbsp; just look back over the
most
recent section looking for related things, but that will not work when
you have scores of sections that might have useful parts!&nbsp; The
basic idea of the building blocks should be in your <span style="font-style: italic;">head</span>. For instance,
after going in the Tutorial through 1.10.4, you will want to have very
present:</p>
<p>
</p>
<ul>
<li>You can use numbers and do arithmetic.</li>
<li>You can store and retrieve data using variable names and
assignment statements.</li>
<li>Python has many useful built-in functions that can affect
the system or return results for you to use.<br>
</li>
<li>You can get keyboard input from the user and print things
back for the user.</li>
<li>Data comes in different types, and you can convert where it
makes sense.</li>
<li>You can use strings and generate them in many
ways:&nbsp; literal strings, addition operator (+), string format
method.</li>
</ul>
Once you have an idea of the appropriate building blocks needed to
solve a specific problem, then you can worry about more
details.&nbsp;
Particularly at the beginning, you are not likely to have all the exact
Python syntax for the parts of your solution nailed down!&nbsp; It
is
not important to <span style="font-style: italic;">remember</span>
it precisely, but it is important to know how to <span style="font-style: italic;">find</span>a
clear explanation efficiently:&nbsp; Know the location in examples
or
in the tutorial, or use the index, the search capacity, summaries,
and/or write things in
notes for yourself - as for an exam.&nbsp; Writing short bits down
is
also useful because the act of writing helps many people absorb what
they are writing. <br>
<br>
As your experience increases
you will get used to and remember more and more stuff, but there is
always the latest&nbsp; ideas/syntax to get used to!&nbsp; Your
notes of what is important but still not in immediate recall will
evolve continuously.<br>
<br>
This multi-tiered approach means that what you absorb should not just
be an enormous
collection of unstructured facts that you plumb through in its entirety
to find a useful idea.&nbsp; You first need to be
particularly aware of the major headings of useful features, and then
do what you need to
drill down to details as necessary.<br>
<br>
This approach is important in the real-world, away from
Python.&nbsp;
The world is awash with way to much information to memorize, but
need to access the information that you need to synthesize and
formulate
solutions/arguments ... effectively!<br>
<br>
The tutorial also talks about the tool, Idle.&nbsp; Of course you
need to get used to your tools.<br>
<p>
</p>
<h2><a class="mozTocH2" name="AfterPython"></a>After
Python and
Underneath It (vid)
</h2>
<p>We have seen how we can tell the computer what to do with the
fairly
simple syntax of Python.&nbsp; The course started there because it
was
relatively easy place to accomplish a lot.&nbsp; As you were
introduced
to it, Python was just given to you.&nbsp; We could immeditately
see,
experimenting in the Shell, that Python worked on your
computer.&nbsp;
But how?&nbsp; Python operates on the top of many layers of
computer
hardware and software.&nbsp; We are going to take an introductory
exploration down into the hardware and logic of computers.&nbsp;
Here
is an outline of that path:</p>
<span style="font-weight: bold;">Binary arithmetic</span>:&nbsp;
We
will see that everything in a computer gets encoded as a
number.&nbsp;&nbsp; The hardware is built essentially on two
state
switches, that handle a <span style="font-style: italic;">bit</span>
of information at a time. We can use different names for the two
choices: true and false or as 1 and 0.&nbsp; A compatible number
system
is important.&nbsp; Rather than our familiar <span style="font-style: italic;">decimal</span> system,
also call <span style="font-style: italic;">base 10</span>,
we will need to understand
the <span style="font-style: italic;">binary</span>
system, also
called <span style="font-style: italic;">base 2</span>.
<p><span style="font-weight: bold;">Machine Language
and Assembler</span>:&nbsp;
Next we work with the instructions that are part of the computer's
hardware.&nbsp; To be feasible in hardware, the instructions need
to be
rather simple.&nbsp; They are the <span style="font-style: italic;">machine
language</span> of a particular computer. We will look at machine
language (actually an extra simple model of a machine language), mostly
though its more human friendly variant, <span style="font-style: italic;">assembler</span>.&nbsp;
We see how higher
level ideas we express in languages like Python can be translated into
and implemented with a very limited group of simple
instructions.&nbsp;
The Python interpreter does this conversion for Python programs.</p>
<p><span style="font-weight: bold;">Boolean Logic
and Circuits</span>:&nbsp;
Once we have an idea of how simple instructions can be combined to
implement high level programs, the final stage is to look at how
hardware can implement individual instructions.&nbsp; In Python we
built up logical expressons with <span style="font-weight: bold;">and</span>,
<span style="font-weight: bold;">or</span>, and <span style="font-weight: bold;">not</span>.&nbsp; We
will look much more
systematically at logical expressions, and see how they relate to
circuits and machine language instructions.&nbsp;
</p>
<h2><a name="Binary"></a>Binary
Arithmetic&nbsp; (vid)</h2>
<h2> </h2>
<p>Computers depend on arithmetic and numerical codes, and the
simplest way to do arithmetic in an electronic computer is with base
2, the binary number system.&nbsp; First review our usual decimal
system, in powers of 10:<br>
<br>
place value
- powers of 10, base 10 (recall anything to the 0 power is 1)<br>
3072
= 3*10<sup>3</sup> + 0*10<sup>2</sup> + 7*10<sup>1</sup>
+ 2*10<sup>0</sup><br>
This
is easiest to write out from right to left, so you start counting
powers from 0). &nbsp;Note that we also need symbols for the
numbers
less than ten (0-9)<br>
We think of 3072 as a <i>number</i>. &nbsp;In
this discussion that is too sloppy: &nbsp;The symbolism is a <i>numeral</i>
representing a number.<br>
Another representation could be a pile of
3072 counters, or a Roman numeral MMMLXXII. &nbsp;<br>
<br>
Also we can
make different numerals by&nbsp;using a different base, in
particular
the simplest one, and the one used in computers hardware:</p>
<h3><a class="mozTocH3" name="binToDec"></a>Converting
binary to
decimal numerals<br>
</h3>
<p style="margin-bottom: 0in;">(included in previous
video)&nbsp;
Binary (base 2) uses powers of 2 for
place value and two symbols 0, 1, for the numbers less than 2:<br>
I
will use a subscript to indicate the different base: &nbsp;11011<sub>2</sub>
means the base 2 numeral 11011: &nbsp;If we expand the powers
explicitly from the right, in normal arithmetic, this means:<br>
1*2<sup>4</sup>
+ 1*2<sup>3</sup> + 0*2<sup>2</sup> + 1*2<sup>1</sup>
+ 1*2<sup>0</sup><br>
=
16 + 8 + 2 + 1 = 27<sub>10</sub>.&nbsp;<br>
The base 10 numeral 27
refers to the same number as the base 2 numeral 11011.<br>
<br>
For
base 2, where the only coefficients are 0 and 1, a shorthand for
converting small&nbsp;base 2 numerals to decimal is to think of the
sequence of the possible powers of 2, and then just add in the values
where there is a 1 in the base 2 numeral:</p>
<table border="0" cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td>
<p><font face="monospace">2<sup>4</sup></font></p>
</td>
<td>
<p><font face="monospace">2<sup>3</sup></font></p>
</td>
<td>
<p><font face="monospace">2<sup>2</sup></font></p>
</td>
<td>
<p><font face="monospace">2<sup>1</sup></font></p>
</td>
<td>
<p><font face="monospace">2<sup>0</sup></font></p>
</td>
<td>
<p>power notation</p>
</td>
</tr>
<tr>
<td>
<p>16</p>
</td>
<td>
<p>8</p>
</td>
<td>
<p>4</p>
</td>
<td>
<p>2</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>decimal values of powers</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>A sample base 2 numeral</p>
</td>
</tr>
<tr>
<td>
<p>16</p>
</td>
<td>
<p>+8</p>
</td>
<td><br>
</td>
<td>
<p>+2</p>
</td>
<td>
<p>+1</p>
</td>
<td>
<p>= 27<sub>10 &nbsp;</sub>Sum of products
(or sum powers with
coefficient 1)</p>
</td>
</tr>
</tbody>
</table>
<p>Looking ahead, download <a target="_blank" href="http://webpages.cs.luc.edu/~cnaiman/COMP150/nt_examples/pipFiles.zip">pipFiles.zip</a>,
and unzip it on your computer or on your flash drive. &nbsp;The
pipFiles directory also contains an Idle shortcut and a module for
studying bases, bases.py.&nbsp; To follow along for now, open Idle
in
this directory.<br>
</p>
<p>
Binary to decimal conversion is done directly by Python.
&nbsp;Try the following in the Python Shell, stopping without a
close
parenthesis, and look at the popup window in the Python shell,
pointing out possible parameters:<br>
int('11011'<br>
note the second
optional parameter, the base. &nbsp;Finish as<br>
int('11011', 2)<br>
see
the correct answer.<br>
<br>
The
applet<br>
<a href="http://courses.cs.vt.edu/~cs1104/number_conversion/convtop.html">http://courses.cs.vt.edu/~cs1104/number_conversion/convtop.html</a><br>
illustrates
place values in all bases from 2 - 16.</p>
<h3><a class="mozTocH3" name="decToBin"></a>Converting
decimal&nbsp;to&nbsp;binary numerals (vid)</h3>
<h3> </h3>
<p>Now we go in the other direction: &nbsp;finding the binary
place
values from a given integer number:<br>
Suppose we have an unknown
int, i, which can be represented as a&nbsp;4 digit decimal.
&nbsp;How
could we recover the digits by doing simple arithmetic? &nbsp;(On a
computer, there is something to do here, since the number is actually
stored in a binary form.) &nbsp;A small amount of algebra can show
us
the general approach: &nbsp;For the algebra we&nbsp;name the 4
digits, say&nbsp;p, q, r, s, then we have<br>
i&nbsp;= p*10<sup>3</sup>
+ q*10<sup>2</sup> + r*10<sup>1</sup> + s<br>
Note all but the last
term are divisible by 10, so<br>
s&nbsp;= i % 10<br>
We have s, so we
can remove it from our power sequence with integer division by 10.
Change i so<br>
i&nbsp;= i//10 = &nbsp;p*10<sup>2</sup> + q*10<sup>1</sup>
+ r<br>
Now use the same trick to recover r! &nbsp;<br>
r&nbsp;= i %
10<br>
Continue, let<br>
i = i//10 = p*10<sup>1</sup> + q<br>
q&nbsp;= i
% 10<br>
One more time, let<br>
i = i//10 = p<br>
p = i % 10<br>
To
illustrate the general algorithm we can go through one more step:
&nbsp;Let&nbsp;<br>
i&nbsp;= i//10 = 0 - - getting &nbsp;a&nbsp;0
result means we are done.<br>
<br>
This can turn into a general
algorithm in Python:</p>
<pre>def decimal(i):<br> """return a string of decimal digits representing <br> the nonnegative integer i."""<br> if i == 0:<br> return "0"<br> numeral = ""<br> while i != 0:<br> digit = i % 10<br> numeral = str(digit) + numeral # add next digit on the LEFT<br> i = i//10<br> return numeral</pre>
<p>Decimal to binary conversion: &nbsp;same idea as for
digits of
unknown number, but generate base is 2, not 10:</p>
<pre>def toBinary(i):<br> """return a string of binary bits representing <br> the nonnegative integer i."""<br> if i == 0:<br> return "0"<br> numeral = ""<br> while i != 0:<br> digit = i % 2<br> numeral = str(digit) + numeral # add next digit on the LEFT<br> i = i//2<br> return numeral</pre>
<p style="margin-bottom: 0in;">For illustration, this can
also be done
by hand. &nbsp;To convert
14<sub>10</sub> to 1110<sub>2</sub>, start with
14 (at the bottom of
the picture) and repeatedly divide by 2 until you get a 0
quotient:<br>
<img src="./Class Notes_files/decToBinManual.png" name="graphics1" alt="Decimal to binary by hand" align="bottom" border="0" height="167" width="182">&nbsp;<br>
Binary
is verbose!&nbsp; We will see that there is a very simple
relationship between base 2 and base 16 =&nbsp;<font face="monospace">2</font><sup><font face="monospace">4</font></sup>.
&nbsp;Base 16 takes up about a quarter of the space of base 2, and
so
it is used in many places to communicate binary information
compactly. &nbsp;<br>
</p>
<h3><a name="Hexadecimal"></a>Hexadecimal
(Base 16) (vid)</h3>
<h3>
</h3>
<p style="margin-bottom: 0in;">
We have not
discussed bases above 10 yet. &nbsp; Problem: &nbsp;We need 16
distinct one-character symbols for 0 through 15. &nbsp;You run out
of
symbols using&nbsp; normal digits at 9. <span style="font-weight: bold;">Solution</span>: then start
with letters, so decimal 10 corresponds to hexadecimal A, 11-&gt;B,
12-&gt;C, 13-&gt;D, 14-&gt;E, 15-&gt;F. &nbsp;The
following table for
0-15 decimal has columns for&nbsp; hexadecimal and also
binary.&nbsp;
We will find the binary useful shortly:</p>
<table cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td>
<p>Dec</p>
</td>
<td>
<p>Hex</p>
</td>
<td>
<p>Bin</p>
</td>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>0000</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>0001</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>2</p>
</td>
<td>
<p>0010</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>3</p>
</td>
<td>
<p>0011</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>4</p>
</td>
<td>
<p>0100</p>
</td>
</tr>
<tr>
<td>
<p>5</p>
</td>
<td>
<p>5</p>
</td>
<td>
<p>0101</p>
</td>
</tr>
<tr>
<td>
<p>6</p>
</td>
<td>
<p>6</p>
</td>
<td>
<p>0110</p>
</td>
</tr>
<tr>
<td>
<p>7</p>
</td>
<td>
<p>7</p>
</td>
<td>
<p>0111</p>
</td>
</tr>
<tr>
<td>
<p>8</p>
</td>
<td>
<p>8</p>
</td>
<td>
<p>1000</p>
</td>
</tr>
<tr>
<td>
<p>9</p>
</td>
<td>
<p>9</p>
</td>
<td>
<p>1001</p>
</td>
</tr>
<tr>
<td>
<p>10</p>
</td>
<td>
<p>A</p>
</td>
<td>
<p>1010</p>
</td>
</tr>
<tr>
<td>
<p>11</p>
</td>
<td>
<p>B</p>
</td>
<td>
<p>1011</p>
</td>
</tr>
<tr>
<td>
<p>12</p>
</td>
<td>
<p>C</p>
</td>
<td>
<p>1100</p>
</td>
</tr>
<tr>
<td>
<p>13</p>
</td>
<td>
<p>D</p>
</td>
<td>
<p>1101</p>
</td>
</tr>
<tr>
<td>
<p>14</p>
</td>
<td>
<p>E</p>
</td>
<td>
<p>1110</p>
</td>
</tr>
<tr>
<td>
<p>15</p>
</td>
<td>
<p>F</p>
</td>
<td>
<p>1111</p>
</td>
</tr>
</tbody>
</table>
<p>The base 16 numeral 2A8C &nbsp;can be expressed as a sum
of terms for different powers of 16. &nbsp;To express this in terms
of normal&nbsp;base 10 numerals,&nbsp; you have to also convert
individual digits. &nbsp;In particular&nbsp;hexadecimal A means
decimal 10 and hexadecimal C means decimal 12. The full expansion,
with powers increasing from the right, is </p>
<table cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td>
<p>&nbsp;&nbsp;&nbsp; 2</p>
</td>
<td>
<p>&nbsp;&nbsp;&nbsp; A</p>
</td>
<td>
<p>&nbsp;&nbsp;&nbsp; 8</p>
</td>
<td>
<p>&nbsp;&nbsp;&nbsp; C</p>
</td>
<td>&nbsp; 2A8C<br>
</td>
</tr>
<tr>
<td>
<p>2*16<sup>3</sup></p>
</td>
<td>
<p>+ 10*16<sup>2</sup></p>
</td>
<td>
<p>+ 8*16<sup>1</sup></p>
</td>
<td>
<p>+ 12*16<sup>0</sup></p>
</td>
<td>
<p>= 10892</p>
</td>
</tr>
</tbody>
</table>
<p>so using the explicit base subscripts, 2A8C<sub>16</sub>
=
10892<sub>10</sub>.<br>
<br>
In Python the&nbsp;conversion of a number
0 through 15 to a hexadecimal digit character can be expressed many
ways.&nbsp; One clear approach is:</p>
<pre>def digitChar(n):<br> '''return single character for digits with decimal value 0 through 15'''<br> if n &lt; 10:<br> return str(n)<br> if n == 10:<br> return 'A'<br> if n == 11:<br> return 'B'<br> if n == 12:<br> return 'C'<br> if n == 13:<br> return 'D'<br> if n == 14:<br> return 'E'<br> if n == 15:<br> &nbsp;&nbsp;return 'F'</pre>
<p>Notice that the <font face="monospace">digitChar</font>
function
trivially produces the right digit for any&nbsp;number 0, 1, 2, ...
9. &nbsp;<br>
<br>
The conversion above from decimal &nbsp;to base 2
and 10 using division and remainders are very similar, except for
division by the right base. &nbsp;We can make a more general
function
that will work with any base 2 through 16:</p>
<pre>def intToBase(i, base):<br> """Return a string representing the nonnegative integer i<br> in the specified base, from 2 to 16."""<br> i = int(i) # if i is a string, convert to int<br> if i == 0:<br> return '0'<br> numeral = ""<br> while i != 0:<br> digit = i % base<br> numeral = digitChar(digit) + numeral # add next digit on LEFT<br> i = i//base<br> return numeral</pre>
<p>There is one further change in intToBase to accommodate bases
from
11
through 16: &nbsp;Instead of creating a digit character with just
<font face="monospace">str(digit)</font>, <font face="monospace">digitChar(digit)</font>is
needed, as defined above. &nbsp;<br>
<br>
The intToBase function and
several others are include in <a href="http://webpages.cs.luc.edu/~cnaiman/COMP150/nt_examples/bases.py">bases.py</a>
in <a href="http://webpages.cs.luc.edu/~cnaiman/COMP150/nt_examples/pipFiles.zip">pipFiles.zip</a>
file referenced
earlier.&nbsp; It sits in the examples directory for the course
(not in
the Python tutorial
examples).&nbsp; <br>
</p>
<p>Understanding hexadecimal allows interpretation of colors in
web
pages or in Python graphics.&nbsp; The Python graphics module has
the
color_rgb function to generate custom colors based on values for the
red, green and blue components in the range 0 to 255. Integers in this
range can be described by a two place hexadecimal&nbsp;
numeral.&nbsp;
Look at&nbsp; what the color_rgb&nbsp; function actually
produces in
the Python Shell:</p>
<p> <span style="font-family: monospace;">&gt;&gt;&gt;
from graphics
import color_rgb</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&gt;&gt;&gt;
color_rgb(255, 35, 0)</span><br style="font-family: monospace;">
<span style="font-family: monospace;"></span><span style="font-family: monospace;">'#ff2300'</span><br style="font-family: monospace;">
</p>
<p>After the marker '#' that indicates the color is not a
predefined
color name, you see the hexadecimal for each color component, ff, 23,
and 00.&nbsp;The same system of '#' followed by six hexadecimal
characters is used in html source attributes, so you can see and
manipulate custom colors in html, too. <br>
</p>
<p>
Now back to the
easy conversions between binary and hexadecimal, mentioned earlier.
&nbsp;</p>
<h4><a class="mozTocH4" name="binToHex"></a>Converting
Binary to
Hexadecimal</h4>
<p>The basic idea is to convert each 4 bits of a binary numeral
to a
single hexadecimal character. In detail:<br>
Group the binary digits
in 4's, starting from the <i><b>right</b></i>.&nbsp;
Example:</p>
<table cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td colspan="2">
<p align="center">10111100</p>
</td>
<td>
<p>start</p>
</td>
</tr>
<tr>
<td>
<p>1011</p>
</td>
<td>
<p>1100</p>
</td>
<td>
<p>split into groups of 4 bits, starting from the <i><b>right</b></i></p>
</td>
</tr>
<tr>
<td>
<p>8+2+1</p>
</td>
<td>
<p>8+4</p>
</td>
<td>
<p>convert: add powers where there is a 1 bit</p>
</td>
</tr>
<tr>
<td>
<p>11</p>
</td>
<td>
<p align="center">12</p>
</td>
<td>
<p>decimal results</p>
</td>
</tr>
<tr>
<td>
<p>B</p>
</td>
<td>
<p align="center">C</p>
</td>
<td>
<p>convert to hexadecimal digits</p>
</td>
</tr>
<tr>
<td colspan="2">
<p align="center">BC</p>
</td>
<td>
<p>final hexadecimal answer</p>
</td>
</tr>
</tbody>
</table>
<p><br>
A bigger example:</p>
<table cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td colspan="3">
<p align="center">1011110011</p>
</td>
<td>
<p>= <i><u><b>00</b></u></i>1001110011
but <i>NOT</i> 1001110011<i><u><b>00</b></u></i></p>
</td>
</tr>
<tr>
<td>
<p>10</p>
</td>
<td>
<p align="center">1111</p>
</td>
<td>
<p>0011</p>
</td>
<td>
<p>split into groups of 4 bits, starting from the <i><b>right</b></i></p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>8+4+2+1</p>
</td>
<td>
<p>2+1</p>
</td>
<td>
<p>convert groups of bits from binary</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p align="center">15</p>
</td>
<td>
<p>3</p>
</td>
<td>
<p>decimal results</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p align="center">F</p>
</td>
<td>
<p>3</p>
</td>
<td>
<p>convert to 2-digit results to hexadecimal digits</p>
</td>
</tr>
<tr>
<td colspan="3">
<p align="center">2F3</p>
</td>
<td>
<p>final hexadecimal answer</p>
</td>
</tr>
</tbody>
</table>
<p><br>
Now the reverse process:</p>
<h4><a class="mozTocH4" name="hexToBin"></a>Hexadecimal
to Binary</h4>
<table cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td colspan="3">
<p>2F3</p>
</td>
<td>
<p align="left">starting hexadecimal numeral</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>F</p>
</td>
<td>
<p>3</p>
</td>
<td>
<p align="left">hex digits </p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>15</p>
</td>
<td>
<p>3</p>
</td>
<td>
<p align="left">decimal (skip if using table
directly)</p>
</td>
</tr>
<tr>
<td>
<p>0010</p>
</td>
<td>
<p>1111</p>
</td>
<td>
<p>0011</p>
</td>
<td>
<p align="left">binary, <i>padded</i>
to 4 bits</p>
</td>
</tr>
<tr>
<td colspan="3">
<p>001011110011</p>
</td>
<td>
<p align="left">combined</p>
</td>
</tr>
<tr>
<td colspan="3">
<p align="center">1011110011</p>
</td>
<td>
<p align="left">final binary numeral, leading 0's
stripped</p>
</td>
</tr>
</tbody>
</table>
<p><br>
See <a href="http://webpages.cs.luc.edu/~cnaiman/COMP150/nt_examples/bases.py">bases.py</a>
in the examples directory for the course. &nbsp;The hexToBin and
binToHex functions manipulate pieces of strings and use some of the
string methods and string indexing syntax from Chapter 2 of the
Hands-on Python Tutorial.<br>
<br>
If you do not want to do any
arithmetic in converting between binary and hexadecimal, you can use
the decimal/hex/binary table above or run the&nbsp;table() function
in bases.py to produce:</p>
<pre>Dec Hex Bin<br> 0 0 0000<br> 1 1 0001<br> 2 2 0010<br> 3 3 0011<br> 4 4 0100<br> 5 5 0101<br> 6 6 0110<br> 7 7 0111<br> 8 8 1000<br> 9 9 1001<br> 10 A 1010<br> 11 B 1011<br> 12 C 1100<br> 13 D 1101<br> 14 E 1110<br> 15 F 1111</pre>
<p>Instant converter applets at
<a href="http://www.easycalculation.com/hex-converter.php">http://www.easycalculation.com/hex-converter.php</a><br>
<br>
The
same idea works for conversion between binary and base 8, octal.
&nbsp;Octal is used to express some Unix/Linux 3-bit permission
codes. &nbsp; </p>
<h4><a class="mozTocH4" name="formattingBases"></a>Formatting
Binary,
Octal, and Hexadecimal in Python (vid)</h4>
<p>This section relates recent ideas to previous Pythonwork, but
it is
not central to the current ideas.&nbsp; It <span style="font-style: italic;">is useful for testing</span>
simple
results you work on by hand, like those in the next section.</p>
<p>You can generate hexadecimal, octal, and binary numerals in
format
strings in Python using&nbsp;format specifiers 'X', 'o', and
'b'&nbsp;
(letter o, for octal, not the number 0). &nbsp;Like the syntax for
float formatting, the base formatting may be used in the format
function or after a colon inside&nbsp;braces in the string format
method:<br>
<br>
<font face="monospace">&gt;&gt;&gt; 'binary:',
format(27,
'b')<br>
</font><font face="monospace">'binary:
11011'</font><br>
<font face="monospace">&gt;&gt;&gt; 'decimal:
{0}, hex: {0:X}, octal:
{0:o}, binary:
{0:b}'.format(27)</font><br>
<font face="monospace">'decimal: 27, hex: 1B, octal:
33, binary: 11011'<br>
</font><font face="monospace"><br>
</font><font face="Times New Roman, serif">Also
Python recognizes binary, octal, and hexadecimal numeric literals.
&nbsp;The literals start with 0 followed by the specifiers b, o
(letter
o), or
X, and then digits appropriate for the base.&nbsp; <br>
</font></p>
<p><font face="monospace">&gt;&gt;&gt; 0b</font><font face="monospace">11011</font><br>
<font face="monospace">27</font><br>
<font face="monospace">&gt;&gt;&gt; 0X</font><font face="monospace">1B</font><br>
<font face="monospace">27</font><br>
<br>
<font face="Times New Roman, serif">The built-in functions
<span style="font-weight: bold;">hex</span>, <span style="font-weight: bold;">oct</span>, and <span style="font-weight: bold;">bin</span> generate strings
with these
notations:</font></p>
<p><font face="monospace">&gt;&gt;&gt;
bin(27)<br>
'0b</font><font face="monospace">11011'</font><br>
<font face="monospace">&gt;&gt;&gt; hex(27)<br>
'</font><font face="monospace">0x</font><font face="monospace">1b'</font></p>
<h4>Sample Binary/Hexadecimal Converson Problems<br>
</h4>
<p>Conversions to do <span style="font-style: italic;">by
hand</span>
to check understanding: &nbsp; (You can confirm with
Python.)&nbsp; <br>
</p>
<ol>
<li>10111 binary to decimal</li>
<li>87 decimal to binary</li>
<li>10011011011 binary to hexadecimal (short way)</li>
<li>3AF hexadeciml to binary (short way)</li>
<li>Python/html graphics color '#a150ff' would be returned by
what
call to the color_rgb function with decimal number parameters?<br>
</li>
</ol>
<h2><a name="Pip"></a>Pip
Assembler (vid)</h2>
<p>As the beginning of the Hands-on Tutorial indicated, computer
hardward does not execute Python directly. &nbsp;Python and other
high level langages must be converted to the very simple set of
instructions that are directly built into the computer hardware, the
<i>machine language</i>. &nbsp;This is the first place
we look
underneath high level languages.</p>
<p>As we will see more in the gates unit, the state inside a
computer
is usually electrical, and the most dependable system uses voltages,
either high or 0 (grounded) . &nbsp;This means <i>two</i>
possibilities. &nbsp;This is a <i>bit</i> of
information, the
smallest possible amount. &nbsp;We will arbitrarily refer to the
two
states as 0 and 1. &nbsp;This is convenient for the binary number
system!</p>
<p>Computers have a <span style="font-style: italic;">Central
Processing Unit </span>(<span style="font-weight: bold;">CPU</span>)
connected by wires
to a memory unit. &nbsp;Operations take place inside the CPU, with
some data maybe transfered in from memory or sent back to memory (and
also external devices, though we will skip that part in our simple
model).</p>
<p>Like in a Python string or list, memory is referenced by
integer
locations,
0, 1, 2, .... &nbsp;There are several design decisions:
&nbsp;one is
how much data to put in a single memory cell that can be individually
referenced. &nbsp;A common unit is a <span style="font-style: italic;">byte</span>
= 8 bits. &nbsp;Pip uses a
byte, as do the common processors used in Windows machines (and the
latest Macs). &nbsp;While a bit has two possible states, a byte has
2<sup>8</sup> = 256 states. &nbsp;Another choice is how
big to allow
memory to be. &nbsp;So that one byte can used to refer to any cell
in
&nbsp;the memory or our simulated machine, we will assume memory
consists of no more than 256 cells (a very limited machine!).</p>
<p>A concept encouraged by Von Neumann in the 1940's was to
encode the
instructions as a form of
data in the computer.&nbsp; Before
this approach, changing the program in a computer involved physically
rewiring the computer!&nbsp; With Von Neumann's approach, an
instruction would be represented as a number in the computer's
memory.&nbsp; Hence an instructionmust be a sequence of 0's
and 1's, like </p>
<p>00010100 00000100 &nbsp;</p>
<p>I introduce the space in the middle only to delineate
individual
bytes.&nbsp;&nbsp; &nbsp;</p>
<p>Since accessing memory is slower than internal operations in
the
CPU, all CPU's have places for special data to be stored inside of
them. &nbsp;One is an Instruction Pointer (<span style="font-weight: bold;">IP</span>), saying where in
memory the next instruction starts. &nbsp;CPU's also have one or
more
fast temporary data storage locations, called <span style="font-style: italic;">registers</span>.
&nbsp;I
follow the simple example in a text we used to use, the Analytical
Engine, which has&nbsp;a single such location, called the <span style="font-style: italic;">Accumulator</span>
or <span style="font-weight: bold;">Acc</span> for
short, that holds a
byte of information, just like a
memory cell. &nbsp;</p>
<h3><a class="mozTocH3" name="pipSim"></a>Pip
Assembler Simulator (vid)<br>
</h3>
<p>For a simple conceptual view, look at the Pip Assembler
simulator
in the class web examples. &nbsp;All files are included in
<a href="http://webpages.cs.luc.edu/~cnaiman/COMP150/nt_examples/pipFiles.zip">pipFiles.zip</a>.
&nbsp;Use a
flash drive if you are on a lab computer!&nbsp; <br>
<br>
The zip archive contains the files needed for the
Pip Assembler Simulator:&nbsp; pipGUI.py, pipText.py, pip.py,
pipHelp.py, hexBin.py, and sample program files,&nbsp;
simple.bin,&nbsp;simple.asm, arith.asm,&nbsp;sum2n.asm,
ifElse.asm.
&nbsp;
</p>
<p>The main program is pipGUI.py.&nbsp; Run it from the
operating
system.&nbsp; In Windows that generally just involves double
clicking
on it the file window. &nbsp;(<span style="font-weight: bold;">No
need to be in Idle -</span> you will not be messing with the
code.)&nbsp;
In the Mac, you can run it from IDLE; alternatively, open a terminal
window and type pthon3 pipGui.py.&nbsp; (Right0-clicking and running
from the python launcher doesn't always work correctly.)<br>
</p>
<p>You
will see a graphical Window. &nbsp;Click on the purple button that
says
BINARY, to see its 'native' state.&nbsp; Look at the window as its
various parts are described:<br>
</p>
<p>The state of the simulated computer is shown in the CPU (lower
left) with its accumulator (Acc) and Instruction Pointer (IP).
&nbsp;The
middle blue and right yellow blocks display memory. &nbsp;</p>
<p>First focus on the big middle blue rectangle labeled CODE.
&nbsp;Instruction code in&nbsp;Pip&nbsp;is placed at the
beginning of
memory. &nbsp;Each instruction takes up two bytes, so for
convenience
bytes are shown in pairs down&nbsp;the right portion of the main
blue
rectangle. &nbsp; We will need to keep track of the locations of
these instructions, so the left column in the &nbsp;blue rectangle
shows the address (in decimal) of the beginning of each instruction.
&nbsp;Beside the decimal address label is the same address in
binary.
&nbsp;Because each instruction is two bytes, the address labels
advance by 2's.</p>
<p>Now look at the right yellow rectangle labeled DATA.
&nbsp;For
simplicity of display, we arbitrarily assume that the data for program
variables is stored in the second half of memory, starting at address
128. &nbsp;Each individual byte is a separate piece of data, so we
show only one per line, at the right. &nbsp;For our simple programs
we will never need more than 8 variables, so only eight locations are
displayed. &nbsp;As in the code section, address labels in decimal
and binary are shown. </p>
<p>The remaining parts of the display are for controlling the
simulator. &nbsp;They do not correspond to parts of Pip.
&nbsp;The
left column of buttons and text boxes is labeled COMMANDS.
&nbsp;You
should have already clicked on the command button labeled
BINARY.&nbsp;</p>
<p>&nbsp;Let us load a machine language program into Pip.
Make sure
you have downloaded simple.bin. &nbsp;You can open it in the Idle
editor, to see the file format, if you like. &nbsp;It contains five
binary instructions. &nbsp;</p>
<p>Type simple.bin into the Filename text box. &nbsp;Then
click LOAD.
&nbsp;The contents of the file appear as the first five
instructions
in Pip.</p>
<h3><a class="mozTocH3" name="machineLang"></a>An
Introduction to
Pip Machine Language (vid)<br>
</h3>
<p>All Pip instructions use the Accumulator. &nbsp;It is
always a
source of data and/or the destination of a result. &nbsp;There are
two other ways Pip refers to data. &nbsp;One is to have the actual
data encoded as the second byte of the instruction. &nbsp;The more
common way is to refer to a location in memory. &nbsp;In this case
the second byte is interpreted as the address in memory where the
data resides. &nbsp; That explains the second byte, so now the
first
byte. &nbsp;It can be logically split into two four bit fields, for
example</p>
<p><b>0001 0100</b> 00000100 &nbsp;</p>
<p>In Pip we will have fewer than 16 basic operations, which are
encoded in the second four bits. &nbsp;</p>
<p>0001 <b>0100</b> 00000100 &nbsp;</p>
<p>The <b>0100</b> of this example means load a
value into the
accumulator. &nbsp;We must distinguish where to get the value from,
either the second byte of the instruction or a specified address in
memory. &nbsp;The first 4 bits (actually only 1 bit is needed)
determine this. &nbsp;The code is that 0000 means&nbsp;a memory
address and 0001 means the actual data is in the second byte of the
instruction. &nbsp;That latter is the case above, where the second
byte is 00000100 or 4 in decimal, so the full meaning of the
instruction is load the value in the second byte (4) into the
accumulator.</p>
<p>Look at the Simulator screen. &nbsp;See that the
accumulator (ACC)
has a value of 0. &nbsp;The instruction pointer (IP) shows the next
instruction to execute. &nbsp;It is also 0. &nbsp;If you look
at
address 0 in the simulator you see the instruction we have been
discussing. &nbsp;Also note that the binary version of the address
0
in the code it highlighted in orange. &nbsp;To more easily follow
what is going on, it will always match IP.&nbsp; Click STEP.
&nbsp;
IP and the corresponding highlight should advance to 2, and the value
in the accumulator should become 00000100 (or 4 in decimal).</p>
<p>One more machine language instruction, the one at address 2:</p>
<p>00000101 10000000&nbsp; &nbsp;&nbsp;</p>
<p>or to look at the parts:</p>
<p>0000 0101 10000000&nbsp; &nbsp;&nbsp;</p>
<p>The second four bits 0101 determine the type of instruction.
&nbsp;In
this case it is "store the contents of the accumulator to an
address in memory". &nbsp;The second byte gives the address
10000000 (or 128 decimal). &nbsp;For the Store instruction the
second
byte only makes sense as an address in memory, and the first four
bits of the instruction, 0000, reflect this. &nbsp; Hence the full
instruction says to store the accumulator value at memory location
128.</p>
<p>Click STEP again. &nbsp;Look at memory location 128 (or
10000000
in binary). &nbsp;Also note IP in the CPU.</p>
<p>We could continue, but this gets tedious. &nbsp;Reading
this
binary is a pain. &nbsp;One of the first programs people wrote was
an
<span style="font-style: italic;">assembler</span>,
which translates
something a bit more human readable into
this binary code. &nbsp;In the assember written for this machine,
the
first two instructions discussed could be written</p>
<p>LOD #4<br>
STO 128</p>
<p>Still not English or as close as Python but closer!
&nbsp;In place
of the second four bit pattern we have a three letter mnemonic.
&nbsp;LOD
is close to LOAD. &nbsp;STO is the beginning of STORE.
&nbsp;The
pound sign is sometimes used to mean 'number'. &nbsp;The first
instruction says to load the number 4. &nbsp;The second instruction
does not have the '#'. &nbsp;This means the other interpretation of
the second byte is used: &nbsp;it refers to a memory location.
&nbsp;Be
mindful of the presence or absence of '#'! &nbsp;It is easy to make
a
mistake.</p>
<p>Click the button NONE under commands. &nbsp;Now you see
the
instructions stated in assembler and all the address labels in
decimal.</p>
<p>We will come back to machine language briefly at the end of
our
discussion of this simple CPU, but for
the most part we will code things in assembler.</p>
<p>The next instruction is LOD #3. &nbsp;From the earlier
examples
you should be able to figure out what that does. &nbsp;Click STEP
to
check. &nbsp;The next instruction is ADD 128. &nbsp;It should
be no
surprise that this involves addition, and from the format you should
see that it involves memory location 128. &nbsp;We need two things
to
add. &nbsp;Memory location 128 is one obvious operand.
&nbsp;The
accumulator is also available. So the instruction adds the
accumulator and memory location 128. &nbsp;The final issue is where
to put the result. &nbsp;Fancier CPU's than Pip have more options,
but in Pip all results go to the accumulator, except in the STOre
instruction where a value is copied FROM the accumulator.
&nbsp;Hence
the sum of the accumulator and memory location 128 are stored back
into the accumulator.</p>
<p>Click STEP to check.</p>
<p>You <i>can</i> put the result of an addition or
any other
operation into memory: &nbsp;It just takes an extra step.
&nbsp;Guess
what the next instruction STO 129 does. &nbsp;Click STEP and check.</p>
<p>Next is the HLT instruction, short for HALT. &nbsp;Click
STEP and
the program stops (indicated on the screen by '- -' as the instruction
pointer.<br>
</p>
<p>Click INIT. &nbsp;This resets IP and ACC to 0.
&nbsp;You could
step through the program again, or to see the result, just click RUN,
and it goes (up to 100 steps) to the end.</p>
<p>In Python and other higher level languages we also store data
in
memory. &nbsp;We&nbsp;refer to the data by <i>name</i>,
not number.
&nbsp;Using names is easier. &nbsp;The assembler can also
handle
that. &nbsp;Click the button DATA under labels. Every place we had
address 128 before, we now have W, and every place we had address
129, we now have X. &nbsp;In this case the machine code was
disassembled (from machine code to assembler code). &nbsp;The
machine
code did not include names, so the simulator fakes it, and always
uses the names you see in the DATA section labels, W, X, Y, Z, T1-4.
&nbsp;(These names have no particular significance: &nbsp;they
are&nbsp;the names used by&nbsp; the old Analytical Engine.)
&nbsp;If
you load a file with variable names, including ones different than W,
X, ..., then pipGUI remembers them and uses them instead.
&nbsp;(The
only restriction for the display is that they cannot be more than 8
characters long.)&nbsp; In Python, variable names always are linked
to
data in memory.&nbsp; In the Pip Assembler Simulator, the
relationship
is very simple and graphic!<br>
</p>
<h3><a class="mozTocH3" name="morePipSim"></a>More
on the Simulator
and Pip (vid)<br>
</h3>
<p>Click HELP. &nbsp;See the message at the bottom.
&nbsp;This gives
context sensitive help. &nbsp;First click on HELP again for a
summary. &nbsp;This shows all the help for the simulator
operations.
&nbsp;Return to here if you have questions. &nbsp;It covers the
command buttons, the comment area at the bottom, the close button,
and it mentions how to get an assembler summary: &nbsp;</p>
<p>Click the HELP button and then click in the blue CODE area.
&nbsp;Try
that now. &nbsp;For reference, the contents of this window are
shown
below:</p>
<pre>Pip Assembler Summary<br> Symbols Used<br> X for a symbolic or numeric data address.<br> #N for a literal number N as data<br> Acc refers to the accumulator<br> L refers to a symbolic code label or numeric code address<br> Instructions Pseudo Python syntax for what happens<br> Data Flow<br> LOD X (or #N) Acc = X (or N)<br> STO X X = Acc (copy Acc to location X)<br> Control<br> JMP L IP = L (go to instruction L)<br> JMZ L if Acc==0: IP = L else: IP = IP+2 (normal)<br> NOP No operation; just go to next instruction<br> HLT Halt execution<br> Arithmetic-Logic<br> ADD X (or #N) Acc = Acc + X (or N)<br> SUB X (or #N) Acc = Acc - X (or N)<br> MUL X (or #N) Acc = Acc * X (or N)<br> DIV X (or #N) Acc = Acc / X (or N)<br> AND X (or #N) if Acc != 0 and X != 0: Acc=1 else: Acc=0<br> NOT if Acc == 0: Acc = 1 else: Acc = 0<br> CPZ X if X == 0: Acc = 1 else: Acc = 0<br> CPL X if X &lt; 0: Acc = 1 else: Acc = 0<br> In source files: An instruction may be preceded by a label<br> and a colon. Any line may end with a comment. A comment<br> starts with ';' and extend to the end of the line.</pre>
<p>We will gradually introduce the 14 instructions and the
assembler
syntax conventions.</p>
<h3><a class="mozTocH3" name="mozTocId204461"></a><a name="Pip1"></a>Format
of My Pip Assembler (vid)<br>
</h3>
<p>See arith.asm from the pipFiles:<br>
<span style="font-family: monospace;">&nbsp;</span><font face="monospace"><br>
&nbsp; </font><span style="font-family: monospace;"></span><font face="monospace">LOD #7 &nbsp; ; acc = 7 &nbsp;
initialize variables<br>
&nbsp; STO W &nbsp;&nbsp; ; W = acc &nbsp;<br>
&nbsp;
LOD #3 &nbsp; ; acc = 3<br>
&nbsp; STO X &nbsp;&nbsp; ; X = acc &nbsp;<br>
&nbsp;
LOD #6 &nbsp; ; acc = 8<br>
&nbsp; STO Y &nbsp;&nbsp; ; Y = acc<br>
&nbsp;<br>
&nbsp;
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;; Z =&nbsp;(W
+ X) * Y / 2<br>
&nbsp;
LOD W &nbsp;&nbsp; ; acc = W &nbsp;&nbsp;&nbsp;</font><br>
<font face="monospace">&nbsp;
ADD X &nbsp;&nbsp; ;&nbsp;acc = acc + X ( = W+X )
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;</font><br>
<font face="monospace">&nbsp; MUL Y
&nbsp;&nbsp; ;
acc = acc * Y ( = (W+X)*Y ) &nbsp; &nbsp;</font><br>
<font face="monospace">&nbsp;
DIV #2&nbsp;&nbsp; ; acc&nbsp;= acc/2&nbsp;( =
(W+X)*Y/2
)</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;<br>
<font face="monospace">&nbsp; STO Z
&nbsp;&nbsp; ; Z = acc
&nbsp;( = (W+X)*Y/2 )</font><br>
<font face="monospace">&nbsp;
HLT&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font></p>
<p>Human comments are allowed starting with a ';' (same idea as
the
'#' in&nbsp;Python, but # is already used in Pip assembler.)
&nbsp;In
the example the comments are a very direct translation into pseudo
Python. &nbsp;I use&nbsp;symbolic data names.&nbsp;</p>
<p>Load arith.asm into pipGUI by typing in the name under
filename, and clicking LOAD.&nbsp; You should see the code, minus
comments. &nbsp;</p>
<p>If you switch your view to the text console (what would appear
in
the&nbsp;Python Shell &nbsp;in Idle) at any point, you will see
that
the computer is showing you the results of playing computer:
&nbsp;A
full history is kept. &nbsp;(I will expect you to show your
understand sequences of Pip instructions by playing computer, and
this text history shows you exactly what you should be able to
generate! &nbsp;You can write your own examples and test
yourself.)<br>
<br>
When the program has halted, press INIT to
reinitialize the CPU. &nbsp;By hand edit some of the LOD
instructions
that initialize the values of W, X, and Y. &nbsp;You could STEP
through
to see one
line at a time execute. &nbsp;If you merely want to see the final
result, just press RUN, and the program runs up to 100 steps or until
it halts. &nbsp;If you look at the text window, you see the whole
history.<br>
</p>
<h3><a name="Assignment_Translation_Applet"></a>Assignment
Translation
Applet Introduction (vid)</h3>
So you can come back to these instructions easily,&nbsp;in a <span style="font-style: italic; font-weight: bold;">separate tab</span>
open the <a href="http://www.course.com/downloads/computerscience/aeonline/6/3/index.html">assignment
statement translation applet</a>.&nbsp;
You are likely to get several pop-up windows depending on your security
settings.&nbsp; Approve running the applet even though the browse
cannot confirm its security certificate.&nbsp; This applet was
unfortunately compiled under an old version of Java, and the current
Java interpreters restrict what you can do with it.&nbsp; In
particular
you should not be able to save data to a file from inside the applet.<br>
<br>
This is a nice applet from the Analytical Engine for analyzing
expressions like Z = (W+X) * Y
/ 2, the then translating them into Pip assembler. &nbsp;For
simplicity, the applet only allows
variables W, X, Y, and Z (ignoring case).&nbsp; <br>
<br>
Start on the instructions on the web page that come after the
applet:&nbsp; Do Step 1, and 2. An initial algorithm before
translation
to assembler, is to analyse the order of operations using the
precedence of the operations, by <span style="font-style: italic;">parsing</span>.
&nbsp;The applet should generate a graphical representaton showing
a
tree of operations after parsing leading down to the final assignment
at the bottom. <br>
<br>
Now continue from Step 3 in the instructions for using the applet,
going
through the steps explained there, and doing the exercises at the
bottom. &nbsp;Note that not all examples are as straightforward as
the
first one, which just does binary operations with the accumulator.<span class="Apple-style-span" style="border-collapse: separate; color: rgb(0, 0, 0); font-family: &#39;Times New Roman&#39;; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: 2; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; font-size: medium;"><span class="Apple-style-span" style="color: rgb(204, 51, 204); font-family: monospace;">&nbsp;
</span></span>Some
expressions, like
the one in Step 5, require several intermediate parts to be remembered.
&nbsp;The convention in this applet is to use variables T1 - T4 as
<span style="font-style: italic;">temporary</span>
variables hold such
results. &nbsp;An even shorter expression
needing a temporary variable T1 is&nbsp; <br>
Z=W/(X+Y)<br>
...<br>
<br>
Translating
expressions yourself, by hand, from a Python-like assignment statement
to assembler, is a basic way to learn to use Pip (and
is likely to be <span style="font-style: italic;">tested</span>).
&nbsp;Ths applet allows you to make up your
own problems and test yourself!<br>
<h3><a class="mozTocH3" name="Loops_AddressLabels"></a>Loops
and
Symbolic
Address Labels</h3>
<p>Consider two ways to sum&nbsp;from 1 to n in Python:</p>
<p><font face="monospace">sum = 0<br>
i = 1<br>
while i &lt;= n:<br>
&nbsp;&nbsp;&nbsp;
sum = sum + i<br>
&nbsp;&nbsp;&nbsp; i = i+1</font> </p>
<p>In assembler it is easier to sum from n down to 1, so the test
is
a comparison to 0:</p>
<p><font face="monospace">sum = 0<br>
while n != 0:<br>
&nbsp;&nbsp;&nbsp;
sum = sum + n<br>
&nbsp;&nbsp;&nbsp; n = n-1</font> </p>
<p>For a loop you need to change the order of execution.
&nbsp;There
is not a WHILE in Pip assembler: &nbsp;There are only the low level
instructions JMP and JMZ. &nbsp;The essence of this section is
seeing
how to use JMP and JMZ to accomplish the same things as Python's
<font face="monospace">while</font> and <font face="monospace">if-else</font>
statements.&nbsp;</p>
<p>For example<br>
&nbsp; &nbsp; JMP 12 &nbsp;<br>
means jump to the
instruction at address 12. &nbsp;in other words,&nbsp;set IP to
12,
rather than advancing IP by 2, like usual.</p>
<p>JMZ (<b>J</b>u<b>m</b>p if <b>z</b>ero)&nbsp;
is a <i>conditional</i>
jump. &nbsp;For example<br>
&nbsp; &nbsp; JMZ 20<br>
means jump to
address 20 <i>if</i> the accumulator is zero.
&nbsp;Otherwise go on
to the next instruction normally. &nbsp;In Pythonesque pseudo code:<br>
&nbsp;
&nbsp; if acc == 0:<br>
&nbsp; &nbsp; &nbsp; &nbsp; IP = 20<br>
&nbsp;
&nbsp; else:<br>
&nbsp; &nbsp; &nbsp; &nbsp; IP = IP + 2 # the usual
case</p>
<p>Both these instructions are needed to translate the Python
while
loops above: &nbsp;This is the first time in the assembler examples
that the exact instruction locations are important, so I show the
addresses on the left. &nbsp;My assembler allows you to enter
optional numeric address labels followed by a colon before any
instruction (as long as you give the memory address accurately):</p>
<p><font face="monospace">0: &nbsp;&nbsp;
LOD #4&nbsp;&nbsp;&nbsp; ;
n = 4&nbsp; # high level for
comparison</font><br>
<font face="monospace">2:
&nbsp;&nbsp; STO
n&nbsp;&nbsp;&nbsp;&nbsp; </font><br>
<font face="monospace">4:
&nbsp;&nbsp; LOD #0&nbsp;&nbsp;&nbsp; ; sum =
0</font><br>
<font face="monospace">6:
&nbsp;&nbsp; STO
sum&nbsp;&nbsp; </font><br>
<font face="monospace">8:&nbsp;
&nbsp; LOD n&nbsp;&nbsp;&nbsp;&nbsp; ; while n != 0:</font><br>
<font face="monospace">10:&nbsp;&nbsp;
JMZ 24
&nbsp;&nbsp; </font><br>
<font face="monospace">12:&nbsp;&nbsp;
ADD sum&nbsp;&nbsp; ;&nbsp;&nbsp;&nbsp;&nbsp;
sum&nbsp;= sum +
n</font><br>
<font face="monospace">14:
&nbsp; STO
sum&nbsp;&nbsp; </font><br>
<font face="monospace">16:
&nbsp; LOD n&nbsp;&nbsp;&nbsp;&nbsp;
;&nbsp;&nbsp;&nbsp;&nbsp; n&nbsp;=
n - 1</font><br>
<font face="monospace">18: &nbsp;
SUB
#1&nbsp;&nbsp;&nbsp; </font><br>
<font face="monospace">20:
&nbsp; STO
n&nbsp;&nbsp;&nbsp;&nbsp; </font><br>
<font face="monospace">22:
&nbsp; JMP 8
&nbsp;&nbsp;&nbsp; <br>
24:
&nbsp; LOD sum&nbsp;&nbsp; ; # for easy display - result in
accumulator</font><br>
<font face="monospace">26:
&nbsp;
HLT&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br>
</font></p>
<p>As with the data addresses considered earlier, we are writing
<i>numerical</i> addresses rather than meaningful <i>names</i>.
&nbsp;This
is also particularly awkward if you insert a new instruction and
change a bunch of addresses.&nbsp; An better alternative is <span style="font-style: italic;">symbolic</span> address
labels.&nbsp; The
previous code with numerical addresses for jumps above is slightly
modified below to have symbolic code address labels. &nbsp;The code
is&nbsp;sum2n.asm in pipFiles: &nbsp;
</p>
<p><font face="monospace">&nbsp;&nbsp;
&nbsp;&nbsp; LOD
#4&nbsp;&nbsp;&nbsp; ;
n = 4&nbsp; # high level for
comparison</font><br>
<font face="monospace">&nbsp;&nbsp;
&nbsp;&nbsp; STO
n&nbsp;&nbsp;&nbsp;&nbsp; </font><br>
<font face="monospace">&nbsp;&nbsp;
&nbsp;&nbsp; LOD #0&nbsp;&nbsp;&nbsp; ; sum =
0</font><br>
<font face="monospace">&nbsp;&nbsp;
&nbsp;&nbsp; STO
sum <br>
</font><font face="monospace">LOOP: LOD
n&nbsp;&nbsp;&nbsp;&nbsp; ;
while n != 0:</font><br>
<font face="monospace">&nbsp;&nbsp;
&nbsp;&nbsp;
JMZ DONE
&nbsp; </font><br>
<font face="monospace">&nbsp;&nbsp;&nbsp;
&nbsp;
ADD sum&nbsp;&nbsp; ;&nbsp;&nbsp;&nbsp;&nbsp;
sum&nbsp;= sum +
n</font><br>
<font face="monospace">&nbsp;&nbsp;&nbsp;
&nbsp; STO
sum&nbsp;&nbsp; </font><br>
<font face="monospace">&nbsp;&nbsp;&nbsp;
&nbsp; LOD n&nbsp;&nbsp;&nbsp;&nbsp;
;&nbsp;&nbsp;&nbsp;&nbsp; n&nbsp;=
n - 1</font><br>
<font face="monospace">&nbsp;&nbsp;&nbsp;
&nbsp;
SUB
#1&nbsp;&nbsp;&nbsp; </font><br>
<font face="monospace">&nbsp;&nbsp;&nbsp;
&nbsp; STO
n&nbsp;&nbsp;&nbsp;&nbsp; </font><br>
<font face="monospace">&nbsp;&nbsp;&nbsp;
&nbsp; JMP LOOP
&nbsp;&nbsp; <br>
DONE: LOD sum&nbsp;&nbsp; ; # for easy display - result in
accumulator</font><br>
<font face="monospace">&nbsp;&nbsp;&nbsp;
&nbsp;
HLT&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br>
</font></p>
<p>PipGUI&nbsp;allows symbolic names up to 8 characters long,
followed
by a colon, to be
placed before an instruction that is a jump <span style="font-style: italic;">target</span>, and then
the same
name can be used in the JMP or JMZ <span style="font-style: italic;">instruction</span>.
&nbsp;In the code
above LOOP is both an instruction label and the target in the JMP
instruction. &nbsp;DONE is both a label and the target in the JMZ
instruction. &nbsp;The while loop syntax is certainly clearer, but
it
an easily automated step in a compiler to switch to the low-level
version, so you do not have to worry about it in a Python program!
&nbsp;Unlike with Python, the indentation I show for sum2n.asm is
not
significant to the assembler. &nbsp;It is merely my convention for
easy reading by humans.</p>
<p>If you want to see numeric code addresses in the simulator,
you
can press the DATA button under LABELS to see only data labels, but
not the code labels that I (and all real assemblers) allow.
&nbsp;In
that view you see the <font face="monospace">LOD n</font>
instruction
is at address 8, and the JMP instruction has operand 8.
&nbsp;Similarly
DONE is replaced with 24 in both places it appeared.&nbsp; The
assembler is smart enough to
count statements to determine correct addresses and to use those
numbers
to translate symbolic address labels.&nbsp; <br>
</p>
<p>Next step
through the program and make sure everything makes sense. &nbsp;The
new features here are the jumps. &nbsp;I WILL ask you to play
computer on paper on a test to follow such a program. &nbsp;With
the
simulator, you can check yourself by following as you single step or
by looking at the history that pipGui records in the text
window.&nbsp;
After running sum2n.asm, here is the log:</p>
<span style="font-family: monospace;"></span><span style="font-family: monospace;"></span><span style="font-family: monospace;">------ CPU initialized from
sum2n.asm
---------</span><br style="font-family: monospace;">
<span style="font-family: monospace;">IP--&gt;&nbsp;
ACC&nbsp;&nbsp;&nbsp; n&nbsp; sum</span><br style="font-family: monospace;">
<span style="font-family: monospace;">--|
0&nbsp;&nbsp;&nbsp;
0&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp; 0</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;0|
2&nbsp;&nbsp;&nbsp;
4&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp;&nbsp; 0</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;2|
4&nbsp;&nbsp;&nbsp;
4&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp; 0</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;4|
6&nbsp;&nbsp;&nbsp;
0&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp; 0</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;6|
8&nbsp;&nbsp;&nbsp;
0&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp; 0</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;8|10&nbsp;&nbsp;&nbsp;
4&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp; 0</span><br style="font-family: monospace;">
<span style="font-family: monospace;">10|12&nbsp;&nbsp;&nbsp;
4&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp; 0</span><br style="font-family: monospace;">
<span style="font-family: monospace;">12|14&nbsp;&nbsp;&nbsp;
4&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp; 0</span><br style="font-family: monospace;">
<span style="font-family: monospace;">14|16&nbsp;&nbsp;&nbsp;
4&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp; 4</span><br style="font-family: monospace;">
<span style="font-family: monospace;">16|18&nbsp;&nbsp;&nbsp;
4&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp; 4</span><br style="font-family: monospace;">
<span style="font-family: monospace;">18|20&nbsp;&nbsp;&nbsp;
3&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp; 4</span><br style="font-family: monospace;">
<span style="font-family: monospace;">20|22&nbsp;&nbsp;&nbsp;
3&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp; 4</span><br style="font-family: monospace;">
<span style="font-family: monospace;">22|
8&nbsp;&nbsp;&nbsp;
3&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp; 4</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;8|10&nbsp;&nbsp;&nbsp;
3&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp; 4</span><br style="font-family: monospace;">
<span style="font-family: monospace;">10|12&nbsp;&nbsp;&nbsp;
3&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp; 4</span><br style="font-family: monospace;">
<span style="font-family: monospace;">12|14&nbsp;&nbsp;&nbsp;
7&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp; 4</span><br style="font-family: monospace;">
<span style="font-family: monospace;">14|16&nbsp;&nbsp;&nbsp;
7&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp; 7</span><br style="font-family: monospace;">
<span style="font-family: monospace;">16|18&nbsp;&nbsp;&nbsp;
3&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp; 7</span><br style="font-family: monospace;">
<span style="font-family: monospace;">18|20&nbsp;&nbsp;&nbsp;
2&nbsp;&nbsp;&nbsp; 3&nbsp;&nbsp;&nbsp; 7</span><br style="font-family: monospace;">
<span style="font-family: monospace;">20|22&nbsp;&nbsp;&nbsp;
2&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp; 7</span><br style="font-family: monospace;">
<span style="font-family: monospace;">22|
8&nbsp;&nbsp;&nbsp;
2&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp; 7</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;8|10&nbsp;&nbsp;&nbsp;
2&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp; 7</span><br style="font-family: monospace;">
<span style="font-family: monospace;">10|12&nbsp;&nbsp;&nbsp;
2&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp; 7</span><br style="font-family: monospace;">
<span style="font-family: monospace;">12|14&nbsp;&nbsp;&nbsp;
9&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp; 7</span><br style="font-family: monospace;">
<span style="font-family: monospace;">14|16&nbsp;&nbsp;&nbsp;
9&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp; 9</span><br style="font-family: monospace;">
<span style="font-family: monospace;">16|18&nbsp;&nbsp;&nbsp;
2&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp; 9</span><br style="font-family: monospace;">
<span style="font-family: monospace;">18|20&nbsp;&nbsp;&nbsp;
1&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp; 9</span><br style="font-family: monospace;">
<span style="font-family: monospace;">20|22&nbsp;&nbsp;&nbsp;
1&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp;&nbsp; 9</span><br style="font-family: monospace;">
<span style="font-family: monospace;">22|
8&nbsp;&nbsp;&nbsp;
1&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp;&nbsp; 9</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;8|10&nbsp;&nbsp;&nbsp;
1&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp;&nbsp; 9</span><br style="font-family: monospace;">
<span style="font-family: monospace;">10|12&nbsp;&nbsp;&nbsp;
1&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp;&nbsp; 9</span><br style="font-family: monospace;">
<span style="font-family: monospace;">12|14&nbsp;&nbsp;
10&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp;&nbsp; 9</span><br style="font-family: monospace;">
<span style="font-family: monospace;">14|16&nbsp;&nbsp;
10&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp; 10</span><br style="font-family: monospace;">
<span style="font-family: monospace;">16|18&nbsp;&nbsp;&nbsp;
1&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp; 10</span><br style="font-family: monospace;">
<span style="font-family: monospace;">18|20&nbsp;&nbsp;&nbsp;
0&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp; 10</span><br style="font-family: monospace;">
<span style="font-family: monospace;">20|22&nbsp;&nbsp;&nbsp;
0&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp; 10</span><br style="font-family: monospace;">
<span style="font-family: monospace;">22|
8&nbsp;&nbsp;&nbsp;
0&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp; 10</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;8|10&nbsp;&nbsp;&nbsp;
0&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp; 10</span><br style="font-family: monospace;">
<span style="font-family: monospace;">10|24&nbsp;&nbsp;&nbsp;
0&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp; 10</span><br style="font-family: monospace;">
<span style="font-family: monospace;">24|26&nbsp;&nbsp;
10&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp; 10</span><br style="font-family: monospace;">
<span style="font-family: monospace;">26|--&nbsp;&nbsp;
10&nbsp;&nbsp;&nbsp; 0&nbsp;&nbsp; 10</span><br style="font-family: monospace;">
<br style="font-family: monospace;">
The first column is like the line number when playing computer in
Python.&nbsp; It gives the Instruction Pointer (IP) value for the
instruction executed.&nbsp; The heading shows
IP--&gt;.&nbsp; The
--&gt;&nbsp; is supposed to repesent an arrow showing what the
IP value
will become as a result fo the instruction (shown in the second
column).&nbsp; By this inclusion I emphasize that next IP value is
a
part of the calulation when an instruction is executed.&nbsp; It is
only of note when there is a jump.&nbsp; Most of the time it is
just
two more than the left column.&nbsp; To the right there are columns
for
the value in the accumulator and all the memory variables that are
referred to. As when we played computer with Python, they show values
after the instruction in the left column is executed.&nbsp; <br>
<br>
Make sure you can play computer, and confirm your results by looking at
logs like this.<br>
<h4><a style="font-family: monospace;" class="mozTocH4" name="pipJumps"></a>More
Practice Using
jumps</h4>
<p>1. &nbsp;Absolute value,&nbsp;in Python: &nbsp;x =
abs(x)</p>
<p>Without the function call we could use the code<br>
<font face="monospace">if
x &lt; 0:</font>&nbsp; # if x&lt;0, do the next line;
otherwise skip
the next line<br>
&nbsp; &nbsp; <font face="monospace">x = -x</font><br>
An
if statementis like a
while statement, except you do not jump back to the
heading.&nbsp;&nbsp; This is the first time we have dealt with
an
inequality.&nbsp; Look at the instruction summary.&nbsp; There
is just
one instruction that deals with an inequality....&nbsp; Think about
it
for yourself.&nbsp; Details are in the video N4G1.&nbsp; My
result is
in abs.asm.<br>
</p>
<p>
2.&nbsp;
Another example to work out:&nbsp; Redo sum2n.asm as
sum2na.asm where you actually translate<br>
&nbsp;
&nbsp; &nbsp; <font face="monospace">while n
&gt;= 0:</font><br>
directly
( not the condition used implicitly before,&nbsp;<font face="monospace">n
!= 0</font>). &nbsp;Look at the full Pip assembler
instruction set.
&nbsp;Note that there is only one instruction that deals with
inequalities, so you have to figure out some way to make it
work.....&nbsp; Think first.&nbsp; The full solution is in the
revised N4G1 video.&nbsp; My solution is in sum2na.asm.<br>
</p>
<p>3.&nbsp; If-else statements are more involved.&nbsp;
Let's start
with a translation of</p>
<p>if x != 0:<br>
&nbsp;&nbsp;&nbsp; y = 2<br>
else:<br>
&nbsp;&nbsp; y = 3<br>
x = 5<br>
</p>
<p>
For simple testing, let us set x in memory in the simulator before
running.&nbsp; That way we do not need to start by storing a value
for
x.&nbsp; (Each of the other examples in this section will deal with
varuable initialization similarly.)<br>
</p>
<p>We have evaluated conditions.&nbsp; <br>
</p>
<p>Testing if x != 0 just involves loading it and a JMZ to
somewhere.</p>
<p style="font-family: monospace;"><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOD
x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ; if
x!=0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JMZ ____<br>
<br>
</p>
<p>We have worked out the approach to assignment
statements.&nbsp; Let
us suppose the statements in the assember code follow the textual order
of the Python.&nbsp; I'll put those sections with space between
them
for further editing:</p>
<p style="font-family: monospace;"><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOD
x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ; if x !=
0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JMZ ____<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOD
#2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ;
y=2&nbsp; if-true clause<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; STO y<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOD #3
&nbsp;&nbsp;&nbsp;&nbsp; ;
y=3&nbsp; if-false clause<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; STO y<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOD #5
&nbsp;&nbsp;&nbsp;&nbsp; ;
x=5&nbsp; past if-else statement<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; STO x
&nbsp;&nbsp;&nbsp; <br>
</p>
<p>The flow of control is new here.&nbsp; We will need jumps
inserted.&nbsp; If the condition is true, we just fall into the
if-true
block, but if it is false we must get to the <span style="font-style: italic;">else</span>
part, which will require a label as a jump target.&nbsp; An easy
name
would be ELSE.&nbsp; It goes as the operand of JMZ and a label on
the
if-false part:</p>
<p style="font-family: monospace;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
LOD
x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ; if x !=
0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JMZ ELSE<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOD
#2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ;
y=2&nbsp; if-true clause<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; STO y<br>
<br>
ELSE: LOD #3 &nbsp;&nbsp;&nbsp;&nbsp; ; y=3&nbsp;
if-false clause<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; STO y<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOD #5
&nbsp;&nbsp;&nbsp;&nbsp; ;
x=5&nbsp; past if-else statement<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; STO x
&nbsp;&nbsp;&nbsp; <br>
</p>
<p>Also note that if the condition is true, Python would do the
if-true
block and automatically skip the <span style="font-style: italic;">else</span>
part each time.&nbsp; In assembler we have to be explicit. That
will
require a jump from the end of the if-true block that happens every
time (JMP, not JMZ), requiring another jump target past the end of the
if-else statement.&nbsp; Let's call this label PAST.<br>
</p>
<p style="font-family: monospace;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
LOD
x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ; if x !=
0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JMZ ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOD
#2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
;&nbsp;&nbsp;&nbsp;&nbsp; y=2&nbsp; if-true clause<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; STO y<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JMP
PAST&nbsp;&nbsp;&nbsp;
; else:<br>
ELSE: LOD #3 &nbsp;&nbsp;&nbsp;&nbsp;
;&nbsp;&nbsp;&nbsp;&nbsp;
y=3&nbsp; if-false clause<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; STO y<br>
PAST: LOD #5 &nbsp;&nbsp;&nbsp;&nbsp; ; x=5&nbsp;
past if-else statement<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; STO x
&nbsp;&nbsp;&nbsp; <br>
</p>
<p>We are finished, since the if-false part can flow right into
the
part past the if-else statement.&nbsp; Look again at the jumps and
confirm that the right parts of the code are visited whether the
condition is true (not 0) or false (0).<br>
</p>
<p>Note:&nbsp; I use a colon to end a code label in my Pip
assembler,
even a name like ELSE.&nbsp; My final code is in jumpClass.asm.<br>
</p>
<p style="font-weight: bold;"><big>In the assember
labels must appear
at the beginning of a line <span style="font-style: italic;">with</span>
an instruction on it, not on a line before the instruction.<br>
</big></p>
<p>The usage is diferent than in Python:&nbsp; In Python a
colon is at
the end of a heading, and further code goes ont he next line. <br>
</p>
Again, in Pip, with low level jumps if-else is harder than in Python!
&nbsp;If we are translating the general form:<br>
<p>
if &nbsp;condition:<br>
&nbsp;
block1<br>
else:<br>
&nbsp; block2<br>
linesPastIf<br>
<br>
then it can be translated to the general Pip form below.&nbsp; The
all-caps parts are assembler code to copy into that exact location.
(For
each if-else construction inthe same program, you would need different
label names.)&nbsp; Note that while <span style="font-family: monospace; font-weight: bold;">else</span>
is a reserved word with a special meaning in Python, I used ELSE merely
as an arbitrarily chosen label name in the assember.&nbsp; The
whole
idea here is that there is not a prepackaged if-else syntax in
assembler!<br>
</p>
<table border="0" cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td><br>
</td>
<td>
<p>Evaluate condition (so false is 0)</p>
</td>
</tr>
<tr>
<td><br>
</td>
<td>
<p>JMZ ELSE &nbsp;(if the condition is false, skip
block1 to the
ELSE label)</p>
</td>
</tr>
<tr>
<td><br>
</td>
<td>
<p>block1 translated</p>
</td>
</tr>
<tr>
<td style="vertical-align: top;"><br>
</td>
<td style="vertical-align: top;">...<br>
</td>
</tr>
<tr>
<td><br>
</td>
<td>
<p>JMP PAST &nbsp;(skipping the else part)</p>
</td>
</tr>
<tr>
<td>
<p>ELSE:</p>
</td>
<td>
<p>block2 translated</p>
</td>
</tr>
<tr>
<td><br>
</td>
<td>
<p>...</p>
</td>
</tr>
<tr>
<td>
<p>PAST: </p>
</td>
<td>
<p>linesPastIf translated (end up here after either block
is
executed)</p>
</td>
</tr>
<tr>
<td><br>
</td>
<td>
<p>...</p>
</td>
</tr>
</tbody>
</table>
<br>
This if-else skeleton is in ifElseSkeleton.asm.<br>
<br>
4.&nbsp; Now an example to work out with your effort, following the
skeleton above.&nbsp; Consider
how to translate<br>
<br>
if x == 0:<br>
&nbsp;&nbsp;&nbsp;&nbsp; y = 3<br>
else:<br>
&nbsp;&nbsp;&nbsp;&nbsp;
y = 5<br>
z = z+y<br>
<br>
We will intialize x, y by hand in the simulator.&nbsp; Solution
workked out in the muddle of video N4G2.&nbsp; Final code will be
in
jumpClass2.asm<br>
<p>
5.&nbsp; Work with your
partner in</p>
<p> on translating into an assembler file (ending in
.asm):<br>
<br>
if z &lt; 0:<br>
&nbsp; &nbsp; z = z + 10<br>
else:<br>
&nbsp;
&nbsp; z = z - 1<br>
z = z * 2<br>
<br>
Test it by <br>
</p>
<ol>
<li>loading the code</li>
<li>giving a value to z</li>
<li>running the code</li>
<li>reinitializing the IP to 0</li>
<li>giving z a value with the opposite sign </li>
<li>running
again.&nbsp; <br>
</li>
</ol>
<p>For comparison, or it you get stuck, my code is in ifElse5.asm.<br>
</p>
<p>6.&nbsp; (Optional extra extention)&nbsp;&nbsp; A
more chalenging
condition in an example for you to work out by yourself and then
check.&nbsp; Not
only is there only one instruction with a size comparison.&nbsp; It
only
compares to 0.&nbsp; What do you do?&nbsp; (Remember algebra
with
inequalities.)&nbsp; Place different values for x
and y in memory by hand in pipGui.py to test the code:&nbsp; <br>
</p>
<p>if y &gt; x:
<br>
&nbsp; &nbsp; x = x*2
<br>
else:
<br>
&nbsp; &nbsp; y = y*2
<br>
z = x + y<br>
</p>
<p>My code is in ifElse6.asm, if you want to compare at the end. <br>
</p>
<p>
See
the assignment <a href="http://webpages.cs.luc.edu/~cnaiman/COMP150/HW/PipPrograms.html">Pip
Program</a>. &nbsp;It is
similar to the code from this section.</p>
<p>This hopefully gives the idea that&nbsp; a high level
language can
be translated.&nbsp; We have kept the Pip simulator very simple,
but
with a few more instructions, we could also handle lists and function
calls. We will not take the time to do that in this course.<br>
</p>
<p>
<b>Aside</b>: &nbsp;Though not
a part of the course, the program for the Pip Simulator is a
collection of Python modules. &nbsp;They show a considerably larger
and more complicated program than anything you have done (over 1000
lines - still much less than the hundreds of thousands of lines of
other Python programs). &nbsp;Still most of what is used is basic
building blocks that you have learned. &nbsp;There are some Python
features used that we did not get to in the Tutorial: &nbsp;I
defined
two of my own kind of objects; I used list comprehension, exception
handling, and some library functions that we did not introduce.
&nbsp;You
have the&nbsp;source code if you are curious! </p>
<h3><a class="mozTocH3" name="translationMachineAssem"></a>Translation
Between
Machine language and Assembler</h3>
<p>We started with machine language and quickly shifted to spend
most
of our time on assembler.&nbsp; The progression&nbsp; is an
important
idea.&nbsp; To show that you understand the idea of encoding an
instruction as a binary number, you should be able to convert both ways
between machine language and assembler (with a table of the op codes
handy).&nbsp; Both algorithms are fully stated next:<br>
</p>
<p><b>Converting to machine language from assembler:</b><br>
if the
assembler code contains a '#':<br>
&nbsp;&nbsp;&nbsp; the first 4 bits
are 0001<br>
else:<br>
&nbsp;&nbsp;&nbsp; the first four bits are
0000<br>
<br>
The second four bits come from the mnemonic as shown in
this table:<br>
&nbsp;&nbsp;&nbsp; ADD 0000<br>
&nbsp;&nbsp;&nbsp; AND
1000<br>
&nbsp;&nbsp;&nbsp; CPZ 1010<br>
&nbsp;&nbsp;&nbsp; CPL
1011<br>
&nbsp;&nbsp;&nbsp; DIV 0011<br>
&nbsp;&nbsp;&nbsp; HLT
1111<br>
&nbsp;&nbsp;&nbsp; JMP 1100<br>
&nbsp;&nbsp;&nbsp; JMZ
1101<br>
&nbsp;&nbsp;&nbsp; LOD 0100<br>
&nbsp;&nbsp;&nbsp; MUL
0010<br>
&nbsp;&nbsp;&nbsp; NOP 1110<br>
&nbsp;&nbsp;&nbsp; NOT
1001<br>
&nbsp;&nbsp;&nbsp; STO 0101<br>
&nbsp;&nbsp;&nbsp; SUB
0001<br>
<br>
if the the mnemonic is HLT or NOT:<br>
&nbsp;&nbsp;&nbsp;
the last byte is 00000000<br>
else if the mnemonic is JMP or JMZ:<br>
&nbsp;&nbsp;&nbsp;
the last byte is the code address (expressed in binary) to jump to<br>
else if
the assembler contains '#':<br>
&nbsp;&nbsp;&nbsp; the last byte is
the number after '#', converted to binary<br>
else:<br>
&nbsp;&nbsp;&nbsp; the
last byte is the address of the data referred to at the end of the
assembler instruction (in binary)<br>
<br>
<b>Converting to assembler
code with numeric labels from machine language:</b><br>
Split the
machine code into the first four bits, the next four bits, and the
last eight bits.<br>
The second four bits of the machine language
determine the mnemonic:<br>
&nbsp;&nbsp;&nbsp; 0000 ADD<br>
&nbsp;&nbsp;&nbsp;
0001 SUB<br>
&nbsp;&nbsp;&nbsp; 0010 MUL<br>
&nbsp;&nbsp;&nbsp; 0011
DIV<br>
&nbsp;&nbsp;&nbsp; 0100 LOD<br>
&nbsp;&nbsp;&nbsp; 0101 STO<br>
&nbsp;&nbsp;&nbsp;
1000 AND<br>
&nbsp;&nbsp;&nbsp; 1001 NOT<br>
&nbsp;&nbsp;&nbsp; 1010
CPZ<br>
&nbsp;&nbsp;&nbsp; 1011 CPL<br>
&nbsp;&nbsp;&nbsp; 1100 JMP<br>
&nbsp;&nbsp;&nbsp;
1101 JMZ<br>
&nbsp;&nbsp;&nbsp; 1110 NOP<br>
&nbsp;&nbsp;&nbsp; 1111
HLT<br>
If the instruction is&nbsp;HLT, NOP or NOT:<br>
&nbsp; &nbsp;
done!<br>
else:<br>
&nbsp; &nbsp; If&nbsp; the first 4 bits are
0001:<br>
&nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; the
mnemonic is
followed by&nbsp;'#'<br>
&nbsp;&nbsp;&nbsp; The assembler code ends
with the the last eight bits converted to decimal</p>
<h4>Sample Machine/Assembler Converson Problems<br>
</h4>
<p>Sample conversions to do by hand for understanding.&nbsp;
(You can
check your answers with pipGUI.py, switching from showing binary
(Binary button) to showing asembler but no labels (None
button).&nbsp;
We have not discussed the encoding of negative numbers.&nbsp; I
only
use 0 through 127 as data values afer a #, though the simulator also
allows -1 through -128.&nbsp; (You can see the binary translations
in
the simulator if you like.)<br>
</p>
<ol>
<li>00010011 00000111&nbsp; machine language to Assembler</li>
<li>00000010 10000001&nbsp; machine language to Assembler</li>
<li>ADD #9&nbsp; assembler to machine language</li>
<li>&nbsp;SUB 130&nbsp; assembler to machine language</li>
</ol>
<h2><a name="Boolean"></a>Boolean
Algebra, Truth Tables, and Digital
Circuits</h2>
<p>We have illustrated a simple machine language and
seen how multiple machine language statements can be used to do
central operations in a high level language. &nbsp;This language is
simple, but still it has been described in words!&nbsp; How can a
machine language be expressed in hardware? &nbsp;This section
addresses that question, in stages. <br>
<br>
First we consider the
direct correspondence between&nbsp;Boolean expressions, truth
tables,
and simple digital circuits. &nbsp;It is useful to be familiar with
all three, since each is more natural or simple in different
situations.&nbsp; It is important to be able to choose the best one
and
convert
between them. &nbsp;In particular we can first express
the operations we want logically, and then in
circuits which could be expressed in hardware.<br>
</p>
<h3><a class="mozTocH4" name="algrbraOverview"></a>Boolean
Algebra and
Truth Tables<br>
</h3>
<p>We have already seen Boolean expressions in Python,
with operations AND, OR, and NOT. &nbsp;We will end up building
more
complicated expressions than we did with Python, and more concise
notation will be useful and is standard in such discussions.
&nbsp;First
we will use 1 and 0 for True and False, our usual symbols to
distinguish a bit of information. &nbsp;Second we will use more
algebraic notation:</p>
<ol>
<li>
<p style="margin-bottom: 0in;">A or B is written with
a + sign:
&nbsp;A + B</p>
</li>
<li>
<p style="margin-bottom: 0in;">A and B
is&nbsp;written just by
putting the parts beside each other,&nbsp;as with mathematical
notation
for multiplication: &nbsp;AB &nbsp;(We will assume <span style="font-style: italic;">one</span> character
variable names like in math, so this makes sense.)</p>
</li>
<li>
<p><i>not A</i> is written: &nbsp;A' <br>
</p>
</li>
</ol>
<p style="margin-bottom: 0in;">Because there are only a
few possible
values for the inputs to the expressions, we can write out a complete
table of possible values, called a <i><b>truth table</b></i>.
In the
leftmost columns we write the variable values in all possible
combinations, and in one or more further columns write values of
results:<br>
<br>
<b>Truth Table for OR &nbsp; 0 only if all inputs are
0</b></p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">A</p>
</td>
<td>
<p align="left">B</p>
</td>
<td>
<p align="left">A+B</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
</tbody>
</table>
<p style="margin-bottom: 0in;"><br>
<b>Truth Table for AND &nbsp; 1
only if all inputs are 1</b></p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">A</p>
</td>
<td>
<p align="left">B</p>
</td>
<td>
<p align="left">AB</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
</tbody>
</table>
<p style="margin-bottom: 0in;"><br>
<b>Truth Table for NOT &nbsp;
reversing the input</b></p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">A</p>
</td>
<td>
<p align="left">A'</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
</tbody>
</table>
<p style="margin-bottom: 0in;"><br>
As in Python assume NOT has highest
precedence followed by AND, with OR last.<br>
<br>
Another Boolean logic operation
that is occasionally used is&nbsp;XOR,&nbsp;short for eXclusive
OR.
&nbsp;It is visually and logically a variation on OR. &nbsp;The
standard OR is true if one <i>or more</i> inputs are true.
&nbsp;XOR
is true when <i>exactly one</i> of the two inputs is true,
or
otherwise put, when the two operands are <i>unequal</i>.
&nbsp;It has
a special operation symbol in Boolean expressions that is also a
variation on the standard symbol for OR. &nbsp;Rather than a plain
'+', it has a circle around it: ⊕&nbsp; &nbsp;<br>
<br>
<b>Truth
Table for a Xor &nbsp; &nbsp;1 when the inputs are <span style="font-style: italic;">unequal</span></b>
</p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">A</p>
</td>
<td>
<p align="left">B</p>
</td>
<td>
<p align="left">A⊕B</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
</tbody>
</table>
<p style="margin-bottom: 0in;">If I use this less familiar
operation in
a larger expression with other binary operations, I will always use
parentheses to indicate the order of operations around the⊕. <br>
</p>
<p style="margin-bottom: 0in;">
We can calculate
truth tables for more complicated expressions, building up one
operation at a time.&nbsp; Consider AB'.&nbsp; Since <span style="font-weight: bold;">not</span> has higher
precedence than <span style="font-weight: bold;">and</span>,
this is the same as A(B')
rather than (AB)'.&nbsp; We need B' calculated before we can
calculate AB'.</p>
<p style="margin-bottom: 0in;">
<b>Truth Table for AB' (involving
intermediate result B')</b></p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">A</p>
</td>
<td>
<p align="left">B</p>
</td>
<td>
<p align="left">B'</p>
</td>
<td>
<p align="left">AB'</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
</tbody>
</table>
<p style="margin-bottom: 0in;"><br>
We can have more input variables
involved as in AB + AC. &nbsp;Here we have three input variables,
and
2*2*2 = 8 combinations of inputs to list.&nbsp; For consistency, it
is traditional to list the input in the order where they appear as
binary numbers for 0, 1, 2, .... Intermediate results are included in
the table in such a way that each column after the input variables is
the result of one operation on one or two previous column:<br>
<br>
<b>Truth Table for AB + AC</b></p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">A</p>
</td>
<td>
<p align="left">B</p>
</td>
<td>
<p align="left">C</p>
</td>
<td>
<p align="left">AB</p>
</td>
<td>
<p align="left">AC</p>
</td>
<td>
<p align="left">AB+AC</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
</tbody>
</table>
<p style="margin-bottom: 0in;"><br>
<b>Truth Table for A(B +&nbsp;C)</b></p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">A</p>
</td>
<td>
<p align="left">B</p>
</td>
<td>
<p align="left">C</p>
</td>
<td>
<p align="left">B+C</p>
</td>
<td>
<p align="left">A(B+C)</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
</tbody>
</table>
<p><br>
You can see from the exhaustive listing of the options in the
last two truth tables that AB+AC &nbsp;= A(B+C) <i>always</i>.
&nbsp;This
is called an <i>identity</i>, and it has the same
formalism as the
<i>distributive</i> property in normal real number algebra,
though
the operations involved are actually completely different!<br>
</p>
<h3><a class="mozTocH4" name="BooleanAlgRules"></a>Rules
of Boolean Algebra</h3>
George
Boole invented the algebra with these two state values, now called
Boolean algebra, and so the Python type is an abbreviation of Boole's
name (bool). &nbsp;Many identities and names match the symbolism
for
the normal&nbsp;algebra you learned with numbers,&nbsp;BUT NOT
ALL!
&nbsp;Ones that are incorrect or undefined in normal algebra are in
<b>boldface</b> in the table below, with a shaded background<br>
<br>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">Property name</p>
</td>
<td>
<p align="left">AND version</p>
</td>
<td>
<p align="left">OR version</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">Commutative</p>
</td>
<td>
<p align="left">AB = BA</p>
</td>
<td>
<p align="left">A+B = B + A</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">Associative</p>
</td>
<td>
<p align="left">(AB)C = A(BC)</p>
</td>
<td>
<p align="left">(A+B)+C = A+(B+C)</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">Distributive</p>
</td>
<td>
<p align="left">AB+AC &nbsp;= A(B+C)</p>
</td>
<td bgcolor="#ffccff">
<p align="left"><b>A+BC &nbsp;= (A+B)(A+C)</b></p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">Identity</p>
</td>
<td>
<p align="left">1A = A</p>
</td>
<td>
<p align="left">0 + A = A</p>
</td>
</tr>
<tr valign="top">
<td bgcolor="#ffccff">
<p align="left">Complement</p>
</td>
<td bgcolor="#ffccff">
<p align="left">(A')' = A</p>
</td>
<td bgcolor="#ffccff">
<p align="left">A + A' = 1</p>
</td>
</tr>
<tr valign="top">
<td bgcolor="#ffccff">
<p align="left">DeMorgan's Law</p>
</td>
<td bgcolor="#ffccff">
<p align="left">(AB)' = A' + B'</p>
</td>
<td bgcolor="#ffccff">
<p align="left">(A+B)' = A' B'</p>
</td>
</tr>
</tbody>
</table>
<h4>Optional Python Aside</h4>
You could also use Python to generate a truth table for a Boolean
expression<span style="font-weight: bold;"></span>.&nbsp;
Python treats 1 and 0 as True and False in Boolean expressions, and can
convert Boolean values to ints.&nbsp; For example the table for
Boolean
expression AB+AC could be generated by this code in <a href="http://webpages.cs.luc.edu/~cnaiman/COMP150/Examples/truth.py">truth.py</a>:<br>
<br>
<span style="font-family: monospace;">print('A B C AB+BC')</span><br style="font-family: monospace;">
<span style="font-family: monospace;">for A in [0, 1]:</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;&nbsp;&nbsp;
for B in [0,
1]:</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
for C in [0, 1]:</span><br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
print(A, B, C, int(A and B or B and C))<br>
<br>
</span>In Python the symbol for xor is ^, and it has precedence
between
<span style="font-weight: bold;">or </span>and <span style="font-weight: bold;">and</span>.<br>
<h3><a class="mozTocH3" name="GatesCircuits"></a>Transistors,
Gates,
and Circuits</h3>
<p style="margin-bottom: 0in;">Various sorts of switches
have been
used historically in computing devices, depending on the technology
of the times: relays (switches actuated by electromagnets), vacuum
tubes, and transistors. &nbsp;All have
the same essential behavior, except transistors are much faster and
more
reliable than the others.&nbsp;&nbsp;I will just refer to the
modern
version, transistors.&nbsp; &nbsp;<br>
<img src="./Class Notes_files/transistor.png" name="graphics2" alt="Transistor" align="bottom" border="0" height="232" width="494"><br>
I will diagram a transistor as a gray circle.&nbsp; A
transistor has three connections, a base, B, an emitter, V<sub>in</sub>,
and a collector, V<sub>out</sub>.
&nbsp;The base acts as a switch:
&nbsp;If the base is grounded, the emitter is&nbsp;not
connected to
the collector.&nbsp; The symbol for ground is shown connected to
the
base in the left diagram above.&nbsp; If a voltage is applied to
the
base, an
electrical connection is enabled between&nbsp;emitter and
collector.&nbsp;
Hence a transistor has two states, switched on or off.<br>
<br>
<br>
Circuits are set up with a voltage
source and opportunities for wires to be&nbsp;grounded.
&nbsp;The
circuits are set up (with electrical resistances - we will skip
elaborate physics) so if a wire is&nbsp;connected to ground, it is
grounded, whether is is also connected to a voltage source or
not.&nbsp; <br>
</p>
<p style="margin-bottom: 0in;">V<sub>in</sub>
is always connected to a
source that might have
a voltage on it or be grounded or be disconnected, while&nbsp;V<sub>out</sub>
may either be disconnected or&nbsp;grounded (but it does not have a
voltage attached). &nbsp;The standard ground symbol is shown at the
bottom of each diagram below. &nbsp;A capital V is used to mean a
consistent voltage source. &nbsp;A connection of the output to
voltage or ground is shown by a gray path.<br>
<img src="./Class Notes_files/notGate.png" name="graphics3" alt="not gate" align="bottom" border="0" height="239" width="661"><br>
In
the simplest situation, V<sub>in</sub>
is&nbsp;definitely connected
to a voltage source and also to an output wire. &nbsp;V<sub>out</sub>
is grounded. &nbsp;In this case the state of&nbsp;the base is
the
only thing variable.&nbsp; As the right diagram shows, if the base
has
a voltage, the emitter circuit
is connected, and ground at V<sub>out</sub> is connected to
the output
through V<sub>in</sub>, so the output becomes
grounded. &nbsp;If the base does not have a voltage, as in the left
diagram, the connection
between the output and ground is broken, and the output is just
connected to the regular voltage source, resulting in a voltage on
the output wire.<br>
<br>
Possibilities in the Figure</p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">Base</p>
</td>
<td>
<p align="left">Output</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">voltage</p>
</td>
<td>
<p align="left">grounded</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">grounded</p>
</td>
<td>
<p align="left">voltage</p>
</td>
</tr>
</tbody>
</table>
<p style="margin-bottom: 0in;"><br>
The circuit provides an&nbsp;output
that is the opposite of the input. &nbsp;If we associate voltage
with
1 and grounded with 0, we get the NOT truth table! &nbsp;The NOT
operation takes only a single transistor. &nbsp;<br>
<br>
Possibilities
in the Figure</p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">B</p>
</td>
<td>
<p align="left">Output = B'&nbsp;</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
</tbody>
</table>
<p style="margin-bottom: 0in;"><br>
We can connect two transistors in
series as shown and use both bases as inputs. &nbsp;<br>
<img src="./Class Notes_files/nandGate.png" name="graphics4" alt="Nand gate" align="bottom" border="0" height="385" width="312"><br>
Only
when both inputs have voltage, as shown, is there&nbsp;a connection
between ground and the output. &nbsp;If either input were grounded,
the connection of ground and output would broken, and the output
would hold voltage rather than being drawn to the ground state.
&nbsp;Hence if we call the inputs A and B and the output X, we
get what is called a NAND gate.<br>
<br>
Truth Table for a Nand gate:</p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">A</p>
</td>
<td>
<p align="left">B</p>
</td>
<td>
<p align="left">X = (AB)'</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
</tbody>
</table>
<p style="margin-bottom: 0in;"><br>
This the truth table for (AB)', NOT&nbsp; (A AND B), and the
combination is commonly abbreviated, NAND. &nbsp;<br>
<br>
We can also
connect two transistors in parallel as shown, still using both bases
as inputs feeding one output. &nbsp;<br>
<img src="./Class Notes_files/norGate.png" name="graphics5" alt="Nor gate" align="bottom" border="0" height="239" width="573"><br>
The
only way to avoid a connection&nbsp;between the output and ground
is
to have&nbsp;both inputs grounded, as shown above, resulting in
voltage at the output. &nbsp;If at least one input has voltage, the
output becomes connected to ground. &nbsp;Hence if we call the
inputs
A and B and the output X, we get what is called a NOR gate:<br>
<br>
Truth Table for a Nor gate:</p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">A</p>
</td>
<td>
<p align="left">B</p>
</td>
<td>
<p align="left">X = (A+B)'</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
</tbody>
</table>
<p><br>
This is the truth table for NOT (A&nbsp; OR B), commonly
abbreviated as NOR. &nbsp;<br>
<br>
To turn a Nor circuit into an Or circuit,&nbsp;a
further&nbsp;NOT operation is needed on the output, requiring one
more transistor. &nbsp;Similarly you can convert a Nand to And with
an
extra transistor. &nbsp;<br>
<br>
In
circuit diagrams, the details of the&nbsp;combinations of
transistors, voltages and grounds needed for the different Boolean
operations discussed above is hidden, or abstracted away. &nbsp;The
operations are given special, more simple symbols:<br>
<br>
<img src="./Class Notes_files/gates.png" name="graphics6" alt="Gate symbols" align="bottom" border="0" height="158" width="232"><br>
The
inputs are assumed to come into the wires on the left and the output
go out from the wire on the right. &nbsp;All the gates that involve
"NOT" have a small circle where the NOT operation would
take place.<br>
<br>
For example the Boolean expression A(B+C)
corresponds to the circuit diagram<br>
<br>
<img src="./Class Notes_files/A-B+C.png" name="graphics7" alt="circuit diagram for A(B+C}" align="bottom" border="0" height="88" width="179"><br>
<br>
Each
input is assumed to correspond to a voltage on a labeled wire,
usually coming from the left. &nbsp;These wires feed gates with
result wires coming out of them. &nbsp; As long as each wire ends
up
going to the left, and not looping, each wire corresponds directly to
one Boolean
expression. &nbsp;Following the wires, putting the symbolic result
as a label on each one in turn, eventually leads us to an
output.&nbsp;
<br>
</p>
<p>There is a direct correspondence between the intermediate
wires
(like the one labeled B+C above),&nbsp; their logical labels, and
intermediate columns you should put in a truth table when looking to
figure out the table for a boolean expression involving multiple
operations.</p>
<p>These
are <i>sequential</i> circuits. &nbsp;Circuits with
loops in them are
also important, but more complicated. &nbsp;They are call
<i>combinatorial</i> circuits and will be briefly discussed
later. </p>
<p>
We will mostly work in terms of AND, OR, and NOT, because of
their familiarity, though NAND and NOR are used more in actual
engineering practice, since they require fewer transistors in a
circuit.<br>
<br>
By putting more than two transistors in series or
parallel, NAND and&nbsp;NOR gates with more than two inputs can be
constructed, hence with a further transistor for each added input,
multi-input AND and OR
gates can be constructed. &nbsp;The same AND and OR gate symbols
are
used in these cases, except more input wires are allowed.&nbsp; <br>
</p>
<h3><a name="GatesApplet"></a>Gates Applet<br>
</h3><br>
<p>Nice gates simulator, but doesn’t use the correct shapes:&nbsp; <a href="http://www.neuroproductions.be/logic-lab/" target="_blank">http://www.neuroproductions.be/logic-lab/</a><br>
<br>-<span style="font-weight: bold;">-&gt;We will probably use this one in class: </span>Here's another one:&nbsp; adorable, but a little more cumbersome to use:&nbsp; <a href="http://www.edumedia.rmit.edu.au/emg/gallery/Project/LogicGates/logic_builder.htm" target="_blank">http://www.edumedia.rmit.edu.au/emg/gallery/Project/LogicGates/logic_builder.htm</a></p>
<p>Addison-Wesley, comes with lab assignment from another text<a href="http://wps.aw.com/aw_brookshear_compsci_8/18/4742/1214158.cw/content/index.html" target="_blank"><br>
http://wps.aw.com/aw_brookshear_compsci_8/18/4742/1214158.cw/content/index.html<br>
<br>
</a></p>
<p>Watch the gatesApplet, as I select and move components, connect them
with
wires, run the circuit and change input values&nbsp; Instructions
are
also
given on the applet web page, beneath the applet. The video ends with a
demonstration discussed inthe next paragraph.&nbsp; <span style="font-style: italic;">Work through the Gates Lab
beneath the
applet.</span><br>
</p>

<p>The
following circuit tests the distributive property, AB+AC = A(B+C),
assuming the inputs are labeled down from the top A, B, C.&nbsp;
The
circuit has outputs for both sides of the identity originating from the
same inputs, that fork two ways.&nbsp; (This is fine, an input can
feed
several
gates.)&nbsp; No matter
how you manipulate the three switches to give all the possible inputs,
the two outputs always match.&nbsp; This is
illustrated for inputs 1, 0, 0 and for 1, 0, 1.&nbsp; The
convention is
that wires only connect at the small round contact points.&nbsp; In
other places wires pass one over another ut are not
connected.&nbsp;
This is the system in the applet, too.<br>
<img style="width: 283px; height: 183px;" alt="AB + AC=A(B+C) in circuits, input 1, 0, 0" src="./Class Notes_files/distrib100.png"></p>
<p><img style="width: 285px; height: 177px;" alt="AB + AC=A(B+C) in circuits, input 1, 0, 1" src="./Class Notes_files/distrib101.png"></p>
<br>
Further Class exercise:&nbsp; Construct a tester for a <a href="http://hwheeler01.github.io/comp150/classnotes/#BooleanAlgRules">Boolean
Algebra identity</a> for
the other distributive property, A+BC = (A+B)(A+C), or
for one of&nbsp;DeMorgan's laws on the bottom line.
&nbsp;Follow the
pattern used before to test A(B+C) = AB + AC:
&nbsp;Have just one set of inputs, but connect them to gates and
outputs for each side of the equation.&nbsp; Show your result to
your
instructor or
a TA.<br>
<h3><a class="mozTocH3" name="boolExprForTruthT"></a>Finding
a Boolean
Expression for a truth table</h3>
<p>In the introduction, I mentioned that we want to be able to
convert between all the representations: circuit, boolean expression,
and truth table. &nbsp;We have discussed the
direct translation between Boolean expressions and circuits, and we
have shown how to convert a Boolean expression into a truth table.
&nbsp;The only direction missing now is from truth table to Boolean
expression.<br>
<b><br>
</b>Below is a truth table for an output X. &nbsp;It
is totally specified by the truth table, <i>without</i>
first being
given by a Boolean expression. &nbsp;To find a Boolean expression
that <i>does</i> correspond to the&nbsp;output X,
first locate a 1 in
the column for X. &nbsp;The final row is an example. &nbsp;This
is
true when we have the exact input values in the row: A is true and B
is true and C is true. &nbsp;That is a simple statement to
translate
into boolean symbolism: &nbsp;ABC. &nbsp;Another row where X is
one
is the third from the bottom, where&nbsp;A is true and B is <b>not</b>
true and C is true. &nbsp;Another way to put this is A is true and
(not B) is true and C is true. &nbsp;Again, this easily translates
into a Boolean expression: &nbsp;AB'C. &nbsp;The chart below
traces
out the sequence of steps, including for the second row :<br>
<font face="monospace"><br>
A
B C&nbsp; X &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
&nbsp; &nbsp;Example</font><br>
<font face="monospace">0
0 0&nbsp; 0<br>
0 0 1&nbsp; 1<br>
0 1 0&nbsp; 0<br>
0 1 1&nbsp; 0<br>
1&nbsp;0
0&nbsp; 0<br>
1&nbsp;0 1&nbsp; 1<br>
1 1 0&nbsp; 0<br>
1 1 1&nbsp; 1 &nbsp;&lt;-
First find an expression producing this 1 and = 0 everywhere else<br>
<br>
A
B C &nbsp;X</font><br>
<font face="monospace">0 0 0&nbsp; 0<br>
0 0 1
&nbsp;1<br>
0 1 0&nbsp; 0<br>
0 1 1 &nbsp;0<br>
1&nbsp;0 0&nbsp; 0<br>
1&nbsp;0
1 &nbsp;1</font> &nbsp;<font face="monospace">&lt;-
Find
expression&nbsp;producing</font> <font face="monospace">this
1 and =
0 everywhere else</font><br>
<font face="monospace">1 1 0&nbsp; 0<br>
1
1 1 &nbsp;1 &nbsp;ABC<br>
<br>
A B C&nbsp; X</font><br>
<font face="monospace">0
0 0 &nbsp;0<br>
0 0 1&nbsp; 1</font>&nbsp;<font face="monospace">&lt;-
Find expression&nbsp;producing</font> <font face="monospace">this 1
and = 0 everywhere else</font><br>
<font face="monospace">0 1 0 &nbsp;0<br>
0
1 1&nbsp; 0<br>
1&nbsp;0 0 &nbsp;0<br>
1&nbsp;0 1&nbsp; 1 &nbsp;AB'C
&nbsp;</font><br>
<font face="monospace">1 1 0&nbsp; 0<br>
1 1 1 &nbsp;1
&nbsp;ABC<br>
<br>
A B C&nbsp; X</font><br>
<font face="monospace">0 0 0
&nbsp;0<br>
0 0 1&nbsp; 1</font>&nbsp;<font face="monospace">A'B'C</font><br>
<font face="monospace">0
1 0 &nbsp;0<br>
0 1 1&nbsp; 0<br>
1&nbsp;0 0 &nbsp;0<br>
1&nbsp;0 1&nbsp;
1 &nbsp;AB'C &nbsp;</font><br>
<font face="monospace">1 1 0&nbsp; 0<br>
1
1 1 &nbsp;1 &nbsp;ABC<br>
<br>
</font>We have expressions = 1 ONLY in
each individual place X is 1. &nbsp;To get X, which is 1 with <span style="font-style: italic;">any</span> of these
inputs, combine with
the OR operation: &nbsp;<br>
<font face="monospace">X
= A'B'C + AB'C + ABC</font> &nbsp;<br>
</p>
<h4>Simplifying Boolean Algebra<br>
</h4>
<p>
A circuit could certainly
be made for X, but it would be easier with a simplification.
&nbsp;One
advantage of Boolean algebra is that it is easy to manipulate
algebraically, for instance using the rules of <a href="http://hwheeler01.github.io/comp150/classnotes/#BooleanAlgRules">Boolean
Algebra</a> discussed earlier. &nbsp;I
will not hold you responsible
for this, but it will shorten some answers, and hence prove to be
convenient!&nbsp; <br>
<br>
Focus on the last two terms:<br>
<font face="monospace">A'B'C
+ (AB'C + ABC)<br>
= A'B'C + AC(B'+B) &nbsp; distributive rule
(factoring out A and C<br>
= A'B'C + AC(1) &nbsp; &nbsp; &nbsp;complement
rule for OR<br>
= A'B'C + AC &nbsp; &nbsp; &nbsp; &nbsp; identity
rule<br>
</font><br>
One general rule that is easy to check that was
not in the earlier rules is<br>
<font face="monospace">A + A = A</font><br>
In
general, this means any expression can be replaced by two ORed copies
of the same expression. &nbsp;In particular the one copy
of&nbsp;AB'C
in the middle of the expression for X can be replaced by two copies
ORed:<br>
<br>
<font face="monospace">X = A'B'C</font> <font face="monospace">+&nbsp;AB'C</font>
<font face="monospace">+ ABC<br>
= A'B'C + AB'C</font> <font face="monospace">+
AB'C + ABC &nbsp; &nbsp; &nbsp;adding a second ORed copy of
AB'C<br>
=
(A'B'C + AB'C)</font> <font face="monospace">+
(AB'C + ABC)
&nbsp;associating parts usefully<br>
= (A'B'C</font> <font face="monospace">+
AB'C)</font> <font face="monospace">+ AC</font>
&nbsp; &nbsp; &nbsp;
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
&nbsp; &nbsp;
&nbsp;&nbsp;using
the result above for the last two terms<font face="monospace"><br>
<br>
Just
as we showed</font> <font face="monospace">AB'C +
ABC = AC, we can
rework the first two terms:<br>
<br>
(A'B'C + AB'C) + AC <br>
= (A' +
A)B'C &nbsp;+ AC</font><br>
<font face="monospace">= (1)B'C &nbsp; &nbsp;
&nbsp; + AC&nbsp; &nbsp; &nbsp;<br>
= &nbsp; &nbsp;B'C + AC</font><br>
<br>
The
general pattern that simplifies is when&nbsp;<span style="font-style: italic;">all but one</span> factor
matches in two terms: &nbsp;then&nbsp;the non matching factor
(negated in one term and not negated in the other) can be completely
removed and leave only one term with the remaining common factors.
&nbsp;Symbolically, if X stands for all the matching factors and Y
is
the <span style="font-style: italic;">one</span>
non matching factor
then <font face="monospace">XY + XY' = X</font>.
</p>
<h4><a class="mozTocH4" name="truthTableExample"></a>A
Further Example:
English to Truth Table to Boolean Expression<br>
</h4>
<p>Find a truth table for the Boolean expression that is true
when
all three inputs (A, B, C) are the same &nbsp;(call this&nbsp;X
initially). &nbsp;Then find the Boolean expression in terms of A,
B,
and C.&nbsp; <br>
<br>
<font face="monospace">A B C&nbsp; X</font><br>
<font face="monospace">0
0 0&nbsp; ?<br>
0 0 1&nbsp; ?<br>
0 1 0&nbsp; ?<br>
0 1 1&nbsp; ?<br>
1&nbsp;0
0&nbsp; ?<br>
1&nbsp;0 1&nbsp; ?<br>
1 1 0&nbsp; ?<br>
1 1 1&nbsp; ?&nbsp;<br>
</font></p>
<p>Coming up with a completed truth table involves an inital
translation from English:</p>
<p>
<font face="monospace">A
B C&nbsp; X</font><br>
<font face="monospace">0 0 0&nbsp; 1<br>
0 0 1&nbsp;
0<br>
0 1 0&nbsp; 0<br>
0 1 1&nbsp; 0<br>
1&nbsp;0 0&nbsp; 0<br>
1&nbsp;0
1&nbsp; 0<br>
1 1 0&nbsp; 0<br>
1 1 1&nbsp; 1 &nbsp;<br>
<br>
Now
what to get a Boolean expression?<br>
</font><br>
<font face="monospace">A B C&nbsp; X</font><br>
<font face="monospace">0
0 0&nbsp; 1</font> &nbsp;&lt;- First find AN
expression matching this 1
and = 0 everywhere else<br>
<font face="monospace">0
0 1&nbsp; 0<br>
0 1 0&nbsp; 0<br>
0 1 1&nbsp; 0<br>
1&nbsp;0 0&nbsp;
0<br>
1&nbsp;0 1&nbsp; 0<br>
1 1 0&nbsp; 0<br>
1 1 1&nbsp; 1</font><br>
<br>
<font face="monospace">A
B C&nbsp; X</font><br>
<font face="monospace">0 0 0&nbsp; 1 &nbsp;A'B'C'</font><br>
<font face="monospace">0
0 1&nbsp; 0<br>
0 1 0&nbsp; 0<br>
0 1 1&nbsp; 0<br>
1&nbsp;0 0&nbsp;
0<br>
1&nbsp;0 1&nbsp; 0<br>
1 1 0&nbsp; 0<br>
1 1 1&nbsp; 1</font>&nbsp;&lt;-
Then find AN expression matching this 1 and = 0 everywhere else<font face="monospace"><br>
<br>
</font><br>
<font face="monospace">A
B C&nbsp; X</font><br>
<font face="monospace">0 0 0&nbsp; 1 &nbsp;A'B'C'</font><br>
<font face="monospace">0
0 1&nbsp; 0<br>
0 1 0&nbsp; 0<br>
0 1 1&nbsp; 0<br>
1&nbsp;0 0&nbsp;
0<br>
1&nbsp;0 1&nbsp; 0<br>
1 1 0&nbsp; 0<br>
1 1 1&nbsp; 1</font>&nbsp;<font face="monospace">ABC<br>
<br>
</font>Then
what?<br>
<br>
Combine with OR:<br>
<br>
<font face="monospace">
X = A'B'C' + ABC</font></p>
<p>A common student error is to skip the last step, and not
combine,
but you are looking for a description of a single output, so your
result must be a single expression!<br>
</p>
<h3><a class="mozTocH3" name="computerCircuits"></a>Addition
in
Computer Circuits</h3>
<p style="margin-bottom: 0in;">OK so we can
convert logical operations to hardware. &nbsp;In all our <i>logical</i>
operations, however, we did not see <i>normal</i>
arithmetic, but we want to be able to do that on a computer!
&nbsp;Since
we are using two state circuits we will do binary arithmetic.
&nbsp;Start
as simply as possible. &nbsp;If we stick to 1 bit additions, there
are not many choices:<font face="monospace"><br>
<br>
&nbsp;0 &nbsp; 0 &nbsp; 1 &nbsp; 1<br>
+0
&nbsp;+1 &nbsp;+0 &nbsp;+1<br>
__ &nbsp;__ &nbsp;__ &nbsp;__<br>
&nbsp;0
&nbsp; 1 &nbsp; 1 &nbsp;10<br>
<br>
</font>The complication is the carry in
the last case. &nbsp;It means we need to keep track of two binary
outputs which we will call sum&nbsp;(the 1's bit) and carry (the
carry bit). &nbsp;All the data is 0's and 1's, so we can write a
complete table:<font face="monospace"><br>
<br>
</font>Table for sum and carry in
binary addition, A+ B<br>
</p>
<table border="1" cellpadding="2" cellspacing="2">
<tbody>
<tr valign="top">
<td>
<p align="left">A</p>
</td>
<td>
<p align="left">B</p>
</td>
<td>
<p align="left">carry</p>
</td>
<td>
<p align="left">sum</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">0</p>
</td>
<td>
<p align="left">1</p>
</td>
</tr>
<tr valign="top">
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">1</p>
</td>
<td>
<p align="left">0</p>
</td>
</tr>
</tbody>
</table>
<p>We are thinking of arithmetic, but see the format of the table
- it
is in the format of a truth table!<br>
You may recognize both the outputs: &nbsp;carry
is AND and sum is XOR. &nbsp;<br>
<br>
If you wish to avoid the XOR
symbolism, you can calculate an equivalent expression in terms of
AND, OR, and NOT, as we can for a truth table. &nbsp;Applying the
technique just introduced for finding a Boolean expression from a
truth table, you find:<br>
A XOR B = AB' + A'B<br>
<br>
This is a <span style="font-style: italic;">half adder</span>
circuit.<br>
<br>
<img src="./Class Notes_files/halfAdder.png" name="graphics8" alt="half adder" align="bottom" border="0" height="100" width="166"><br>
</p>
<p>The video animates this circuit.&nbsp; If you like you can
construct
and test the circuit for yourself in the gates applet, <br>
</p>
<p>
To
understand more complicated circuits it is useful to give a simpler
symbol for repeatedly used circuits. &nbsp;We will use the half
adder
several times in more complicated situations, and will give the half
adder its own symbol<br>
<br>
<img src="./Class Notes_files/halfAdderAbs.png" name="graphics9" alt="Symbol for half adder" align="bottom" border="0" height="100" width="166"><br>
<br>
When
you do addition using place value with two multi-digit numbers,
you actually have to add three digits together at a time in general:
&nbsp;a digit from each number, and a possible <i>carry</i>
from the previous place. &nbsp;An example as you might have written
it in primary school to add 5147 and&nbsp;7689<span style="font-family: monospace;">:</span><br style="font-family: monospace;">
<br style="font-family: monospace;">
<span style="font-family: monospace;">&nbsp; 1 11</span><font style="font-family: monospace;"> &nbsp; carries<br>
&nbsp;&nbsp; 5147&nbsp; decimal numeral</font><br style="font-family: monospace;">
<font style="font-family: monospace;">&nbsp;+
7689&nbsp; decimal numeral<br>
&nbsp; _____<br>
= 12836</font>&nbsp; &nbsp;<br>
<br>
If
you are adding multi bit binary numerals, that means adding three
inputs that can be 0 or 1, with a sum at most 3, still only needing 2
bits of output. &nbsp;<br>
<br>
<span style="font-family: monospace;">&nbsp;&nbsp;
</span><font style="font-family: monospace;">111&nbsp;&nbsp;
carries<br>
&nbsp;&nbsp;&nbsp;
011&nbsp; binary numeral</font><br style="font-family: monospace;">
<font style="font-family: monospace;">&nbsp;+&nbsp;
111&nbsp; binary
numeral<br>
&nbsp; _____<br>
=&nbsp; 1010</font>
<br>
<br>
We can put two half adders together with one extra OR gate to
create a <span style="font-style: italic;">full adder</span>,
which
adds three single bit inputs, as
illustrated below in terms of the just-introduced half adder
symbol.&nbsp; If we label the three inputs A, B, and "carry in",
then we can start adding A and B with a half adder. &nbsp;The sum
output can be added to the carry in with another half adder to
produce the final sum bit. &nbsp;Both half adders have a carry bit.
&nbsp;If either one produces a carry, then there is a carry in the
final answer, so the carry bits need to go through an OR gate to
procuce the final carry.<br>
<br>
<img src="./Class Notes_files/fullAdderAbs1.png" name="graphics10" alt="full adder from two half adders" align="bottom" border="0" height="169" width="307"><br>
<br>
Recreating this in the gates applet is shown in the video, and also
below in pictures.&nbsp; The most significant output bit
(carry) in at the bottom.&nbsp; You could also create your own and
test
it in
the gates applet, but the circuits are getting more complicated to
reproduce by hand!<br>
.<img style="width: 357px; height: 187px;" alt="full adder 1+1+1" src="./Class Notes_files/full111.png">&nbsp;
1+1+1 =11</p>
<p><span style="font-style: italic;"><img style="width: 355px; height: 182px;" alt="Full adder adding 1, 0, 1" src="./Class Notes_files/full101.png">&nbsp;
</span>1+0+1=10 <span style="font-style: italic;"> </span><br>
The full adder,
too, can be used in more complicated circuits, so we will give it its
own symbol:<br>
<br>
<img src="./Class Notes_files/fullAdderAbs.png" name="graphics11" alt="full adder symbol" align="bottom" border="0" height="110" width="156">&nbsp;<br>
<br>
Once
you have full adders you can chain them together to create a
multi-bit adder. &nbsp;For example, a circuit to add two three-bit
numbers could get inputs A<sub>2</sub>, A<sub>1</sub>,
A<sub>0</sub>,
and B<sub>2</sub>, B<sub>1</sub>, B<sub>0</sub>,
where the subscripts
indicate the power to which 2 is raised&nbsp;in the binary place
value. &nbsp;The result produces three sum bits for 2 raised to
powers 0, 1, and 2, and a further bit for the final carry
(representing 2<sup>3</sup>). The addition in the lowest
order bit
has <span style="font-style: italic;">no</span>
carry in, so only a
half adder is needed:<br>
<br>
<img src="./Class Notes_files/3BitAdderAbs.png" name="graphics12" alt="3 bit adder" align="bottom" border="0" height="259" width="160"><br>
<br>
Recreating this in the gates applet is shown below in pictures, and is
simulated in action in the video.&nbsp; For
example, consider these two calculations: <br>
<br>
<span style="font-family: monospace;">&nbsp;</span><font style="font-family: monospace;">11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<br>
</font><span style="font-family: monospace;">&nbsp;</span><font style="font-family: monospace;"><span style="font-family: monospace;">011&nbsp;&nbsp;
010 </span><br style="font-family: monospace;">
<span style="font-family: monospace;"></span></font><font style="font-family: monospace;">+101&nbsp; +101 </font><br style="font-family: monospace;">
<span style="font-family: monospace;"></span><font style="font-family: monospace;"><span style="font-family: monospace;">
____&nbsp; ____ &nbsp; </span><br style="font-family: monospace;">
<span style="font-family: monospace;">1000&nbsp;&nbsp;
111 </span></font><font style="font-family: monospace;"><br>
</font></p>
<p>The pictures below show these two calculations in a circuit,
with
the more significant bits in both the input and output are lower down
in the diagram.&nbsp; The top summands in the manual calculations
above
correspond tothe leftmost column of switches, and the bottom summmands
reappear slightly to the right.&nbsp; <br>
</p>
<p><img style="width: 387px; height: 289px;" alt="3 bit adder 011+101" src="./Class Notes_files/3bit011_101.png">&nbsp;
011+101=1000<br>
</p>
<p><img style="width: 385px; height: 291px;" alt="3 bit adder 010+101" src="./Class Notes_files/3bit010_101.png">&nbsp;
010+101 = 111
<br>
<font face="monospace"><br>
</font>
</p>
<h3><a class="mozTocH3" name="computerCircuits2"></a><a name="Multiplexers"></a>Multiplexers</h3>
<p><span style="font-weight: bold;"></span>A
multiplexer chooses one of several data
lines.&nbsp; In an n-bit multiplexer input consists of&nbsp;2<sup>n</sup>
data lines and
&nbsp;n
control lines for some positive value of n. &nbsp;There is one
output
line. &nbsp;The n control lines have 2<sup>n</sup>
possible states and hence they can be wired to determine which
of&nbsp;2<sup>n</sup>data
lines should go to the one output line.&nbsp; For example if the
control lines hold a memory address, multiplexers can be used to fetch
the data fromthe proper source.&nbsp; For a dynamic illustration,
see
the <a href="http://anh.cs.luc.edu/150/notes/video/Multiplexers/Multiplexers.html">video</a>.&nbsp;
The simplest version to illustrate is a 1-bit multiplexer shown
below.&nbsp; It shows 2 data line and 1 control line (the
control line can choose between two states).&nbsp; In the pictures
below data bits are indexed by 0 at the top, 1 below, and the one
control
line at the bottom chooses between them.&nbsp;&nbsp; For
example, in
the first picture the control
line is off (0), so the input with index 0 (the upper one) has its
state (on, 1) transmitted through to the output wire, lighting the
light.<br>
<img style="width: 317px; height: 223px;" alt="multiplexer with 2 data lines" src="./Class Notes_files/mp01-0.png"> d0=1,
d1=0,
control choosing d0 = 1<br>
<img style="width: 317px; height: 222px;" alt="d0=1, d1=0, control choosing d1" src="./Class Notes_files/mp01-1.png"> d0=1,
d1=0,
control choosing d1 = 0<br>
<img style="width: 316px; height: 221px;" alt="d0=0, d1=0, control choosing d1" src="./Class Notes_files/mp00-1.png"> d0=0,
d1=0,
control choosing d1 </p>
<p>The pictures below, and also the Multipler video show a 2-bit
mutiplexer, with 4 data lines and 2 control lines. &nbsp;(Do you
see
that it is
composed of three of the simpler multiplexers?) &nbsp;In general
there could be 2<sup>n</sup>&nbsp; data lines and n
control
lines.&nbsp; The data lines in the picture are numbered 00 through
11
from top to
bottom.&nbsp; The top control line has the less significant bit.<br>
</p>
<p><img style="width: 437px; height: 257px;" alt="d00=0, d01=0, d10=0, d11=1, control 01" src="./Class Notes_files/mp1000-01.png">
d00=0,
d01=0, d10=0, d11=1, control choosing d01 = 0<br>
</p>
<p><img style="width: 440px; height: 260px;" alt="d00=0,d01=1,d10=0,d11=0, control 11" src="./Class Notes_files/mp0010-01.png"> d00=0,
d01=1, d10=0, d11=0, control choosing d01 = 1<br>
</p>
<img style="width: 441px; height: 261px;" alt="d00=0,d01=1,d10=0,dii=0, control 01" src="./Class Notes_files/mp0010-11.png"> d00=0,
d01=1, d10=0, d11=0, control choosing d11 = 0<br>
<p>A
demultiplexer does the reverse: &nbsp;n control lines and one data
input line deliver the input value to one of 2<sup>n</sup>
output
data lines.<br>
<br>
Multiplexers are needed to fetch data from one of
many memory addresses.&nbsp; Instructions must be fetched, using
the IP
address to feed the control lines.&nbsp; We need to get data into a
register, like the accumulator in Pip, using the address byte in an
instruction to feed the control lines.&nbsp;
Also Demultiplexers are needed for the reverse: &nbsp;getting data
from the accumulator to one of many memory addresses.
&nbsp;Multiplexers
can also be used inside a CPU to get the result from a specified
operation code: &nbsp;The computer actually works out all possible
operations at the same time, feeding data lines into a
multiplexer;&nbsp; the op code feeds the control lines of this
multiplexer to pick the result
associated with the right op code.<br>
</p>
<h3>
<a name="Latch_Circuit"></a>Latch Circuit</h3>
<p>
</p>
<p>We have only
considered sequential circuits - signals flow through and nothing is
kept. &nbsp;We need a combinatorial circuit, one with a loop in it,
to have memory. &nbsp;Loops in circuits can get tricky.<br>
<br>
A latch can
remember a value.&nbsp; We examine it in steps.<br>
<font face="monospace"><br>
<img src="./Class Notes_files/latch.png" name="graphics13" alt="latch" align="bottom" border="0" height="145" width="235"><br>
<br>
</font>It
has two main direct inputs <font face="monospace">d</font>,
the data
value, and <font face="monospace">g</font>, which
is 1 as we shall
see when the circuit should <span style="font-weight: bold;">g</span>et
the data. &nbsp;Note the two lines
feeding back from the nand outputs <font face="monospace">y</font>
and
<font face="monospace">z</font>.
&nbsp;Also <font face="monospace">z</font>
flows to the final circuit
output <font face="monospace">q</font>.
&nbsp;The three nand gates correspond to Boolean relationships <font face="monospace">x = (dg)'; z =
(xy)'; y = (g'z)' &nbsp;<br>
<br>
</font>If <font face="monospace">g</font>
is 1, then <font face="monospace">g'</font> is 0,
and this simplifies
to <font face="monospace">x = (d1)' = d'; y = (0z)' =
(0)' = 1</font>,
so <font face="monospace">z = (d'1)' = (d')' = d</font>,
and <font face="monospace">q
= z: &nbsp;</font>that means the value of <font face="monospace">d</font>
is transmitted to the output, whatever <font face="monospace">d</font>
is, and however it changes over time.<font face="monospace"><br>
<br>
<img src="./Class Notes_files/latch-g1.png" name="graphics15" alt="latch with g 1" align="bottom" border="0" height="150" width="230"><br>
<br>
</font>On the other hand, if
<font face="monospace">g</font> is 0, then <font face="monospace">g'</font>
is 1, and it is more complicated, and we must take the old value of <font face="monospace">z</font>
into account: &nbsp;call that old value <font face="monospace">q</font>,
so <font face="monospace">q = z</font>.
Then&nbsp;<font face="monospace">x
= (0d)' = 1</font>, and <font face="monospace">d</font>
has no
further effect. &nbsp;<font face="monospace">y = (1q)'
= q'</font>
which then circles around to make <font face="monospace">z
= (1q')' =
q</font>, which is what it was before, so the loop <i>maintains
its
old value</i> <i>of </i><font face="monospace"><i>z</i></font>
(and
also its value of <font face="monospace">y</font>
similarly),
independent of how <font face="monospace">d</font>
is changed!
&nbsp;<font face="monospace"><br>
<br>
<img src="./Class Notes_files/latch-g0.png" name="graphics17" alt="latch with g 0" align="bottom" border="0" height="144" width="229"><br>
<br>
</font>It
is not quite that simple if you view the latch video. &nbsp;If you
try
to
recreate it and run it in a simulator with lower input g = 1, you can
switch the upper input d and have it behave as expected.&nbsp;
However
if you change d to 1 and then change g to 0, then depending on your
Java implementation for the applet, you could see the
circuit flash continuously, back and forth between the two pictures
below:<br>
</p>
<p><img style="width: 311px; height: 148px;" alt="flash loop 1" src="./Class Notes_files/latchBad10-1.png"></p>
<p><img style="width: 314px; height: 151px;" alt="flash loop 0" src="./Class Notes_files/latchBad10-0.png"><br>
That <i>transition</i>
of g from 1
to 0 is a problem. &nbsp;This is a <span style="font-style: italic;">timing</span>
issue.&nbsp; See the slight
alteration below.&nbsp; See that two extra NOT gates are inserted.
&nbsp;In
a static logical state they cancel each other out, but they change
the <i>timing</i> when the signal from g alters and
splits. &nbsp;Now
runing a simulation works, if you start from a stable state, with any
sequence of input data, and it should
work (hopefully in whatever version of Java your browser is
using).&nbsp; <br>
</p>
<p><img style="width: 313px; height: 228px;" alt="With g=1, data 1 passes though" src="./Class Notes_files/latch11.png"> With g=1,
data
1 passes though.&nbsp; If data were switched to 0, output would go
to 0.</p>
<p><img style="width: 309px; height: 226px;" alt="g to 0, keep output 1" src="./Class Notes_files/latch10-1.png">&nbsp;
g to 0, keep output 1</p>
<p><img style="width: 317px; height: 225px;" alt="g at 0, data to 0, but output still 1" src="./Class Notes_files/latch00-1.png">&nbsp;
g at 0, data switched to 0, but output still 1<br>
</p>
<p><img style="width: 314px; height: 231px;" alt="g to 1, output matched data, 0" src="./Class Notes_files/latch01.png">&nbsp;
g to 1,
output matched data, 0<br>
</p>
<p><br>
&nbsp;When the lower input (g) is 1, the output changes with
the upper input (d). &nbsp;When g is changed to 0, the last output
is
remembered, no matter what you do later to d.&nbsp;<br>
<br>
This
example indicates the importance of timing. &nbsp;We have left out
a
discussion of the regular alternating clock signal that is used to
synchronize and stabilize outputs.&nbsp; A deeper examination of
circuits would include a clock.<br>
<br>
<br>
See
the <a href="http://webpages.cs.luc.edu/~cnaiman/COMP150/HW/Gates.html">gates
homework</a>.<br>
</p>
<h3><a name="VLSI"></a>Very Large Scale
Integration in Circuits (VLSI)<br>
</h3>
We have given an idea of how the logic works to build up a main
parts
of a computer from transistors, but we have left out the
scale,&nbsp;
Millions are needed.&nbsp; Hundreds of millions are in the latest
chips.&nbsp; There is the big issue of creating
complicated processors cheaply, with millions of logical components
and connections.&nbsp; The central advance that allowed this is
photolithography.&nbsp; The manufacturing starts with a large thin
slice
of a pure silicon.&nbsp; The
trick is using optical masks and light sensitive coatings that
are easy to&nbsp;remove based on whether light has
interacted with it or not. &nbsp;Where the light sensitive coating
has
been
removed, the surface may be etched, leaving the most recent surface
material only where it is desired.&nbsp; Alternately the electrical
properties of the silicon can be changed by doping it in the exposed
places.
&nbsp;This is done over and over with different detailed masks and
chemicals for
millions of gates and
connections <span style="font-style: italic;">simultaneously</span>.&nbsp;
A schematic, omitting all the
chemistry needed for the transformations, is below:<br>
<p>
<img style="width: 406px; height: 479px;" alt="Photolithographic Chip Fabrication Cycle" src="./Class Notes_files/chipPhotoLithography.png"></p>
<p>For much more detail (going far beyond this course!),
see&nbsp; <a href="http://www.lithoguru.com/scientist/lithobasics.html">VLSI</a>
or
this extensive and technical <a href="http://www.cse.nd.edu/courses/cse462/www/lectures/L05_Fabrication.pdf">pdf</a>.&nbsp;
</p>
<h2><a class="mozTocH2" name="Conclusion"></a>Conclusion</h2>
<p>So we have gotten as far down to basics as we are going to in
this
class.&nbsp; (Below
this is chemistry and physics!) &nbsp;We have described some of the
most important hardware used in creating a computer, seen how
millions of components can be put together efficiently to create a
machine with
its machine language, and some of the major points in the translation
between machine language and a high level language. &nbsp;<br>
<br>
There is much more to study.&nbsp; Here are a few examples:<br>
</p>
<ul>
<li>
<p style="margin-bottom: 0in;">Comp 264, Computer
Systems, covers
what lies under high level languages in much greater depth.<br>
</p>
</li>
<li>
<p style="margin-bottom: 0in;">A sequence of
programming courses,
starting with Comp 170, show ideas needed for more sophisticated
programs to solve much larger problems. </p>
</li>
<li>
<p style="margin-bottom: 0in;">There are a great many
topics in
computer science beyond programming, addressed in upper level courses:
&nbsp;</p>
<ul>
<li>
<p style="margin-bottom: 0in;">networking and
security,</p>
</li>
<li>
<p style="margin-bottom: 0in;">devising algorithms
for handling
all kinds of enormous collections of data,<br>
<br>
</p>
</li>
<li>organizing and accessing enormous databases<br>
</li>
<li>
<p style="margin-bottom: 0in;">getting many
processors and many
computers to work together effectively on enormous problems, </p>
</li>
<li>
<p style="margin-bottom: 0in;">dealing with the
many legal and
ethical issues around computing, </p>
</li>
<li>
<p style="margin-bottom: 0in;">approximating human
intelligence
(so far only in specialized ways), </p>
</li>
<li>
<p>and finally finding the limits of computing - it
cannot
solve all problems. &nbsp;</p>
</li>
</ul>
</li>
</ul>
<p>There is much more to learn and apply to the pressing problems
of
today and tomorrow! &nbsp; We live in the information age!
&nbsp;
Will you be a leader in it?</p>
<p>We have been dealing with the current practical model, with
Boolean
electical components on a chip.&nbsp; Completely different
approaches
are being researched and may have practical&nbsp; application in
the
future:&nbsp;optical computers, quantum computers, DNA computers,
.... </p>
<p>
&nbsp;
</p>
</body></html>