<h1>Roof Replacement Prospect Scale</h1>

<h2>Overview</h2>
<p>I made this project to help effectively and efficiently identify prospects for roof replacements. Roofing companies can use this program to utilize public real estate data to identify the best homes for concentrating their marketing efforts.</p>

<p>I've combined 2 similar datasets, cleaned them, and ran them through my program. The program gives each property a score, based on the following criteria:</p>
  <ul>
    <li><strong>Price of the home -</strong> The more expensive the home, the more expensive the roof.</li>
    <li><strong>Size of the home -</strong> Larger homes have larger roof areas</li>
    <li><strong>Age of the home -</strong> The roof age can be determined by the age of the home in many cases.The best roof replacement prospects are homes with asphalt roofs around 30 years old and metal roofs around 50 years old.</li>
    <li><strong>Most recent sale of the home -</strong> Roofs are often replaced before, during, or after the home sales process, so we want to use this datapoint to evaulate each prospect.</li>
    <li><strong>Known material of the home's roof -</strong> If we know what kind of roof the home has, we can determine how long it's expected to last, and therefore when it's like;y due for replacement.</li>
  </ul>

<h2>The Data</h2>

<p>Both datasets can be found on kaggle and were scraped from Trulia's public listings.</p>
<p><a href="https://www.kaggle.com/datasets/promptcloud/trulia-property-listing-dataset-2020" target="_blank">Dataset 1</a></p>

<p><a href="https://www.kaggle.com/datasets/promptcloud/real-estate-data-from-trulia" target="_blank">Dataset 2</a></p>

<p>This information is used to compile a score for each home in the dataset. Roofing companies can then focus their marketing and sales efforts on the homes with the highest scores with their strategies of choice - direct mailers, door knocking, etc.</p>


<h2>How to run the program</h2>

<h3>Clone the repository</h3>

<p><a href="https://github.com/ctroutman23/roof-replacement-prospect-scale" target="_blank">Repository link</a</p>


<h3>Set Up Virtual Environment</h3>

<h4>Mac & Linux</h4>
<ol>                            
    <li><code>python3 -m venv venv</code></li>            
    <li><code>source venv/bin/activate</code></li>
    <li><code>deactivate</code></li>
</ol>
<h4>Windows</h4>  
<ol>
    <li><code>python -m venv venv</code></li>
    <li><code>venv\Scripts\activate</code></li>
    <li><code>deactivate</code></li>
</ol>


<h3>Install Required Packages</h3>

<p>All packages you need are located in the <code>requirements.txt</code> file. You can simply install them through the command below:</p>

<code>pip3 install -r requirements.txt</code>

<p>Pandas is the only package/library required to run this program. You can also install it by running the following command: <code>pip install pandas</code></p>

<p>Pandas is a python library that allows us to read in, clean, filter, and manipulate data. Using pandas, we can set up, clean, and draw the results we want from our data within a single python file.</p>

<p>Once you've cloned the repository, set up your virtual environment, and installed pandas; then you're ready to run the <code>main.py</code> file on your machine.</p>


<h3>Expected Output</h3>
<p>When you run the <code>main.py</code> file, it will create a new csv file 
within the <code>cleaned_combined_data/</code> folder. This csv holds the scores for each 
property in our combined dataset, making data interpretation and visualization available for roofing companies.</p>

<h2>Features</h2>

<ol>
    <li>Loading Data - This program reads in 2 datasets using <code>pd.read_csv</code>.</li>
    <li>Clean & Operate on Data - This program filters both datasets down to the same number of 
    columns and merges them together using <code>pd.concat.</code></li>
    <li>Calculate New Values - This program creates new columns to hold the scores for each property, 
    measuring their rating as a roof replacement lead.</li>
    <li>Data Visualization - Running this program creates a new csv, which appends our results to 
    our combined/cleaned datset. This dataset is then used to create a Tableau dashboard, which you can access<a href='https://public.tableau.com/views/RoofReplacementProspectScale/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link' target="_blank"> HERE</a</li>
    <li>Best Practices - This program uses a virtual environment. See instructions above.</li>
    <li>Data Interpretation - This program includes clear, detailed comments in the 
    <code>main.py</code> file, and a clear explanation of the program results in this README. See below: </li>
</ol>


<h2>Data Interpretation</h2>
  <ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
  </ul>






