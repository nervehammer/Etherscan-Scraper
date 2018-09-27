# Etherscan-Scraper
Scrap etherscan.io for <a href=https://etherscan.io/contractsVerified>verified contract</a> and outputs csv containing address, dateverified, Eth balance, txn count

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

3. output will be in current directory with timestamp named e.g. `VerifiedContracts-20180927_111610.csv` 
