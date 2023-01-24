# Oxford Waste Collection

Python script to get the next waste collection dates for a given address in Oxford.

## Usage

1. Install requirements from requirements.txt (`pip install -r requirements.txt`)
2. Find the UPRN for your address from here: https://www.findmyaddress.co.uk/search
3. Call the `get_collection_dates(uprn, post_code)` method with your UPRN and Post Code.
4. Your next collection dates will be printed to stdout

## Next Steps

I'll adapt this for use in the [hacs_waste_collection_schedule](https://github.com/mampfes/hacs_waste_collection_schedule) plugin to Home Assistant