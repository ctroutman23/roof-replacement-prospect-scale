This project seeks to call, filter, craft, and present real estate & storm data for 
the purposes of roofing marketing. 

I'm seeking out data that will help me identify homeowners who need
a new roof, using 2 different datasets.

Both datasets can be found on kaggle and were scraped from Trulia's records.
<p><a href="https://www.kaggle.com/datasets/promptcloud/trulia-property-listing-dataset-2020">Dataset 1</a></p>

<p><a href="https://www.kaggle.com/datasets/promptcloud/real-estate-data-from-trulia">Dataset 2</a></p>

<strong>In real estate data, I'll be looking at the data points below:</strong>
  
    -Age of the Home
    -Most Recent Listing
    -Most recent photos of the roof
    -Square footage of the house
    -Values of comprable homes in the same market


<strong>In the storm data,  I'll be looking at the data points below:</strong>

    -Areas hit by 1 in. of hail or greater in the past 2 years
    -Areas hit by 60 mph winds or greater in the past 2 years


<strong>Connection Between Real Estate & Storm Data</strong>

Together, this data is meant to help roofing companies locate the best potential 
jobs in the Kentucky/Indiana area. You could use it for marketing purposes in whichever 
area you select data for.

The real estate data helps us determine the best residential roof jobs in the area, and 
the storm data tells us which of them are likely to have their roof covered by their home 
insurance policy. We can identify people who know they need a new roof, and help them uncover 
the best deal.


<h2>Steps to Get Started</h2>


<h3>Set Up Virtual Environment</h3>

<strong>Mac</strong>            <strong>Windows</strong>                  <strong>Linux</strong>
python3 -m venv venv            
source venv/bin/activate

When you're not working on your project, you can turn off the virtual environment with
the <strong>$deactivate</strong> command.


<h3>Install Required Packages</h3>

All packages you need are located in the requirements.txt file. You can simply install them through the command below.
Make sure you use the pecific commands for your machine. Also, make sure to check and update the versions in the requirements.txt
file if they are no longer up to date.

<strong>Mac</strong>                <strong>Windows</strong>                <strong>Linux</strong>
pip3 install -r requirements.txt

Our required packages include the following:

<strong>Requests</strong>
<p>The requests library enables us to easily use HTTP requests(GET, POST, DELETE, etc.). 
This will be useful in calling our APIs</p>

<strong>Pandas</strong>
<p>Pandas is a python library that allows us to read in, clean, filter, and manipulate data.</p>

<h3>Set Up API Calls</h3>

In order to get the real estate and storm data, we'll use APIs. There are several APIs that will work. 
In this case I chose "Postman" for real estate data and "The National Weather Service" for up to date storm data.

You can find links to both APIs below:

<a href="https://www.postman.com/realestateapis" target="_blank">Postman Real Estate APIs<a>

<a href="https://www.weather.gov/documentation/services-web-api" target="_blank">National Weather Service<a>

Check out the <strong>set_up.py</strong> file to see the API calls.

In that file we call and test our APIs to get the data we want.


<h3>Read in the Datasets</h3>


<h3>Clean the data</h3>


<h3>Filter for the specific data you want</h3>


<h3>Join and Group Data</h3>


<h3>Draw Marketing Related Conclusions</h3>





