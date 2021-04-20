## Various scripts and spreadsheets pertaining to the scoring of the Mapillary Dataset by country for computer vision purposes.

Imagelocator.py: Reads in the images and sorts them by country.

Datalabels.py: Reads from the new directory of sorted images and writes the image name, location, and score to a CSV file.

Detectron2_mapillary.py: Originally a Colab Notebook, trains and runs the Facebook Detectron Object Detection model on the Mapillary Dataset.
