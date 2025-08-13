
Prerequisites: 

Download fma_metadata and fma_small.zip from https://github.com/mdeff/fma [any other FMA set can be used for classification but visualisations have not been tested]                                                                    , 
Place fma_metadata and fma_small inside a directory called 'data' (data/fma_metadata/[file].csv) 

Usage: 
Create a Python 3.11 virtual environment, activate it and run this line:
> pip install -r requirements.txt (this may take some time to install, the OpenL3 package uses tensorflow as a dependency, several gigabyte download)
                            

First open 'embedding.ipynb', and check the filepath + name you want to use for your embedding set before running the main extraction cell. 

As long as a few embeddings are created at this point, you can open 'main.ipynb' in a separate tab and work with the limited embedding set whilst you wait for 'embedding.ipynb' to finish
- Adjust embedding set to read from by changing 'EMBED_PATH'
                                                                           
'main.ipynb' uses echonest.csv and tracks.csv, so ensure they are accessible and in the correct file location.

'genres.csv' was an investigation in exploring richer genre taxonomies in fma_large before realising it was too infeasible to test with due to the quantity of embeddings generated. 
