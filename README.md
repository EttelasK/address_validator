Address Validator
======================
+ Created: 2016

Description
-----------
Address Validator allows the user to upload a csv file with addresses that may have missing data. The address validator script will run each of the addresses through google maps API and return the actual street address.  Address Validator will print out a csv file of every street address once all addresses have been scanned.  

Use
-----------
This script is intended to be used by companies looking to mail a large number of conacts with missing or incomplete addresses. 

## Sample
+ Data Input: BIDDEFORD, ME, 4005, CORRECT BUILDING PRODUCTS
+ Data Return: CORRECT BUILDING PRODUCTS, 8 Morin St, Biddeford, ME 04005, United States

## Instructions
1. Save contact list file as 'Bad File.csv' in the same folder as this python script.
2. Enter in your googlemaps API key:
```python
api_key = 'API-KEY-HERE!'
```
3. Run script and open the 'Full Address.csv' file in the same folder as this python script.
