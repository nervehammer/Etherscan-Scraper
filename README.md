# Etherscan-Scraper
Scrap etherscan.io for <a href=https://etherscan.io/contractsVerified>verified contracts</a> and outputs csv containing address, dateverified, Eth balance, txn count

## Usage

1. Install required packages

    ```
    $ pip install -r requirements.txt
    ```

2. Run the script

    ```
    // Parse 6 page of verified contracts with 
    // default delay of 0.1 sec between each page 
    $ python scraper.py 6
    ```
    
    ```
    // Parse 9 page of verified contracts with 
    // default delay of 2 sec between each page 
    $ python scraper.py 9 2
    ```

3. output will be in current directory with current timestamp e.g. `VerifiedContracts-20180927_111610.csv` 

## Warning 
Using this script to scrap etherscan.io is against their Terms of Service. It is for educational purpose. Use it at your own risk. I am not liable for any damages. 
