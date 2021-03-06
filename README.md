# get-jgi-data
A tutorial describing how to download data from a metagenomic project from jgi.  Lots of details can be found here
https://genome.jgi.doe.gov/portal/help/download.jsf#/api

### 1. Find your project and the xml file containing all the remote server paths to your data - this is the hardest part.
First you need to go the genome portal of JGI and find your project so that you can download the html file with all of the paths to all of the dfferent types of data housed at JGI for your project.. These include taxonomy, raw and filtered reads, and of course functions!!

For example, the link to some amazing DEEP CORE data can be found here at the link below.  The keyword that should be in this link is Comhiguestration.
https://genome.jgi.doe.gov/portal/pages/dynamicOrganismDownload.jsf?organism=Comhiguestration

### 2. Navigate to the DOWNLOAD.  Should be a box with a grey background located near the top of the page. 
Click on the button labeled Open Downloads as XML and save this file as a txt file called *all-jgi-dat.xml*

### 3. Create a cookie so JGI can validate your credintials
You can do this by running the make-a-cookie.shx bash script.  You will need to edit this script with your own credientials for username and password and then run it in the directory where you will want to download files. Run it like this.
   
    bash make-a-cookie.shx

### 4.  Explore the all-jgi-dat.xml to identify the files that you want to download and look for defining key words that indicate the files you want.  For example.  The COG functions for a metagenomic data set will usually contain the text "assembled.COG".  This text can be used to generate a bash script that will generate a curl command to download each of the COG annotations for your assembled metagenomic data.  Run the script like so, and be sure to inspect the resulting bash scritp to make sure that it will download only the files that you expect. Also, you should read the help menu of the gen-curl-for-jgi.py command by typing python gen-curl-for-jgi.py -h

    python gen-curl-for-jgi.py -html all-jgi-dat.xml -o curl-command-for-cog-functions.shx -keyword assembled.COG
    
### 5. Begin the download.  THis may take a long time and even stall.  You may need to run it over night.. or if you are so awesome, you could edit the curl command to keep trying until you get a result.  Persistence is key here.  This is how to run the bash script

    bash curl-command-for-cog-functions.shx
    
### 6.  When you have the files you want and you are ready to merge them... let me know and I'll continue to work on this tutorial. 

## Here is how I go about downloading MAGs from JGI. 

### 1. Go to the IMG website and select "Metagenome Bins" from the "Find Genomes" dropdown menu 

![Image of JGI Search](https://github.com/jvineis/get-jgi-data/blob/master/Screen%20Shot%202020-04-15%20at%2011.23.22%20AM.png)

### 2. Use the Advanced search option to look for the taxon that you are interested in.

![Image of JGI taxon search](https://github.com/jvineis/get-jgi-data/blob/master/chlorobium-search.png)

### 3. Select all of the MAGs that you want and export the table.. That should look like this.

![Image of Chlorobium table](https://github.com/jvineis/get-jgi-data/blob/master/Chloroium_table.png)

### 4. Copy the IDs in the "IMG Genome ID" from the table and convert to a string with spaces between so that you can paste it into the JGI Genome portal page like shown below.  This search will return the Genome portal data that you can add to your cart.. Then select the little cart icon at the top of the page and work out wich files you want to download.  A descent search term for genomes is .*\.fna

![Image of portal search](https://github.com/jvineis/get-jgi-data/blob/master/Genome_portal_search.png)

### 5.  Hope that helps!
