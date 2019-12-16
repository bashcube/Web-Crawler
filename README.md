# Web-Crawler

* ## Requirements:
  You should have python installed on your local machine along
  with following libraries:
  * html5lib
  * bs4
  ```bash
  $ pip install html5lib
  $ pip install bs4
  ```
  
* ## Usage:
  Clone the repo on your local machine using command:
  ```bash
  $ git clone https://github.com/bashcude/Web-Crawler.git
  ```
  Run the code using following commands:
  ```bash
  $ cd Web-Crawler
  $ python scraper.py
  __        __   _            ____                    _            
  \ \      / /__| |__        / ___|_ __ __ ___      _| | ___ _ __  
   \ \ /\ / / _ \ '_ \ _____| |   | '__/ _` \ \ /\ / / |/ _ \ '__| 
    \ V  V /  __/ |_) |_____| |___| | | (_| |\ V  V /| |  __/ |    
     \_/\_/ \___|_.__/       \____|_|  \__,_| \_/\_/ |_|\___|_|    

  WEBSITE : +++Enter-Website-Name+++
  ```
  
  * ## Description:
    <p>
    The following code uses requests and bs4 library to get the 
    href tags from the index page of the website provided.
    Then it eleminates links leading to other websites and prints the 
    directories of the website's folder.</p>
    <p>
    This can be prevented by adding crawl delay of reasonable time 
    which will make the process time consuming/boring and possibly 
    stopping the crawler.
    Another way of stopping the crawler is by disallowing all search 
    engines from accessing the folders/files.
    </p>
