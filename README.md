# get-jgi-data
A tutorial describing how to download data from a metagenomic project from jgi

### 1. Find your project and the xml file containing all the remote server paths to your data - this is the hardest part.
First you need to go the genome portal of JGI and find your project so that you can download the html file with all of the paths to all of the dfferent types of data housed at JGI for your project.. These include taxonomy, raw and filtered reads, and of course functions!!

For example, the link to some amazing DEEP CORE data can be found here at the link below.  The keyword that should be in this link is Comhiguestration.
https://genome.jgi.doe.gov/portal/pages/dynamicOrganismDownload.jsf?organism=Comhiguestration

### 2. Navigate to the DOWNLOAD.  Should be a box with a grey background located near the top of the page. 
Click on the button labeled Open Downloads as XML and save this file as a txt file called *all-jgi-dat.xml*

### 3. Create a cookie so JGI can validate your credintials
You can do this by running the make-a-cookie.shx bash script.  You will need to edit this script with your own credientials.
    bash make-a-cookie.shx

