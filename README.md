<h1>Roof Replacement Prospect Scale</h1>

<h2>Overview</h2>
<p>I made this project to help effectively and efficiently identify prospects for roof replacements. Roofing companies can use this program to utilize public real estate data to identify the best homes for concentrating their marketing efforts.</p>

<p>I've combined 2 similar datasets, cleaned them, and ran them through my program. The program gives each property a score, based on the following criteria:</p>
  <ul>
    <li>Price of the home</li>
    <li>Size of the home</li>
    <li>Age of the home</li>
    <li>Most recent sale of the home</li>
    <li>Known material of the home's roof</li>
  </ul>

<h2>The Data</h2>

<p>Both datasets can be found on kaggle and were scraped from Trulia's public listings.</p>
<p><a href="https://www.kaggle.com/datasets/promptcloud/trulia-property-listing-dataset-2020">Dataset 1</a></p>

<p><a href="https://www.kaggle.com/datasets/promptcloud/real-estate-data-from-trulia">Dataset 2</a></p>

<p>This information is used to compile a score for each home in the dataset. Roofing companies can then focus their marketing and sales efforts on the homes with the highest scores with their strategies of choice - direct mailers, door knocking, etc.</p>


<h2>How to run the program</h2>

<h3>Fork the repository</h3>

<p><a href="https://github.com/ctroutman23/roof-replacement-prospect-scale">Repository link</a</p>


<h3>Set Up Virtual Environment</h3>

<h4>Mac</h4>
<ol>                            
    <li>python3 -m venv venv</li>            
    <li>source venv/bin/activate</li>
    <li>deactivate</li>
</ol>
<h4>Windows</h4>  
<ol>
    <li>pip install virtualenv</li> 
    <li>python -m venv venv</li>
    <li>venv\Scripts\activate</li>
    <li>deactivate</li>
</ol>
<h4>Linux</h4>
<ol>
    <li>pip install virtualenv</li>
    <li>virtualenv virtualenv_name</li>
    <li>source virtualenv_name/bin/activate</li>
    <li>deactivate</li>
</ol>


<h3>Install Required Packages</h3>

<p>All packages you need are located in the <strong>requirements.txt</strong> file. You can simply install them through the command below:</p>

<strong>pip or pip3 install -r requirements.txt</strong>

<p>Pandas is the only package/library required to run this program. You can also install it by running the following command: <strong>pip</strong> or<strong>pip3 install pandas</strong></p>

<p>Pandas is a python library that allows us to read in, clean, filter, and manipulate data. Using pandas we can set up, clean, and drw the results we want from our data within a single python file.</p>

<p>As long as you have the datasets downloaded, all you need to do now is run the <strong>main.py</strong> file.</p>


<h3>Expected Output</h3>
<p>When you run the <strong>main.py</strong> file, it will create a new csv file 
within the <code>cleaned_combined_data/</code> folder. This csv holds the scores for each 
property in our combined dataset.</p>

<h2>Features</h2>

<ol>
    <li>Loading Data - This program reads in 2 datasets using <i>pandas.read_csv</i>.</li>
    <li>Clean & Operate on Data - This program filters both datasets down to the same number of columns and merges them together using <i>pd.concat.</i></li>
    <li>Calculate New Values - This program creates new columns to hold the scores for each property, measuring their rating as a roof replacement lead.</li>
    <li>Data Visualization - Running this program creates a new csv, which appends our results to our combined/cleaned datset. This dataset is then used to create a Tableau dashboard.</li>
    <li>Best Practices - This program uses a virtual environment. See instructions above.</li>
    <li>Data Interpretation - This program includes clear, detailed comments in the <strong>main.py</strong> file, and a clear explanation of the program results in this README. See below: </li>
</ol>


<h2>Data Interpretation</h2>






