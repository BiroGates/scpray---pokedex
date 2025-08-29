## Solution
### The ideia
We are goint to break down the problem of treating all the data in submodules
- Extract
    - Here we extract all the data ( scrapy )
- Trasnform
    - Here we transform all the data we got from the previous step
- Load
    - Here we load all the data in the datbase doing the necessary transformations if needed



### Evolutions
Here lies the worst part of all this case scenario, we need to treat this a saperate case, first loading all the cards
of the evolutions and just then in the `transform` step we chage these data to be something we can put on the datbabase.


